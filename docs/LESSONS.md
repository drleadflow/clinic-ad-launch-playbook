# Lessons log (what changed the method, and why)

Dated. Newest first. Each entry names the run it came from and the rule it produced. Add to this file, never to memory.

## 2026-09-25 · MDW lip filler $399 (33 statics, Shift Framework, awareness audit, motion tests)
- **Statics before motion.** Animating before the slate was chosen burned credits on a layout that got redesigned twice. Rule: motion is a week-two decision on proven winners (phase 13), never part of production.
- **State the hero's size.** The first flat-lay had an empty centre. Rule: every layout prompt states the hero element's width as a percentage of frame and where the type stacks relative to it.
- **Belief-level angles were missing.** The 16-angle bank covers product and proof only. The Shift Framework (Core 6 beliefs) added time, money, help, cost of inaction and identity lanes and produced 13 statics in one pass. Rule: phase 14 runs after the first roster, before wave 2.
- **Awareness audit is a gate.** Mapping the slate to Schwartz's five stages showed zero unaware, thin problem-aware, no retargeting. Eight cells fixed it. Rule: phase 15, mandatory before the build sheet. Unaware and problem-aware cells carry no price and run in their own ad set with a soft CTA.
- **Deterministic text beats re-rolling.** Lifting the type as a diff mask (dark pixels, zone-restricted) from a generated static and compositing it onto a new background gave an exact result where a second generation drifted. Same layer burns onto video. Tools: `overlay-text-on-video.py`.
- **Higgsfield CLI traps.** Session expiry mid-batch; "failed" with no reason (retry once, then change the recipe: drop the portrait, shorten lines); `$399` eaten by the shell in a folder name (never put `$` in paths); zsh not splitting `$args` (wrapper is bash). Tool: `tools/hf-gen.sh`.
- **Notes-style cells duplicate lines.** Two of two runs. Fix in one refinement: shorter lines, "each line once, never repeated", eight lines max.
- **Lisa-portrait plus numbered procedure steps failed twice** on the render side. Rule: step lists go text-only; portraits carry a headline, not a procedure.
- **Packaging is the deliverable.** A build sheet with the exact landing URL in a copy block, primary text per cell, ad-set assignment, and a checklist the builder signs removed every "which page" question. A hub page links every artifact. Rule: phase 16.
- **Narrate.** A long silent run got "are you gonna tell me what you are doing" and a stop. Rule: one line at every phase boundary and before every batch render.
- **Fill Lisa's book first.** When a client has a new second provider, tag scripts PRACTICE vs PROVIDER so the practice-level ones re-shoot later without a rewrite.

## 2026-09-04 to 09-18 · TVAAI Endolaser, CO2, T-Shape, Mommy Tummy
- Price is a decision, not a fact: every price on the client sheet is marked live or unapproved; unapproved means no price on any ad.
- Device-led copy loses to offer-led copy. Lead with price, included, bonus.
- Never a computed total in a headline ("3 sessions × $X"); one price shape per image.
- A fabricated before/after on a synthetic model is a compliance failure, not a style choice. Real B/A only, unretouched, "Individual results vary."
- Excalidraw beats Figma for the creative board on a Starter plan (tool-call caps stalled a column).
- The client review page (in-feed mockups, approve / changes / notes) gets three answers in one send: slate, claims, budget.
- Ad Library video research: Apify scraper without a `fields` projection, dedupe by video URL, rank by days running × variants.
- Mirrored funnel pattern: page in the client's CRM, logic on a backend, tracking on both.
