# GTAlmanac video kit

Everything needed to turn a script + narration into a 1080×1920 GTAlmanac short.
The full procedure lives in the `gtalmanac-shorts` skill; this folder is the code.

| File | What it does |
| --- | --- |
| `setup.sh` | One-time install in an episode folder (pocketsphinx, num2words, fonts, Playwright check). |
| `align.py` | Word timestamps from the narration → `words.json`. Add missing words to `CUSTOM`. |
| `captions.py` | `chunks.txt` → `captions.json` (2–4 word caption blocks). |
| `video.html` | Page template (background, header, captions). Only the VIDEO-SPECIFIC blocks change. |
| `build.py` | Injects captions, words and duration → `page.html`. |
| `render.js` | `preview`, `capcheck`, `cover`, `video` (Playwright → ffmpeg). |
| `cutout.py` / `sheet.py` | White-background removal / QA contact sheets. |
| `page_template.html` | Portuguese download page (player, download buttons, titles, caption). |
| `tools/narrate.py` | Narration through the GitHub narrator robot (`tts/` → `audio/`). |
| `tools/images.py` | Images through the GitHub image robot (`img/` → `images/`). |
| `tools/splice.py` | Puts `scenes_html.txt` + `scenes_js.txt` into `video.html`. |
| `tools/make_page.py` | Fills `page_template.html` for an episode. |
| `examples/` | Scene code from Ep. 8 (unboxing grid), Ep. 9 (quote reveal, price ladder, traffic light), Ep. 10 (leaked memo highlight, price flip). |

Quick start in a fresh folder:

```bash
mkdir -p /home/claude/epNN/assets && cd /home/claude/epNN
cp /home/claude/gtalmanac/kit/{setup.sh,align.py,captions.py,build.py,render.js,cutout.py,sheet.py,video.html} .
bash setup.sh
```
