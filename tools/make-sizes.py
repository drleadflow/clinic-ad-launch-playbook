"""Build feed (4:5 / 1:1 normalised) and story (9:16) versions of every PNG in a creative folder.
Usage: python3 make-sizes.py <creative_dir> [glob]
Story rule: black canvas, ad centred inside the IG safe zone (250px top/bottom).
Notes/screenshot ads extend their own paper colour instead of black."""
import sys, glob, os
from PIL import Image
W, H, SAFE = 1080, 1920, 250
d = sys.argv[1]; pat = sys.argv[2] if len(sys.argv) > 2 else '*.png'
os.makedirs(f'{d}/story', exist_ok=True); os.makedirs(f'{d}/feed', exist_ok=True)
n = 0
for f in sorted(glob.glob(f'{d}/{pat}')):
    name = os.path.basename(f)[:-4]
    im = Image.open(f).convert('RGB'); w, h = im.size
    fh = round(h * 1080 / w)
    im.resize((1080, fh), Image.LANCZOS).save(f'{d}/feed/{name}-{"4x5" if fh > 1080 else "1x1"}.png', optimize=True)
    notes = 'notes' in name.lower()
    bg = im.getpixel((5, h // 2)) if notes else (1, 3, 2)
    avail = H - 2 * SAFE
    s = min(1080 / w, (H if notes else avail) / h); sw, sh = round(w * s), round(h * s)
    canvas = Image.new('RGB', (W, H), bg)
    canvas.paste(im.resize((sw, sh), Image.LANCZOS), ((W - sw) // 2, (H - sh) // 2))
    canvas.save(f'{d}/story/{name}-9x16.png', optimize=True); n += 1
print(n, 'assets sized in', d)
