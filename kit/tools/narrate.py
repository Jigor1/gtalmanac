"""Get a narration MP3 through the GitHub narrator robot (.github/workflows/narrate.yml).
usage: python3 narrate.py <name> <script.txt> <out.mp3> [--repo <clone>]  (default: the clone this file is in)
Writes tts/<name>.json with the exact script text, pushes it, then waits (up to ~4 min)
for audio/<name>.mp3 (or audio/<name>.error.txt) and copies the MP3 to <out.mp3>.
Each run spends ElevenLabs credits: never call it twice for the same script."""
import json, os, subprocess, sys, time, shutil

args = sys.argv[1:]
repo = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))  # the clone this tool lives in
if "--repo" in args:
    i = args.index("--repo"); repo = args[i + 1]; del args[i:i + 2]
name, script, out = args
text = open(script, encoding="utf-8").read().strip()
git = lambda *a, **k: subprocess.run(["git", "-C", repo, *a], check=k.get("check", True), capture_output=True, text=True)

git("fetch", "-q", "origin", "main"); git("reset", "-q", "--hard", "FETCH_HEAD")
if os.path.exists(f"{repo}/audio/{name}.mp3"):
    sys.exit(f"audio/{name}.mp3 already exists - pick a new name (credits are spent per job).")
os.makedirs(f"{repo}/tts", exist_ok=True)
json.dump({"text": text, "voice_id": "pNInz6obpgDQGcFmaJgB", "model_id": "eleven_multilingual_v2"},
          open(f"{repo}/tts/{name}.json", "w", encoding="utf-8"), ensure_ascii=False)
git("add", f"tts/{name}.json")
git("-c", "user.name=Claude", "-c", "user.email=noreply@anthropic.com", "commit", "-q", "-m",
    f"tts: {name}\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>")
for _ in range(3):
    if git("push", "-q", "origin", "main", check=False).returncode == 0: break
    git("pull", "-q", "--rebase", "origin", "main", check=False); time.sleep(3)
else:
    sys.exit("push failed")
print("job pushed, waiting for the robot...", flush=True)
t0 = time.time()
while time.time() - t0 < 240:
    time.sleep(10)
    git("fetch", "-q", "origin", "main")
    files = git("ls-tree", "-r", "--name-only", "FETCH_HEAD").stdout.split()
    if f"audio/{name}.mp3" in files or f"audio/{name}.error.txt" in files:
        git("reset", "-q", "--hard", "FETCH_HEAD")
        if os.path.exists(f"{repo}/audio/{name}.error.txt"):
            sys.exit("robot error: " + open(f"{repo}/audio/{name}.error.txt").read()[:500])
        shutil.copy(f"{repo}/audio/{name}.mp3", out)
        print(f"ok: {out} after {time.time() - t0:.0f}s")
        sys.exit(0)
sys.exit("timeout: no audio after 4 min - check the Actions tab of Jigor1/gtalmanac")
