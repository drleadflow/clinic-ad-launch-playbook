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
- **Codex image_gen returns transparent PNGs and `codex exec` blocks on stdin.** The wrapper closes stdin (`< /dev/null`) and flattens alpha onto the paper colour before cropping. Rule: any new render backend gets a wrapper with the same four arguments and a live test before it enters the docs. Tool: `tools/codex-gen.sh`.
- **Confirm the ad account before building.** A client can have two: the previous agency's and yours. Ours had the client's own pixel and campaigns with our UTMs; the other had a bigger history and the same page and Instagram attached. The build went into the wrong one and was deleted. Rule: phase 0 records the account id, business name and pixel id together, and the build sheet control panel names the wrong account explicitly. Check `get_ad_accounts` for duplicates by client name.
- **Read history from the account you will spend in.** The previous agency's account said videos win; ours said the static price card wins and videos never got delivery. Benchmarks and control cells come from your own account.
- **Custom Audience TOS is per account and per user.** A fresh account cannot create website audiences until both are accepted in the browser. Do it during phase 0 setup, not on launch day.
- **Never put a judgement word about the viewer in a headline.** "Is it vain to want lip filler?" was disapproved (mislabelled as Financial by the automated reviewer; the real trigger is the personal-attribute read). Rule: hooks name the situation, never the viewer's trait. "Wanting a little more is allowed" passed the same gate. Keep a copy-only variant and an image variant ready so a disapproval costs one round trip, not a day.
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

## 2026-09-26 · MDW Botox run (second offer, same client)
- **Old creatives can point at dead pages.** The July Botox ads linked to a page that now 404s. Rule: before reusing any account winner as a control, read its link and curl it. Reuse the post only if the link is live; otherwise rebuild the creative from the video id with the live URL.
- **Advantage+ audience caps the hard age floor at 25.** Set `age_min` 25 and put the real range in `age_range` as a suggestion.
- **Story padding: sample the pad color from a known background zone**, not the canvas edge at mid-height (it hit a photo and padded a cream ad with grey). Sample just above the footer bar, and check dark-footer designs by hand.
- **Look at every page image before reusing it.** The offer page carried a treatment-room photo with another clinic's signage. Nothing from a client page goes on an ad unseen.
- **Second offer for the same client takes about a third of the time**: brand system, logo and provider media ids, audiences and ad set settings all carry over. Reuse them by id, change only the offer facts and age band.
