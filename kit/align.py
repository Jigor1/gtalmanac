"""Force-align the narration to the script -> words.json (word-level timestamps).
usage: python3 align.py narration.mp3 script.txt
The script must be the exact text sent to the TTS. Money/percent must be spelled out;
plain integers (6, 2013) are converted automatically."""
import sys, json, re, wave, subprocess, os
from pocketsphinx import Decoder
import pocketsphinx
from num2words import num2words
CUSTOM = {  # ARPAbet for words missing from CMUdict - add new names here
    "gta": "JH IY T IY EY", "gtalmanac": "JH IY T IY AO L M AH N AE K",
    "leonida": "L IY OW N IY D AH", "lucia": "L UW S IY AH", "zelnick": "Z EH L N IH K",
    "rockstar": "R AA K S T AA R", "netflix": "N EH T F L IH K S", "xbox": "EH K S B AA K S",
    "youtuber": "Y UW T UW B ER", "youtubers": "Y UW T UW B ER Z", "tgg": "T IY JH IY JH IY", "rubius": "R UW B IY AH S", "montages": "M AA N T AA ZH IH Z",
    "pegi": "P EH G IY", "esrb": "IY EH S AA R B IY", "fetishes": "F EH T IH SH IH Z", "lohan": "L OW AH N", "gamestop": "G EY M S T AA P", "ps": "P IY EH S", "xbox's": "EH K S B AA K S IH Z",
    "crossbody": "K R AO S B AA D IY", "keychain": "K IY CH EY N", "macca": "M AE K AH", "swizzle": "S W IH Z AH L",
    "kart": "K AA R T", "warhorse": "W AO R HH AO R S", "klima": "K L IY M AH", "qssr": "K Y UW EH S EH S AA R", "upscaler": "AH P S K EY L ER",
}
audio, script = sys.argv[1], open(sys.argv[2]).read()
DICT = os.path.join(os.path.dirname(pocketsphinx.__file__), "model", "en-us", "cmudict-en-us.dict")
known = set(l.split()[0].split("(")[0] for l in open(DICT, encoding="utf-8", errors="ignore") if l.strip())
CUSTOM = {w: p for w, p in CUSTOM.items() if w not in known}   # only words the dictionary lacks
known |= set(CUSTOM)
if re.search(r"[$%€£]", script):
    sys.exit("Spell out money/percent in the script (e.g. 'fifty-nine ninety-nine').")
def num(m):
    n = int(m.group(0))
    return num2words(n, to="year") if 1900 <= n <= 2099 and len(m.group(0)) == 4 else num2words(n)
text = re.sub(r"\d+", num, script.lower())
words = []
for w in re.findall(r"[a-z']+(?:-[a-z']+)*", text):
    if "-" in w:
        j = w.replace("-", "")
        words += [j] if j in known else w.split("-")
    else:
        words.append(w)
words = [w.strip("'") for w in words if w.strip("'")]
oov = sorted(set(w for w in words if w not in known))
if oov:
    sys.exit("Words missing from the dictionary - add ARPAbet to CUSTOM in align.py: " + ", ".join(oov))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", audio, "-ar", "16000", "-ac", "1", "_a16k.wav"], check=True)
with wave.open("_a16k.wav") as f:
    data = f.readframes(f.getnframes())
d = Decoder(samprate=16000, bestpath=False)
for w, p in CUSTOM.items():
    d.add_word(w, p, True)
d.set_align_text(" ".join(words))
d.start_utt(); d.process_raw(data, full_utt=True); d.end_utt()
out = [{"w": s.word.split("(")[0], "s": round(s.start_frame / 100, 2), "e": round((s.end_frame + 1) / 100, 2)}
       for s in d.seg() if s.word not in ("<s>", "</s>", "<sil>")]
if len(out) != len(words):
    sys.exit(f"Alignment failed ({len(out)} of {len(words)} words). Check that script.txt matches the audio exactly.")
json.dump(out, open("words.json", "w"))
for i, o in enumerate(out):
    print(f"{i:3d} {o['s']:6.2f} {o['w']}")
