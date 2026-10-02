# AI UGC video: reference frame, talking avatar, voice, edit

How we make phone-style UGC videos with an AI presenter for a clinic offer, after the statics are approved. Built on a med-spa lip flip and per-unit tox run. Statics first, always: this is phase 13 work or a separate approved video wave, never part of the first slate.

## Rules that do not bend
- The presenter is an illustration of a patient experience, never a provider, never a before/after, never a result claim. Third-person captions if the client asks for them ("she", not "I got").
- No fabricated outcomes. Any "what it looks like" moment is an illustration or a clearly labelled animated explainer.
- Keys come from your secret manager at run time. Never paste one into a script, a doc or a chat.

## 1. Character (images first, approved before any video)
1. Build a reference board of real phone-shot creator frames for the target age and setting (car, kitchen, bathroom mirror, couch). Log every source URL. Exclude anyone recognisable (celebrities, public figures).
2. One-shot identity: edit a real reference frame into an original fictional person ("original fictional character", never "replace the woman", which trips content filters). The real frame supplies the framing, light, grain and phone lens; that is what makes it read as UGC.
3. Make 3 to 4 options per character, pick one, then render her in 3 to 5 settings from the same identity.
4. Run the image QC pass (`ad-creative-qc` or equivalent): no fake app UI, no covered mouth, nothing that reads as an AI before/after, gestures that match the script (pointing at the lips means the lips, not the cheek).

## 2. Script
- Hook, body, CTA as separate clips of 5 to 10 seconds. Pad each line to the clip length so the model does not ad-lib to fill time.
- CAPS on the one word that carries stress.
- Research the category's hooks and CTAs before writing. In tox, most top organic videos had no spoken CTA, and question CTAs drove comments; test a question CTA against "book" before assuming.
- Keep one locked prompt per character (setting, framing, wardrobe, delivery). Only the dialogue line changes between clips.

## 3. Talking avatar
- Image-to-video with native speech. Seedance 2.5 gave the most natural talking avatar; Gemini Omni Flash was second and cheaper per second. Have two providers ready: we lost a day to one provider's outage and another's credit balance.
- Seedance outputs 10-bit HEVC. Convert to 8-bit RGB before any colour work or the takes go grey.
- Expect ad-libs, dropped words and mis-hearings. Transcribe every take (Whisper word timestamps) and trim by words, not by eye. Re-roll any take that drops a key word (the offer name, the price).

## 4. Voice
- Voices drift between takes. Clone the best take's voice once (ElevenLabs instant clone from 30 to 60 seconds of the generated audio), then run every take through speech-to-speech with that clone. It keeps the model's timing, so lip sync holds.
- Use the multilingual speech-to-speech model if the English one blurs a term (it turned "lip flips" into "whip flips").
- The client usually prefers the character's original voice over any stock voice; clone it rather than swapping it.

## 5. Edit
- Colour-match every take to the first (per-take stats and a LUT), then a gentle grade: lower contrast, slightly lower saturation, lifted highlights, a little handheld shake. Over-clean footage reads as AI.
- Hide jump cuts with a small punch-in (about 1.08x) on alternate takes plus the colour match. A visible lighting change at a cut is the giveaway.
- Cutaways: an animated line-art explainer for the mechanism (labelled "Illustration") and a calm payoff shot of the character. No result shots.
- Export clean cuts with no burned captions plus an `.srt` sidecar. Burned captions landed on faces; captions go on later in the editor or platform where placement can be checked.
- 9:16 master, 4:5 crop, about -16 LUFS.

## 6. QC before the client sees it
Watch every cut at full speed with sound. Check: the price and offer name are spoken correctly, no ad-libbed claims, no lip-sync drift past a few frames, no colour jump at cuts, captions file matches the audio.

## Cost and time (one character, three hooks, two bodies, one CTA)
Roughly 8 to 12 clips with re-rolls, about $0.15 per second of 1080p on the cheaper provider, plus voice conversion. Plan a day for the first character and half a day for each one after, because the locked prompt and pipeline carry over.
