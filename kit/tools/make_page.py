"""Build the Portuguese download page for an episode from kit/page_template.html.
usage: python3 make_page.py page.json <out_dir>
page.json = {"ep": "11", "label": "The $400 GTA 6 box", "dur": "53 s", "slug": "400-dollar-box",
             "titles": ["...", "...", "..."], "caption": "caption text + hashtags"}
Writes <out_dir>/ep<ep>.html. Publish it with the Artifact tool: file_path = that html,
root = <out_dir>, files = {"video.mp4": "video.mp4", "capa.png": "capa.png", "capa2.png": "capa2.png"},
capabilities = {"downloads": {}}. The three files must sit in <out_dir> and stay under 15 MB each."""
import html, json, os, sys
spec = json.load(open(sys.argv[1], encoding="utf-8")); out = sys.argv[2]
tpl = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "page_template.html"), encoding="utf-8").read()
e = lambda s: html.escape(str(s), quote=False)
rep = {"{{EP}}": e(spec["ep"]), "{{LABEL}}": e(spec["label"]), "{{DUR}}": e(spec["dur"]), "{{SLUG}}": e(spec["slug"]),
       "{{T1}}": e(spec["titles"][0]), "{{T2}}": e(spec["titles"][1]), "{{T3}}": e(spec["titles"][2]), "{{CAPTION}}": e(spec["caption"])}
for k, v in rep.items():
    tpl = tpl.replace(k, v)
os.makedirs(out, exist_ok=True)
dst = os.path.join(out, f"ep{spec['ep']}.html")
open(dst, "w", encoding="utf-8").write(tpl)
print("page ready:", dst)
