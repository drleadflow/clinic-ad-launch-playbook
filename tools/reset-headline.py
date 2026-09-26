#!/usr/bin/env python3
"""Replace headline lines on a flat-background static without a visible patch.
Clears a box by interpolating each row between the background just outside the box, then sets new lines
in a condensed font sized to a measured cap height.
usage: reset-headline.py <img> <x0,y0,x1,y1> <font.ttf> <align left|center> <anchor_x> "<LINE>|<cap>|<ytop>" ...
"""
import sys
from PIL import Image, ImageDraw, ImageFont

def clear(im, box):
    x0, y0, x1, y1 = box; px = im.load()
    for y in range(y0, y1):
        a = px[max(0, x0 - 4), y]; b = px[min(im.width - 1, x1 + 4), y]
        for x in range(x0, x1):
            t = (x - x0) / max(1, x1 - x0)
            px[x, y] = tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

def font_for_cap(path, cap):
    sz = cap
    while True:
        f = ImageFont.truetype(path, sz); b = f.getbbox('H')
        if b[3] - b[1] >= cap: return f
        sz += 1

def main():
    img, box, font, align, ax = sys.argv[1:6]
    im = Image.open(img).convert('RGB'); clear(im, tuple(int(v) for v in box.split(',')))
    d = ImageDraw.Draw(im); ax = int(ax)
    for spec in sys.argv[6:]:
        txt, cap, ytop = spec.split('|'); f = font_for_cap(font, int(cap))
        hb = f.getbbox('H'); bb = d.textbbox((0, 0), txt, font=f); w = bb[2] - bb[0]
        x = ax - bb[0] if align == 'left' else ax - w // 2 - bb[0]
        d.text((x, int(ytop) - hb[1]), txt, font=f, fill=(22, 20, 18))
    im.save(img); print('ok', img)

if __name__ == '__main__':
    main()
