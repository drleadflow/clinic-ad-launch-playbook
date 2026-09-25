#!/usr/bin/env bash
# Run before a launch. Every line must say ok.
ok(){ printf '  ok   %s\n' "$1"; }; bad(){ printf '  MISSING  %s  -> %s\n' "$1" "$2"; F=1; }; F=0
echo "Clinic Ad Launch Playbook: dependency check"
command -v python3 >/dev/null && ok "python3" || bad "python3" "brew install python"
python3 -c "import PIL" 2>/dev/null && ok "Pillow" || bad "Pillow" "pip3 install -r requirements.txt"
python3 -c "import numpy" 2>/dev/null && ok "numpy" || bad "numpy" "pip3 install -r requirements.txt"
python3 -c "import docx" 2>/dev/null && ok "python-docx" || bad "python-docx" "pip3 install -r requirements.txt"
command -v ffmpeg >/dev/null && ok "ffmpeg" || bad "ffmpeg" "brew install ffmpeg"
command -v higgsfield >/dev/null && ok "higgsfield CLI $(higgsfield --version 2>/dev/null | cut -d' ' -f2)" || bad "higgsfield CLI" "npm i -g @higgsfield/cli"
if command -v higgsfield >/dev/null; then higgsfield auth token >/dev/null 2>&1 && ok "higgsfield session" || bad "higgsfield session" "higgsfield auth login (browser)"; fi
[ -n "${APIFY_TOKEN:-}" ] && ok "APIFY_TOKEN" || echo "  note  APIFY_TOKEN not set: Ad Library and Reddit sweeps run through the Apify MCP instead"
command -v git >/dev/null && ok "git" || bad "git" "xcode-select --install"
command -v gh >/dev/null && ok "gh" || echo "  note  gh not installed (only needed to push the private assets repo)"
ls ~/Library/CloudStorage/GoogleDrive-* >/dev/null 2>&1 && ok "Google Drive desktop mounted" || echo "  note  no Google Drive mount: deliver creatives via a shared folder of your choice"
echo; echo "MCP servers this skill expects in the agent (not checkable from shell): Meta Ads, Notion, Apify, Google Drive."
[ $F -eq 0 ] && echo "All required dependencies present." || { echo "Fix the MISSING lines first."; exit 1; }
