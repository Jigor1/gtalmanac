"""Inject captions + narration duration into video.html -> page.html.
usage: python3 build.py narration.mp3"""
import sys, subprocess
dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", sys.argv[1]]))
h = open("video.html").read().replace("__CAPS__", open("captions.json").read()).replace("__DUR__", f"{dur:.3f}").replace("__WORDS__", open("words.json").read())
open("page.html", "w").write(h)
print(f"page.html ready, duration {dur:.2f}s")
