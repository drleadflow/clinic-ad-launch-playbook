#!/usr/bin/env bash
# Higgsfield CLI wrapper for static generation. Bash, not zsh, on purpose (zsh does not split "$args").
# usage: hf-gen.sh <cell-id> <out-dir> "<ref1,ref2,...>" "<prompt>"   [MODEL=nano_banana_pro] [ASPECT=4:5] [RES=2k]
# refs = comma list of Higgsfield media ids or local image paths. Writes <out-dir>/<cell>.png and <out-dir>/jobs/<cell>.json
# Retries once on "failed" or "Session expired" (after `higgsfield auth token`). Exit 1 if still failed.
set -u
cell="$1"; out="$2"; refs="$3"; prompt="$4"
MODEL="${MODEL:-nano_banana_pro}"; ASPECT="${ASPECT:-4:5}"; RES="${RES:-2k}"
mkdir -p "$out/jobs"
args=(); IFS=',' read -ra R <<< "$refs"; for r in "${R[@]}"; do [ -n "$r" ] && args+=(--image-references "$r"); done
run() {
  timeout 600 higgsfield generate create "$MODEL" --aspect_ratio "$ASPECT" --resolution "$RES" "${args[@]}" --wait --json --prompt "$prompt" > "$out/jobs/$cell.json" 2>&1
  python3 - "$out/jobs/$cell.json" "$out/$cell.png" "$cell" <<'PY'
import json,re,subprocess,sys
s=open(sys.argv[1]).read(); m=re.search(r'\[\s*\{.*\}\s*\]',s,re.S)
j=json.loads(m.group(0))[0] if m else {}
u=j.get('result_url'); st=j.get('status')
if u:
    subprocess.run(['curl','-s','-L','-o',sys.argv[2],u]); print(sys.argv[3],'ok',u); sys.exit(0)
print(sys.argv[3],'FAILED',st or s[-200:].replace('\n',' ')); sys.exit(2)
PY
}
run && exit 0
if grep -q "Session expired" "$out/jobs/$cell.json"; then higgsfield auth token >/dev/null 2>&1 || echo "run: higgsfield auth login"; fi
echo "$cell retry"; run && exit 0
echo "$cell failed twice: change the recipe (drop the portrait, shorten lines), do not re-roll a third time"; exit 1
