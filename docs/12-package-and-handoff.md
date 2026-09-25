# 16 · Package and handoff (Notion build sheet + hub)

**When:** after the slate is final. **Time:** 1 hour. **Output:** two Notion pages (or equivalent), a delivery folder, a private repo commit.

The deliverable is not the PNGs. It is a document a stranger can build the campaign from without asking a question.

## The build sheet (one page, in this order)
0. **The landing URL alone**, in a code block, with UTMs, and the four-step procedure to set it and verify it (paste, add `utm_content={{ad.name}}` in the parameters field, open the preview, check the address bar).
1. Control panel: every ID (ad account, page, IG, pixel, CRM location), objective, geo, audience, budget, launch decision.
2. Allowed claims vs never-say list.
3. Campaign build: naming, settings that apply to every ad (Standard Enhancements off, one text + one headline), ad sets with cells assigned, CTA and budget per set.
4. Creative roster: every cell with the primary text and headline to paste, the shared closing line, files by folder, which cells launch first.
5. Pre-flight checklist the builder signs, ending with "saved as paused, owner flips it on".
6. Success and kill lines.
7. Blockers the client signs before spend.
8. Compliance guardrails.
9. Where everything lives.

## The hub (one page)
A table of every artifact in phase order with a link each: research, remix, strategy, angle bank, Shift Framework, copy, creatives folder, scorecard, build sheet. Then client context pages, account IDs, the slate by wave, open items, a dated status log. Convert the campaign markdown files into sub-pages so nothing lives only on disk.

## Delivery folder
`masters/`, `feed-4x5/`, `story-9x16/`, `motion/`, `docs/`, plus the contact sheet at the root. Do not put `$` in the folder name (the shell eats it).

## Gate
A second person opens the build sheet cold and can name the landing URL, the ad sets, and the first twelve ads without asking. Templates: `templates/handoff/`.
