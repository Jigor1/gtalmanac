"""Download images through the GitHub image robot (.github/workflows/fetch-images.yml).
usage: python3 images.py <episode> <items.json> <dest_dir> [--repo /home/claude/gtalmanac]
items.json = [{"name": "memo", "page": "https://article..."},      # page -> its og:image
              {"name": "klima", "wiki": "Martin Klíma"},           # Wikipedia main photo (lang: "en" default)
              {"name": "box", "url": "https://.../box.jpg"},       # direct image link
              {"name": "store", "commons": "GameStop store front"}] # Wikimedia Commons search
Pushes img/<episode>.json, waits (up to ~4 min) for images/<episode>/_report.json and copies
every file it got into <dest_dir>. Prints the report (errors included). Public links only:
never put signed URLs, tokens or keys in a job (the repository is public)."""
import json, os, subprocess, sys, time, shutil

args = sys.argv[1:]
repo = "/home/claude/gtalmanac"
if "--repo" in args:
    i = args.index("--repo"); repo = args[i + 1]; del args[i:i + 2]
ep, items_file, dest = args
items = json.load(open(items_file, encoding="utf-8"))
git = lambda *a, **k: subprocess.run(["git", "-C", repo, *a], check=k.get("check", True), capture_output=True, text=True)

git("fetch", "-q", "origin", "main"); git("reset", "-q", "--hard", "FETCH_HEAD")
if not os.path.exists(f"{repo}/.github/workflows/fetch-images.yml"):
    sys.exit("the image robot is not installed yet (.github/workflows/fetch-images.yml) - ask Igor to install it")
os.makedirs(f"{repo}/img", exist_ok=True)
rep = f"images/{ep}/_report.json"
if os.path.exists(f"{repo}/{rep}"):
    git("rm", "-q", "-r", f"images/{ep}")
json.dump({"items": items}, open(f"{repo}/img/{ep}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
git("add", "-A", *[p for p in ("img", "images") if os.path.exists(f"{repo}/{p}")])
git("-c", "user.name=Claude", "-c", "user.email=noreply@anthropic.com", "commit", "-q", "-m",
    f"img: {ep}\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>")
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
    if rep in git("ls-tree", "-r", "--name-only", "FETCH_HEAD").stdout.split():
        git("reset", "-q", "--hard", "FETCH_HEAD")
        report = json.load(open(f"{repo}/{rep}"))
        os.makedirs(dest, exist_ok=True)
        for r in report:
            if r.get("file"):
                shutil.copy(f"{repo}/images/{ep}/{r['file']}", os.path.join(dest, r["file"]))
        print(json.dumps(report, indent=1))
        print(f"done after {time.time() - t0:.0f}s -> {dest}")
        sys.exit(0)
sys.exit("timeout: no images after 4 min - check the Actions tab of Jigor1/gtalmanac")
