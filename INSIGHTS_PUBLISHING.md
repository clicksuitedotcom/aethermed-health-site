# AetherMed Insights Publishing Notes

Insights pages are generated from `scripts/build_insights.py`.

## Add or Update an Article

1. Add the article image to `assets/` with a descriptive filename.
2. Edit the `ARTICLES` list in `scripts/build_insights.py`.
3. Use a lowercase, hyphenated `slug`.
4. Choose 1 primary category and optional secondary categories from `CATEGORIES`.
5. Add 3-5 public tags. Avoid duplicate category names as tags.
6. Write a unique meta description, image alt text, CTA and article sections.
7. Run:

```bash
python3 scripts/build_insights.py
```

8. Check generated files under `insights/`.
9. Commit and deploy with:

```bash
npx wrangler deploy
```

## SEO Rules

- Canonical URLs live under `/insights/{primary-category}/{article-slug}/`.
- Old `/guides/` URLs are redirected in `_worker.js`.
- `sitemap.xml` should include only final canonical URLs.
- Search pages and tag archives with fewer than 3 articles should be `noindex, follow`.
- Each medical article must include the approved medical and service disclaimer.
