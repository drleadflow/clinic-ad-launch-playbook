# AGENTS.md — Clinic Ad Launch Playbook

You are running the Clinic Ad Launch Playbook for one med-spa offer. The method is in `docs/`, the run order and rules are in `skill/SKILL.md`. Read `skill/SKILL.md` first, then `docs/LESSONS.md`.

Rules that apply to every turn:
- Run `./tools/check-deps.sh` before the first render. Every required line must say ok.
- Report one line at every phase boundary and before every render batch. Do not run silently.
- Statics before motion. Motion is phase 13, winners only.
- Nothing on an image that is not on the client's page or a verified source. One price per image. Real before/afters only, unretouched, "Individual results vary." Zero em dashes anywhere.
- Never commit client prices, portraits, media ids, account ids or rendered creatives to this repo. They belong in the private assets repo and in `references/clients/<client>.md` (gitignored).
- Render with `tools/hf-gen.sh`. If a cell fails twice, change the recipe; do not roll a third time.
- Every phase writes its numbered file into `campaigns/<client>-<offer>-<MMDD>/` and one dated line into the lessons or daily log.

Platform notes for Codex are in `docs/14-run-on-codex.md`. Image generation in `docs/13-image-generation.md`.
