# Clinic Ad Launch Playbook

**The four-day ad launch system we run for med spas, aesthetic clinics and IV bars. Every phase, every rule, every prompt.**

Most clinic ads fail the same way: no research trail, copy invented from nothing, a pile of PNGs instead of a plan, and a client who cannot tell what they are approving. This repo is the fix we use at [Dr. Lead Flow](https://doctorleadflow.com). It turns a landing page and a price list into a graded, sized, compliance-checked wave of ads with a launch document and a four-week decision plan, in about four working days.

Use it yourself with the templates below, or [have us run it for your clinic](https://doctorleadflow.com).

## The map

```
0 Intake ─► 1 Research ─► 2 Remix ─► 3 Angles ─► 4 Strategy ─► 5 Copy
        ─► 6 Produce ─► 7 QA + Grade ─► 8 Sizes + Board ─► 9 Benchmark
        ─► 10 Launch doc + Workout ─► 11 Client review ─► 12 Build ─► 13 Weeks 1–4
```

| Day | Phases | Output |
|---|---|---|
| 1 | 0 to 3 | client sheet, research brief, remix pack, 40+ angle roster |
| 2 | 4 to 7 | 12-cell creative matrix, copy, 12 rendered statics, scorecard |
| 3 | 8 to 11 | feed + story sizes, creative board, benchmark, launch doc, review page |
| 4 to 5 | 12 | build, pre-flight, activate on the owner's go |

Read the phases in order in [docs/](docs/00-workflow-map.md). Each one says what goes in, what comes out, and the gate that must pass before the next.

## The four laws (everything else follows)

1. **The patient is the hero.** The headline is her sentence, not the provider's résumé. The provider appears as a gloved hand, a handpiece, or a name line. One credential ad per set, no more.
2. **Open on a belief she already holds.** "Creams did nothing." "Lasers burn." "Non-invasive is a Groupon." Move her one step, never leap.
3. **One ad, one desire.** Mechanism, identity, honesty. Claims are dead in a market where every page says "radiant".
4. **Honesty is the differentiator nobody in your city is using.** Publish the downtime. Say "a course" before the sale. Name the risk. It reads as authority because it is.

## What is in here

- `docs/` the method, phase by phase, with gates and time budgets
- `docs/compliance/` the med-spa claims checklist (FDA wording, before/after, financing disclosures, pixel and PHI)
- `templates/campaign-folder/` the numbered files every launch produces
- `templates/prompts/` the static-ad prompt skeletons for any image model
- `templates/review-page/` the client review page: every ad as an in-feed mockup with approve, changes, notes
- `tools/` `make-sizes.py` (feed 4:5 and story 9:16 with safe zones), `make-board.py` (Excalidraw creative board), research recipes for the Ad Library and Reddit
- `examples/` a filled scorecard and benchmark so you can see what "done" looks like

## What is not in here

Client prices, portraits, media ids, account ids and approvals. Those live in the private side of the practice you run this for. The templates use `<client>`, `<offer>`, `<city>` on purpose.

## Run your first launch

1. Copy `templates/campaign-folder/` to `campaigns/<client>-<offer>-<MMDD>/`.
2. Fill `01-research.md` from the landing page, the Ad Library and the forums (recipes in `tools/`).
3. Work through docs 03 to 09. Do not skip the scorecard.
4. Build the review page, send one link, ask for three things: the slate, the claims, the budget.
5. Launch paused, pre-flight every box, activate on the owner's go, then follow the workout plan.

## License

Docs and templates: [CC BY-NC 4.0](LICENSE-DOCS.md). Scripts: [MIT](LICENSE). Share it, adapt it, do not resell it.

Built by [Dr. Lead Flow](https://doctorleadflow.com), an AI lead-generation agency for health professionals.
