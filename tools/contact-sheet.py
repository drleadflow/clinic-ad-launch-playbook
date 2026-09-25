#!/usr/bin/env python3
"""Tile masters into one QA sheet with labels. usage: contact-sheet.py <out.jpg> <cols> <png>..."""
import sys; from PIL import Image, ImageDraw
out, cols, files = sys.argv[1], int(sys.argv[2]), sys.argv[3:]
ims=[(f.split('/')[-1].rsplit('.',1)[0], Image.open(f).convert('RGB').resize((360,450))) for f in files]
rows=(len(ims)+cols-1)//cols; sheet=Image.new('RGB',(360*cols,480*rows),'white'); d=ImageDraw.Draw(sheet)
for i,(k,im) in enumerate(ims):
    x,y=(i%cols)*360,(i//cols)*480; sheet.paste(im,(x,y)); d.text((x+8,y+455),k,fill='black')
sheet.save(out,quality=85); print('sheet',len(ims),out)
