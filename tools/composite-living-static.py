"""Living static v3: animate ONLY a text-free photo box, put it back under the untouched text layer, export 1080x1350 and 1080x1920.
Usage: composite-living-static.py <master.png> <animated_crop.mp4> <overlay.png> <box "x0,y0,x1,y1"> <pad_ox> <canvas_w> <out_4x5.mp4> <out_9x16.mp4>
overlay.png = master with the photo box transparent; any text that overlaps the box is left opaque (protected patch).
animated_crop.mp4 = image-to-video whose start frame was the box padded to 9:16 with black bars (pad_ox = left bar, canvas_w = padded width)."""
import subprocess, sys
from PIL import Image
master, vid, overlay, box, pad_ox, canvas_w, out45, out916 = sys.argv[1:9]
x0, y0, x1, y1 = map(int, box.split(',')); pad_ox = int(pad_ox); canvas_w = int(canvas_w)
W, H = Image.open(master).size; bw, bh = x1 - x0, y1 - y0
fc = (f"[0:v]scale={canvas_w}:{bh}:flags=lanczos,crop={bw}:{bh}:{pad_ox}:0,setsar=1[p];"
      f"[1:v]scale={W}:{H}[m];[m][p]overlay={x0}:{y0}:shortest=1[base];"
      f"[2:v]scale={W}:{H}[o];[base][o]overlay=0:0:shortest=1,scale=1080:-2:flags=lanczos,pad=1080:1350:(ow-iw)/2:(oh-ih)/2:color=0x010302,format=yuv420p[out]")
subprocess.run(["ffmpeg", "-nostdin", "-y", "-v", "error", "-i", vid, "-loop", "1", "-i", master, "-loop", "1", "-i", overlay, "-filter_complex", fc, "-map", "[out]", "-c:v", "libx264", "-crf", "17", "-preset", "medium", "-r", "30", "-an", "-movflags", "+faststart", out45], check=True)
fc916 = "[0:v]pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=0x010302,format=yuv420p[out]"
subprocess.run(["ffmpeg", "-nostdin", "-y", "-v", "error", "-i", out45, "-filter_complex", fc916, "-map", "[out]", "-c:v", "libx264", "-crf", "17", "-preset", "medium", "-an", "-movflags", "+faststart", out916], check=True)
print("ok", out45, out916)
