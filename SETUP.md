# Setup: run this playbook on a fresh machine

Target: a new ad manager or agent clones this repo and produces the same outputs as the reference runs (TVAAI Endolaser/CO2/T-Shape/Mommy Tummy, MDW lip filler) with no tribal knowledge.

## 1. Tools
```bash
brew install python ffmpeg
pip3 install -r requirements.txt
npm i -g @higgsfield/cli && higgsfield auth login     # browser OAuth; sessions expire, re-run when a job says "Session expired"
./tools/check-deps.sh                                   # every required line must say ok
```

## 2. Agent (Claude Code) and MCP servers
Install the skill so the agent runs the phases in order:
```bash
cp -r skill ~/.claude/skills/clinic-ad-launch
```
Connect these MCP servers in the agent: **Meta Ads** (account history, later the paused build), **Apify** (Ad Library and Reddit sweeps), **Notion** (build sheet and hub), **Google Drive** (delivery folder). Optional: NotebookLM CLI (`nlm`) if you keep an ad brain notebook.

## 3. Private side (never in this repo)
Client prices, portraits, media ids, account ids, approvals and rendered creatives live in a private assets repo (we use `clinic-ad-launch-ops`) and in the agent's private client sheet (`references/clients/<client>.md`). This repo holds the method only.

## 4. First run
```bash
cp -r templates/campaign-folder campaigns/<client>-<offer>-<MMDD>
```
Then follow `skill/SKILL.md` phase by phase. Each phase writes its numbered file and reports one line before moving on.
