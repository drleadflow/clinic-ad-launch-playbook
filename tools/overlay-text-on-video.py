#!/usr/bin/env python3
"""Lift the text layer (static minus background) and burn it over an AI-animated
background video. Aligns the video to the background by brute-force scale/offset
search on a downscaled luminance image, then writes feed 4:5 and story 9:16.

usage: overlay-text-on-video.py <bg.png> <static.png> <anim.mp4> <out_4x5.mp4> <out_9x16.mp4> [thresh=40]
"""
import sys, subprocess, json
import numpy as np
from PIL import Image, ImageChops, ImageFilter

bg_p, st_p, vid_p, out45, out916 = sys.argv[1:6]
TH = int(sys.argv[6]) if len(sys.argv) > 6 else 40
W, H = 1080, 1350

bg = Image.open(bg_p).convert("RGB"); st = Image.open(st_p).convert("RGB")
diff = np.asarray(ImageChops.difference(bg, st)).max(axis=2)
mask = Image.fromarray(((diff > TH) * 255).astype("uint8")).filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.GaussianBlur(0.8))
text = Image.merge("RGBA", (*st.split(), mask))

probe = json.loads(subprocess.check_output(["ffprobe","-v","error","-select_streams","v:0","-show_entries","stream=width,height,r_frame_rate,nb_frames","-of","json",vid_p]))["streams"][0]
vw, vh = probe["width"], probe["height"]; fps = eval(probe["r_frame_rate"])

# --- align: find scale s and offset (ox,oy) so that bg*s crop matches frame 0 ---
f0 = subprocess.check_output(["ffmpeg","-v","error","-i",vid_p,"-frames:v","1","-f","rawvideo","-pix_fmt","rgb24","-"])
f0 = Image.frombytes("RGB",(vw,vh),f0)
def lum(im, w): return np.asarray(im.convert("L").resize((w, round(im.height*w/im.width)), Image.BILINEAR), dtype=np.float32)
small_f = lum(f0, 160); best = (1e18, None)
for s in np.linspace(0.85, 1.15, 31):          # video scale relative to "bg width == frame width"
    bw = round(160 * s); sb = lum(bg, bw)
    if sb.shape[0] < small_f.shape[0] or sb.shape[1] < small_f.shape[1]: continue
    for oy in range(0, sb.shape[0]-small_f.shape[0]+1, 2):
        for ox in range(0, sb.shape[1]-small_f.shape[1]+1, 2):
            e = np.abs(sb[oy:oy+small_f.shape[0], ox:ox+small_f.shape[1]] - small_f).mean()
            if e < best[0]: best = (e, (s, ox, oy))
err, (s, ox, oy) = best
scale = vw / (bg.width * s)                     # bg px -> video px
print(f"align err={err:.2f} scale={s:.3f} off=({ox},{oy}) at 160px", file=sys.stderr)
# text layer in video coordinates
tw, th = round(bg.width*scale), round(bg.height*scale)
text_v = text.resize((tw, th), Image.LANCZOS)
OX, OY = round(ox/160*bg.width*scale), round(oy/160*bg.width*scale)
layer = Image.new("RGBA", (vw, vh), (0,0,0,0)); layer.paste(text_v, (-OX, -OY), text_v)
layer.save(out45 + ".textlayer.png")

def fit_cover(im, W, H):
    k = max(W/im.width, H/im.height); r = im.resize((round(im.width*k), round(im.height*k)), Image.LANCZOS)
    x = (r.width-W)//2; y = (r.height-H)//2; return r.crop((x, y, x+W, y+H))

dec = subprocess.Popen(["ffmpeg","-v","error","-i",vid_p,"-f","rawvideo","-pix_fmt","rgb24","-"], stdout=subprocess.PIPE)
enc = subprocess.Popen(["ffmpeg","-v","error","-y","-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-r",str(fps),"-i","-","-c:v","libx264","-pix_fmt","yuv420p","-crf","17","-movflags","+faststart",out45], stdin=subprocess.PIPE)
n = 0
while True:
    raw = dec.stdout.read(vw*vh*3)
    if len(raw) < vw*vh*3: break
    fr = Image.frombytes("RGB", (vw, vh), raw).convert("RGBA"); fr.alpha_composite(layer)
    enc.stdin.write(fit_cover(fr.convert("RGB"), W, H).tobytes()); n += 1
enc.stdin.close(); enc.wait(); dec.wait()
cream = bg.getpixel((10, 10))
subprocess.run(["ffmpeg","-v","error","-y","-i",out45,"-vf",f"pad=1080:1920:0:285:color=#{cream[0]:02x}{cream[1]:02x}{cream[2]:02x}","-c:v","libx264","-pix_fmt","yuv420p","-crf","17","-movflags","+faststart",out916], check=True)
print("ok", n, "frames", out45, out916)
