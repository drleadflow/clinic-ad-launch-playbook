# Image generation: Higgsfield first, any model second

The playbook renders statics with the Higgsfield CLI. Nothing in the method depends on Higgsfield specifically; it depends on a model that (a) takes reference images, (b) renders exact quoted strings, (c) returns a URL you can curl. Swap the model, keep the recipe.

## Higgsfield CLI (the reference path)
```bash
npm i -g @higgsfield/cli
higgsfield auth login            # browser OAuth. Sessions expire; a job that prints "Session expired" needs this again
higgsfield model list            # image models include nano_banana_pro, gpt_image_2_5, flux_2
higgsfield model get nano_banana_pro   # accepted params for a job type
higgsfield upload create ./lisa.jpg    # -> media id (UUID). Use ids for anything reused across cells
```
**References.** `--image-references` takes a UUID or a local path (paths auto-upload). Order matters: the prompt says "the FIRST reference image is…", "the SECOND reference image (logo)…". Reuse one uploaded id for a real person across the whole run so identity stays consistent. A stale id that starts producing drift is "poisoned": upload again.

**Statics.** `nano_banana_pro`, `--aspect_ratio 4:5`, `--resolution 2k`, `--wait --json`. Text rendering is the best of the models we have tried; it still duplicates lines in list-style layouts, so keep lists short and say "each line once".

**Edits.** To change one thing on an existing image, pass that image as the first reference and write the prompt as an edit: "Edit the reference image and change nothing else: remove X, extend the marble…". This is how vials were removed from a flat-lay and how a CTA was moved inside a table without touching the rest.

**Video from a still.** `seedance_2_0 --start-image bg.png --aspect_ratio 3:4 --resolution 1080p --duration 5 --generate_audio false`. Image-to-video models do not offer 4:5; render 3:4 and let the compositor cover-crop. Never animate text. Animate a text-free background, then burn the text layer per frame (`tools/overlay-text-on-video.py`).

**The wrapper.** `tools/hf-gen.sh <cell> <out-dir> "<ref1,ref2>" "<prompt>"` runs one job, parses the JSON, downloads the PNG, retries once on failure or session expiry, and refuses a third roll. Run several cells in parallel with `&` and `wait`. Then `tools/contact-sheet.py qa.jpg 4 out/*.png` and look at the sheet before anything else.

## The prompt recipe (model-independent)
```
[VISUAL SYSTEM] style, palette, typography, "editorial photography inside a direct-response layout"
[PHOTO or IDENTITY LOCK] which reference is which; "use unaltered", "do not retouch the lips", or the identity lock for a real person
[LAYOUT top to bottom] numbered elements, every on-image string in single quotes, the hero's size as a percentage of frame
[LIGHTING] one line
[QUALITY] "all text crisp, correctly spelled, exactly the quoted strings and nothing else; one price only; no cut-off text; no duplicated lines"
[AVOID] the model's failure modes for this layout (extra objects, people, brand names, syringes, emojis, watermark)
```
Skeletons in `templates/prompts/`. Batch of 5 to 8, one QA sheet, at most one refinement per cell. If the second render still drifts, stop rolling: lift the good text as a diff mask and composite it (`overlay-text-on-video.py` does this for video; the same PIL logic works on a still).

## Failure modes we have hit, and the rule each produced
| Symptom | Rule |
|---|---|
| "Session expired" mid-batch | wrapper refreshes the token and retries; if it persists, `higgsfield auth login` |
| status "failed", no reason, twice | change the recipe: drop the portrait, shorten lines, remove the numbered list |
| duplicated line in a Notes layout | eight lines max, "each line once, never repeated" |
| headline stack drifts left on a regenerate | composite the type from the good version instead of a third roll |
| empty centre in a flat-lay | state the hero's width as a percentage and where the type sits |
| folder named `Lip Filler $399` became `Lip Filler ` | never `$` in a path |
| zsh did not split the reference flags | the wrapper is bash |

## Using a different image model
Keep the recipe, swap the call. Requirements for a substitute: reference images (at least two: one photo, one logo), exact text, 2k output, an aspect of 4:5 or a crop path to it. Known options in the Higgsfield catalogue itself: `gpt_image_2_5` (strong text, weaker identity lock), `flux_2` (fast, weaker text). Outside Higgsfield the same recipe applies. `tools/codex-gen.sh` is the shipped sibling for Codex's built-in image_gen (same four arguments, local reference files only, tested). For OpenAI Images, Gemini image or Ideogram, copy its shape. Whatever the model, the gates are the same: contact sheet, strings exact, one price, real photos unaltered, identity true.

## Motion, only for winners (phase 13)
- `tools/living-static-particles.py master.png out45.mp4 out916.mp4 [seconds fps push density]`: procedural particles and a slow push-in over the finished static. No AI touches the master.
- Background animation + text burn: generate a text-free version of the scene, animate it with seedance (locked camera, particles only), then `tools/overlay-text-on-video.py bg.png static.png anim.mp4 out45.mp4 out916.mp4`.
