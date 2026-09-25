# Prompt skeleton: illustrated-hero flat-lay (the AP-style lips card, generalised)

Use when the offer has a single iconic symbol (lips, a brow arch, a droplet) and you want a set that is not the DR skeleton. Fill the frame. State the hero's size.

```
[VISUAL SYSTEM] High-end aesthetics med spa static ad, editorial flat-lay photography, top-down. Use the FIRST reference image only for the <hero sticker/illustration> and the <table material>-and-gold-rim table style; do not copy its empty layout. The SECOND reference is the <client> logo: small, top center, unaltered.
[LAYOUT] The composition fills the frame with no empty centre: the hero is LARGE, about 55 to 60 percent of the frame width, centred slightly below the middle; the headline stack sits tight above it; the price and CTA sit tight below it, all inside the table circle. A few <prop> sprigs at the edges only. All type black, crisp, exactly these strings and nothing else:
  Headline, large elegant high-contrast serif caps, N lines: '...' / '...'
  Small letterspaced sans caps under it: '...'
  Below the hero, very large heavy sans: '$<price>' with small caps beside it '<qualifier>'
  Bottom strip small caps: '<included line>' and 'BOOK NOW'
Background: <white marble | blush paper | black marble with gold type | cream linen> table with thin gold rim.
[LIGHTING] soft window light, warm cream, subtle shadows.
[QUALITY] magazine-grade, print-sharp typography, one price only.
[AVOID] no vials, no bottles, no syringes, no people, no extra words, no emojis, no watermark, no duplicated text.
```
Variants: swap the background per cell so a set of five does not look like one template. Awareness cells: remove the price line and swap 'BOOK NOW' for 'LEARN MORE'.
Living version: generate the same scene with no text as a background, animate it (locked camera, particles only), then burn the text layer from the static onto every frame with `tools/overlay-text-on-video.py`. Never animate the text itself.
