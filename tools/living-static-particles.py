"""Living static, procedural: slow push-in + warm gold glitter/bokeh drift over a finished master.
No AI touches the master, so real patient photos, identity-locked staff and all text stay exact.
Usage: living-static-particles.py <master.png> <out_4x5.mp4> <out_9x16.mp4> [seconds=6] [fps=30] [push=1.04] [density=140]
"""
import sys, subprocess, numpy as np
from PIL import Image, ImageFilter
master_path, out45, out916 = sys.argv[1:4]
secs = float(sys.argv[4]) if len(sys.argv) > 4 else 6; fps = int(sys.argv[5]) if len(sys.argv) > 5 else 30
push = float(sys.argv[6]) if len(sys.argv) > 6 else 1.04; density = int(sys.argv[7]) if len(sys.argv) > 7 else 140
W, H = 1080, 1350
m = Image.open(master_path).convert('RGB'); m = m.resize((W, round(m.height * W / m.width)), Image.LANCZOS)
if m.height != H:  # centre-crop or pad to 4:5
    if m.height > H: t = (m.height - H) // 2; m = m.crop((0, t, W, t + H))
    else: c = Image.new('RGB', (W, H), m.getpixel((5, 5))); c.paste(m, (0, (H - m.height) // 2)); m = c
n = int(secs * fps); rng = np.random.default_rng(7)
# particles: x, y (in canvas px), radius, speed (px/frame up), drift (px/frame x), phase, brightness
P = np.stack([rng.uniform(0, W, density), rng.uniform(0, H, density), rng.uniform(2.5, 11, density),
              rng.uniform(0.25, 1.2, density), rng.uniform(-0.25, 0.25, density), rng.uniform(0, 6.28, density),
              rng.uniform(0.35, 1.0, density)], axis=1)
gold = np.array([214, 168, 74], dtype=np.float32)
def sprite(r):
    s = int(r * 4) | 1; yy, xx = np.mgrid[:s, :s]; c = s // 2
    g = np.exp(-((xx - c) ** 2 + (yy - c) ** 2) / (2 * (r * 0.9) ** 2)); return g.astype(np.float32)
enc = subprocess.Popen(["ffmpeg", "-nostdin", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                        "-r", str(fps), "-i", "-", "-c:v", "libx264", "-crf", "17", "-preset", "medium", "-an", "-pix_fmt", "yuv420p",
                        "-movflags", "+faststart", out45], stdin=subprocess.PIPE)
base = np.asarray(m).astype(np.float32)
for i in range(n):
    t = i / max(n - 1, 1); z = 1 + (push - 1) * t  # linear push-in
    cw, ch = int(W / z), int(H / z); x0, y0 = (W - cw) // 2, (H - ch) // 2
    frame = np.asarray(m.crop((x0, y0, x0 + cw, y0 + ch)).resize((W, H), Image.LANCZOS)).astype(np.float32)
    for x, y, r, sp, dr, ph, br in P:
        yy = (y - sp * i) % (H + 20) - 10; xx = (x + dr * i + 6 * np.sin(ph + i * 0.05)) % W
        tw = br * (0.55 + 0.45 * np.sin(ph + i * 0.12))  # twinkle
        s = sprite(r); h, w = s.shape; ix, iy = int(xx) - w // 2, int(yy) - h // 2
        xa, ya = max(ix, 0), max(iy, 0); xb, yb = min(ix + w, W), min(iy + h, H)
        if xb <= xa or yb <= ya: continue
        sub = s[ya - iy:yb - iy, xa - ix:xb - ix][..., None] * tw
        frame[ya:yb, xa:xb] = frame[ya:yb, xa:xb] * (1 - sub * 0.95) + gold * sub * 0.95
    enc.stdin.write(np.clip(frame, 0, 255).astype(np.uint8).tobytes())
enc.stdin.close(); enc.wait()
subprocess.run(["ffmpeg", "-nostdin", "-y", "-v", "error", "-i", out45, "-vf", "pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=0x010302,format=yuv420p",
                "-c:v", "libx264", "-crf", "17", "-preset", "medium", "-an", "-movflags", "+faststart", out916], check=True)
print("ok", out45, out916)
