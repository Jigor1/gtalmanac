"""Build timed caption chunks -> captions.json.
usage: python3 captions.py chunks.txt
chunks.txt: one caption chunk per line (2-4 words), in spoken order. Tokens are separated by spaces.
  TEXT      = display text consuming 1 spoken word
  TEXT:n    = display text consuming n spoken words  (e.g. $59.99:4 for 'fifty nine ninety nine')
  *TEXT     = key token (numbers, punchlines) shown in yellow
Lines starting with # are ignored. The total must equal the number of words in words.json."""
import sys, json
W = json.load(open("words.json"))
lines = [l.strip() for l in open(sys.argv[1]) if l.strip() and not l.startswith("#")]
i, chunks = 0, []
for c in lines:
    toks = []
    for raw in c.split():
        key = raw.startswith("*"); raw = raw.lstrip("*")
        txt, n = raw, 1
        if ":" in raw and raw.rsplit(":", 1)[1].isdigit():
            txt, n = raw.rsplit(":", 1)[0], int(raw.rsplit(":", 1)[1])
        if i + n > len(W):
            sys.exit(f"Too many tokens at chunk '{c}' (only {len(W)} spoken words).")
        toks.append({"t": txt, "k": key, "s": W[i]["s"], "e": W[i + n - 1]["e"]}); i += n
    chunks.append({"toks": toks, "s": toks[0]["s"]})
if i != len(W):
    sys.exit(f"Chunks consume {i} words but the audio has {len(W)}. Next unmatched: {[w['w'] for w in W[i:i+6]]}")
end = W[-1]["e"] + 1.0
for j, c in enumerate(chunks):
    nxt = chunks[j + 1]["s"] if j + 1 < len(chunks) else end
    c["e"] = min(nxt, c["toks"][-1]["e"] + 0.9)
json.dump(chunks, open("captions.json", "w"))
for c in chunks:
    print(f'{c["s"]:6.2f}-{c["e"]:6.2f}  ' + " ".join(t["t"] for t in c["toks"]))
