"""Remove the white background around a box-art / product image -> transparent PNG.
usage: python3 cutout.py input.png output.png [--keep x0,y0,x1,y1 ...]
--keep restores white areas INSIDE the object (e.g. a white PS5 banner that touches the
background), given in input-image pixel coordinates."""
import sys, numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage
src, dst = sys.argv[1], sys.argv[2]
keeps = [tuple(map(int, a.split(","))) for a in sys.argv[4::2]] if "--keep" in sys.argv else []
im = Image.open(src).convert("RGB"); a = np.asarray(im).astype(int)
white = (a.min(axis=2) > 232) & ((a.max(axis=2) - a.min(axis=2)) < 22)
lab, _ = ndimage.label(white)
border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
fg = ~np.isin(lab, list(border))
for x0, y0, x1, y1 in keeps:
    fg[y0:y1, x0:x1] = True
fg = ndimage.binary_fill_holes(fg); fg = ndimage.binary_opening(fg, iterations=1); fg = ndimage.binary_erosion(fg, iterations=2)
alpha = Image.fromarray((fg * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.1))
out = im.copy(); out.putalpha(alpha)
out.crop(Image.fromarray((fg * 255).astype(np.uint8)).getbbox()).save(dst)
print("saved", dst)
