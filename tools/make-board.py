"""Generate an Excalidraw creative board from campaign folders.
Usage: python3 make-board.py out.excalidraw <campaign_dir> [<campaign_dir> ...]
One column per campaign, one section per filename prefix, grade from 12-scorecard.md on each card.
Open the file at excalidraw.com, in Excalidraw Plus, or with the Obsidian Excalidraw plugin."""
import sys, os, glob, json, re, base64, io, random, time
from PIL import Image
out, camps = sys.argv[1], sys.argv[2:]
CW, CH, G, P, COLS = 180, 225, 24, 120, 6
els, files = [], {}
def txt(i, x, y, t, size=20, color="#1e1e1e"):
    els.append({"type": "text", "id": i, "x": x, "y": y, "width": len(t) * size * .55, "height": size * 1.3, "text": t, "fontSize": size, "fontFamily": 1, "strokeColor": color, "textAlign": "left", "verticalAlign": "top", "baseline": size})
for ci, camp in enumerate(camps):
    grades = {}
    sc = os.path.join(camp, '12-scorecard.md')
    if os.path.exists(sc):
        for line in open(sc):
            m = re.match(r'\|\s*(?:\d+\s*\|\s*)?([\w\-]+)\s*\|\s*([\d.]+)\s*\|', line)
            if m: grades[m.group(1)] = float(m.group(2))
    x0 = ci * (COLS * (CW + G) + 300); y = 0
    txt(f"t{ci}", x0, y, os.path.basename(camp.rstrip('/')).upper(), 44); y += 80
    secs = {}
    for f in sorted(glob.glob(os.path.join(camp, 'creative', 'feed', '*.png'))):
        secs.setdefault(os.path.basename(f).split('-')[0], []).append(f)
    for sec, items in sorted(secs.items()):
        rows = (len(items) + COLS - 1) // COLS
        els.append({"type": "rectangle", "id": f"s{ci}{sec}", "x": x0 - 16, "y": y - 16, "width": COLS * (CW + G) + 16, "height": 50 + rows * (CH + G + 30) + 16, "strokeColor": "#c9a441", "backgroundColor": "#faf6ee", "fillStyle": "solid", "roughness": 0, "strokeWidth": 1, "roundness": {"type": 3}})
        txt(f"st{ci}{sec}", x0, y, sec, 24, "#7a5c1e"); y += 50
        for i, f in enumerate(items):
            cx, cy = x0 + (i % COLS) * (CW + G), y + (i // COLS) * (CH + G + 30)
            name = re.sub(r'-(4x5|1x1)$', '', os.path.basename(f)[:-4]); fid = re.sub(r'\W', '', camp + name)
            im = Image.open(f).convert('RGB'); w, h = im.size; im = im.resize((520, round(h * 520 / w)), Image.LANCZOS)
            b = io.BytesIO(); im.save(b, 'JPEG', quality=58, optimize=True)
            files[fid] = {"mimeType": "image/jpeg", "id": fid, "dataURL": "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode(), "created": int(time.time() * 1000)}
            els.append({"type": "image", "id": "i" + fid, "x": cx, "y": cy, "width": CW, "height": CH if h > w else CW, "fileId": fid, "status": "saved", "scale": [1, 1]})
            g = grades.get(name); txt("l" + fid, cx, cy + CH + 4, name[:26] + (f"  {g}" if g else ""), 14, "#15803d" if g and g >= 8.5 else "#1e1e1e")
        y += rows * (CH + G + 30) + 40
for e in els:
    for k, v in {"strokeColor": "#1e1e1e", "backgroundColor": "transparent", "fillStyle": "solid", "strokeWidth": 1, "roughness": 1, "opacity": 100, "angle": 0, "seed": random.randint(1, 10**9), "version": 1, "versionNonce": random.randint(1, 10**9), "isDeleted": False, "groupIds": [], "frameId": None, "boundElements": [], "updated": int(time.time() * 1000), "link": None, "locked": False}.items():
        e.setdefault(k, v)
json.dump({"type": "excalidraw", "version": 2, "source": "clinic-ad-launch-playbook", "elements": els, "appState": {"viewBackgroundColor": "#ffffff"}, "files": files}, open(out, 'w'))
print(len(els), 'elements', len(files), 'images ->', out)
