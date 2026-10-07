"""Contact sheet for QA. usage: python3 sheet.py out.jpg img1.png img2.png ...   (or: --video out.mp4 t1 t2 ...)"""
import sys, subprocess, os
from PIL import Image, ImageDraw
out = sys.argv[1]; args = sys.argv[2:]
if args and args[0] == "--video":
    os.makedirs("chk", exist_ok=True); files = []
    for t in args[2:]:
        f = f"chk/v_{t}.png"; subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", t, "-i", args[1], "-frames:v", "1", f], check=True); files.append(f)
else:
    files = args
w, h, cols = 360, 640, 6
s = Image.new("RGB", (cols * w, ((len(files) + cols - 1) // cols) * h))
for i, f in enumerate(files):
    im = Image.open(f).convert("RGB").resize((w, h)); ImageDraw.Draw(im).text((8, 8), os.path.basename(f), fill="yellow")
    s.paste(im, ((i % cols) * w, (i // cols) * h))
s.save(out, quality=88); print("saved", out)
