# 06 · Production (2 to 3 hours per 12)

Any capable image model works; we use Higgsfield's image models at 2k. Prompt structure, always: `[VISUAL SYSTEM]` (palette, type, lighting, layout, locked) → `[IDENTITY LOCK]` when a real person appears → `[LAYOUT top to bottom]` with every on-image string in quotes → `[LIGHTING]` (direction, quality, Kelvin, lens) → `[QUALITY]` → `[AVOID]`. Templates in `templates/prompts/`.

Loop: batch of six → wait → download → contact sheet → read it → at most two refinements per index → reword instead of re-rolling a text defect → deliver masters.

Real staff: attach the portrait as a reference, lock likeness, and QA the crop against the reference. A media id that has been through a failed real-face job is poisoned; re-upload. Never feed staff portraits to automated ad engines that reject faces.

Human-looking AI people: real skin micro-texture, natural asymmetry, stated ages, average builds, dignified, eyes open, no distress, no before/after.

Video: three paths. Edit what you own (caption cuts, opener swaps, end cards). Fully AI units (UGC on a mirror, on the table, notes-to-voice). Clinician units (walk-and-talk, founder launch, authority desk) which need a 60-second phone clip or an identity-locked avatar.

Organic reel to paid ad (edit what you own): pull the client's best procedure reels, strip the audio (commercial tracks get blocked in paid placements), generate an instrumental bed with a licensed music model and confirm it has no vocals, keep the clinic's own burned-in hook, add a 2 to 3 second end card in the offer's visual system (price, the deposit action, physician line, address), crossfade into it, normalise to about -16 LUFS, export 9:16 at 1080x1920 and a 4:5 crop that keeps the logo and hook text in frame, with the 9:16 fine print above the bottom UI zone. Gates before it runs: patient ad consent for every face, and the treatment mode confirmed when the footage or overlay names a depth.
