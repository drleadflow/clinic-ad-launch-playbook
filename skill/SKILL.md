---
name: clinic-ad-launch
description: Run the Clinic Ad Launch Playbook end to end for one med-spa offer: research, remix, angles, belief shift, copy, statics, awareness audit, sizes, scorecard, build sheet and hub. Trigger on "run the ad workflow on <offer url>" or /clinic-ad-launch.
---

# Clinic Ad Launch (playbook skill)

Public method, private data. This skill runs the phases in `docs/` of the clinic-ad-launch-playbook repo. Client prices, portraits, media ids and account ids live in a private client sheet you create at `references/clients/<client>.md` (never commit it here).

## Before anything
0. Not on Claude Code? `docs/14-run-on-codex.md` and `AGENTS.md` cover Codex and other agents. Same tools, same phases.
1. `tools/check-deps.sh` must print no MISSING line.
2. Read the client sheet if it exists. If not, build it from the landing page (phase 0) before generating anything.
3. **Narrate.** Say one line at every phase boundary and before every render batch. Silence is a failure mode.
4. Dates and prices: every price is marked live or unapproved. Unapproved means no price on any ad.

## The laws (never break)
1. Nothing on an image that is not on the client's page or a verified source.
2. Every static follows the skeleton (`templates/prompts/skeleton-static.md`) or a named alternate style (`templates/prompts/flatlay-hero.md`, notes, forum card). Editorial photography inside a direct-response layout.
3. Copy passes the anti-slop and compliance gates (`docs/compliance/`). Zero em dashes. No apostrophes in big on-image headlines.
4. AI people must read human; real staff only with identity lock from a fresh reference. Real before/afters only, unretouched, "Individual results vary."
5. One price anchor per image, never a computed total.
6. Patient is the hero. Provider appears as a name line, hands, or one credential cell per set.

## Phases (write the numbered file, report one line, move on)
| # | Phase | Doc | Output |
|---|---|---|---|
| 0 | Intake | `docs/00-workflow-map.md` | `00-client-sheet.md` (private) |
| 1 | Research | `docs/01-research.md` | `01-research.md`: 20+ library ads with days live, competitor prices, 10+ VOC lines, open lanes |
| 2 | Remix | `docs/02-remix-pack.md` | `02-remix-pack.md` + `03-scripts.md` |
| 3 | Angles | `docs/03-angles-and-roster.md` | `10-angle-bank.md`, `11-roster.md` |
| 4 | Strategy | `docs/04-creative-strategy.md` | `09-creative-strategy.md`, `06-creative-framework.md` |
| 5 | Copy | `docs/05-copy.md` | `03-copy.md` |
| 6 | Produce wave 1 | `docs/06-production.md` | `creative/` masters via `tools/hf-gen.sh`, QA sheet via `tools/contact-sheet.py` |
| 7 | QA + grade | `docs/07-grading.md` | `12-scorecard.md` |
| 8 | Sizes + board | `docs/06-production.md` | `tools/make-sizes.py`, `tools/make-board.py` |
| 9 | Benchmark | `docs/08-benchmark.md` | `13-library-benchmark.md` |
| 14 | **Belief shift** | `docs/10-belief-shift.md` | `13-shift-framework.md` (+ `tools/shift-docx.py` for the Word version) → wave 2 statics (one per Core 6 belief, two visual systems) |
| 15 | **Awareness audit** | `docs/11-awareness-audit.md` | five-stage table → wave 3 (unaware, problem aware, retargeting), no price on the cold ends |
| 10 | Launch + workout | `docs/09-launch-and-workout.md` | `04-launch-doc.md`, `05-workout-plan.md` |
| 16 | **Package + handoff** | `docs/12-package-and-handoff.md` | build sheet + hub (`templates/handoff/`), delivery folder, private repo commit |
| 11 | Client review | `templates/review-page/` | three approvals: slate, claims, budget |
| 12 | Build | `docs/09-launch-and-workout.md` | paused campaign, pre-flight signed, owner activates |
| 13 | Weeks 1 to 4 | workout plan | motion versions of winners only now (`tools/living-static-particles.py`, `tools/overlay-text-on-video.py`) |

## Production rules (from `docs/LESSONS.md`; full guide in `docs/13-image-generation.md`)
- Render with `tools/hf-gen.sh <cell> <dir> "<refs>" "<prompt>"` (Higgsfield) or `tools/codex-gen.sh` with the same arguments on Codex (local reference files only). It retries once on failure and refreshes an expired session. A second failure means change the recipe, not re-roll.
- Prompt structure: `[VISUAL SYSTEM] → [IDENTITY LOCK] → [LAYOUT with exact quoted strings and the hero's size as a percentage] → [LIGHTING] → [QUALITY] → [AVOID]`.
- Notes-style cells: eight lines max, "each line once, never repeated".
- Portrait cells carry a headline, not a numbered procedure (fails on the render side).
- Text drift on a regenerate: lift the type from the good version as a diff mask and composite it. Do not roll a third time.
- Never `$` in a folder name.
- Statics before motion. Motion is phase 13.

## Handoff rules
- The build sheet opens with the landing URL alone in a code block and the four-step verify procedure.
- Every cell has its primary text and headline on the build sheet, not in a separate file.
- Unaware and problem-aware cells: own ad set, no price, Learn More. Retargeting: own set, warm only, Book Now.
- A hub page links every artifact and converts the campaign markdown into sub-pages.
- Log every phase to your daily log; milestones to the client note.
