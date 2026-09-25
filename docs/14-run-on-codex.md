# Running the playbook on Codex (or any agent that is not Claude Code)

The method is markdown, shell tools and Python. Nothing in it needs a specific agent. What changes per platform is where the instructions live and how the agent reaches Meta, Notion, Apify and Drive.

## Codex CLI
1. **Instructions.** Codex reads `AGENTS.md` at the repo root (included here). It also loads skills from `~/.codex/skills/<name>/SKILL.md` with the same frontmatter as Claude Code skills:
   ```bash
   cp -r skill ~/.codex/skills/clinic-ad-launch
   ```
2. **Tools.** Same shell: `./tools/check-deps.sh`, `tools/hf-gen.sh`, `tools/contact-sheet.py`, `tools/make-sizes.py`, `tools/shift-docx.py`. Codex runs bash directly, so the Higgsfield path is identical.
3. **MCP servers.** Add them once:
   ```bash
   codex mcp add meta-ads   -- <command that starts your Meta Ads MCP server>
   codex mcp add notion     -- <command for the Notion MCP server>
   codex mcp add apify      -- <command for the Apify MCP server>
   codex mcp list
   ```
   Or edit `~/.codex/config.toml` under `[mcp_servers.<name>]` with `command`, `args`, `env`. Codex plugins already cover Google Drive on some installs (`plugins."google-drive@openai-curated"`), which replaces the Drive MCP for delivery.
4. **Images.** Two paths. (a) Higgsfield CLI exactly as `docs/13-image-generation.md`, no MCP needed. (b) Codex's built-in `image_gen` tool through `tools/codex-gen.sh`, the twin of `hf-gen.sh` with the same four arguments:
   ```bash
   tools/codex-gen.sh <cell> <out-dir> "<ref1.png,ref2.png>" "<prompt>"     # ASPECT=4:5 by default
   ```
   It runs `codex exec` non-interactively (stdin closed, `-s workspace-write`, approvals off), tells the agent to call `image_gen` once with your references as `referenced_image_paths`, copies the PNG into `<out-dir>/<cell>.raw.png`, flattens the (usually transparent) PNG onto the paper colour (`BG=FCFAF4` by default, pass another hex for dark cells), then cover-crops to the aspect as `<cell>.png`. Tested 2026-09-25: about 50 seconds per render, output 1122x1402 (already 4:5), strings rendered exactly, reference logo placed. Differences from Higgsfield: references must be local files (no media ids), no 2k option, no identity-lock guarantee for real people (verify on the contact sheet), and each render spends your ChatGPT plan's image budget. Portrait cells still belong on Higgsfield until you have checked identity drift on Codex yourself.
5. **Reading images.** Codex can view local PNGs; point it at the contact sheet the same way. The QA gate is the same: strings exact, one price, real photos unaltered.
6. **Narration.** Codex is quieter by default. The skill's "one line per phase boundary" rule still applies; ask it to report before every render batch.

## Other agents (Gemini CLI, Hermes, OpenClaw)
Give them `AGENTS.md` (or their equivalent system file) plus `skill/SKILL.md` as context, connect whatever MCP or tool bridge they use for Meta and Notion, and keep the tools directory on PATH. The campaign folder, the numbered files and the gates are the contract; the agent is interchangeable.

## What does not transfer
Private client sheets, media ids and account ids. Recreate `references/clients/<client>.md` on the new machine from the private assets repo before phase 1.
