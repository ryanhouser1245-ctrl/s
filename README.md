# GoodEats promotional site

A dependency-free, static marketing page for GoodEats. Its job is to introduce the brand and send visitors to the GoodEats Discord. It does not accept orders, payments, or customer requests, and has no tracking or staff queue.

## What the site does

- Promotes GoodEats with the black-and-gold editorial design and locally served food photo and font.
- Shows the supplied offer copy: half off a group order, with a $30 minimum. Visitors are directed to Discord for the offer details.
- Links to `https://discord.gg/PMyUgUWJn` in a new tab.
- Collects no personal information and sends no order data to Discord. The offer is displayed as marketing copy only; the website does not calculate or apply a discount.

## Run locally

```bash
python3 server.py
```

The dependency-free preview server builds an allowlisted static bundle in `public/` and serves it on port `4173` (or the `PORT` environment variable). It serves only the public bundle; no order or request API is present.

## Deploy to Render

`render.yaml` defines a Render Static Site. Connect this repository as a new Blueprint in Render; the build script copies only `index.html`, the hero image, and the licensed font into `public/`. The database, private files, README, and Python files are not included in the published directory. No database, persistent disk, staff password, or paid web-service plan is needed for this marketing-only site.

Render will provide a temporary `onrender.com` address after deployment. To use a custom public domain, add the domain in the Render dashboard and configure the DNS records at your domain registrar. The Render Blueprint has not been deployed yet.

## Files

- `index.html` — editable marketing page and styles.
- `images/group-order-editorial.jpg` — self-hosted hero image.
- `fonts/` — self-hosted font and its OFL license.
- `build_static.py` — copies only those approved public files into `public/`.
- `server.py` — local static-only preview server; Render serves the static bundle directly.
