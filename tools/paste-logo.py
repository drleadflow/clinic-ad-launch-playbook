#!/usr/bin/env python3
"""Paste a real logo (transparent PNG) onto a generated static instead of trusting the model to draw it.
usage: paste-logo.py <image> <logo.png> <mode> [out]
  mode top-right   : clears the right end of the top bar (bar colour sampled at the corner) and places the logo
  mode box:x0,y0,x1,y1 : fills that box with the colour sampled at its top-left pixel and centres the logo in it
"""
import sys
from PIL import Image

def logo_fit(logo, h):
    lg = logo.crop(logo.getbbox())
    return lg.resize((max(1, int(lg.width * h / lg.height)), h), Image.LANCZOS)

def top_bar_height(im, x):
    ref = im.getpixel((x, 4)); y = 0
    while y < im.height // 4 and sum(abs(a - b) for a, b in zip(im.getpixel((x, y)), ref)) < 40:
        y += 1
    return y

def main():
    src, logo_p, mode = sys.argv[1:4]; out = sys.argv[4] if len(sys.argv) > 4 else src
    im = Image.open(src).convert('RGB'); logo = Image.open(logo_p).convert('RGBA')
    W, H = im.size
    if mode == 'top-right':
        bar = min(top_bar_height(im, W - 12), 220)
        box = (int(W * 0.70), 0, W, bar)
    else:
        box = tuple(int(v) for v in mode.split(':')[1].split(','))
    col = im.getpixel((box[2] - 3, box[1] + 3))
    im.paste(col, box)
    lg = logo_fit(logo, int((box[3] - box[1]) * 0.62))
    x = box[2] - lg.width - int(W * 0.03) if mode == 'top-right' else box[0] + (box[2] - box[0] - lg.width) // 2
    y = box[1] + (box[3] - box[1] - lg.height) // 2
    im.paste(lg, (x, y), lg)
    im.save(out); print(out, 'box', box, 'bar colour', col)

if __name__ == '__main__':
    main()
