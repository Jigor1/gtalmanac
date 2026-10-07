"""Put an episode's scenes into video.html.
usage: python3 splice.py video.html scenes_html.txt scenes_js.txt
scenes_html.txt must hold the whole block from '<!-- ===== VIDEO-SPECIFIC SCENES (HTML) START ===== -->'
to '<!-- ===== VIDEO-SPECIFIC SCENES (HTML) END ===== -->', and scenes_js.txt the block from
'// ===== VIDEO-SPECIFIC SCENES (JS) START =====' to '// ===== VIDEO-SPECIFIC SCENES (JS) END =====',
markers included (see kit/examples)."""
import re, sys
page, h, j = sys.argv[1:4]
v = open(page).read()
H = open(h).read().rstrip("\n"); J = open(j).read().rstrip("\n")
v, n1 = re.subn(r"  <!-- ===== VIDEO-SPECIFIC SCENES \(HTML\) START ===== -->.*?<!-- ===== VIDEO-SPECIFIC SCENES \(HTML\) END ===== -->", lambda m: H, v, flags=re.S)
v, n2 = re.subn(r"// ===== VIDEO-SPECIFIC SCENES \(JS\) START =====.*?// ===== VIDEO-SPECIFIC SCENES \(JS\) END =====", lambda m: J, v, flags=re.S)
if n1 != 1 or n2 != 1:
    sys.exit("markers not found - keep the START/END marker lines in both scene files")
open(page, "w").write(v)
print("scenes spliced into", page)
