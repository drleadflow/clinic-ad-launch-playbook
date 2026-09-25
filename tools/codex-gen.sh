#!/usr/bin/env bash
# Codex twin of hf-gen.sh: renders one static with Codex's built-in image_gen tool (ChatGPT login, no API key).
# usage: codex-gen.sh <cell-id> <out-dir> "<ref1.png,ref2.png,...>" "<prompt>"     [ASPECT=4:5] [BG=FCFAF4] [MODEL=<codex model>]
# image_gen often returns a transparent PNG; the wrapper flattens it onto BG (hex, default cream paper) before cropping.
# refs must be LOCAL FILES (image_gen takes referenced_image_paths); Higgsfield media ids do not work here.
# Output: <out-dir>/<cell>.png cover-cropped to ASPECT (image_gen returns 1024x1536 or 1536x1024), plus <out-dir>/jobs/<cell>.codex.txt
# Retries once. Exit 1 if no image came back.
set -u
cell="$1"; out="$(cd "$(mkdir -p "$2" && echo "$2")" && pwd)"; refs="$3"; prompt="$4"
ASPECT="${ASPECT:-4:5}"; BG="${BG:-FCFAF4}"; MODEL="${MODEL:-}"
mkdir -p "$out/jobs"
paths=(); IFS=',' read -ra R <<< "$refs"
for r in "${R[@]}"; do
  [ -z "$r" ] && continue
  if [[ "$r" =~ ^[0-9a-f]{8}-[0-9a-f]{4}- ]]; then echo "$cell: '$r' is a Higgsfield media id; codex-gen needs local files" >&2; exit 3; fi
  [ -f "$r" ] || { echo "$cell: reference not found: $r" >&2; exit 3; }
  paths+=("$(cd "$(dirname "$r")" && pwd)/$(basename "$r")")
done
reflist=""; n=1
for p in "${paths[@]}"; do reflist+="Reference image $n: $p"$'\n'; n=$((n+1)); done
target="$out/$cell.raw.png"
instr="You are a render worker. Do exactly this and nothing else:
1. Call the image_gen tool ONCE. referenced_image_paths = every path listed under References (in that order; the prompt refers to them as FIRST, SECOND). Portrait orientation. Prompt = everything between <prompt> and </prompt>, verbatim.
2. Copy the generated PNG to exactly this path: $target
3. Reply with only that path. No commentary, no extra files, no edits to the prompt.
References:
${reflist:-(none)}
<prompt>
$prompt
</prompt>"
run() {
  local start; start=$(date +%s)
  codex exec --skip-git-repo-check -C "$out" -s workspace-write -c approval_policy='"never"' ${MODEL:+-m "$MODEL"} -o "$out/jobs/$cell.codex.txt" "$instr" < /dev/null > "$out/jobs/$cell.codex.log" 2>&1
  if [ ! -s "$target" ]; then   # fallback: newest generated image since start
    local f; f=$(find ~/.codex/generated_images -name '*.png' -newermt "@$start" -print0 2>/dev/null | xargs -0 ls -t 2>/dev/null | head -1)
    [ -n "$f" ] && cp "$f" "$target"
  fi
  [ -s "$target" ]
}
run || { echo "$cell retry"; run; } || { echo "$cell failed twice: change the recipe; see $out/jobs/$cell.codex.log"; exit 1; }
python3 - "$target" "$out/$cell.png" "$ASPECT" "$BG" <<'PY'
import sys; from PIL import Image
src,dst,asp,bg=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]; aw,ah=[int(x) for x in asp.split(':')]
im=Image.open(src)
if im.mode in ("RGBA","LA","P"):
    im=im.convert("RGBA"); base=Image.new("RGBA",im.size,tuple(int(bg[i:i+2],16) for i in (0,2,4))+(255,)); base.alpha_composite(im); im=base
im=im.convert('RGB'); W,H=im.size; t=aw/ah
if W/H>t: nw=round(H*t); x=(W-nw)//2; im=im.crop((x,0,x+nw,H))
else: nh=round(W/t); y=(H-nh)//2; im=im.crop((0,y,W,y+nh))
im.save(dst); print(f"{dst} {im.size[0]}x{im.size[1]} (raw {W}x{H})")
PY
echo "$cell ok"
