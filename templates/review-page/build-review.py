"""Build a client review page from a campaign folder.
Usage: python3 build-review.py <campaign_dir> <offer_key> "<Offer label>" out.html
Reads creative/feed/*.png, 12-scorecard.md (grades), 03-copy.md (families), embeds 720px JPEG previews as data URIs.
Then publish out.html anywhere that can host a static page (a Claude artifact with a db capability gives you shared approvals)."""
import sys, json, glob, os, re, base64, io
from PIL import Image
camp, key, label, out = sys.argv[1:5]
grades = {}
for line in open(os.path.join(camp, '12-scorecard.md')) if os.path.exists(os.path.join(camp, '12-scorecard.md')) else []:
    m = re.match(r'\|\s*(?:\d+\s*\|\s*)?([\w\-]+)\s*\|\s*([\d.]+)\s*\|\s*[^|]*\|\s*([^|]*)\|', line)
    if m: grades[m.group(1)] = (float(m.group(2)), m.group(3).strip())
cards = []
for f in sorted(glob.glob(os.path.join(camp, 'creative', 'feed', '*.png'))):
    name = re.sub(r'-(4x5|1x1)$', '', os.path.basename(f)[:-4])
    im = Image.open(f).convert('RGB'); w, h = im.size; im = im.resize((720, round(h * 720 / w)), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, 'JPEG', quality=72, optimize=True)
    g = grades.get(name, (None, ''))
    cards.append({"id": f"{key}__{name}", "offer": key, "name": name, "grade": g[0], "note": g[1], "ratio": '1x1' if f.endswith('1x1.png') else '4x5', "primary": "<primary text from 03-copy.md>", "headline": "<headline>", "desc": "<description>", "cta": "Learn more", "src": "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()})
data = {"offers": [{"key": key, "label": label}], "cards": cards}
tpl = open(os.path.join(os.path.dirname(__file__), 'review-page.html')).read()
open(out, 'w').write(tpl.replace('window.__CARDS__ /* replace with the object written by build-review.py */', json.dumps(data)))
print(len(cards), 'cards ->', out)
