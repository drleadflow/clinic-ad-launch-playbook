# Ad Library research at scale (Apify)

Browser scraping of the Ad Library is fine for eyeballing; for video research use Apify.

1. Build the Ad Library URL with your filters, for example:
   `https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=US&q=%22<device>%22&media_type=video&search_type=keyword_exact_phrase`
2. Run actor `curious_coder/facebook-ads-library-scraper` with `{"urls":[{"url":"<that url>"}],"count":400}`. About $0.75 per 1,000 ads.
3. Fetch the dataset **without** a `fields` projection; nested arrays (videos, cards) are dropped by projection.
4. Parse locally: `snapshot.videos[0].video_hd_url`, `video_preview_image_url`, `snapshot.body.text`, `start_date_formatted`, `end_date_formatted`, `collation_count` (variants). Dedupe by video URL, keep one row per page, rank by days running × variants.
5. Split English patient-facing from dealer B2B, and note when one agency template is cloned across dozens of clinics: that template is the floor, not the target.

Never reuse a competitor's footage. Steal the structure.
