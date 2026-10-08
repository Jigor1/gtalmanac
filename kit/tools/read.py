"""Read full article text through the GitHub reader robot (.github/workflows/read-articles.yml).
usage: python3 read.py <name> <url> [<url> ...] [--out <dir>] [--repo <clone>]
Pushes read/<name>.json (max 15 urls), waits up to ~4 min for articles/<name>/_report.json
and copies the 01.txt, 02.txt... files (TITLE/DATE/URL/SUMMARY + body text) to <dir> (default ./articles_<name>).
Prints the report. Public pages only; never put tokens in a job (the repo is public)."""
import json, os, subprocess, sys, time, shutil
args = sys.argv[1:]
repo = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
out = None
for flag in ("--repo", "--out"):
    if flag in args:
        i = args.index(flag); v = args[i + 1]; del args[i:i + 2]
        if flag == "--repo": repo = v
        else: out = v
name, urls = args[0], args[1:]
out = out or f"articles_{name}"
git = lambda *a, **k: subprocess.run(["git", "-C", repo, *a], check=k.get("check", True), capture_output=True, text=True)
git("fetch", "-q", "origin", "main"); git("reset", "-q", "--hard", "FETCH_HEAD")
if not os.path.exists(f"{repo}/.github/workflows/read-articles.yml"):
    sys.exit("the reader robot is not installed yet - ask Igor to install read-articles.yml")
rep = f"articles/{name}/_report.json"
if os.path.exists(f"{repo}/{rep}"): git("rm", "-q", "-r", f"articles/{name}")
os.makedirs(f"{repo}/read", exist_ok=True)
json.dump({"urls": urls}, open(f"{repo}/read/{name}.json", "w"), indent=1)
git("add", "-A", *[p for p in ("read", "articles") if os.path.exists(f"{repo}/{p}")])
git("-c", "user.name=Claude", "-c", "user.email=noreply@anthropic.com", "commit", "-q", "-m",
    f"read: {name}\n\nCo-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>")
for _ in range(3):
    if git("push", "-q", "origin", "main", check=False).returncode == 0: break
    git("pull", "-q", "--rebase", "origin", "main", check=False); time.sleep(3)
else: sys.exit("push failed")
print("job pushed, waiting for the robot...", flush=True)
t0 = time.time()
while time.time() - t0 < 240:
    time.sleep(8)
    git("fetch", "-q", "origin", "main")
    if rep in git("ls-tree", "-r", "--name-only", "FETCH_HEAD").stdout.split():
        git("reset", "-q", "--hard", "FETCH_HEAD")
        os.makedirs(out, exist_ok=True)
        report = json.load(open(f"{repo}/{rep}"))
        for r in report:
            if r.get("file"): shutil.copy(f"{repo}/articles/{name}/{r['file']}", os.path.join(out, r["file"]))
        print(json.dumps(report, indent=1)); print(f"done after {time.time()-t0:.0f}s -> {out}")
        sys.exit(0)
sys.exit("timeout: nothing after 4 min - check the Actions tab of Jigor1/gtalmanac")
