from __future__ import annotations

import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE = "https://aethermed.health"
TODAY = "2026-07-22"


CATEGORIES = {
    "medical-in-china": {
        "name": "Medical In China",
        "description": "Start here for broad, patient-friendly explainers about accessing medical care in China as an international patient. This category covers second medical opinions, how China-based care may fit into a wider treatment decision, what overseas families should clarify before travel, and how AetherMed coordinates preliminary pathways without replacing clinical judgment. Articles in this category are designed for early research: they help patients understand whether China may be worth exploring, what information hospitals usually need, and where a remote review or in-person assessment may be appropriate.",
        "service": "Free Assessment",
    },
    "hospitals-doctors": {
        "name": "Hospitals & Doctors",
        "description": "Guidance on choosing the right hospital, department, specialist and international-patient support pathway in China. This category explains how hospital level, specialist experience, department fit, location, language support and appointment availability can shape the patient journey. It is not a ranking of doctors or a promise of access; instead, it helps families ask better questions before choosing where to send records or request an appointment.",
        "service": "Hospital and doctor matching",
    },
    "specialty-treatment": {
        "name": "Specialty & Treatment",
        "description": "Disease, specialty and treatment-pathway explainers for international patients comparing care options in China. Content in this category may cover oncology, hepatobiliary care, cardiology, neurology, orthopedics, rehabilitation, preventive health and other specialties as the library grows. Articles are educational and coordination-focused: they describe evaluation steps, record needs and questions to raise with licensed clinicians, not diagnosis or individualized treatment recommendations.",
        "service": "Specialty pathway coordination",
    },
    "medical-journey-guides": {
        "name": "Medical Journey Guides",
        "description": "Practical planning guidance for the full international patient journey: medical records, translation, travel planning, hospital admission, payment, interpretation, discharge documents and return-home follow-up. These articles help patients and caregivers prepare the non-clinical work that often determines whether an overseas medical visit is organized, understandable and safe. They also clarify the limits of remote review, appointment estimates and travel planning before a hospital completes its own evaluation.",
        "service": "End-to-end case coordination",
    },
    "success-stories": {
        "name": "Success Stories",
        "description": "Authorized or carefully anonymized patient stories showing how international medical coordination can work in real situations. These stories focus on process, preparation, communication and care navigation rather than promising outcomes. Because medical cases are sensitive, AetherMed only publishes stories when consent, privacy protection and compliance review are appropriate. If no story is available yet, patients can still use our general journey insights to understand the steps involved.",
        "service": "Patient journey support",
    },
    "news": {
        "name": "News",
        "description": "Updates from AetherMed, hospital-network developments, policy changes and industry information relevant to international patients considering care in China. News content is time-sensitive and should be read with its publication date in mind. AetherMed uses this section to share operational updates and useful context, while medical decisions remain the responsibility of receiving hospitals and licensed professionals after case review.",
        "service": "AetherMed updates",
    },
}


ARTICLES = [
    {
        "slug": "how-to-get-a-second-medical-opinion-in-china",
        "title": "How to Get a Second Medical Opinion in China",
        "description": "Learn how international patients can request a second medical opinion in China, what information supports review, and how AetherMed coordinates next steps.",
        "lede": "A second medical opinion in China can help international patients compare treatment options, understand important risks, and decide whether travelling to China for care is realistic. The quality of the review depends heavily on how clearly the case and the patient’s questions are presented.",
        "primary_category": "medical-in-china",
        "categories": ["medical-in-china"],
        "tags": ["Second Opinion", "Remote Consultation", "Medical Records Review", "International Patients"],
        "image": "second-medical-opinion-china.webp",
        "image_alt": "Preparing for a second medical opinion in China.",
        "published": "2026-07-22",
        "updated": "2026-07-22",
        "featured": True,
        "sections": [
            ("When a second opinion may be useful", [
                "International patients often request a medical second opinion when they have a complex or uncertain diagnosis, proposed surgery, cancer treatment options, transplant questions, a rare condition, or a need to compare specialist availability across countries.",
                "A review is most useful when the doctor can see the original diagnosis, recent imaging, pathology, laboratory data, current medicines, previous treatment, and the patient’s goals. The reviewing doctor may confirm the current plan, identify questions for further testing, or explain whether an in-person assessment is necessary.",
                "Patients considering overseas care should also review treatment-abroad checklists and understand treatment risks, alternatives, complications and aftercare before making a decision.",
            ]),
            ("What information supports a useful review?", [
                "The exact requirements depend on the condition and the receiving hospital. In most cases, a concise record set should show the diagnosis, timeline, current symptoms, key questions, recent imaging reports and original image files when requested.",
                "Relevant pathology, laboratory results, operation notes, discharge summaries, current medicines, allergies, previous treatments and important medical conditions should be included. The goal of the review should also be clear: confirming a diagnosis, comparing treatment options, assessing surgery or exploring whether treatment in China may be feasible.",
                "For cancer cases, pathology review may require slides or a paraffin block. Confirm availability, cost and submission instructions with the reviewing institution in advance.",
            ]),
            ("What a Chinese hospital or doctor may provide", [
                "Depending on the specialty, available records and hospital policy, the review may provide general feasibility feedback, recommended next tests, possible treatment pathways or an indication of whether an in-person visit or multidisciplinary review may be appropriate.",
                "A remote review may not provide a final diagnosis or binding treatment plan without physical examination, local testing, hospital registration and formal consent. Availability also varies by hospital and doctor.",
            ]),
        ],
        "cta": "Share your diagnosis, available records and goals. AetherMed will assess whether China may be a practical option and suggest appropriate coordination next steps.",
    },
    {
        "slug": "medical-treatment-in-china-guide",
        "title": "Medical Treatment in China: A Guide for International Patients",
        "description": "Explore medical treatment in China for international patients, including hospital selection, medical review, travel, costs, admission and follow-up.",
        "lede": "International patients may explore medical treatment in China for specialist expertise, another opinion, different treatment approaches or more practical access to care. The process requires more than booking an appointment: the hospital must review the case, suitable doctors must be identified, and travel, payment, interpretation and follow-up must be planned.",
        "primary_category": "medical-in-china",
        "categories": ["medical-in-china", "medical-journey-guides"],
        "tags": ["China", "International Patients", "Complete Guide", "Case Management", "Before You Travel"],
        "image": "medical-treatment-in-china-guide.webp",
        "image_alt": "International patient discussing medical treatment in China.",
        "published": "2026-07-22",
        "updated": "2026-07-22",
        "featured": True,
        "sections": [
            ("When might treatment in China be worth exploring?", [
                "Potential reasons include seeking a second medical opinion, accessing specialist assessment for a complex or rare situation, comparing surgical and non-surgical treatment pathways, or exploring integrative approaches where clinically appropriate and supervised by qualified professionals.",
                "These are reasons to investigate, not promised advantages. Cost, timing, suitability and outcomes depend on the condition, hospital assessment, doctor availability and treatment plan. Patients should also consider travel risk, complications and continuity of care.",
            ]),
            ("1. Find out whether China could be an option", [
                "Start by sharing a concise medical summary, diagnosis, recent test results, imaging and treatment history. Explain your goals, preferred timing, language needs and approximate budget. AetherMed can assess whether China may be a practical option and identify missing information.",
                "This initial assessment is not a diagnosis or guarantee of hospital acceptance. Use the medical-record preparation guide to create a review-ready package.",
            ]),
            ("2. Understand which hospitals and doctors may fit your case", [
                "Records are considered against relevant hospitals, departments and specialists. Matching should be based on the condition, proposed type of care, doctor expertise, language requirements, location and budget, not hospital reputation alone.",
                "A remote second medical opinion in China may help clarify possible next steps before travel. Final diagnosis and treatment decisions may still require an in-person examination or additional tests.",
            ]),
            ("3. Prepare your appointments and travel", [
                "If the patient decides to proceed, the next stage may include confirming hospital and doctor appointments, preparing hospital invitation documentation where required, checking current visa rules, and arranging flights, accommodation, interpretation and a flexible itinerary.",
                "Estimated costs and dates remain conditional. Patients should plan follow-up care before travelling and keep room in the schedule for additional tests or changes after evaluation.",
            ]),
            ("4. Arrive with a clear plan", [
                "Arrival support may include airport pickup, accommodation check-in and a briefing on the hospital visit and local arrangements. Patients should keep passports, appointment details, medicines, medical records and payment methods accessible.",
            ]),
            ("5. Navigate hospital visits and treatment", [
                "Hospital visits may involve registration, deposits, consultation, examinations and additional tests before a final plan is confirmed. During treatment, a case manager or interpreter can support communication, registration, payments, testing routes and pharmacy coordination, but cannot make medical decisions.",
                "Ask about alternatives, important risks, expected recovery, possible complications and changes to estimated costs.",
            ]),
            ("6. Return home with clear records and follow-up", [
                "Before returning home, collect discharge summaries, procedure notes, imaging and laboratory results, medication instructions, follow-up guidance and itemized bills. Confirm warning signs, fitness to travel and who to contact with questions.",
            ]),
        ],
        "cta": "Not sure whether medical treatment in China may be appropriate for your situation? Share a brief description of your condition and available medical records.",
    },
    {
        "slug": "prepare-medical-records-for-china",
        "title": "Preparing Medical Records for Treatment in China",
        "description": "Learn how to prepare medical records for treatment in China, including summaries, imaging files, medication lists, translation and secure sharing.",
        "lede": "If you are considering treatment in China, well-organized medical records help a hospital understand your diagnosis, previous care and current needs. A concise summary, key reports, original imaging files and a complete medication list can support a more focused initial review.",
        "primary_category": "medical-journey-guides",
        "categories": ["medical-journey-guides", "medical-in-china"],
        "tags": ["Medical Records", "Medical Records Review", "Translation", "International Patients"],
        "image": "prepare-medical-records-china.webp",
        "image_alt": "Medical records prepared for specialist review in China.",
        "published": "2026-07-22",
        "updated": "2026-07-22",
        "featured": True,
        "sections": [
            ("Key takeaways", [
                "Start with a one-page case summary and a short list of questions for the specialist. Include the most relevant reports and original imaging files, arranged in chronological order.",
                "List every current medicine, dose, frequency, allergy and important previous treatment. Use clear filenames and the secure sharing method requested by the coordinator or hospital. Do not delay urgent or emergency care while waiting for an overseas review.",
            ]),
            ("Who this guide is for", [
                "This guide is for patients and families preparing records for a specialist consultation, second opinion or planned medical care in China. If you are still deciding whether an overseas review is appropriate, read the second opinion guide and the overview of the international patient journey.",
            ]),
            ("1. Create a one-page medical summary", [
                "Give the reviewing team a fast, accurate overview. Include your confirmed or suspected diagnosis, when symptoms began, major treatments or procedures, current symptoms, other medical conditions, allergies and the reason you are seeking care in China. Finish with three to five focused questions.",
            ]),
            ("2. Gather the records that matter most", [
                "The exact requirements depend on your condition, but a typical medical records review in China may need diagnosis reports, referral letters, discharge summaries, operation notes, laboratory results, pathology reports and relevant test reports.",
                "Radiology reports plus original CT, MRI, PET or ultrasound image files may be needed when available. A treatment timeline and current medication list can help the reviewing team understand what has already happened and what questions remain.",
            ]),
            ("3. Organize files so the case is easy to review", [
                "Arrange documents from oldest to newest or use clearly labelled folders such as Summary, Pathology, Imaging, Laboratory, Procedures and Medications. Use filenames that combine the date, record type and facility. Avoid screenshots when the full report or original file is available.",
            ]),
            ("4. Check language and translation needs", [
                "Some international departments may accept English-language records, while other hospitals or specialists may request Chinese translations or a bilingual summary. Confirm requirements before paying for translation. Names, dates, measurements, medicine doses and clinical terms must remain consistent with the source record.",
            ]),
            ("5. Share health information carefully", [
                "Medical records contain sensitive personal information. Use the secure upload or transfer method specified for your case, confirm the recipient and keep a copy of everything submitted. Do not post records through public links or open social channels.",
            ]),
            ("Before you submit: a quick check", [
                "Make sure the summary matches the source reports, dates and medicine doses are complete, imaging includes original files when available, files open correctly, and the hospital’s preferred language, file type, transfer method and size limit have been confirmed.",
            ]),
        ],
        "cta": "Not sure whether your records are ready? Share a brief description of your condition and available records. AetherMed can outline possible next steps.",
    },
    {
        "slug": "international-patient-journey-china",
        "title": "What the International Patient Journey in China Looks Like",
        "description": "Understand the international patient journey in China, from medical-record review and hospital matching to travel, admission, discharge and follow-up.",
        "lede": "The international patient journey in China involves more than booking a hospital appointment. It usually includes medical-record preparation, preliminary review, hospital and specialist matching, travel planning, registration, interpretation, payment, discharge documents and follow-up at home.",
        "primary_category": "medical-journey-guides",
        "categories": ["medical-journey-guides"],
        "tags": ["Case Management", "Travel Planning", "Hospital Admission", "Returning Home", "International Patients"],
        "image": "international-patient-journey-china.webp",
        "image_alt": "International patient journey for medical care in China.",
        "published": "2026-07-22",
        "updated": "2026-07-22",
        "featured": True,
        "sections": [
            ("Key takeaways", [
                "Confirm medical feasibility before making non-refundable travel arrangements. Expect the hospital to request additional records, tests or an in-person assessment before confirming a final treatment plan.",
                "Plan for language support, payment arrangements, accommodation and a family caregiver where appropriate. Before returning home, collect complete records, medication instructions, bills and follow-up information.",
            ]),
            ("1. Initial inquiry and Free Assessment", [
                "The journey usually starts with a short intake describing the diagnosis, current symptoms, previous treatment, goals, preferred timing and available budget. Patients may also submit key reports or imaging. The purpose is to assess whether China may be a realistic option before the family invests heavily in travel.",
            ]),
            ("2. Medical review and hospital matching", [
                "Records are organized and considered against possible hospitals, departments or specialists. Matching should consider the condition, clinical expertise, language needs, likely timing, location and budget, not reputation alone.",
                "In complex cases, a second medical opinion in China or further record review may be useful before travel. A hospital may provide preliminary feasibility feedback, but the final diagnosis, eligibility and treatment plan may change after registration, examination or additional testing.",
            ]),
            ("3. Appointment and travel planning", [
                "Once a possible pathway is identified, the coordinator and patient clarify the proposed hospital, doctor or department, anticipated visit dates, required documents and estimated costs. Planning may include a hospital invitation letter, visa materials, flights, accommodation, airport arrival, an interpreter and a day-by-day schedule.",
                "Visa approval, appointment timing and doctor availability cannot be guaranteed. Before travelling, discuss fitness to travel, medicines and possible complications with an appropriate clinician.",
            ]),
            ("4. Arrival, registration and the first hospital visit", [
                "Patients often ask what happens during the first hospital visit in China. The practical sequence may include identity and appointment verification, registration, payment or deposit, review of records, consultation, examinations and booking additional tests. These steps can occur on one day or across several visits.",
            ]),
            ("5. Treatment, payment and changes to the plan", [
                "If the hospital recommends treatment, ask for an explanation of the proposed procedure or therapy, alternatives, important risks, expected length of stay, estimated charges and likely follow-up needs. Estimates may change because of additional tests, clinical findings, complications, medicines, room type or length of stay.",
            ]),
            ("6. Discharge, returning home and follow-up", [
                "Before leaving the hospital, request the discharge summary, procedure or operation notes, imaging and laboratory results, pathology information where relevant, medication list, follow-up instructions and itemized bills. Arrange a handover to the home doctor and confirm whether remote follow-up may be available.",
            ]),
        ],
        "cta": "Planning medical care in China? Share your condition, available records and preferred timing. AetherMed can outline possible hospital pathways and next steps.",
    },
]


TAG_GROUPS = {
    "Specialty": [],
    "Treatment & Review": ["Second Opinion", "Remote Consultation", "Medical Records Review"],
    "Patient Journey": ["Before You Travel", "Medical Records", "Translation", "Travel Planning", "Hospital Admission", "Case Management", "Returning Home"],
    "Location": ["China"],
    "Audience & Format": ["International Patients", "Complete Guide"],
}


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def slugify(value: str) -> str:
    return value.lower().replace("&", "and").replace(" ", "-").replace(":", "").replace(",", "")


def article_url(article: dict) -> str:
    return f"/insights/{article['primary_category']}/{article['slug']}/"


def absolute(path: str) -> str:
    return f"{SITE}{path}"


def rel_to_root(depth: int) -> str:
    return "../" * depth or "./"


def header(depth: int, active: str = "Insights") -> str:
    root = rel_to_root(depth)
    insights = f"{root}insights/"
    return f"""
    <header class="site-header legal-header">
      <a class="brand" href="{root}index.html#top" aria-label="AetherMed Health home">
        <span class="brand-mark" aria-hidden="true"><img src="{root}assets/aethermed-logo.png" alt="" /></span>
        <span><strong>AetherMed</strong><small>China Care, Global Access</small></span>
      </a>
      <nav class="main-nav" aria-label="Primary navigation">
        <a href="{root}index.html#why">Services</a>
        <a href="{root}index.html#network">Hospitals & Doctors</a>
        <a href="{root}index.html#journey">Journey</a>
        <a href="{insights}" aria-current="{ 'page' if active == 'Insights' else 'false' }">Insights</a>
        <a href="{root}index.html#contact">Contact</a>
      </nav>
      <div class="header-actions"><a class="button button-small" href="{root}index.html#contact">Free Assessment</a></div>
    </header>
"""


def footer(depth: int) -> str:
    root = rel_to_root(depth)
    return f"""
    <footer class="site-footer">
      <div class="footer-brand-block">
        <div class="footer-brand-row"><img src="{root}assets/aethermed-logo.png" alt="AetherMed logo" loading="lazy" decoding="async" /><strong>AetherMed</strong></div>
        <p>AetherMed coordinates medical access in China for international visitors, from free assessment and hospital matching to appointments, travel support, in-China interpretation, and follow-up documentation.</p>
      </div>
      <nav class="footer-links" aria-label="Footer navigation">
        <a href="{root}index.html#why">Services</a>
        <a href="{root}index.html#network">Hospitals & Doctors</a>
        <a href="{root}index.html#journey">Journey</a>
        <a href="{root}insights/">Insights</a>
        <a href="{root}privacy.html">Privacy Policy</a>
        <a href="{root}terms.html">Terms & Conditions</a>
      </nav>
      <div class="footer-offices">
        <div><strong>Email</strong><p><a href="mailto:info@aethermed.health">info@aethermed.health</a></p></div>
      </div>
      <p class="footer-rights">© 2026 AetherMed. All rights reserved.</p>
    </footer>
"""


def layout(title: str, description: str, canonical_path: str, body: str, depth: int, *, robots: str = "index, follow", og_type: str = "website", image: str = "/assets/hero-medical-travel-v2.png", schema: dict | list | None = None, extra_script: str = "") -> str:
    schema_html = ""
    if schema:
        schema_html = f'<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False, indent=2)}</script>'
    root = rel_to_root(depth)
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{esc(title)}</title>
    <meta name="description" content="{esc(description)}" />
    <meta name="robots" content="{esc(robots)}" />
    <link rel="canonical" href="{absolute(canonical_path)}" />
    <meta property="og:site_name" content="AetherMed Health" />
    <meta property="og:type" content="{esc(og_type)}" />
    <meta property="og:title" content="{esc(title)}" />
    <meta property="og:description" content="{esc(description)}" />
    <meta property="og:url" content="{absolute(canonical_path)}" />
    <meta property="og:image" content="{absolute(image)}" />
    <meta name="twitter:card" content="summary_large_image" />
    <link rel="icon" type="image/png" href="{root}assets/aethermed-logo.png" />
    <link rel="apple-touch-icon" href="{root}assets/aethermed-logo.png" />
    <link rel="stylesheet" href="{root}styles.css" />
    {schema_html}
  </head>
  <body>
{header(depth)}
{body}
{footer(depth)}
{extra_script}
  </body>
</html>
"""


def tag_link(tag: str, depth: int) -> str:
    root = rel_to_root(depth)
    return f'<a class="insight-chip" href="{root}insights/tags/{slugify(tag)}/">{esc(tag)}</a>'


def category_link(cat: str, depth: int) -> str:
    root = rel_to_root(depth)
    return f'<a class="insight-category-link" href="{root}insights/{cat}/">{esc(CATEGORIES[cat]["name"])}</a>'


def card(article: dict, depth: int) -> str:
    root = rel_to_root(depth)
    url = f"{root}{article_url(article).lstrip('/')}"
    cat_links = " ".join(category_link(cat, depth) for cat in article["categories"])
    shown_tags = article["tags"][:2]
    plus = len(article["tags"]) - len(shown_tags)
    tags = " ".join(tag_link(tag, depth) for tag in shown_tags)
    if plus:
        tags += f'<span class="insight-chip insight-chip-muted">+{plus}</span>'
    return f"""
        <article class="insight-card" data-title="{esc(article['title'])}" data-summary="{esc(article['description'])}" data-categories="{esc(' '.join(CATEGORIES[c]['name'] for c in article['categories']))}" data-tags="{esc(' '.join(article['tags']))}">
          <a class="insight-card-image" href="{url}"><img src="{root}assets/{esc(article['image'])}" alt="{esc(article['image_alt'])}" loading="lazy" decoding="async" /></a>
          <div class="insight-card-body">
            <div class="insight-card-categories">{cat_links}</div>
            <h2><a href="{url}">{esc(article['title'])}</a></h2>
            <div class="insight-card-tags">{tags}</div>
            <p>{esc(article['description'])}</p>
            <time datetime="{article['updated']}">Updated {article['updated']}</time>
          </div>
        </article>
"""


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def breadcrumbs(items: list[tuple[str, str]]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": absolute(url)}
            for i, (name, url) in enumerate(items)
        ],
    }


def collection_schema(path: str, name: str, description: str) -> list[dict]:
    return [
        {
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "@id": absolute(path) + "#webpage",
            "url": absolute(path),
            "name": name,
            "description": description,
            "isPartOf": {"@type": "WebSite", "name": "AetherMed Health", "url": SITE + "/"},
            "publisher": {"@type": "Organization", "name": "AetherMed Health", "url": SITE + "/", "logo": absolute("/assets/aethermed-logo.png")},
        },
        breadcrumbs([("Home", "/"), ("Insights", "/insights/")]),
    ]


def render_home() -> None:
    featured = [a for a in ARTICLES if a.get("featured")]
    category_cards = "\n".join(
        f'<a class="insight-category-card" href="./{slug}/"><strong>{esc(cat["name"])}</strong><span>{esc(cat["description"].split(".")[0])}.</span></a>'
        for slug, cat in CATEGORIES.items()
    )
    tag_cloud = "\n".join(tag_link(tag, 1) for group in TAG_GROUPS.values() for tag in group if tag)
    data_json = json.dumps([
        {
            "title": a["title"],
            "summary": a["description"],
            "categories": [CATEGORIES[c]["name"] for c in a["categories"]],
            "tags": a["tags"],
            "url": article_url(a),
        }
        for a in ARTICLES
    ], ensure_ascii=False)
    body = f"""
    <main class="insights-page">
      <section class="insights-hero">
        <p class="section-kicker">AetherMed Insights</p>
        <h1>Insights</h1>
        <p>Practical guidance for international patients exploring medical care in China.</p>
        <p>Explore clear, patient-focused articles on accessing hospitals and doctors in China, specialty treatment pathways, planning your medical journey, real patient experiences, and AetherMed updates.</p>
        <a class="button" href="../index.html#contact">Get a Free Assessment</a>
      </section>
      <section class="insights-browser" aria-label="AetherMed Insights browser">
        <aside class="insights-sidebar" aria-label="Search and filters">
          <div class="insights-sidebar-block">
            <p class="section-kicker">Search</p>
            <form class="insights-search-form" action="./search/" method="get" data-insights-search>
              <label class="sr-only" for="insights-query">Search articles</label>
              <input id="insights-query" name="q" type="search" placeholder="Search articles" autocomplete="off" />
              <div class="insights-search-actions">
                <button class="button button-small" type="submit">Search</button>
                <button class="button button-small button-light" type="button" data-clear-search>Clear</button>
              </div>
            </form>
            <p class="insights-search-status" aria-live="polite" data-search-status></p>
          </div>
          <div class="insights-sidebar-block">
            <p class="section-kicker">Categories</p>
            <div class="insight-category-list">{category_cards}</div>
          </div>
          <div class="insights-sidebar-block">
            <p class="section-kicker">Tags</p>
            <div class="insight-tag-cloud">{tag_cloud}</div>
          </div>
        </aside>
        <div class="insights-article-feed">
          <div class="section-heading compact-heading"><p class="section-kicker">Featured Insights</p><h2>Recently updated articles</h2></div>
          <div class="insight-card-grid" data-search-results>{"".join(card(a, 1) for a in featured)}</div>
        </div>
      </section>
      <section class="insights-cta">
        <h2>Not sure where to begin?</h2>
        <p>Share your medical records and treatment needs. AetherMed can help coordinate the next steps with suitable hospitals and doctors in China.</p>
        <a class="button" href="../index.html#contact">Get a Free Assessment</a>
      </section>
    </main>
"""
    script = f"""
    <script>
      window.AETHERMED_INSIGHTS = {data_json};
    </script>
    <script src="../insights/insights-search.js"></script>
"""
    write(ROOT / "insights/index.html", layout(
        "Insights | Medical Care in China for International Patients | AetherMed",
        "Explore AetherMed Insights on medical care in China, hospitals and doctors, treatment pathways, medical journey planning, patient stories, and news.",
        "/insights/",
        body,
        1,
        schema=collection_schema("/insights/", "Insights", "Practical guidance for international patients exploring medical care in China."),
        extra_script=script,
    ))


def render_category(slug: str, cat: dict) -> None:
    articles = [a for a in ARTICLES if slug in a["categories"]]
    cards = "".join(card(a, 2) for a in articles) if articles else '<div class="insights-empty"><h2>Articles are coming soon</h2><p>This category is ready for future AetherMed content. Browse the latest Insights or request a free assessment if you need help now.</p><a class="button" href="../../index.html#contact">Get a Free Assessment</a></div>'
    related_tags = sorted({tag for a in articles for tag in a["tags"]}) or ["International Patients"]
    body = f"""
    <main class="insights-page">
      <nav class="insight-breadcrumb" aria-label="Breadcrumb"><a href="../../">Home</a><span>›</span><a href="../">Insights</a><span>›</span><span>{esc(cat['name'])}</span></nav>
      <section class="insights-hero compact">
        <p class="section-kicker">Category</p>
        <h1>{esc(cat['name'])}</h1>
        <p>{esc(cat['description'])}</p>
        <a class="button" href="../../index.html#contact">{esc(cat['service'])}</a>
      </section>
      <section class="insights-section">
        <div class="section-heading"><p class="section-kicker">Latest Content</p><h2>Articles in {esc(cat['name'])}</h2></div>
        <div class="insight-card-grid">{cards}</div>
      </section>
      <section class="insights-section insights-tag-section">
        <div class="section-heading"><p class="section-kicker">Related Tags</p><h2>Continue exploring</h2></div>
        <div class="insight-tag-cloud">{"".join(tag_link(tag, 2) for tag in related_tags)}</div>
      </section>
    </main>
"""
    schema = collection_schema(f"/insights/{slug}/", cat["name"], cat["description"])
    schema[1] = breadcrumbs([("Home", "/"), ("Insights", "/insights/"), (cat["name"], f"/insights/{slug}/")])
    write(ROOT / f"insights/{slug}/index.html", layout(
        f"{cat['name']} | AetherMed Insights",
        cat["description"][:155],
        f"/insights/{slug}/",
        body,
        2,
        schema=schema,
    ))


def render_article(article: dict) -> None:
    cat = CATEGORIES[article["primary_category"]]
    depth = 3
    root = rel_to_root(depth)
    section_html = "\n".join(
        f"<h2>{esc(title)}</h2>\n" + "\n".join(f"<p>{esc(p)}</p>" for p in paragraphs)
        for title, paragraphs in article["sections"]
    )
    tag_html = "".join(tag_link(tag, depth) for tag in article["tags"])
    category_html = " ".join(category_link(c, depth) for c in article["categories"])
    url = article_url(article)
    schema = [
        {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": article["title"],
            "description": article["description"],
            "image": absolute(f"/assets/{article['image']}"),
            "datePublished": article["published"],
            "dateModified": article["updated"],
            "author": {"@type": "Organization", "name": "AetherMed Health"},
            "publisher": {"@type": "Organization", "name": "AetherMed Health", "logo": {"@type": "ImageObject", "url": absolute("/assets/aethermed-logo.png")}},
            "mainEntityOfPage": absolute(url),
            "articleSection": cat["name"],
        },
        breadcrumbs([("Home", "/"), ("Insights", "/insights/"), (cat["name"], f"/insights/{article['primary_category']}/"), (article["title"], url)]),
    ]
    body = f"""
    <main class="article-page">
      <nav class="insight-breadcrumb" aria-label="Breadcrumb"><a href="../../../">Home</a><span>›</span><a href="../../">Insights</a><span>›</span><a href="../">{esc(cat['name'])}</a><span>›</span><span>{esc(article['title'])}</span></nav>
      <article class="article-layout insight-article">
        <div class="article-category-row">{category_html}</div>
        <h1>{esc(article['title'])}</h1>
        <div class="article-tag-row">{tag_html}</div>
        <p class="article-lede">{esc(article['lede'])}</p>
        <p class="article-date"><time datetime="{article['published']}">Published {article['published']}</time> · <time datetime="{article['updated']}">Updated {article['updated']}</time></p>
        <img class="article-hero-image" src="{root}assets/{esc(article['image'])}" alt="{esc(article['image_alt'])}" width="1600" height="900" />
        {section_html}
        <h2>What AetherMed can help with</h2>
        <p>AetherMed coordinates practical access to medical care in China. Depending on the case, support may include initial information review, medical-record organization and translation, hospital and doctor matching, remote consultation coordination, appointment and travel support, in-China case management and interpretation, and discharge and follow-up documentation. All diagnoses, eligibility decisions and treatment plans are made by the receiving hospital and its licensed medical professionals.</p>
        <div class="article-cta"><h2>Request a Free Assessment</h2><p>{esc(article['cta'])}</p><a class="button" href="{root}index.html#contact">Request a Free Assessment</a></div>
        <div class="medical-disclaimer"><strong>Medical and Service Disclaimer</strong><p>This article is provided for general educational and informational purposes only. It does not constitute medical advice, diagnosis, treatment, a medical recommendation, legal advice, insurance advice, or a guarantee that any hospital, doctor, procedure, appointment, visa, treatment outcome, timeline, or cost will be available or suitable for a particular patient. AetherMed provides international medical coordination and related support services; it does not independently diagnose medical conditions, prescribe treatment, or replace consultation with a licensed physician. Remote consultations and preliminary assessments have limitations and cannot replace an in-person clinical examination or emergency medical care. If you are experiencing a medical emergency, contact your local emergency services immediately. Use of AetherMed’s website and services is subject to our <a href="{root}terms.html">Terms & Conditions</a> and <a href="{root}privacy.html">Privacy Policy</a>.</p></div>
      </article>
    </main>
"""
    write(ROOT / f"insights/{article['primary_category']}/{article['slug']}/index.html", layout(
        f"{article['title']} | AetherMed Insights",
        article["description"],
        url,
        body,
        depth,
        og_type="article",
        image=f"/assets/{article['image']}",
        schema=schema,
    ))


def render_tags() -> None:
    counts: dict[str, int] = {}
    for article in ARTICLES:
        for tag in article["tags"]:
            counts[tag] = counts.get(tag, 0) + 1
    for tag, count in counts.items():
        slug = slugify(tag)
        articles = [a for a in ARTICLES if tag in a["tags"]]
        robots = "index, follow" if count >= 3 else "noindex, follow"
        body = f"""
    <main class="insights-page">
      <nav class="insight-breadcrumb" aria-label="Breadcrumb"><a href="../../../">Home</a><span>›</span><a href="../../">Insights</a><span>›</span><span>{esc(tag)}</span></nav>
      <section class="insights-hero compact">
        <p class="section-kicker">Tag</p>
        <h1>{esc(tag)}</h1>
        <p>Articles connected to {esc(tag)} across AetherMed Insights. Tag archives with fewer than three substantial articles are available for navigation but kept out of search indexing until the topic is mature.</p>
      </section>
      <section class="insights-section"><div class="insight-card-grid">{"".join(card(a, 3) for a in articles)}</div></section>
    </main>
"""
        write(ROOT / f"insights/tags/{slug}/index.html", layout(
            f"{tag} | AetherMed Insights",
            f"Explore AetherMed Insights articles tagged {tag}.",
            f"/insights/tags/{slug}/",
            body,
            3,
            robots=robots,
        ))


def render_search() -> None:
    data_json = json.dumps([
        {"title": a["title"], "summary": a["description"], "categories": [CATEGORIES[c]["name"] for c in a["categories"]], "tags": a["tags"], "url": article_url(a), "image": a["image"], "alt": a["image_alt"], "updated": a["updated"]}
        for a in ARTICLES
    ], ensure_ascii=False)
    body = """
    <main class="insights-page">
      <section class="insights-hero compact">
        <p class="section-kicker">Search Insights</p>
        <h1>Search Results</h1>
        <p>Search AetherMed articles by title, summary, category or tag. Do not enter personal medical details into this search box.</p>
        <form class="insights-search-form" action="./" method="get" data-insights-search-page>
          <label class="sr-only" for="search-query">Search articles</label>
          <input id="search-query" name="q" type="search" placeholder="Search Insights" autocomplete="off" />
          <button class="button" type="submit">Search</button>
        </form>
        <p class="insights-search-status" aria-live="polite" data-search-status></p>
      </section>
      <section class="insights-section"><div class="insight-card-grid" data-search-results></div><div class="insights-empty" data-empty-search hidden><h2>No matching articles yet</h2><p>Try a broader topic, browse categories, or request a free assessment if you need case-specific coordination.</p><a class="button" href="../../index.html#contact">Get a Free Assessment</a></div></section>
    </main>
"""
    script = f'<script>window.AETHERMED_INSIGHTS = {data_json};</script><script src="../../insights/insights-search.js"></script>'
    write(ROOT / "insights/search/index.html", layout(
        "Search Insights | AetherMed",
        "Search AetherMed Insights articles about medical care in China.",
        "/insights/search/",
        body,
        2,
        robots="noindex, follow",
        extra_script=script,
    ))


def render_search_js() -> None:
    write(ROOT / "insights/insights-search.js", r"""
(function () {
  const articles = window.AETHERMED_INSIGHTS || [];
  const normalize = (value) => String(value || "").toLowerCase();
  const matches = (article, query) => {
    const haystack = normalize([article.title, article.summary, ...(article.categories || []), ...(article.tags || [])].join(" "));
    return !query || haystack.includes(normalize(query));
  };
  const cardHtml = (article) => `
    <article class="insight-card">
      ${article.image ? `<a class="insight-card-image" href="${article.url}"><img src="../../assets/${article.image}" alt="${article.alt || ""}" loading="lazy" decoding="async" /></a>` : ""}
      <div class="insight-card-body">
        <div class="insight-card-categories">${(article.categories || []).map((name) => `<span class="insight-category-link">${name}</span>`).join("")}</div>
        <h2><a href="${article.url}">${article.title}</a></h2>
        <div class="insight-card-tags">${(article.tags || []).slice(0, 2).map((tag) => `<span class="insight-chip">${tag}</span>`).join("")}</div>
        <p>${article.summary}</p>
        ${article.updated ? `<time datetime="${article.updated}">Updated ${article.updated}</time>` : ""}
      </div>
    </article>`;

  document.querySelectorAll("[data-insights-search]").forEach((form) => {
    const input = form.querySelector("input[type='search']");
    const status = document.querySelector("[data-search-status]");
    const cards = Array.from(document.querySelectorAll("[data-search-results] .insight-card"));
    const clear = document.querySelector("[data-clear-search]");
    const apply = () => {
      const query = normalize(input.value.trim());
      let count = 0;
      cards.forEach((card) => {
        const haystack = normalize([card.dataset.title, card.dataset.summary, card.dataset.categories, card.dataset.tags].join(" "));
        const show = !query || haystack.includes(query);
        card.hidden = !show;
        if (show) count += 1;
      });
      if (status) status.textContent = query ? `${count} matching article${count === 1 ? "" : "s"}.` : "";
    };
    form.addEventListener("submit", (event) => { event.preventDefault(); apply(); });
    input.addEventListener("input", apply);
    if (clear) clear.addEventListener("click", () => { input.value = ""; apply(); input.focus(); });
  });

  document.querySelectorAll("[data-insights-search-page]").forEach((form) => {
    const params = new URLSearchParams(window.location.search);
    const input = form.querySelector("input[type='search']");
    const results = document.querySelector("[data-search-results]");
    const empty = document.querySelector("[data-empty-search]");
    const status = document.querySelector("[data-search-status]");
    const render = () => {
      const query = input.value.trim();
      const list = articles.filter((article) => matches(article, query));
      results.innerHTML = list.map(cardHtml).join("");
      if (empty) empty.hidden = list.length !== 0;
      if (status) status.textContent = query ? `${list.length} result${list.length === 1 ? "" : "s"} for "${query}".` : "Showing all Insights.";
    };
    input.value = params.get("q") || "";
    form.addEventListener("submit", () => {});
    render();
  });
})();
""")


def render_sitemap() -> None:
    urls = [("/", "1.0", "weekly"), ("/privacy.html", "0.3", "monthly"), ("/terms.html", "0.3", "monthly"), ("/insights/", "0.8", "weekly")]
    urls.extend((f"/insights/{slug}/", "0.6", "weekly") for slug in CATEGORIES)
    urls.extend((article_url(a), "0.7", "monthly") for a in ARTICLES)
    urls.append(("/insights/tags/international-patients/", "0.4", "monthly"))
    body = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path, priority, freq in urls:
        body.append(f"  <url>\n    <loc>{absolute(path)}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>{freq}</changefreq>\n    <priority>{priority}</priority>\n  </url>")
    body.append("</urlset>\n")
    write(ROOT / "sitemap.xml", "\n".join(body))


def main() -> None:
    render_home()
    for slug, cat in CATEGORIES.items():
        render_category(slug, cat)
    for article in ARTICLES:
        render_article(article)
    render_tags()
    render_search()
    render_search_js()
    render_sitemap()


if __name__ == "__main__":
    main()
