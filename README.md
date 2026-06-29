# AetherMed Health Website

Official static website for **AetherMed Health**:

**https://aethermed.health**

AetherMed Health is an international medical coordination service helping patients outside China connect with reputable hospitals, doctors, and care teams in China. The site explains the service model, patient journey, hospital and doctor matching process, and the first-step consultation flow.

## What This Website Does

- Introduces AetherMed Health as an international medical service brand.
- Explains how overseas patients can access medical care in China.
- Covers the full service journey: case review, medical translation, hospital and doctor matching, remote second opinion, travel support, admission escort, and follow-up.
- Provides bilingual Chinese/English content switching.
- Includes a consultation request form placeholder that can later connect to email, CRM, WhatsApp, or another backend service.

## Live Site

Production domain:

```text
https://aethermed.health
https://www.aethermed.health
```

Hosting:

```text
Cloudflare Pages / Workers & Pages
```

Domain registrar:

```text
GoDaddy
```

DNS:

```text
Managed by Cloudflare
```

## Repository Structure

```text
.
├── index.html    # Main website structure and content
├── styles.css    # Responsive visual design
├── script.js     # Language switcher and demo form behavior
├── _headers      # Cloudflare security headers
└── README.md     # Project documentation
```

## Technology

This is a lightweight static website.

- HTML
- CSS
- Vanilla JavaScript
- No build step
- No framework dependency
- No server required for the current version

Because the site is static, it is fast, easy to maintain, and simple to deploy.

## Local Preview

Open `index.html` directly in a browser.

Or run a simple static server from this folder:

```bash
python3 -m http.server 4173
```

Then open:

```text
http://localhost:4173
```

## Deployment Flow

The production deployment is connected to GitHub through Cloudflare Pages.

Recommended update flow:

1. Edit the website files locally.
2. Commit changes to Git.
3. Push to GitHub.
4. Cloudflare Pages automatically deploys the latest `main` branch.
5. The live site updates at `https://aethermed.health`.

Typical commands:

```bash
git status
git add index.html styles.css script.js README.md _headers
git commit -m "Describe the website update"
git push
```

## Cloudflare Pages Settings

Use these settings if the site needs to be reconnected:

```text
Repository: clicksuitedotcom/aethermed-health-site
Branch: main
Framework preset: None
Build command: empty
Build output directory: /
```

Custom domains:

```text
aethermed.health
www.aethermed.health
```

## DNS Notes

The domain was registered through GoDaddy, but DNS should be managed in Cloudflare.

GoDaddy should use the Cloudflare nameservers assigned to `aethermed.health`.

Do not point the live domain back to GoDaddy Website Builder records unless the hosting strategy changes.

## Content Notes

The website describes a medical coordination service. It should avoid making guaranteed medical outcomes or claims such as:

- guaranteed cure
- best doctor
- lowest price
- guaranteed appointment
- guaranteed treatment result

Recommended tone:

- clear
- professional
- internationally accessible
- patient-centered
- medically careful
- transparent about hospital and physician confirmation

## Future Improvements

Possible next steps:

- Connect the consultation form to email, CRM, WhatsApp, or a secure backend.
- Add real hospital/service partner pages after permissions are confirmed.
- Add patient FAQ pages.
- Add privacy policy and terms pages.
- Add structured SEO metadata.
- Add analytics through Cloudflare Web Analytics or another privacy-aware analytics tool.
- Add downloadable medical record preparation checklist.

## Maintenance Owner

Repository:

```text
https://github.com/clicksuitedotcom/aethermed-health-site
```

Production:

```text
https://aethermed.health
```
