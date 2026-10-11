from __future__ import annotations

import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE = "https://aethermed.health"
TODAY = "2026-10-11"

GOOGLE_TAG = """    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-34YKBXVDEF"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-34YKBXVDEF');
    </script>
"""


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
        "slug": "complex-biliary-cancer-case-review-china",
        "title": "How AetherMed Coordinates Review of a Complex Biliary Cancer Case",
        "description": "Learn how AetherMed coordinates records, specialist matching, hospital review and travel planning for a complex biliary cancer assessment in China.",
        "lede": "A complex biliary cancer case rarely turns on one scan or one procedure. The review may need to connect the tumour location, pathology, biliary obstruction, drainage history, liver function, previous treatment and the patient's current condition. AetherMed coordinates the information and hospital pathway so the receiving specialists can assess the case. The hospital and licensed clinicians make every diagnosis and treatment decision.",
        "primary_category": "medical-journey-guides",
        "categories": ["medical-journey-guides", "specialty-treatment"],
        "tags": ["Bile Duct Cancer", "Biliary Cancer", "Multidisciplinary Review", "Medical Records", "International Patients", "Treatment Planning"],
        "image": "01-complex-biliary-cancer-case-review-china.webp",
        "image_alt": "International patient and family member discussing anonymised biliary imaging with a medical coordinator and specialist in China.",
        "published": "2026-10-06",
        "updated": "2026-10-06",
        "featured": True,
        "sections": [
            ("Step 1: Free Assessment and a focused question", [
                "The first step is to define what the patient needs from the review. The question may concern operability, another local procedure, systemic treatment, management of recurrent obstruction, or a second opinion after previous treatment. AetherMed records the current diagnosis, symptoms, recent complications, treatment history, home country, language needs and preferred timing. This initial assessment does not confirm medical suitability or hospital acceptance.",
            ]),
            ("Step 2: Build a review-ready biliary cancer file", [
                "Pathology reports and, if requested, pathology slides or tissue-block information.",
                "Recent contrast CT or MRI and MRCP images in their original digital format, with reports.",
                "ERCP, PTC, drainage and stent procedure notes, including dates and current device status.",
                "A dated treatment timeline covering surgery, chemotherapy, radiotherapy and local procedures.",
                "Recent liver function, bilirubin, blood counts, kidney function, coagulation and relevant tumour-marker results.",
                "A current medication list, allergies, infection history and a concise clinical summary.",
            ], "If fever, jaundice, confusion, severe pain or another urgent change is developing, the patient should seek local medical care immediately. An overseas document review cannot manage an emergency. Keep the original report beside any English translation and use a simple index so dates and procedures can be matched."),
            ("Step 3: Match the case to the right hospital team", [
                "Biliary cancers can involve hepatobiliary surgery, medical oncology, gastroenterology, interventional radiology, radiation oncology, pathology and imaging. Matching therefore depends on the clinical question rather than the diagnosis name alone. AetherMed can identify potential specialist or multidisciplinary routes and confirm what the hospital wants to review. It does not rank a hospital as universally best or promise access to a particular doctor or technology.",
            ]),
            ("Step 4: Coordinate medical review and questions", [
                "The receiving team may ask for missing imaging, pathology confirmation, updated laboratory tests or a consultation before giving an opinion. The review may consider surgery, systemic therapy, biliary drainage, radiotherapy or selected local treatments such as ablation or photodynamic therapy. Listing an option does not mean it is appropriate. Tumour extent, anatomy, prior procedures, infection risk, organ function and treatment goals can all change the decision.",
                "A second medical opinion in China can clarify how specialists interpret the evidence and what additional assessment is required without committing the patient to travel or treatment.",
            ]),
            ("Step 5: Plan appointments and travel only after review", [
                "If an in-person assessment is recommended, AetherMed can coordinate appointment requests, estimated timelines, documents, interpretation, accommodation, airport transfers and local transport where available. Patients should keep bookings flexible until the hospital confirms the pathway. Costs and timing may change if repeat imaging, drainage, infection treatment or a longer admission becomes necessary.",
            ]),
            ("Step 6: Connect treatment and follow-up", [
                "During the China phase, coordination may include registration, interpretation, schedule updates and communication of practical requirements. Before the patient returns home, the hospital should provide procedure or treatment records, medication instructions, follow-up timing, warning signs and a plan for transferring information to the home doctor.",
            ]),
            ("What AetherMed can help with", [
                "For patients considering medical tourism in China, AetherMed can organise and translate records, prepare a case index, identify potential biliary cancer review routes, coordinate hospital questions and appointments, and support interpretation, travel arrangements and follow-up documentation where available. AetherMed does not diagnose, recommend a treatment independently, manage emergencies or guarantee acceptance, timing, cost or outcome.",
            ]),
        ],
        "cta": "Share the diagnosis, pathology, recent imaging, drainage or stent history, treatment timeline and latest blood results. AetherMed can outline the information needed for an initial hospital coordination review.",
        "include_standard_help": False,
        "disclaimer": "This article is for general educational information only and is not medical advice, diagnosis, treatment, or a guarantee of access, suitability, cost, timing, or outcome. AetherMed provides medical coordination and does not independently diagnose or prescribe treatment. Final eligibility and treatment decisions are made by the receiving hospital and licensed clinicians after appropriate assessment. Remote review cannot replace an in-person examination or emergency care. Appointments and hospital acceptance depend on clinical review, institutional policy, and capacity; costs and timelines are estimates, not guarantees. If you may have a medical emergency, contact local emergency services immediately. Use of AetherMed's services is subject to its Terms & Conditions and Privacy Policy.",
    },
    {
        "slug": "photodynamic-therapy-complex-bile-duct-cancer-xian-hospital-case",
        "title": "Photodynamic Therapy for Complex Bile Duct Cancer: A Xi'an Hospital Case",
        "description": "Explore a Xi'an hospital-reported bile duct cancer PDT case, how photodynamic therapy works, its evidence limits and questions patients should ask.",
        "lede": "A May 2026 report from the First Affiliated Hospital of Xi'an Jiaotong University described photodynamic therapy for a patient with complex bile duct cancer at its Land Port campus. The report is useful as an example of a specialised local treatment pathway. It does not show that photodynamic therapy is suitable for every bile duct cancer or that the reported result can be expected in another patient.",
        "primary_category": "success-stories",
        "categories": ["success-stories", "specialty-treatment", "hospitals-doctors"],
        "tags": ["Bile Duct Cancer", "Photodynamic Therapy", "Cholangiocarcinoma", "Xi'an", "Hepatobiliary Care", "Hospital-Reported Cases"],
        "image": "02-photodynamic-therapy-bile-duct-cancer-xian-case.webp",
        "image_alt": "Multidisciplinary hepatobiliary team reviewing generic bile duct imaging and a photodynamic therapy concept.",
        "published": "2026-10-08",
        "updated": "2026-10-08",
        "featured": True,
        "sections": [
            ("What the hospital reported", [
                "The hospital's WeChat article states that its specialised hepatobiliary surgical team carried out precision photodynamic therapy for a complex cholangiocarcinoma case. The available source record does not provide enough verified detail to restate the patient's full diagnosis, prior treatment, device, photosensitising medicine, complications or follow-up. These points should be confirmed with the hospital before patient comparison.",
            ]),
            ("How photodynamic therapy works", [
                "Photodynamic therapy uses a photosensitising medicine followed by light at a selected wavelength. When the medicine is activated in the target area, the reaction can damage local tumour tissue. For bile duct cancer, light may be delivered through an endoscopic or percutaneous route, often in the wider context of biliary drainage and stent management. The medicine, light system, timing and treatment field vary by programme.",
            ]),
            ("When PDT may be discussed", [
                "Published literature mainly discusses endobiliary PDT as a local palliative option for selected patients with unresectable perihilar or extrahepatic cholangiocarcinoma and malignant biliary obstruction. It is not a substitute for determining whether surgery is possible or for considering current systemic treatment. The position of the tumour, drainage anatomy, infection control, previous procedures, liver function and the patient's goals all affect suitability.",
                "The British Society of Gastroenterology guideline states that adjunctive endobiliary photodynamic therapy is not standard care for hilar or distal cholangiocarcinoma receiving palliative treatment. Clinical reviews likewise describe PDT as a context-dependent local biliary strategy rather than an established survival-prolonging treatment.",
            ]),
            ("What the evidence can and cannot show", [
                "Earlier studies and meta-analyses reported signals for improved biliary drainage, quality of life or survival in selected unresectable cases, but much of the evidence was non-randomised or otherwise limited. Results can be affected by drainage quality, infection, stent strategy, repeat treatment and access to systemic therapy. A 2023 systematic review of PDT combined with chemotherapy found a survival association but concluded that stronger evidence was still needed before establishing a standard approach.",
                "Population averages cannot predict an individual patient's result, and evidence about one PDT protocol does not validate every medicine, light-delivery system or treatment schedule.",
            ]),
            ("Risks and practical limits", [
                "Photosensitivity reactions can occur, so patients may need strict light-avoidance instructions after the medicine.",
                "Cholangitis, sepsis, liver abscess, abdominal pain, bleeding or other biliary-procedure complications may occur.",
                "Drainage or stent problems may require urgent reassessment or another procedure.",
                "PDT treats a local area and may not address disease elsewhere in the body.",
                "Availability, regulatory status, admission requirements and cost must be confirmed for the individual hospital and date.",
            ]),
            ("Questions for a specialist review", [
                "Is the disease resectable, and has a hepatobiliary multidisciplinary team reviewed the case?",
                "What is the aim of PDT in this case, and what alternatives are being compared?",
                "Which photosensitiser and light-delivery method would be used?",
                "How will biliary drainage, infection prevention and stent care be managed?",
                "What monitoring, light precautions, repeat sessions and follow-up are expected?",
                "Is the proposed treatment routinely available, part of a study or subject to special approval?",
            ]),
            ("What AetherMed can help with", [
                "For patients considering medical tourism in China, AetherMed can organise and translate pathology, imaging and biliary-procedure records, identify potential hospital review routes, and coordinate questions about multidisciplinary assessment, current PDT availability, appointments, interpretation and travel where available. AetherMed does not determine eligibility, provide PDT, promise access or guarantee a result.",
            ]),
            ("Source and republication note", [
                "English adaptation based on the First Affiliated Hospital of Xi'an Jiaotong University WeChat article '交医精术 | 生命之光！交大一附院陆港院区成功开展复杂胆管癌光动力治疗', published 20 May 2026 (source ID 2655923034_1). The hospital-reported case has been summarised conservatively; additional clinical context comes from clinical guidelines and peer-reviewed reviews. This is not a verbatim translation. Patient details, protocol, outcome and current availability must be reconfirmed before patient comparison.",
            ]),
        ],
        "cta": "Share the pathology, recent CT or MRI and MRCP, drainage or stent reports, treatment history and current blood results. AetherMed can help prepare the information needed for an initial specialist coordination assessment.",
        "include_standard_help": False,
        "disclaimer": "This article is for general educational information only and is not medical advice, diagnosis, treatment, or a guarantee of access, suitability, cost, timing, or outcome. AetherMed provides medical coordination and does not independently diagnose or prescribe treatment. Final eligibility and treatment decisions are made by the receiving hospital and licensed clinicians after appropriate assessment. Remote review cannot replace an in-person examination or emergency care. Appointments and hospital acceptance depend on clinical review, institutional policy, and capacity; costs and timelines are estimates, not guarantees. If you may have a medical emergency, contact local emergency services immediately. Use of AetherMed's services is subject to its Terms & Conditions and Privacy Policy. This is a hospital-reported institutional case, not an independently verified outcome or a prediction for another patient.",
    },
    {
        "slug": "prepare-neurology-imaging-reports-overseas-specialist-review",
        "title": "Preparing Neurology Imaging and Reports for an Overseas Specialist Review",
        "description": "Prepare neurology scans, reports, videos and a clear symptom timeline for an overseas specialist review, with practical tips for secure transfer and translation.",
        "lede": "An overseas neurology review is easier to assess when the specialist can see the original scans, understand how symptoms changed over time and connect each test to a clinical question. A short, organised record set is usually more useful than a large folder of unexplained files.",
        "primary_category": "medical-journey-guides",
        "categories": ["medical-journey-guides", "specialty-treatment"],
        "tags": ["Neurology", "Medical Records", "MRI", "Specialist Review", "Second Opinion", "International Patients"],
        "image": "01-neurology-records-overseas-specialist-review.webp",
        "image_alt": "International patient and family member reviewing organised neurology scans and reports with a medical coordinator.",
        "published": "2026-09-29",
        "updated": "2026-09-29",
        "featured": True,
        "sections": [
            ("Start with one clear clinical question", [
                "State the main reason for the review in one or two sentences. You may be seeking diagnostic clarification, a treatment review, an opinion on surgery or another procedure, or advice about further testing. Add the current diagnosis or suspected diagnosis, the most important symptoms and the decision you need help with. This helps the receiving team identify the right neurologist or multidisciplinary service.",
            ]),
            ("Send images as well as written reports", [
                "A radiology report summarises the original reader's findings, but it does not replace the scan. Provide the original digital files for relevant MRI, CT, PET, SPECT or angiography studies, preferably in DICOM format, together with the report. Label each study with the date, body area, contrast status and facility. Do not rely only on photographs of films or screenshots if the original files are available.",
                "Include the earliest useful scan and the most recent scan so the specialist can compare change over time.",
                "Keep each study in its original folder structure and avoid renaming individual DICOM files.",
                "Add pathology, neurophysiology or laboratory reports when they affect the neurological question.",
                "Ask before uploading very large studies and use the hospital's approved secure transfer method.",
            ]),
            ("Build a concise neurological timeline", [
                "List the date or approximate month when each major symptom began, how it progressed and what changed after treatment. Include hospital admissions, falls, seizures, loss of consciousness, infections and major medication changes. For parkinsonism or other movement disorders, note tremor, slowness, stiffness, balance, speech, swallowing, sleep and cognitive changes. A specialist still needs a clinical history and examination; imaging alone may not establish the diagnosis.",
                "Parkinson's disease is diagnosed clinically. Imaging may support the assessment or help exclude other conditions, which is why the symptom history and examination findings should travel with the scans.",
            ]),
            ("Add videos and examination records when useful", [
                "Short videos can help document intermittent symptoms such as tremor, gait changes, involuntary movements, speech episodes or seizures, but record them only when it is safe and with the patient's consent. Note the date, medication timing and what the viewer should notice. Include formal neurological examination notes and standardised scores if your treating team has recorded them.",
            ]),
            ("Prepare medication and treatment information", [
                "Use generic medicine names where possible, with dose, frequency, start date and reason for use.",
                "Record benefits, side effects and why a medicine was stopped or changed.",
                "List implanted devices, previous neurosurgery, rehabilitation and other relevant treatment.",
                "Include allergies, major medical conditions and current mobility or care needs.",
            ]),
            ("Translate for clarity without changing the source", [
                "Keep the original report and attach an English translation if requested. The translation should preserve dates, measurements, anatomical terms and uncertainty such as 'possible' or 'cannot exclude.' Do not edit the original record or convert a preliminary impression into a confirmed diagnosis. A short bilingual index can show the file name, document type, date and language.",
                "Use AetherMed's broader medical-record preparation guide for a complete file checklist. If the question is whether another interpretation or treatment path should be considered, review how to request a second medical opinion in China.",
            ]),
            ("Protect privacy and keep a complete copy", [
                "Use a secure upload route approved by the receiving organisation. Check that the patient name, date of birth and study date match across the files, and keep an unchanged backup. Share only the records needed for the review and confirm who may access them. If urgent symptoms are developing, seek local emergency care rather than waiting for an overseas response.",
            ]),
            ("What AetherMed can help with", [
                "For patients considering medical tourism in China, AetherMed can help organise and translate neurology records, prepare an indexed imaging list, identify an appropriate hospital or specialist review route, and coordinate secure submission, appointments, interpretation and the practical patient journey where available. AetherMed does not interpret scans, diagnose a neurological condition or guarantee hospital acceptance.",
            ]),
        ],
        "cta": "Share your main neurological question, diagnosis or suspected diagnosis, symptom timeline and a list of available scans. AetherMed can outline what may be needed for an initial coordination assessment.",
        "include_standard_help": False,
        "disclaimer": "This article is for general educational information only and is not medical advice, diagnosis, treatment, or a guarantee of access, suitability, cost, timing, or outcome. AetherMed provides medical coordination and does not independently diagnose or prescribe treatment. Final eligibility and treatment decisions are made by the receiving hospital and licensed clinicians after appropriate assessment. Remote review cannot replace an in-person examination or emergency care. Appointments and hospital acceptance depend on clinical review, institutional policy, and capacity; costs and timelines are estimates, not guarantees. If you may have a medical emergency, contact local emergency services immediately. Use of AetherMed's services is subject to its Terms & Conditions and Privacy Policy.",
    },
    {
        "slug": "alpha-synuclein-pet-tracer-parkinsons-research",
        "title": "An Alpha Synuclein PET Tracer Study for Earlier Parkinson's Disease Diagnosis",
        "description": "Learn what Huashan Hospital's alpha-synuclein PET tracer registration study may mean for Parkinson's research—and why it is not yet a routine diagnostic test.",
        "lede": "A June 2026 report from Huashan Hospital said that a domestically developed alpha-synuclein PET tracer had entered a clinical registration study for earlier Parkinson's disease diagnosis. The project is relevant because alpha-synuclein is closely linked to Parkinson's pathology, but a registration study is research. It does not mean the tracer is already an approved or routinely available diagnostic test.",
        "primary_category": "specialty-treatment",
        "categories": ["specialty-treatment", "hospitals-doctors", "news"],
        "tags": ["Parkinson's Disease", "Alpha Synuclein", "PET Imaging", "Huashan Hospital", "Clinical Research", "Neurology"],
        "image": "02-alpha-synuclein-pet-tracer-parkinsons-research.webp",
        "image_alt": "Neurologist and nuclear medicine researcher reviewing a generic brain PET scan in a modern imaging research suite.",
        "published": "2026-10-01",
        "updated": "2026-10-01",
        "featured": True,
        "sections": [
            ("Why alpha synuclein is being studied", [
                "Alpha-synuclein is a protein found in the nervous system. In Parkinson's disease and related synucleinopathies, abnormal forms can accumulate in nerve cells. Researchers have long sought a PET tracer that can enter the brain, bind selectively to relevant alpha-synuclein deposits and produce a signal that can be measured reliably in living people.",
                "That is technically difficult. The target is present at relatively low density, different diseases may contain different forms of alpha-synuclein, and a tracer can also bind to other structures. These problems can affect image interpretation and diagnostic accuracy.",
            ]),
            ("What PET tracer research is designed to test", [
                "A PET tracer is a small amount of a radiolabelled compound used to visualise a biological target. Before a tracer can support routine care, studies need to evaluate safety, radiation dosimetry, brain uptake, selectivity, image reproducibility and whether the signal separates relevant patient groups from controls. Researchers must also determine what a positive or negative result means for an individual patient.",
                "Early human studies of other alpha-synuclein tracers show both the promise and the limits of the field. A study of ACI-12589 reported a signal in multiple system atrophy but low and variable binding in sporadic Parkinson's disease. A small first-in-human study of MK-7337 reported elevated signals in selected brain regions in participants with Parkinson's disease, while also noting off-target binding concerns. These are different tracers and cannot be used to predict the performance of the Huashan tracer.",
            ]),
            ("What the Huashan Hospital report means", [
                "The hospital's WeChat report describes the start of a clinical registration study for a domestically developed alpha-synuclein PET tracer. In practical terms, the study is intended to generate evidence required for regulatory and clinical evaluation. The public title alone does not establish the study protocol, participant criteria, accuracy, approval status or present availability to international patients. Those details must be confirmed with the hospital and the applicable trial or regulatory record.",
            ]),
            ("Why this research could matter", [
                "If a tracer is eventually validated, it could help researchers examine disease biology in living patients, select participants for trials, measure target engagement and study progression. It may also contribute to earlier or more specific assessment. Whether it improves diagnosis or changes treatment must be shown in appropriately designed studies; the launch of a registration study does not prove those benefits.",
            ]),
            ("Questions to ask before considering a research assessment", [
                "What is the exact tracer and study registration number?",
                "Is the study recruiting, and what are the inclusion and exclusion criteria?",
                "Is participation intended for diagnosis, research measurement or treatment selection?",
                "What radiation exposure, preparation, visits and follow-up are required?",
                "Will individual results be returned, and could they change clinical care?",
                "Are international participants accepted, and who pays for study-related and non-study care?",
            ]),
            ("What AetherMed can help with", [
                "For patients considering medical tourism in China, AetherMed can help organise neurology records, clarify the question for specialist review, contact potential hospital pathways and coordinate questions about current study status, eligibility review, appointments, interpretation and travel where available. AetherMed does not operate the study, interpret PET images or guarantee recruitment, access, diagnosis or outcome.",
            ]),
            ("Source and republication note", [
                "English adaptation based on Huashan Hospital's WeChat article '国内首个自主研发的帕金森病早诊α-syn PET示踪剂启动临床注册研究，精准早诊迈出关键一步', published 2 June 2026 (source ID 2671320834_1). Additional context is drawn from cited clinical guidance and published alpha-synuclein PET studies. This is not a verbatim translation, and the hospital study details should be reconfirmed before publication.",
            ]),
        ],
        "cta": "Share your diagnosis or suspected diagnosis, symptom history, current treatment, recent neurological assessment and imaging list. AetherMed can help identify the information needed to ask a hospital about specialist review or relevant research routes.",
        "include_standard_help": False,
        "disclaimer": "This article is for general educational information only and is not medical advice, diagnosis, treatment, or a guarantee of access, suitability, cost, timing, or outcome. AetherMed provides medical coordination and does not independently diagnose or prescribe treatment. Final eligibility and treatment decisions are made by the receiving hospital and licensed clinicians after appropriate assessment. Remote review cannot replace an in-person examination or emergency care. Appointments and hospital acceptance depend on clinical review, institutional policy, and capacity; costs and timelines are estimates, not guarantees. If you may have a medical emergency, contact local emergency services immediately. Use of AetherMed's services is subject to its Terms & Conditions and Privacy Policy. The tracer described is a research subject and should not be understood as an approved or routinely available clinical test.",
    },
    {
        "slug": "breast-cancer-mdt-international-consultation-guangdong-provincial-peoples-hospital",
        "title": "Breast Cancer MDT International Consultation at Guangdong Provincial People's Hospital",
        "description": "Learn how Guangdong Provincial People's Hospital reports its breast cancer MDT international consultation and what patients should prepare for review.",
        "lede": "A breast cancer multidisciplinary team (MDT) brings different specialties together to review one case. For an international patient, the value is not simply the number of doctors involved: it is whether the team receives complete pathology, imaging, treatment history and a clear clinical question.",
        "primary_category": "hospitals-doctors",
        "categories": ["hospitals-doctors", "specialty-treatment"],
        "tags": ["Guangdong Provincial People's Hospital", "Breast Cancer", "MDT Review", "International Consultation", "Medical Records"],
        "image": "02-breast-cancer-mdt-guangdong-provincial-peoples-hospital.webp",
        "image_alt": "Multidisciplinary breast cancer team discussing an anonymised case with an international patient.",
        "published": "2026-09-17",
        "updated": "2026-09-17",
        "featured": True,
        "sections": [
            ("What the hospital reports about its international MDT", [
                "Guangdong Provincial People's Hospital describes its Wednesday Breast Cancer International Consultation as a platform established by Professor Liao Ning. The hospital says the programme began in late 2019 and brings Chinese and international speakers together to discuss difficult cases, treatment standards and developments in the field.",
                "A September 2026 hospital notice summarised a previous discussion involving an anonymised 45-year-old premenopausal patient with recurrent, widely metastatic breast cancer and a PALB2 alteration. According to the notice, specialists from several disciplines offered opinions and Professor Liao integrated the MDT discussion into a proposed next-step plan. This is a hospital-reported educational case, not evidence that the same approach is appropriate for another patient.",
            ]),
            ("Why an MDT may be useful in a complex breast cancer case", [
                "Breast cancer decisions can depend on pathology, stage, previous treatment, current disease sites, menopausal status, general health and biomarkers such as ER, PR and HER2. Surgery, systemic treatment and radiotherapy may also need to be sequenced rather than considered separately.",
                "The National Cancer Institute's breast cancer treatment overview notes that multidisciplinary management can be important when planning preoperative treatment and local therapy. An MDT does not guarantee agreement or a specific treatment; it should make the reasoning, uncertainties and next information needs clearer.",
            ]),
            ("What an international patient should prepare", [
                "A one-page summary of the diagnosis, current symptoms, treatment goals and questions for the MDT.",
                "The original pathology report, immunohistochemistry and biomarker results, including ER, PR, HER2 and other tests relevant to the case.",
                "A chronological treatment history showing surgery, radiotherapy and each systemic therapy, with dates, response, toxicity and reason for change.",
                "Recent imaging reports and original DICOM files where available, plus the comparison images needed to show change over time.",
                "Current medicines, allergies, performance status, major medical conditions and recent blood-test results.",
                "Previous molecular or germline testing reports, with confirmation of whether a finding is germline or somatic when known.",
            ], "The NCI guide to breast cancer diagnosis explains how pathology, imaging and biomarker testing help define the disease and support treatment planning. For practical file organisation, follow AetherMed's medical-record preparation checklist."),
            ("Questions to clarify before requesting a review", [
                "Is the consultation an educational case conference, a formal patient consultation or both?",
                "Which specialties are expected to review the case, and will the patient receive a written summary?",
                "Does the team need pathology slides, tissue blocks or repeat biomarker testing?",
                "Can the review be completed remotely, or is an in-person examination required?",
                "What language support, fees, scheduling rules and international-patient access route apply?",
            ], "The hospital's public notice describes a programme and a reported discussion; it should not be read as confirmation that every overseas case can be submitted, that a named expert will attend, or that the service is available on a particular date. Current access must be confirmed directly with the hospital."),
            ("What AetherMed can help with", [
                "For patients considering medical tourism in China, AetherMed can help organise and translate breast cancer records, identify missing pathology or imaging, formulate focused questions, and explore an appropriate hospital or MDT review route. Where available, we can coordinate consultation scheduling, interpretation, travel and follow-up documents. The receiving hospital decides whether it can accept the case, which specialists participate and what assessment or treatment is appropriate.",
            ]),
            ("Source and republication note", [
                "Adapted into English from Guangdong Provincial People's Hospital's official website notice '[9月9日]普外乳腺科周三乳腺癌MDT国际会诊', published 4 September 2026. Programme details and the anonymised case summary are attributed to the hospital. Participation, access route, fees, specialists and current availability must be confirmed with the hospital; the reported case does not predict another patient's recommendation or outcome.",
            ]),
        ],
        "cta": "Share your pathology, biomarker results, imaging, treatment history and current questions. AetherMed can review whether the records are ready for an initial hospital or MDT coordination request.",
        "include_standard_help": False,
        "disclaimer": "This article is for general educational information only and is not medical advice, diagnosis, treatment, or a guarantee of access, suitability, cost, timing, or outcome. AetherMed provides medical coordination and does not independently diagnose or prescribe treatment. Final eligibility and treatment decisions are made by the receiving hospital and licensed clinicians after appropriate assessment. Remote review cannot replace an in-person examination or emergency care. Appointments and hospital acceptance depend on clinical review, institutional policy, and capacity; costs and timelines are estimates, not guarantees. If you may have a medical emergency, contact local emergency services immediately. Use of AetherMed's services is subject to its Terms & Conditions and Privacy Policy. This is a hospital-reported educational case, not an independently verified outcome or a prediction for another patient.",
    },
    {
        "slug": "car-t-case-manager-international-patient-journey",
        "title": "How a Case Manager Supports an International CAR-T Patient Journey",
        "description": "Learn how a case manager supports international CAR-T patients in China through records, hospital review, travel, treatment logistics and follow-up.",
        "lede": "For an international patient, CAR-T treatment can involve far more than one hospital appointment. Records, eligibility review, manufacturing or protocol timing, travel, a caregiver, local accommodation, interpretation, monitoring and follow-up all need to connect. A case manager helps organise these moving parts - but does not make medical decisions.",
        "primary_category": "medical-journey-guides",
        "categories": ["medical-journey-guides", "specialty-treatment"],
        "tags": ["CAR-T Therapy", "Case Management", "International Patients", "Treatment Planning", "Follow-Up"],
        "image": "01-car-t-case-manager-international-patient-journey.webp",
        "image_alt": "International patient and caregiver reviewing a CAR-T journey plan with a medical case manager and clinician in China.",
        "published": "2026-09-15",
        "updated": "2026-09-15",
        "featured": True,
        "sections": [
            ("What a dedicated case manager does - and does not do", [
                "A medical case manager in China is a coordination contact between the patient, family, AetherMed and the receiving hospital. The role is to keep information, schedules and practical tasks aligned. The hospital's licensed clinicians decide whether CAR-T is appropriate, which product or protocol may be considered, what tests are required and how risks are managed.",
                "If you are still exploring eligibility, read CAR-T Therapy in China: A First Guide for International Patients. The National Cancer Institute also explains the collection, cell-modification and infusion stages and notes that serious toxicities can occur.",
            ]),
            ("1. Initial inquiry and Free Assessment", [
                "The case manager records the diagnosis, current condition, previous treatment, goals, preferred timing, country, language needs and whether a caregiver can travel. The first task is to identify what the patient is asking the hospital to assess and which records are missing - not to promise a place or quote a final treatment plan.",
            ]),
            ("2. Medical review and doctor matching", [
                "The case manager organises pathology, imaging, treatment history, recent disease assessment, laboratory results and relevant transplant or cellular-therapy records. Files may need indexing or translation before submission. Hospital matching should consider the exact disease and target, the team and programme, toxicity-management resources, international-patient route and current availability.",
                "Use AetherMed's medical-record preparation guide to build a review-ready package. A preliminary response may request updated tests, pathology review, a remote consultation or another treatment step before travel.",
            ]),
            ("3. Appointment and travel support", [
                "If the hospital agrees to proceed with further assessment, the case manager helps confirm the department, expected visit window, required documents, estimated deposits and the sequence of appointments. Coordination may include invitation-letter information, travel planning, accommodation near the hospital, interpretation and a caregiver plan. Patients should avoid non-refundable bookings until the hospital pathway is sufficiently clear.",
            ]),
            ("4. Arrival in China", [
                "Before the first hospital visit, the case manager checks identification, appointment details, original records, medication information and payment arrangements. On arrival, support may include airport or accommodation coordination and an orientation to registration, testing and hospital procedures. New clinical findings can still change the schedule.",
            ]),
            ("5. Treatment-stage coordination", [
                "During the hospital phase, the case manager supports communication, interpretation, scheduling, payment logistics and updates requested by the clinical team. CAR-T pathways may include collection, treatment while cells are prepared, conditioning chemotherapy, infusion and close monitoring, but the exact sequence varies by product, protocol and patient.",
                "Because cytokine release syndrome, neurological effects and infection can be serious, symptoms must be reported to the treating team immediately. The NCI patient overview describes these risks. The case manager can help communication, but emergency decisions belong to clinicians.",
            ]),
            ("6. Follow-up at home", [
                "Before departure, the case manager helps collect discharge summaries, medication instructions, laboratory and imaging results, emergency contacts and the hospital's follow-up schedule. The patient should know which warning signs require urgent local care and how information will be handed to the home doctor. Follow-up requirements can continue well beyond the trip.",
            ]),
            ("What AetherMed can help with", [
                "For patients considering medical tourism in China, AetherMed can assign a coordination contact, organise and translate records, identify possible CAR-T hospital pathways, track hospital questions, and support appointments, interpretation, travel, admission logistics and return-home documentation where available. We do not diagnose, decide CAR-T eligibility, select a product, control hospital capacity or guarantee acceptance, timing, cost or outcome.",
            ]),
        ],
        "cta": "Share your diagnosis, treatment history, latest disease assessment and preferred timing. AetherMed can identify the information needed for an initial coordination review and outline possible next steps.",
        "include_standard_help": False,
        "disclaimer": "This article is for general educational information only and is not medical advice, diagnosis, treatment, or a guarantee of access, suitability, cost, timing, or outcome. AetherMed provides medical coordination and does not independently diagnose or prescribe treatment. Final eligibility and treatment decisions are made by the receiving hospital and licensed clinicians after appropriate assessment. Remote review cannot replace an in-person examination or emergency care. Appointments and hospital acceptance depend on clinical review, institutional policy, and capacity; costs and timelines are estimates, not guarantees. If you may have a medical emergency, contact local emergency services immediately. Use of AetherMed's services is subject to its Terms & Conditions and Privacy Policy.",
    },
    {
        "slug": "west-china-hospital-failing-mitral-bioprosthetic-valve",
        "title": "How West China Hospital Approached a Failing Mitral Bioprosthetic Valve",
        "description": "See how West China Hospital planned a reported high-risk mitral valve-in-valve case using CT simulation, Heart Team review, and the BATMAN technique.",
        "lede": "A hospital-reported case from West China Hospital shows how CT simulation, multidisciplinary review, transcatheter valve-in-valve treatment, and a leaflet-management technique were combined for a patient considered at high risk for repeat open surgery.",
        "primary_category": "hospitals-doctors",
        "categories": ["hospitals-doctors", "specialty-treatment", "success-stories"],
        "tags": ["West China Hospital", "Structural Heart Disease", "Mitral Valve", "Valve-in-Valve", "Hospital-Reported Cases"],
        "image": "02-west-china-hospital-mitral-valve-in-valve-batman.webp",
        "image_alt": "Structural-heart team reviewing CT images before mitral valve-in-valve treatment.",
        "published": "2026-09-10",
        "updated": "2026-09-10",
        "featured": True,
        "sections": [
            ("The clinical problem: a replacement valve can also deteriorate", [
                "A surgical bioprosthetic mitral valve can gradually narrow, leak, or develop mixed dysfunction. When symptoms return, the team must determine whether the problem is structural deterioration, thrombosis, infection, paravalvular leakage, patient-prosthesis mismatch, or another cause. The decision is not automatically between another open operation and one standard catheter procedure.",
            ]),
            ("What West China Hospital reported", [
                "West China Hospital reported treating an anonymised 72-year-old woman whose surgically implanted mitral bioprosthesis had deteriorated about seven years after the original operation. She had chest tightness, shortness of breath, reduced exercise tolerance, severe pulmonary hypertension, and a high predicted risk of left ventricular outflow tract obstruction. The hospital described repeat open surgery as high risk after multidisciplinary assessment.",
                "The cardiac and vascular surgery team led by Chief Physician Hu Jia worked with the anaesthesia and transoesophageal-echocardiography team led by Chief Physician Song Haibo. They planned a transfemoral venous, transseptal transcatheter mitral valve-in-valve procedure, or MVIV. Pre-procedure CT simulation showed that a conventional valve-in-valve implant could leave an unacceptably narrow new outflow tract.",
            ]),
            ("Why the team added the BATMAN technique", [
                "During mitral valve-in-valve implantation, the new valve can displace the old bioprosthetic leaflet toward the interventricular septum. In a susceptible anatomy, this can obstruct blood leaving the left ventricle and cause severe haemodynamic instability. The hospital therefore combined MVIV with balloon-assisted translocation of the mitral anterior leaflet, known as BATMAN. The intended purpose was to move the leaflet toward the left atrium and preserve a larger neo-left-ventricular outflow tract.",
                "The hospital described this as China's first transfemoral-transseptal MVIV combined with BATMAN. The 'first' claim applies to this specific combined approach, not to all mitral valve-in-valve procedures or all transcatheter mitral interventions.",
            ]),
            ("Imaging and teamwork shaped the procedure", [
                "The reported pathway used CT reconstruction and simulated valve implantation before the procedure, then transoesophageal echocardiography during transseptal puncture, leaflet crossing, balloon expansion, and valve deployment. This illustrates why structural-heart cases often require cardiac surgery, interventional cardiology, imaging, anaesthesia, and perioperative teams to agree on anatomy, alternatives, rescue plans, and monitoring.",
                "The 2025 ESC/EACTS valvular-heart-disease guideline states that mitral valve-in-valve treatment may be considered for selected patients at increased surgical risk when anatomy is suitable, with the treatment choice made by an interdisciplinary Heart Team.",
            ]),
            ("The reported short-term outcome - and its limits", [
                "According to the hospital report, the key procedural steps took about two and a half hours and estimated blood loss was approximately 10 mL. Immediate echocardiography showed a stable valve, normal opening and closing, no obvious paravalvular leak, and no sign of left ventricular outflow tract obstruction. The patient was extubated in the operating room, returned to a standard ward, mobilised the next day, and was discharged on day seven.",
                "These are hospital-reported peri-procedural and discharge observations from one case. They do not establish long-term durability, comparative safety, freedom from reintervention, or suitability for another patient. Follow-up echocardiography and clinical monitoring remain important.",
                "NICE guidance on transcatheter mitral valve-in-valve implantation highlights the need for careful patient selection, specialist centres, and governance for this type of intervention.",
            ]),
            ("What international patients should prepare", [
                "The operative report and implant card for the original mitral bioprosthesis, including model and size.",
                "Recent transthoracic and transoesophageal echocardiography, cardiac CT, and the original image files where available.",
                "Symptoms, functional limitation, pulmonary-pressure measurements, rhythm history, anticoagulation, and current medication list.",
                "Previous cardiac operations, coronary disease, kidney and lung function, frailty, infection history, and other surgical-risk factors.",
                "A clear question for the Heart Team: redo surgery, valve-in-valve treatment, another catheter strategy, or continued medical management.",
            ], "The receiving Heart Team may request repeat imaging or additional testing before deciding whether any intervention is suitable."),
            ("What AetherMed can help with", [
                "For patients considering medical tourism in China, AetherMed can help organise valve records, echocardiography, CT images, previous operative reports, medication history, and current cardiac assessments for a structural-heart review. We can identify possible hospital and Heart Team routes, clarify missing imaging or tests, and coordinate remote review, appointments, interpretation, travel, admission logistics, and follow-up documents where available. The receiving team makes the final diagnosis and decides whether surgery, MVIV, BATMAN, or another option is appropriate.",
            ]),
            ("Source and republication note", [
                "Adapted into English from West China Hospital's official WeChat report '国内首例！华西医院成功实施手术精准解决二尖瓣生物瓣衰败问题', published 29 June 2026 (source ID 2652794063_2). Patient identity remains anonymised. Procedure details and short-term observations are attributed to the hospital report and should not be interpreted as independently verified outcomes or predictions for other patients.",
            ]),
        ],
        "cta": "Share the original valve information, recent echocardiography and CT, prior operative report, symptoms, and current medical summary for an initial coordination assessment.",
        "include_standard_help": False,
        "disclaimer": "This article is for general educational information only and is not medical advice, diagnosis, treatment, or a guarantee of access, suitability, cost, timing, or outcome. AetherMed provides medical coordination and does not independently diagnose or prescribe treatment. Final eligibility and treatment decisions are made by the receiving hospital and licensed clinicians after appropriate assessment. Remote review cannot replace an in-person examination or emergency care. Appointments and hospital acceptance depend on clinical review, institutional policy, and capacity; costs and timelines are estimates, not guarantees. If you may have a medical emergency, contact local emergency services immediately. Use of AetherMed's services is subject to its Terms & Conditions and Privacy Policy. This is a hospital-reported institutional case, not an independently verified outcome or a prediction for another patient.",
    },
    {
        "slug": "prepare-car-t-case-hospital-review-china",
        "title": "How AetherMed Prepares a CAR-T Case for Hospital Review",
        "description": "Learn how AetherMed prepares a CAR-T case for hospital review in China, including the clinical summary, pathology, imaging, treatment history, and safety tests.",
        "lede": "A hospital cannot assess a CAR-T request from a diagnosis label alone. A useful review package connects the pathology, treatment chronology, current disease status, safety information, and the patient's specific question in a format the receiving team can evaluate.",
        "primary_category": "medical-journey-guides",
        "categories": ["medical-journey-guides", "specialty-treatment"],
        "tags": ["CAR-T Therapy", "Medical Records", "Hospital Review", "International Patients", "Treatment Planning"],
        "image": "01-car-t-case-hospital-review.webp",
        "image_alt": "International patient, medical coordinator and haematologist reviewing an organised CAR-T case file in China.",
        "published": "2026-09-08",
        "updated": "2026-09-08",
        "featured": True,
        "sections": [
            ("Why case preparation matters", [
                "A CAR-T hospital review is not a general request for a price or appointment. The receiving team needs to decide whether the diagnosis, treatment history, current disease status, organ function, infection risk, and practical timing justify a formal assessment. A well-prepared case helps the hospital identify missing information and respond to the actual clinical question. It does not guarantee eligibility.",
                "Start with CAR-T Therapy in China: A First Guide for International Patients if you need an overview of eligibility, treatment stages, risks, and logistics.",
            ]),
            ("1. Define the question before collecting files", [
                "AetherMed first clarifies what the patient wants the hospital to assess: an approved CAR-T product, a second opinion on treatment sequencing, a possible clinical study, or another haematology option. We record the diagnosis, current country, treating doctor, urgency, preferred timing, language needs, and whether the patient can travel with a caregiver. This prevents a large file upload from arriving without a usable request.",
            ]),
            ("2. Build a concise clinical summary", [
                "Confirmed diagnosis, subtype, stage or risk classification, and date of diagnosis.",
                "A chronological treatment table showing each regimen, dates, best response, relapse or progression, toxicity, and reason for stopping.",
                "Stem-cell transplant, prior cellular therapy, radiotherapy, surgery, and significant complications.",
                "Current symptoms, performance status, active problems, medications, allergies, and the patient's main treatment goal.",
            ], "The summary should let a specialist understand the case before opening the attachments."),
            ("3. Collect the disease-specific evidence", [
                "For lymphoma, leukaemia, or myeloma, the team may need original pathology reports, immunohistochemistry, flow cytometry, cytogenetics, molecular tests, bone-marrow reports, target-antigen information, and the most recent PET-CT, CT, MRI, or other disease assessment. Imaging reports are useful, but the hospital may also request DICOM image files or pathology slides for review.",
                "A published CAR-T referral documentation list illustrates why treatment summaries, current laboratory tests, cardiac assessment, imaging, and diagnosis-specific reports are commonly requested. Each Chinese hospital sets its own requirements.",
            ]),
            ("4. Add safety and treatment-readiness information", [
                "Recent blood counts, kidney and liver function, coagulation, infection screening, cardiac testing, neurological history, and information about active infection may affect whether review can proceed. The hospital may ask for updated tests even when similar results are already available. A remote review cannot replace its own examination or pre-treatment work-up.",
                "The NSW Agency for Clinical Innovation's CAR-T patient information and checklist shows how heart, kidney, lung, neurological, infection, and disease assessments can form part of preparation. Protocols vary by product and centre.",
            ]),
            ("5. Organise, translate, and quality-check the records", [
                "Keep original reports and translations together; do not replace or alter the source document.",
                "Use clear English filenames with the test type and date, and remove duplicate screenshots.",
                "Create one treatment chronology and one file index so reviewers can find the supporting evidence.",
                "Flag pending tests, missing pathology, uncertain drug names, and conflicting dates instead of guessing.",
            ], "See Preparing Medical Records for Treatment in China for the broader record-preparation principles."),
            ("6. Match the case and submit a focused review package", [
                "Hospital matching should consider the exact disease, target, product or protocol, specialist team, toxicity-management capability, international-patient route, and current availability. AetherMed submits only the relevant package and a focused question list. The hospital may request repeat pathology, new imaging, further treatment, an online consultation, or an in-person assessment before making any decision.",
            ]),
            ("What AetherMed can help with", [
                "For patients considering medical tourism in China, AetherMed can help turn fragmented CAR-T records into a structured hospital-review package, coordinate translation, identify possible haematology and cellular-therapy teams, track requested updates, and arrange consultations, appointments, interpretation, travel documentation, and follow-up materials where available. AetherMed does not diagnose, select a CAR-T product, determine eligibility, or guarantee acceptance, cost, timing, trial enrolment, or outcome.",
            ]),
        ],
        "cta": "Submit your pathology, treatment history, latest disease assessment, recent laboratory results, and any previous transplant or cellular-therapy records for an initial coordination review.",
        "include_standard_help": False,
        "disclaimer": "This article is for general educational information only and is not medical advice, diagnosis, treatment, or a guarantee of access, suitability, cost, timing, or outcome. AetherMed provides medical coordination and does not independently diagnose or prescribe treatment. Final eligibility and treatment decisions are made by the receiving hospital and licensed clinicians after appropriate assessment. Remote review cannot replace an in-person examination or emergency care. Appointments and hospital acceptance depend on clinical review, institutional policy, and capacity; costs and timelines are estimates, not guarantees. If you may have a medical emergency, contact local emergency services immediately. Use of AetherMed's services is subject to its Terms & Conditions and Privacy Policy.",
    },
    {
        "slug": "complex-atrial-flutter-pulsed-field-ablation-china-japan-friendship-hospital",
        "title": "A Complex Atrial Flutter Case Treated with Pulsed Field Ablation at China-Japan Friendship Hospital",
        "description": "Learn what a hospital-reported complex atrial flutter case at China-Japan Friendship Hospital shows about pulsed field ablation and specialist review.",
        "lede": "A hospital-reported case from China-Japan Friendship Hospital offers a useful view of how newer ablation technology may be considered for a complex heart-rhythm problem - and why specialist mapping and case-specific assessment remain essential.",
        "primary_category": "success-stories",
        "categories": ["success-stories", "hospitals-doctors", "specialty-treatment"],
        "tags": ["China-Japan Friendship Hospital", "Cardiology", "Atrial Flutter", "Pulsed Field Ablation", "Hospital-Reported Cases"],
        "image": "02-complex-atrial-flutter-pfa-china-japan-friendship-hospital.webp",
        "image_alt": "Cardiac electrophysiology team reviewing a 3D rhythm map during a pulsed field ablation procedure.",
        "published": "2026-09-03",
        "updated": "2026-09-03",
        "featured": True,
        "sections": [
            ("What the hospital reported", [
                "China-Japan Friendship Hospital reported in July 2026 that its team had completed the hospital's first pulsed field ablation procedure for a complex atrial flutter case. The source positions the procedure as a hospital milestone. It does not, by itself, establish that pulsed field ablation is suitable for every person with atrial flutter or that one institutional case predicts long-term results.",
            ]),
            ("Atrial flutter is not the same as atrial fibrillation", [
                "Both conditions are abnormal atrial rhythms, but their electrical mechanisms and ablation targets can differ. Typical atrial flutter often follows a recognised circuit in the right atrium. Atypical or complex flutter may involve scar tissue, previous surgery or ablation, or a circuit in another part of the atria. An electrophysiology team may use three-dimensional mapping and intracardiac signals to identify the pathway before selecting where and how to ablate.",
                "The 2025 international clinical consensus statement on atrial tachycardia emphasises mechanism-based mapping, procedural safety, and institutional quality for focal and re-entrant atrial tachycardias.",
            ]),
            ("What pulsed field ablation does", [
                "Pulsed field ablation, or PFA, uses short electrical pulses to create irreversible electroporation in targeted cells. Unlike radiofrequency energy or cryotherapy, it is described as a non-thermal ablation method. Its tissue selectivity is one reason it has attracted interest, particularly for pulmonary-vein isolation in atrial fibrillation. The device, waveform, catheter position, dose, and rhythm mechanism still matter, and PFA does not remove the need for careful mapping or complication management.",
                "NICE guidance on PFA for atrial fibrillation describes the procedure and evidence for atrial fibrillation. Evidence for a specific complex-flutter circuit should not be assumed to be identical to the evidence for pulmonary-vein isolation.",
            ]),
            ("Why a complex flutter case needs specialist review", [
                "The team must confirm the rhythm mechanism rather than relying on symptoms alone.",
                "Prior ablation, heart surgery, congenital anatomy, scar, implanted devices, and other heart disease can change the map and procedural plan.",
                "The ablation energy and catheter system must suit the intended target and the team's experience.",
                "Stroke risk, anticoagulation, anaesthesia, vascular access, and post-procedure monitoring require individual planning.",
                "Acute termination of a rhythm is not the same as durable freedom from recurrence; follow-up remains necessary.",
            ], "These factors require an individual electrophysiology assessment and cannot be resolved from a diagnosis label alone."),
            ("What this hospital-reported success story can - and cannot - show", [
                "The report indicates that a high-level Chinese hospital is applying a newer ablation technology to a complex rhythm case and building institutional experience beyond standard atrial-fibrillation workflows. That is relevant to international patients seeking specialist assessment in China. However, a single hospital report cannot compare PFA with radiofrequency ablation, define complication rates, prove superiority, or confirm that the same technology is routinely available for another patient's rhythm.",
            ]),
            ("Questions to ask before travelling", [
                "Has the rhythm been documented on ECG, Holter monitoring, or an electrophysiology study?",
                "Is the proposed target typical flutter, atypical flutter, atrial tachycardia, atrial fibrillation, or more than one rhythm?",
                "Why is PFA being considered instead of radiofrequency, cryoablation, medication, or another strategy?",
                "Which device and mapping system would be used, and what is the team's experience with this specific rhythm?",
                "What are the expected hospital stay, anticoagulation plan, follow-up schedule, estimated cost, and alternatives if the rhythm recurs?",
            ], "The hospital should confirm the proposed approach after reviewing the patient's current records and clinical status."),
            ("What AetherMed can help with", [
                "For patients considering medical tourism in China, AetherMed can help organise ECGs, Holter reports, echocardiography, imaging, prior ablation reports, medication history, and discharge records for specialist review. We can help identify possible cardiology and electrophysiology routes, clarify additional tests requested by the hospital, and coordinate remote review, appointments, interpretation, travel, admission, and follow-up documentation where available. The hospital and electrophysiology team make the final diagnosis, technology choice, and treatment decision.",
            ]),
            ("Source and republication note", [
                "Adapted into English from China-Japan Friendship Hospital's official WeChat article '救治现场丨中日友好医院成功完成首例脉冲消融术，精准剿灭复杂‘房扑’', published 6 July 2026 (source ID 2649902596_2). The hospital-reported case is presented as an institutional experience, not an independently verified outcome or a prediction for other patients. Clinical details in this article are limited to information that could be verified from the source record and external medical references.",
            ]),
        ],
        "cta": "Share the rhythm diagnosis, ECG or Holter evidence, prior procedure reports, current medication list, and recent cardiac testing for an initial coordination assessment.",
        "include_standard_help": False,
        "disclaimer": "This article is for general educational information only and is not medical advice, diagnosis, treatment, or a guarantee of access, suitability, cost, timing, or outcome. AetherMed provides medical coordination and does not independently diagnose or prescribe treatment. Final eligibility and treatment decisions are made by the receiving hospital and licensed clinicians after appropriate assessment. Remote review cannot replace an in-person examination or emergency care. Appointments and hospital acceptance depend on clinical review, institutional policy, and capacity; costs and timelines are estimates, not guarantees. If you may have a medical emergency, contact local emergency services immediately. Use of AetherMed's services is subject to its Terms & Conditions and Privacy Policy. This is a hospital-reported institutional case, not an independently verified outcome or a prediction for another patient.",
    },
    {
        "slug": "car-t-therapy-china-international-patients",
        "title": "CAR-T Therapy in China: A First Guide for International Patients",
        "description": "A first guide to CAR-T therapy in China for international patients, covering eligibility, hospital review, treatment steps, risks, timing, and costs.",
        "lede": "CAR-T can offer an important treatment option for selected blood cancers, but it is not a single infusion or a treatment for every patient. International patients need to understand eligibility, hospital access, risks, logistics, and follow-up before planning travel.",
        "primary_category": "medical-in-china",
        "categories": ["medical-in-china", "specialty-treatment", "medical-journey-guides"],
        "tags": ["CAR-T Therapy", "Cancer Care", "International Patients", "Treatment Planning", "Clinical Trials"],
        "image": "01-car-t-therapy-china-first-guide.webp",
        "image_alt": "International patient discussing a CAR-T pathway with a haematologist and medical coordinator in China.",
        "published": "2026-09-01",
        "updated": "2026-09-01",
        "featured": True,
        "sections": [
            ("What CAR-T therapy is", [
                "CAR-T is a personalised form of immunotherapy. T cells are collected from a patient, genetically modified to recognise a target on cancer cells, expanded in a controlled facility, and returned by infusion. Most established CAR-T products are used for selected blood cancers rather than for every cancer type. The target, product, treatment line, prior therapies, organ function, infection status, and current disease burden all affect eligibility.",
                "For a more detailed explanation, read What Is CAR-T Therapy and How Does It Work? The US National Cancer Institute also explains the manufacturing process and major risks.",
            ]),
            ("Why international patients explore CAR-T in China", [
                "China has NMPA-approved autologous CAR-T products as well as hospital-based research programmes. For example, the NMPA conditionally approved ciltacabtagene autoleucel for a defined group of adults with relapsed or refractory multiple myeloma in 2025. An approval for one product and indication does not mean that every hospital offers it or that a patient qualifies.",
                "International patients may also explore China because several major hospitals have haematology, cellular-therapy, intensive-care, neurology, infectious-disease, transfusion, and laboratory teams involved in the pathway. Product availability, clinical trials, costs, appointment timing, and international access must be checked for each case.",
            ]),
            ("Which patients may be considered", [
                "The diagnosis and molecular or antigen profile match a specific approved product or research protocol.",
                "The cancer is relapsed or refractory and the required prior treatments have been completed, where applicable.",
                "The patient has adequate performance status and organ function for collection, conditioning, infusion, and monitoring.",
                "Active infection and other immediate risks have been assessed and managed.",
                "The treating team believes the expected benefit-risk balance is reasonable compared with other available options.",
            ], "Eligibility cannot be established from a diagnosis name alone. Pathology, flow cytometry or molecular results, treatment dates and responses, complications, recent imaging, blood counts, organ-function tests, and current medications may all be needed."),
            ("What the treatment pathway may involve", [
                "Initial inquiry and Free Assessment: organise the diagnosis, treatment history, current status, and main clinical question.",
                "Medical review and hospital matching: identify relevant haematology and cellular-therapy teams and confirm what records they require.",
                "Appointment and travel planning: coordinate remote review where available, expected timing, visa documentation, accommodation, and a caregiver plan.",
                "Arrival and hospital assessment: repeat examinations may be required before final acceptance or cell collection.",
                "Treatment and monitoring: the pathway may include leukapheresis, manufacturing, bridging treatment, lymphodepletion, infusion, and close inpatient or outpatient observation.",
                "Discharge and follow-up: patients need clear emergency instructions, medication plans, scheduled reviews, and records for their home doctor.",
            ], "The exact sequence and setting depend on the product, hospital, clinical status, and treatment plan."),
            ("Risks, timing and cost", [
                "CAR-T can cause severe or life-threatening complications, including cytokine release syndrome, neurological toxicity, infections, prolonged low blood counts, and other product-specific risks. Long-term follow-up is important. Manufacturing time, admission length, caregiver requirements, and total cost vary with the product, hospital, complications, additional treatment, and travel. Early estimates are not guarantees.",
            ]),
            ("What AetherMed can help with", [
                "For patients considering medical tourism in China, AetherMed can help organise and translate medical records, identify possible hospital and specialist routes, clarify whether a proposed option is an approved treatment or clinical study, and coordinate preliminary review, appointments, travel documentation, interpretation, admission logistics, and follow-up materials where available. AetherMed cannot determine CAR-T eligibility or guarantee hospital acceptance, product availability, trial enrolment, cost, timing, or outcome.",
            ]),
        ],
        "cta": "Submit the pathology report, treatment history, latest imaging, laboratory results, current disease assessment, and any previous transplant or cellular-therapy records for an initial coordination review.",
        "include_standard_help": False,
        "disclaimer": "This article is for general educational information only and is not medical advice, diagnosis, treatment, or a guarantee of access, suitability, cost, timing, or outcome. AetherMed provides medical coordination and does not independently diagnose or prescribe treatment. Final eligibility and treatment decisions are made by the receiving hospital and licensed clinicians after appropriate assessment. Remote review cannot replace an in-person examination or emergency care. Appointments and hospital acceptance depend on clinical review, institutional policy, and capacity; costs and timelines are estimates, not guarantees. If you may have a medical emergency, contact local emergency services immediately. Use of AetherMed's services is subject to its Terms & Conditions and Privacy Policy.",
    },
    {
        "slug": "ruijin-hospital-car-t-lymphoma-cases",
        "title": "What Two Hospital-Reported CAR-T Cases at Ruijin Hospital Show About Multidisciplinary Care",
        "description": "Review two hospital-reported CAR-T cases at Ruijin Hospital and what they show about assessment, multidisciplinary care, risks, and follow-up.",
        "lede": "Two anonymised lymphoma cases reported by Ruijin Hospital illustrate how assessment, treatment sequencing, toxicity planning, and follow-up fit around a CAR-T infusion.",
        "primary_category": "success-stories",
        "categories": ["success-stories", "hospitals-doctors", "specialty-treatment"],
        "tags": ["Ruijin Hospital", "CAR-T Therapy", "Lymphoma", "Multidisciplinary Care", "Hospital-Reported Cases"],
        "image": "02-ruijin-hospital-car-t-cases.webp",
        "image_alt": "Multidisciplinary cellular-therapy team reviewing an anonymised CAR-T case.",
        "published": "2026-08-30",
        "updated": "2026-08-30",
        "featured": True,
        "sections": [
            ("Why the care pathway matters as much as the infusion", [
                "CAR-T is not a single appointment. It requires diagnosis confirmation, eligibility assessment, treatment sequencing, cell collection and manufacturing, conditioning therapy, infusion, monitoring for serious toxicities, and longer-term follow-up. The two cases reported by Ruijin Hospital show why multidisciplinary planning and clear response timepoints matter when discussing a hospital-reported success story.",
                "For a plain-language introduction to the treatment itself, read What Is CAR-T Therapy and How Does It Work?",
            ]),
            ("Case 1: high-risk DLBCL with central nervous system involvement", [
                "The hospital described Ms Z, aged 69, who was diagnosed in 2022 with diffuse large B-cell lymphoma (DLBCL) involving the central nervous system and bone marrow. The report also noted stage IV disease, a high International Prognostic Index score, and double expression. After the response to first-line treatment was considered inadequate, the team used a second-line regimen. The hospital reported complete remission after four cycles.",
                "Because the team remained concerned about the risk of recurrence, the International Medical Department arranged remote domestic and international expert discussion through its 'Double I' consultation model. CAR-T was subsequently selected. The reported pathway included cell collection and processing, lymphodepleting conditioning, infusion, and inpatient monitoring by haematology, intensive care, neurology, nutrition, and transfusion specialists.",
                "After infusion, Ms Z reportedly developed high fever, reduced oxygen saturation, cytokine release syndrome (CRS), and neurological symptoms including disorientation and tongue tremor. The hospital stated that these complications were treated according to its planned response pathway. She was discharged after nearly one month. The article reported complete remission at the one-month assessment and that she was doing well at nearly six months. These were time-limited observations, not proof of cure.",
            ]),
            ("Case 2: relapsed double-hit DLBCL", [
                "The second patient, Ms C, was 70 and had been diagnosed with high-risk, double-hit DLBCL in 2021. According to the hospital, first-line treatment was complicated by bone-marrow suppression and a lung infection. After the infection was managed, she received a second-line regimen and was reported to be in complete remission after eight cycles in December 2021.",
                "A new lesion was identified in late 2023 and biopsy confirmed relapse. The treating team considered her age and ability to tolerate further intensive chemotherapy before proceeding with CAR-T in January 2024. The report described mild CRS and neurological toxicity that resolved after treatment. At approximately day 100, the hospital reported a complete response on PET-CT and good quality of life. Again, this is one hospital-reported assessment at a defined follow-up point.",
            ]),
            ("What these cases illustrate", [
                "Response to earlier treatment and current disease status influence when CAR-T is considered.",
                "Older age alone does not determine eligibility; organ function, infection status, performance status, disease biology, and prior treatment also require review.",
                "CRS and neurological toxicity can occur even when a reported outcome is favourable, so monitoring and rapid multidisciplinary response are central to the treatment pathway.",
                "Complete remission at one month, day 100, or six months is not the same as a guaranteed long-term remission or cure.",
            ], "The US National Cancer Institute also identifies CRS, neurological effects, infections, and other complications as important CAR-T risks. Product indications, protocols, and monitoring requirements vary by country and hospital."),
            ("What AetherMed can help with", [
                "For international patients exploring CAR-T in China, AetherMed can help organise pathology, imaging, treatment history, current disease assessments, and complication records for an initial hospital review. We can identify possible haematology or cellular-therapy routes, clarify additional tests requested by the hospital, and coordinate consultations, appointments, travel documents, interpretation, admission logistics, and follow-up materials where available.",
                "Ruijin Hospital's official overview describes it as a Grade-A tertiary comprehensive teaching hospital. Current international-patient access, CAR-T products, eligibility, schedules, costs, and hospital acceptance must be confirmed for each case.",
            ]),
            ("Source and republication note", [
                "Adapted into English from the Ruijin Hospital International Medical Department WeChat article 'Ruijin Hospital International Medical Department Successfully Performs CAR-T Cell Therapy', published 28 April 2024. Patient names remain anonymised. Details above reflect the hospital's report and should not be interpreted as independently verified outcomes or predictions for other patients.",
            ]),
        ],
        "cta": "If you are exploring CAR-T in China, submit the pathology, treatment history, latest imaging, laboratory results, and current disease assessment for an initial coordination review.",
        "include_standard_help": False,
        "disclaimer": "This article is for general educational information only and is not medical advice, diagnosis, treatment, or a guarantee of access, suitability, cost, timing, or outcome. AetherMed provides medical coordination and does not independently diagnose or prescribe treatment. Final eligibility and treatment decisions are made by the receiving hospital and licensed clinicians after appropriate assessment. Remote review cannot replace an in-person examination or emergency care. Appointments and hospital acceptance depend on clinical review, institutional policy, and capacity; costs and timelines are estimates, not guarantees. If you may have a medical emergency, contact local emergency services immediately. Use of AetherMed's services is subject to its Terms & Conditions and Privacy Policy. The patient accounts above are anonymised, historical, hospital-reported cases. Individual experiences and outcomes vary, and no case represents or guarantees another patient's eligibility, treatment course, response, remission, safety, or survival.",
    },
    {
        "slug": "what-is-grade-a-tertiary-hospital-china",
        "title": "What Is a Grade-A Tertiary Hospital in China?",
        "description": "Understand what Grade-A tertiary hospital means in China, what the rating shows, and how international patients can choose the right hospital route.",
        "lede": "For international patients, a hospital's 3A status can be useful context - but it is not a shortcut to choosing the right department, doctor, or access route.",
        "primary_category": "medical-in-china",
        "categories": ["medical-in-china"],
        "tags": ["Public Hospitals", "Hospital Selection", "International Patients", "Specialist Care", "China Healthcare System"],
        "image": "01-grade-a-tertiary-hospital-china.webp",
        "image_alt": "International patient reviewing hospital options with a medical coordinator in a large Chinese hospital.",
        "published": "2026-08-24",
        "updated": "2026-08-24",
        "featured": True,
        "sections": [
            ("What the term actually means", [
                "China's hospital classification uses two related ideas. The level describes a hospital's role and service capacity within the health system. A tertiary hospital generally manages complex or serious conditions, provides specialist services, supports teaching or research, and receives referrals from other facilities. The grade reflects the result of an official hospital assessment. 'Grade A tertiary', often shortened to '3A' or written san jia in Chinese, therefore combines a tertiary level with a Grade A assessment.",
                "The current national framework is set by China's National Health Commission's tertiary-hospital assessment standard. It looks beyond building size or reputation and includes requirements relating to lawful operation, medical quality and safety, service, management, performance, and continuous improvement.",
            ]),
            ("What a Grade-A tertiary rating can tell you", [
                "The hospital has been assessed as a high-level institution within China's formal hospital system.",
                "It is likely to have broad diagnostic, inpatient, surgical, critical-care, and specialist resources, although the exact mix varies.",
                "It may be better equipped to coordinate several departments when a case is complex or involves multiple conditions.",
                "It is usually an important referral centre for its city or region and may also support teaching and clinical research.",
            ], "These are general characteristics. The exact departments, capabilities, and international-patient arrangements still need to be checked hospital by hospital."),
            ("What the rating does not tell you", [
                "A 3A label is not a universal ranking and does not prove that one hospital is the best choice for a particular diagnosis. Two Grade-A tertiary hospitals can have very different strengths. One may have a nationally recognised haematology service, while another is more relevant for liver surgery, neurology, rehabilitation, or a specific paediatric condition.",
                "The rating also does not confirm that a named doctor is available, that an international patient will be accepted, that an international department treats the relevant condition, or that a particular procedure or clinical trial is currently open. Those questions require a case-specific review.",
            ]),
            ("What international patients should check", [
                "Clinical fit: the department and specialist team should match the diagnosis and the question you want answered.",
                "Access route: confirm whether the case should go through the regular public system, an international medical department, or another pathway.",
                "Records: ask which imaging, pathology, laboratory results, treatment summaries, and translations are required before review.",
                "Practical support: verify language assistance, appointment timing, payment arrangements, estimated length of stay, and follow-up planning.",
                "Current availability: specialist schedules, beds, procedures, technologies, and research programmes can change.",
            ], "For a broader explanation of access routes, read How Foreigners Can Access Hospitals in China."),
            ("How AetherMed can help with hospital selection", [
                "AetherMed can review the patient's diagnosis, treatment history, current medical question, language needs, timing, and budget range before identifying possible hospital and specialist routes. We can help organise and translate records, submit them for preliminary review where available, clarify missing information, and coordinate appointments and travel steps after a hospital responds.",
                "Our approach is explained in How AetherMed Matches International Patients with Hospitals and Specialists in China. The final diagnosis, eligibility decision, and treatment plan always remain with the receiving hospital and licensed clinicians.",
            ]),
        ],
        "cta": "Send a concise case summary and recent records. AetherMed can assess the coordination needs and outline possible hospital routes in China.",
        "include_standard_help": False,
    },
    {
        "slug": "in-vivo-car-t-myeloma-wuhan-union-hospital",
        "title": "In Vivo CAR-T for Myeloma: What a Wuhan Union Hospital Report Really Means",
        "description": "Understand Wuhan Union Hospital's early in vivo CAR-T report for myeloma, the later Phase 1 context, limitations, risks, and patient questions.",
        "lede": "A Wuhan Union Hospital report drew attention to an experimental way of generating CAR-T cells inside the body. The research is scientifically important, but the small early cohort and later trial status require careful interpretation.",
        "primary_category": "specialty-treatment",
        "categories": ["specialty-treatment", "hospitals-doctors", "news"],
        "tags": ["Wuhan Union Hospital", "CAR-T Therapy", "Multiple Myeloma", "Clinical Research", "Haematology"],
        "image": "02-in-vivo-car-t-myeloma-wuhan-union.webp",
        "image_alt": "Cellular-therapy research team reviewing in vivo CAR-T laboratory data.",
        "published": "2026-08-23",
        "updated": "2026-08-23",
        "featured": True,
        "sections": [
            ("What conventional CAR-T usually involves", [
                "Most established CAR-T pathways begin by collecting a patient's T cells. A laboratory then engineers and expands those cells before they are returned by infusion. The process can take several weeks and usually includes lymphodepleting chemotherapy before infusion. The US National Cancer Institute describes this ex vivo manufacturing pathway and notes that serious complications can include cytokine release syndrome, neurological effects, and infection.",
                "Read AetherMed's plain-language guide, What Is CAR-T Therapy and How Does It Work?",
            ]),
            ("What 'in vivo' CAR-T changes", [
                "In vivo CAR-T aims to deliver genetic instructions directly inside the body so that some of the patient's own T cells become CAR-T cells without being removed and manufactured in a separate laboratory. If this approach eventually proves safe, effective, and reproducible, it could simplify production and shorten parts of the pathway. Those potential advantages remain research questions; they are not established benefits for routine patients.",
            ]),
            ("What Wuhan Union Hospital reported", [
                "In July 2025, Wuhan Union Hospital reported early clinical work using an investigational anti-BCMA in vivo CAR-T approach for relapsed or refractory multiple myeloma. The related Lancet communication described research led by the hospital's Institute of Hematology with industry collaborators. The hospital article reported results in four patients and stated that the approach avoided leukapheresis and lymphodepleting chemotherapy.",
                "The hospital reported an objective response in all four participants and stringent complete responses in two. It also stated that no grade 4 or higher toxicities were observed apart from haematologic toxicity. These figures came from a very small, early cohort reported by the institution. They cannot establish comparative effectiveness, long-term durability, or safety for a wider patient population.",
                "The early communication is indexed in PubMed, and the hospital's own research news report identifies trial NCT06691685.",
            ]),
            ("What the later Phase 1 publication adds", [
                "A later Phase 1 publication provides a more cautious context. It describes a single-arm, open-label study of five heavily pretreated male participants who received one dose of the investigational vector, with a median follow-up of six months. The primary objective was safety and tolerability; efficacy measures were preliminary. The publication states that the trial stopped early in 2025 and no further participants were enrolled.",
                "That matters for international patients: a scientific publication can be important without creating a currently available treatment route. Trial status, regulatory oversight, hospital eligibility, manufacturing controls, monitoring capacity, and longer follow-up all need independent confirmation. In vivo CAR-T should not be treated as interchangeable with approved or hospital-established ex vivo CAR-T products.",
                "See the later Phase 1 PubMed record and the ClinicalTrials.gov record for study-level information.",
            ]),
            ("Questions patients should ask", [
                "Is the proposed therapy an approved product, hospital programme, investigator-initiated study, or registered clinical trial?",
                "What is the target antigen, and does the patient's current disease meet the protocol criteria?",
                "How many participants have been treated, for how long, and which adverse events were observed?",
                "What monitoring, intensive-care support, infection prevention, and long-term follow-up are required?",
                "Is enrolment currently open, and can international patients legally and practically be considered?",
            ], "Current trial status and international-patient eligibility must be confirmed directly with the receiving hospital and study team."),
            ("What AetherMed can help with", [
                "For patients considering medical tourism in China, AetherMed can help organise pathology, treatment history, laboratory results, imaging, and current disease assessments for review by relevant haematology or cellular-therapy teams in China. We can clarify whether a hospital is considering an established treatment route, a research protocol, or neither, and coordinate consultations, interpretation, appointments, travel, and follow-up logistics where available. We cannot determine eligibility or promise access to an investigational therapy.",
            ]),
            ("Source and republication note", [
                "Adapted into English from Wuhan Union Hospital's official report \"登上《柳叶刀》！协和成功完成全球首例体内CAR-T疗法治疗骨髓瘤\", published 4 July 2025, corresponding to WeChat source ID 2650868905_2. The hospital report reflects early institutional findings. This article also incorporates the later Phase 1 publication and does not present the research as routine clinical availability or as a prediction of outcome.",
            ]),
        ],
        "cta": "If you are exploring CAR-T for multiple myeloma in China, submit your diagnosis, prior treatment history, latest response assessment, and recent laboratory results for an initial coordination review.",
        "include_standard_help": False,
    },
    {
        "slug": "public-vs-private-hospitals-china-international-patients",
        "title": "Public vs Private Hospitals in China: Which Route Fits an International Patient?",
        "description": "Compare public, private, and international hospital routes in China, including specialist access, language support, costs, and coordination.",
        "lede": "The best hospital route is not determined by ownership alone. For an international patient, the stronger choice is the one that matches the diagnosis, specialist, access pathway, communication needs, and practical budget.",
        "primary_category": "medical-in-china",
        "categories": ["medical-in-china", "hospitals-doctors"],
        "tags": ["Public Hospitals", "Private Hospitals", "International Medical Departments", "Hospital Selection", "International Patients"],
        "image": "01-public-vs-private-hospitals-china.webp",
        "image_alt": "International patient comparing public and private hospital routes with a medical coordinator in China.",
        "published": "2026-08-17",
        "updated": "2026-08-17",
        "featured": True,
        "sections": [
            ("There is more than one hospital route", [
                "International patients often frame the decision as public hospital versus private hospital. In practice, there are three common routes: a standard department in a public hospital, an international or VIP department inside a public hospital, and a private or international hospital. The right route depends on the condition, specialist fit, urgency, language needs, budget, insurance, and the level of coordination required.",
                "Beijing's official medical guide notes that both public and non-public institutions provide English-language services, while some public hospitals operate dedicated international medical departments. Availability still differs by hospital and department.",
            ]),
            ("Public hospitals: strongest when specialist depth matters", [
                "China's large public tertiary hospitals are often the first place to explore for a complex diagnosis, advanced surgery, multidisciplinary review, rare disease, or access to a highly specialised team. Major academic hospitals may combine broad departments with research and referral experience. However, the hospital's overall reputation does not automatically identify the best doctor or confirm that an international patient will be accepted.",
            ]),
            ("Public hospitals at a glance", [
                "Potential advantages: broad specialist coverage, multidisciplinary resources, high-volume clinical teams, and access to complex inpatient care.",
                "Possible limitations: busier systems, less English support in standard departments, unfamiliar digital registration, limited appointment slots, and payment or deposit requirements.",
            ], "Best for: patients whose priority is a particular department, specialist, procedure, or complex-care pathway rather than hotel-style service."),
            ("Private hospitals: strongest when convenience and continuity lead", [
                "Private hospitals and international clinics often provide bilingual booking, longer consultations, more familiar service processes, commercial-insurance support, and easier coordination between outpatient visits. This can be valuable for routine care, diagnostics, rehabilitation, maternity, paediatrics, or ongoing follow-up. The trade-off is that fees are usually higher, and a private facility may not have the same depth in every complex specialty.",
            ]),
            ("Private hospitals at a glance", [
                "Potential advantages: multilingual communication, simpler scheduling, service continuity, clearer patient support, and sometimes broader commercial-insurance arrangements.",
                "Possible limitations: higher fees, variable emergency capability, and the need to confirm whether the required specialist, intensive care, procedure, or technology is available on site.",
            ], "Best for: patients prioritising accessibility, language support, coordinated routine care, or a more familiar international service environment."),
            ("The middle route: an international department in a public hospital", [
                "An international medical department can combine access to a major public hospital's specialists with more coordinated registration, language assistance, private rooms, or commercial-insurance processes. It may be a strong option for overseas patients, but it is not simply a faster doorway to every doctor or treatment. Services, fees, eligible departments, bed capacity, and appointment rules must be checked case by case.",
                "Shanghai's official guide offers a practical public-versus-private overview and shows how hours, insurance, fees, and emergency arrangements can differ across facilities.",
            ]),
            ("A practical decision checklist", [
                "Clinical fit: Which department and named team regularly manage this diagnosis?",
                "Access: Is the patient eligible for the standard, VIP, international, or private route?",
                "Timing: Is a remote record review possible before travel, and how soon could an appointment occur?",
                "Communication: Are interpretation and English-language consent materials available?",
                "Cost and insurance: What requires a deposit, what is estimated, and what may be reimbursed?",
                "Continuity: Who will coordinate tests, admission, discharge records, and follow-up after returning home?",
            ], "Use these questions to compare actual hospital pathways rather than relying on ownership or reputation alone."),
            ("What AetherMed can help with", [
                "For patients considering medical tourism in China, AetherMed can review the medical question, diagnosis, records, timing, language needs, and budget before comparing possible public, international-department, and private routes. We can help organise and translate records, identify relevant hospitals and specialists, seek preliminary feedback where available, and coordinate appointments and treatment logistics after a hospital responds.",
                "Read how AetherMed matches patients with hospitals and specialists. Final acceptance and medical decisions remain with the receiving hospital and clinicians.",
            ]),
        ],
        "cta": "Share a concise case summary and recent records. We can outline suitable hospital routes and the information needed for an initial review.",
        "include_standard_help": False,
    },
    {
        "slug": "professor-jianfeng-zhou-car-t-legacy-china",
        "title": "Professor Jianfeng Zhou's CAR-T Legacy and the Search for More Accessible Treatment in China",
        "description": "Explore Professor Jianfeng Zhou's CAR-T legacy at Wuhan Tongji Hospital through three hospital-reported patient cases, with context on access, risks, and limitations.",
        "lede": "His work at Wuhan Tongji Hospital helped connect laboratory research, clinical care, and the practical question of how more patients might reach cellular therapy.",
        "primary_category": "hospitals-doctors",
        "categories": ["hospitals-doctors", "specialty-treatment", "success-stories"],
        "tags": ["Professor Jianfeng Zhou", "Tongji Hospital Wuhan", "CAR-T Therapy", "Haematology", "Clinical Research", "International Patient Stories", "Hospital-Reported Cases"],
        "image": "02-professor-jianfeng-zhou-car-t-legacy.webp",
        "image_alt": "A multidisciplinary cellular-therapy team reviewing CAR-T laboratory data.",
        "published": "2026-08-13",
        "updated": "2026-08-13",
        "featured": True,
        "sections": [
            ("Professor Jianfeng Zhou and Wuhan Tongji Hospital", [
                "Professor Jianfeng Zhou (1966-2022) was a haematologist at Tongji Hospital, Tongji Medical College, Huazhong University of Science and Technology in Wuhan. He served as director of the hospital's Department of Haematology and led work in blood cancers and cellular immunotherapy. This article is retrospective: Professor Zhou died in March 2022 and cannot be contacted or booked for consultation.",
            ]),
            ("From laboratory work to clinical questions", [
                "CAR-T therapy modifies immune cells so they can recognise a target on cancer cells. Professor Zhou's team worked with researchers and clinicians to develop and study CAR-T approaches for relapsed or refractory blood cancers. The programme included regular discussion between laboratory scientists and clinical teams, allowing observations from treated patients to inform later research questions.",
                "A report from the Hubei Provincial Health Commission described this clinical-research collaboration. Peer-reviewed work involving Professor Zhou also examined CD19/CD22 CAR-T combination therapy for selected patients with relapsed or refractory double-hit lymphoma.",
            ]),
            ("What 'more accessible' meant in this work", [
                "Accessibility is not only the price of the cell product. It also involves manufacturing, hospital capability, patient selection, management of serious side effects, and the time needed to move from assessment to infusion. Professor Zhou's work drew attention to domestic development and hospital-based research as possible ways to expand treatment options.",
                "In a historical hospital report, Tongji Hospital described its first use of a marketed domestic CAR-T product and quoted RMB 1.2 million for that product at the time. The report said this was around 40% of the price abroad. Those figures are historical, case-specific, and not a current quotation.",
            ]),
            ("Three hospital-reported cases from the team's work", [
                "The following accounts were published by Tongji Hospital at different points in the team's CAR-T work. They show the range of cases reviewed by the programme, but they are not clinical-trial summaries and cannot predict how another patient will respond.",
            ]),
            ("Maggie: acute lymphoblastic leukaemia after transplant failure", [
                "Tongji Hospital reported that Maggie, a 21-year-old patient living in Dubai, travelled to Wuhan after chemotherapy and a previous stem-cell transplant had failed. She received two stages of CAR-T treatment in 2016 and required intensive monitoring during a serious inflammatory reaction. The hospital's 2019 follow-up said that testing continued to show no detectable leukaemia cells more than three years later. This was a historical individual outcome, not a guarantee of long-term remission for other patients.",
            ]),
            ("Mr Chen: an international multiple myeloma case", [
                "A 2018 hospital report described a 58-year-old patient from Switzerland whose multiple myeloma had progressed after a stem-cell transplant, chemotherapy, and several targeted treatments. After CAR-T treatment in Wuhan, the hospital reported at roughly two months that visible masses had resolved and disease measurements were below the test's detection limit. The report did not establish how a different patient, product, or later treatment setting would perform.",
            ]),
            ("'Daxiong': double-hit diffuse large B-cell lymphoma", [
                "In 2021, Tongji Hospital reported on a 31-year-old patient with relapsed or refractory double-hit diffuse large B-cell lymphoma who had developed infection and viral myocarditis during chemotherapy. He later received a newly marketed domestic CAR-T product. At the follow-up described in the hospital report, PET-CT showed complete remission, and the hospital said that cytokine release syndrome and neurological toxicity had not been observed in his treatment course. That experience should not be read as evidence that these complications are uncommon.",
            ]),
            ("Research does not equal routine availability", [
                "A published study or hospital-reported case does not show that the same treatment is open to every patient. Current access depends on the exact cancer type and target, previous treatment, organ function, infection status, approved indications, trial criteria, hospital capacity, and whether international patients can be enrolled. The treating team must also explain cytokine release syndrome, neurological toxicity, infections, prolonged low blood counts, and other risks.",
                "Later publications continue to acknowledge Professor Zhou's contribution to CAR-T research, including a long-term study of a fully human CAR-T therapy for multiple myeloma. This does not establish individual eligibility or present-day availability.",
            ]),
            ("What international patients should verify", [
                "Which current hospital team will review the case and who is responsible for treatment.",
                "Whether the option is an approved commercial treatment, an investigator-initiated study, or a registered clinical trial.",
                "The exact diagnosis, target, inclusion and exclusion criteria, and required previous treatments.",
                "An itemised estimate covering the cell product, testing, hospital stay, side-effect management, and follow-up.",
                "How long the patient and caregiver must remain near the hospital and what emergency plan applies.",
            ], "Current availability and requirements must be confirmed directly with the receiving hospital."),
            ("What AetherMed can help with", [
                "AetherMed can help organise records, identify current haematology or cellular-therapy teams in China, request a preliminary hospital review, and coordinate practical next steps. It cannot arrange a consultation with Professor Zhou, determine CAR-T eligibility, guarantee trial enrolment, or promise a price or treatment result.",
            ]),
            ("Source note", [
                "This article was prompted by and adapted from the hospital feature \"群医闪耀 | 周剑峰：研制出国人用得起的 CAR-T\", published by the official WeChat account of Tongji Hospital, Tongji Medical College, Huazhong University of Science and Technology. The English version has been rewritten for international readers and checked against hospital, government, and peer-reviewed sources.",
            ]),
        ],
        "cta": "If you are exploring CAR-T in China, submit the diagnosis, pathology, treatment history, and latest disease assessment for an initial coordination review.",
        "include_standard_help": False,
        "disclaimer": "This article is for general educational information only and is not medical advice, diagnosis, treatment, or a guarantee of access, suitability, cost, timing, or outcome. AetherMed provides medical coordination and does not independently diagnose or prescribe treatment. Final eligibility and treatment decisions are made by the receiving hospital and licensed clinicians after appropriate assessment. Remote review cannot replace an in-person examination or emergency care. Appointments and hospital acceptance depend on clinical review, institutional policy, and capacity; costs and timelines are estimates, not guarantees. If you may have a medical emergency, contact local emergency services immediately. Use of AetherMed's services is subject to its Terms & Conditions and Privacy Policy. CAR-T products, clinical trials, indications, prices, and international-patient access change over time. Historical research and individual cases do not predict another patient's outcome. The patient accounts above are historical, hospital-reported cases. Individual experiences and outcomes vary, and no case represents or guarantees another patient's eligibility, treatment course, response, remission, safety, or survival.",
    },
    {
        "slug": "how-aethermed-matches-patients-hospitals-specialists-china",
        "title": "How AetherMed Matches International Patients with Hospitals and Specialists in China",
        "description": "Learn how AetherMed reviews medical records and patient priorities to match international patients with suitable hospitals and specialists in China.",
        "lede": "The diagnosis is only the starting point. The right match also depends on the clinical question, hospital route, timing, language needs, and whether the team is currently accepting suitable cases.",
        "primary_category": "medical-journey-guides",
        "categories": ["medical-journey-guides", "hospitals-doctors"],
        "tags": ["Hospital Matching", "Doctor Matching", "Medical Records", "Case Management", "International Patients"],
        "image": "01-aethermed-hospital-specialist-matching.webp",
        "image_alt": "International patient reviewing hospital and specialist options with a medical coordinator.",
        "published": "2026-08-11",
        "updated": "2026-08-11",
        "featured": True,
        "sections": [
            ("Why the most famous hospital is not always the right match", [
                "China has large public hospitals, international medical departments, private providers, specialist centres, and research teams. A famous hospital is not automatically the best fit for every patient. AetherMed's matching process starts with the case itself, then narrows the options to hospitals and specialists whose current scope appears relevant.",
            ]),
            ("Matching starts with a clear clinical question", [
                "A diagnosis such as cancer, a neurological disorder, or a complex surgical condition can involve several subspecialties. The useful question is often more specific: Is the patient seeking confirmation of a diagnosis? A surgical opinion? A comparison of treatment paths? Access to a particular technology? Or a review after prior treatment has not worked as expected?",
            ]),
            ("What AetherMed reviews", [
                "The confirmed or suspected diagnosis and the main question the patient wants answered.",
                "Recent imaging, pathology, laboratory results, treatment history, current medicines, and relevant complications.",
                "The patient's age, overall condition, urgency, travel readiness, language needs, and preferred city.",
                "Whether the request is for a second opinion, outpatient assessment, planned procedure, longer treatment, or trial enquiry.",
                "Any practical limits, including timing, budget range, caregiver needs, and follow-up after returning home.",
            ], "Well-organised records make this review more useful. See Preparing Medical Records for Treatment in China."),
            ("How the shortlist is built", [
                "The team compares the case with known hospital departments, specialist interests, international patient routes, and the information required for an initial review. This may produce one clear route or a short list. When two options look reasonable, the comparison should focus on clinical fit and current availability, not a generic ranking.",
                "Foreign patients can use different hospital routes in China. Our guide to accessing hospitals in China explains the main differences. Beijing's official medical guide also shows why international service arrangements must be checked hospital by hospital.",
            ]),
            ("What AetherMed can help with", [
                "AetherMed can organise the case summary, identify possible hospital and specialist routes, submit records for preliminary review, clarify missing information, and coordinate appointment logistics. If the first route is not available, the team can discuss reasonable alternatives. AetherMed does not rank doctors as 'best', make clinical decisions, or guarantee that a hospital will accept a case.",
            ]),
            ("What the patient receives", [
                "The initial output may include a request for additional records, a suggested department or hospital route, questions for the receiving team, and the next coordination step. It is not a diagnosis or final treatment plan. The hospital may request more tests or an in-person examination before confirming whether treatment is suitable.",
            ]),
            ("Where matching fits in the six-step journey", [
                "Hospital and specialist matching is the second stage of AetherMed's six-step journey: initial enquiry and Free Assessment; medical review and hospital matching; appointment and travel planning; arrival and the first hospital visit; treatment and payment coordination; and discharge and follow-up.",
                "Read the full international patient journey in China before making travel arrangements.",
            ]),
        ],
        "cta": "Send a concise case summary and the most recent medical records. AetherMed will review the coordination needs and outline possible hospital or specialist routes in China.",
        "include_standard_help": False,
        "disclaimer": "This article is for general educational information only and is not medical advice, diagnosis, treatment, or a guarantee of access, suitability, cost, timing, or outcome. AetherMed provides medical coordination and does not independently diagnose or prescribe treatment. Final eligibility and treatment decisions are made by the receiving hospital and licensed clinicians after appropriate assessment. Remote review cannot replace an in-person examination or emergency care. Appointments and hospital acceptance depend on clinical review, institutional policy, and capacity; costs and timelines are estimates, not guarantees. If you may have a medical emergency, contact local emergency services immediately. Use of AetherMed's services is subject to its Terms & Conditions and Privacy Policy.",
    },
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
    {
        "slug": "how-aethermed-free-assessment-works",
        "title": "How AetherMed's Free Medical Assessment Works",
        "description": "Learn how AetherMed's free assessment reviews your goals and medical records, identifies missing information, and outlines possible care pathways in China.",
        "lede": "AetherMed's free medical assessment is an initial coordination review for international patients exploring medical treatment in China. It helps organize the key facts of your case, identify missing information, and understand whether there may be a practical hospital or specialist pathway in China.",
        "primary_category": "medical-journey-guides",
        "categories": ["medical-journey-guides", "medical-in-china"],
        "tags": ["Medical Records", "Treatment Planning", "Case Management", "International Patients"],
        "image": "aethermed-free-medical-assessment.webp",
        "image_alt": "International patient reviewing a free medical assessment with an AetherMed coordinator.",
        "published": "2026-07-28",
        "updated": "2026-07-28",
        "featured": True,
        "sections": [
            ("Who is the assessment for?", [
                "The assessment is designed for international patients and families who are considering care in China but do not yet know which hospital, department, or specialist may fit their needs. It may be useful if you want to compare treatment options, seek a second opinion, explore a specialist service, or understand the practical steps before travel.",
                "It is particularly helpful when you can explain your confirmed or suspected diagnosis, current symptoms, previous tests or medical opinions, what you hope to clarify or achieve in China, your preferred timing, language needs, travel constraints, and approximate budget.",
            ]),
            ("What should you submit?", [
                "Start with a short medical summary and the most relevant recent reports. You do not need to send every document you have at the first step; the goal is to help the coordination team understand the case clearly enough to identify what may be missing.",
                "Depending on the condition, useful files may include consultation notes, discharge summaries, pathology reports, laboratory results, imaging reports, and a current medication list. Original CT or MRI image files may be requested later.",
                "Remove unrelated personal information where possible and use AetherMed's secure submission channel. Do not send medical records through public comments or social media.",
            ]),
            ("What happens after you submit your information?", [
                "First, AetherMed checks whether the information is clear enough for an initial review. If essential details are missing, a coordinator may ask focused follow-up questions.",
                "Next, the team considers practical factors such as the relevant specialty, potential hospital route, international-patient access, language support, timing, and travel needs. Where the case appears suitable to explore further, AetherMed can outline possible next steps.",
                "These next steps may include preparing a formal medical-record review, requesting a remote specialist consultation where available, or asking a hospital to assess the case.",
            ]),
            ("What will you receive?", [
                "The response may identify information still needed before a hospital review, one or more potential hospital, department, or specialist pathways to investigate, whether a remote review may be worth requesting before travel, and an indicative sequence of next steps.",
                "The level of detail depends on the records supplied and the complexity of the case. An initial medical assessment in China cannot confirm eligibility, treatment, cost, timing, or outcome. Those decisions remain with the receiving hospital and licensed doctors.",
            ]),
            ("How should you use the result?", [
                "Treat the assessment as a planning tool. Compare the suggested pathway with advice from your current doctor, ask what additional tests may be needed, and consider travel risk, continuity of care, insurance, and follow-up at home.",
                "The assessment is not a diagnosis, a medical second opinion, or a promise that a hospital will accept your case. It is a practical first step for understanding whether China may be worth exploring and what information should be prepared next.",
            ]),
        ],
        "cta": "Share a brief description of your condition, your goals, and the medical records you already have. AetherMed will review the information for coordination purposes and explain the practical next step, where appropriate.",
    },
    {
        "slug": "ruijin-hospital-multidisciplinary-consultations",
        "title": "How a Multidisciplinary Team at Ruijin Hospital Helped Uncover a Hidden Condition",
        "description": "See how an MDT at Ruijin Hospital helped identify a hidden condition in Ms. X, and learn what international patients should know before a review.",
        "lede": "A multidisciplinary team, or MDT, brings doctors from relevant specialties together to review one case. This can be useful when symptoms are unclear, test results involve more than one organ system, or several treatment routes need to be considered.",
        "primary_category": "hospitals-doctors",
        "categories": ["hospitals-doctors", "success-stories"],
        "tags": ["Ruijin Hospital", "MDT Review", "International Patient Departments", "Patient Story", "Shanghai"],
        "image": "ruijin-hospital-mdt-international-patients.webp",
        "image_alt": "International patient attending a multidisciplinary consultation with doctors in Shanghai.",
        "published": "2026-07-30",
        "updated": "2026-07-30",
        "featured": True,
        "sections": [
            ("Ms. X's case: a warning sign found during testing", [
                "A case published by Ruijin Hospital's International Medical Department describes a patient referred to as Ms. X. She was 63 and living with type 2 diabetes. She sought medical help after losing weight, but had no other obvious discomfort when she was admitted.",
                "A routine urine test found an increased white blood cell count. A non-contrast abdominal CT then showed swelling and inflammatory changes around the left kidney.",
                "The International Medical Department organized a review involving radiology, interventional medicine, infectious diseases, nephrology, urology, and endocrinology. According to the hospital's account, the team diagnosed type 2 diabetes complicated by previously hidden multiple abscesses in both kidneys and developed an individual treatment plan.",
                "The original article describes Ms. X as recovering after the MDT-led care plan. It does not provide enough clinical detail to assess the treatment itself, the length of recovery, or which parts of the plan were decisive. Her experience should therefore be read as an example of coordinated case review, not evidence that another patient will receive the same diagnosis, treatment, or result.",
            ]),
            ("Why an MDT mattered in this case", [
                "Ms. X did not arrive with a clear set of symptoms pointing to kidney abscesses. The concern emerged through urine testing and CT imaging. Diabetes also affected the clinical context.",
                "Bringing the relevant specialties together allowed the findings to be considered from diagnostic, infection, kidney, urological, endocrine, imaging, and possible interventional perspectives.",
                "The team needed for any individual patient will depend on the condition and the hospital's assessment. Some cases need a single specialist first; others may benefit from coordinated discussion across several departments.",
            ]),
            ("When might an international patient ask about an MDT?", [
                "An MDT review may be worth exploring when the diagnosis remains uncertain after previous consultations, several specialties are likely to influence the treatment decision, test results need to be reviewed together rather than one at a time, or a complex or recurrent condition requires a coordinated second opinion.",
                "Not every case needs an MDT. The hospital may recommend one specialist, further tests, or an in-person examination first. Availability, participating departments, fees, timing, and the form of any written opinion should be confirmed before travel.",
            ]),
            ("Preparing records for review", [
                "International patients should provide a concise medical summary, recent clinic or discharge notes, laboratory results, imaging reports, and original imaging files when requested.",
                "A clear question helps the hospital decide which specialties may need to participate. For example, the patient may ask whether a diagnosis is complete, whether different departments should review the case together, or whether a proposed treatment plan needs another specialist perspective.",
            ]),
            ("Source note", [
                "This article is adapted and translated from a Chinese-language article originally published by Shanghai Jiao Tong University School of Medicine Affiliated Ruijin Hospital on the official WeChat account of Ruijin Hospital International Medical Department. The English version has been edited for international readers.",
                "Details of Ruijin Hospital's International Medical Department and MDT services should be reconfirmed with the hospital before publication and before any patient makes arrangements. Individual experiences and outcomes vary.",
            ]),
        ],
        "cta": "If you are considering a multidisciplinary consultation in China, share your diagnosis, recent records, and the specific decision you want reviewed. AetherMed can help clarify the practical route and information requirements.",
    },
    {
        "slug": "how-foreigners-access-hospitals-china",
        "title": "How Foreigners Can Access Hospitals in China",
        "description": "Learn how foreigners can access hospitals in China, compare public and international patient routes, prepare records, and plan appointments or admission.",
        "lede": "Foreign patients can use medical services in China, but the best route depends on the hospital, specialty, language needs, urgency, and whether the visit is for an outpatient opinion, testing, or planned treatment. Starting with the right department can prevent avoidable delays.",
        "primary_category": "medical-in-china",
        "categories": ["medical-in-china", "hospitals-doctors"],
        "tags": ["International Patients", "Public Hospitals", "International Patient Departments", "Hospital Admission", "China"],
        "image": "how-foreigners-access-hospitals-china.webp",
        "image_alt": "International patient speaking with a coordinator at a hospital in China.",
        "published": "2026-08-04",
        "updated": "2026-08-04",
        "featured": True,
        "sections": [
            ("Choose the right hospital access route", [
                "Large public hospitals often provide broad specialist resources. Some have an international medical department or a designated international patient service, while others use the standard outpatient system.",
                "Private and international hospitals may offer easier English-language access, but their specialty coverage and fees vary. The best route depends on the condition, specialty, language needs, timing, and whether the patient needs an opinion, testing, admission, or planned treatment.",
                "AetherMed can help international patients organize records, identify suitable hospital and specialist options, submit enquiries, coordinate appointment logistics, and connect the consultation with later testing or treatment planning. Hospital acceptance and clinical decisions remain with the receiving institution.",
            ]),
            ("1. Define what you need", [
                "Be specific about the purpose of the hospital visit: a second opinion, a specialist assessment, diagnostic testing, surgery planning, ongoing treatment, or admission for a defined procedure.",
                "The diagnosis alone may not identify the correct hospital. The relevant subspecialty, procedure, current clinical question, and urgency often matter more than the general hospital name.",
            ]),
            ("2. Prepare a concise medical file", [
                "Include a short case summary, diagnoses, recent reports, imaging, pathology, medication list, allergies, previous treatment, and your main questions.",
                "Clear records help a hospital decide which department should review the case and whether additional information is needed before an appointment can be confirmed.",
            ]),
            ("3. Confirm the department and appointment route", [
                "Ask whether the hospital accepts direct international enquiries, requires a coordinator or referral, and can review records before booking.",
                "Confirm the doctor or department, visit type, expected language support, deposit or payment requirements, and what original documents to bring. City guidance may help identify hospitals with international services, but current arrangements should always be confirmed directly with the hospital.",
            ]),
            ("4. Plan for travel, testing, and admission", [
                "An outpatient consultation does not automatically mean admission or treatment. Additional tests may be requested, and a treatment plan may change after an in-person examination.",
                "Keep travel plans flexible until the hospital confirms the next step. Patients should also think through interpretation, payment, accommodation, caregiver support, discharge documents, and follow-up with their home doctor.",
            ]),
            ("Questions to clarify before travelling", [
                "Has the hospital reviewed enough information to select the correct department? Is the appointment confirmed, and what identification or registration documents are required?",
                "Will interpretation be available for the consultation and consent process? What deposits, estimated fees, and payment methods apply?",
                "If treatment is recommended, how will admission, follow-up, and travel changes be handled?",
            ]),
        ],
        "cta": "Share your diagnosis, goals, and available medical records. We will review the coordination needs and outline possible next steps in China.",
    },
    {
        "slug": "what-is-car-t-therapy",
        "title": "What Is CAR-T Therapy and How Does It Work?",
        "description": "Understand how CAR-T therapy works, who may be considered, the treatment process, important risks, and questions international patients should ask.",
        "lede": "CAR-T therapy is a form of immunotherapy that modifies a patient's own T cells so they can recognize a specific target on cancer cells. It has become an option for some people with certain blood cancers, usually after specialist assessment and often after other treatments. It is not suitable for every cancer or every patient.",
        "primary_category": "specialty-treatment",
        "categories": ["specialty-treatment", "medical-in-china"],
        "tags": ["CAR-T Therapy", "Oncology", "Haematology", "Treatment Planning", "International Patients"],
        "image": "what-is-car-t-therapy.webp",
        "image_alt": "Patient discussing CAR-T therapy with a haematology-oncology specialist.",
        "published": "2026-08-06",
        "updated": "2026-08-06",
        "featured": True,
        "sections": [
            ("How CAR-T therapy works", [
                "CAR-T therapy is a personalized cell therapy. T cells are collected from the patient's blood, changed in a laboratory so they can produce a chimeric antigen receptor, expanded, tested, and then returned to the patient by infusion.",
                "Many patients receive short-course lymphodepleting chemotherapy before infusion. This preparation is intended to create space for the CAR-T cells. After infusion, close monitoring is needed for early side effects and a longer follow-up plan.",
                "The US National Cancer Institute describes CAR-T as a complex process in which T cells are collected, engineered, expanded, and returned to the patient. The details can vary by product, trial protocol, hospital, and diagnosis.",
            ]),
            ("Who might be considered?", [
                "Eligibility depends on the exact diagnosis and cancer-cell target, previous treatments, disease status, infections, organ function, overall health, and the approved or research options available at the treating center.",
                "CAR-T is established for selected blood cancers. Use in most solid tumors remains investigational, and patients should ask whether a proposed pathway is an approved treatment, a clinical trial, or another form of specialist assessment.",
            ]),
            ("Why do some international patients explore CAR-T in China?", [
                "China has one of the world's largest CAR-T research landscapes. Trials are conducted across multiple hospitals and investigate different targets, specialties, and diseases, including blood cancers and selected solid tumors.",
                "A large trial portfolio does not mean that every study is recruiting, accepts international patients, or is appropriate for an individual case. Hospital review, trial criteria, documentation, timing, and language support all matter.",
                "Cost can also be a reason to compare China with other countries. AetherMed's preliminary market estimates suggest that, in selected and genuinely comparable pathways, quoted costs in China may be around half a US or European pathway. These ratios are not standard prices or guaranteed savings. Patients should compare written, itemized estimates from the treating hospitals rather than headline figures.",
            ]),
            ("What are the main risks?", [
                "CAR-T can cause serious and sometimes life-threatening complications. Cytokine release syndrome may bring fever, low blood pressure, breathing difficulty, or organ problems.",
                "Neurological toxicity may cause confusion, language problems, tremor, seizures, or reduced consciousness. Infection, prolonged low blood counts, and other immune effects are also possible.",
                "Regulators also require ongoing monitoring for secondary T-cell malignancies after treatment. These risks make experienced multidisciplinary care and rapid access to emergency support essential.",
            ]),
            ("What should an international patient prepare?", [
                "Prepare a confirmed pathology diagnosis, the most recent disease assessment, treatment history, response to prior therapy, complications, and current medications.",
                "Useful records may include laboratory results, imaging, pathology or molecular reports, and information about whether relevant tissue samples are available.",
                "Patients should ask about eligibility, product or trial status, manufacturing time, total expected stay, caregiver needs, monitoring, emergency plans, payment, and follow-up after returning home.",
            ]),
        ],
        "cta": "If you are exploring CAR-T or another specialist cancer treatment in China, submit your diagnosis and treatment history for an initial coordination review.",
    },
]


TAG_GROUPS = {
    "Specialty": ["Oncology", "Haematology", "Multiple Myeloma", "Lymphoma", "Cancer Care", "Breast Cancer", "Cardiology", "Atrial Flutter", "Structural Heart Disease", "Mitral Valve", "Specialist Care"],
    "Treatment & Review": ["Second Opinion", "Remote Consultation", "International Consultation", "Medical Records Review", "Medical Records", "Hospital Review", "MDT Review", "Multidisciplinary Care", "CAR-T Therapy", "Treatment Planning", "Clinical Trials", "Pulsed Field Ablation", "Valve-in-Valve"],
    "Patient Journey": ["Before You Travel", "Medical Records", "Treatment Planning", "Translation", "Travel Planning", "Hospital Admission", "Case Management", "Follow-Up", "Returning Home"],
    "Location": ["China", "Shanghai"],
    "Audience & Format": ["International Patients", "Complete Guide", "International Patient Departments", "Public Hospitals", "Private Hospitals", "Hospital Selection", "China Healthcare System", "Clinical Research", "Patient Story", "Hospital-Reported Cases", "Ruijin Hospital", "Wuhan Union Hospital", "China-Japan Friendship Hospital", "West China Hospital", "Guangdong Provincial People's Hospital"],
}


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def slugify(value: str) -> str:
    return value.lower().replace("&", "and").replace("'", "").replace(" ", "-").replace(":", "").replace(",", "")


def article_url(article: dict) -> str:
    return f"/insights/{article['primary_category']}/{article['slug']}/"


def sorted_articles(articles: list[dict]) -> list[dict]:
    return sorted(articles, key=lambda a: (a["updated"], a["published"], a["title"]), reverse=True)


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
{GOOGLE_TAG}    <meta charset="utf-8" />
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
    content = "\n".join(line.rstrip() for line in content.splitlines()) + ("\n" if content.endswith("\n") else "")
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
    featured = sorted_articles([a for a in ARTICLES if a.get("featured")])
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
        for a in sorted_articles(ARTICLES)
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
    articles = sorted_articles([a for a in ARTICLES if slug in a["categories"]])
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
    section_parts = []
    for section in article["sections"]:
        title, paragraphs, *after = section
        if after:
            content = "<ul>\n" + "\n".join(f"<li>{esc(p)}</li>" for p in paragraphs) + "\n</ul>\n<p>" + esc(after[0]) + "</p>"
        else:
            content = "\n".join(f"<p>{esc(p)}</p>" for p in paragraphs)
        section_parts.append(f"<h2>{esc(title)}</h2>\n{content}")
    section_html = "\n".join(section_parts)
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
    standard_help = "<!-- Article-specific service section appears above. -->" if article.get("include_standard_help") is False else """<h2>What AetherMed can help with</h2>
        <p>AetherMed coordinates practical access to medical care in China. Depending on the case, support may include initial information review, medical-record organization and translation, hospital and doctor matching, remote consultation coordination, appointment and travel support, in-China case management and interpretation, and discharge and follow-up documentation. All diagnoses, eligibility decisions and treatment plans are made by the receiving hospital and its licensed medical professionals.</p>"""
    if article.get("disclaimer"):
        disclaimer = esc(article["disclaimer"])
        disclaimer = disclaimer.replace("Terms &amp; Conditions", f'<a href="{root}terms.html">Terms &amp; Conditions</a>')
        disclaimer = disclaimer.replace("Privacy Policy", f'<a href="{root}privacy.html">Privacy Policy</a>')
    else:
        disclaimer = f'This article is provided for general educational and informational purposes only. It does not constitute medical advice, diagnosis, treatment, a medical recommendation, legal advice, insurance advice, or a guarantee that any hospital, doctor, procedure, appointment, visa, treatment outcome, timeline, or cost will be available or suitable for a particular patient. AetherMed provides international medical coordination and related support services; it does not independently diagnose medical conditions, prescribe treatment, or replace consultation with a licensed physician. Remote consultations and preliminary assessments have limitations and cannot replace an in-person clinical examination or emergency medical care. If you are experiencing a medical emergency, contact your local emergency services immediately. Use of AetherMed’s website and services is subject to our <a href="{root}terms.html">Terms & Conditions</a> and <a href="{root}privacy.html">Privacy Policy</a>.'
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
        {standard_help}
        <div class="article-cta"><h2>Request a Free Assessment</h2><p>{esc(article['cta'])}</p><a class="button" href="{root}index.html#contact">Request a Free Assessment</a></div>
        <div class="medical-disclaimer"><strong>Medical and Service Disclaimer</strong><p>{disclaimer}</p></div>
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
        articles = sorted_articles([a for a in ARTICLES if tag in a["tags"]])
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
        for a in sorted_articles(ARTICLES)
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
    article_dates = {article_url(article): article["updated"] for article in ARTICLES}
    for path, priority, freq in urls:
        lastmod = article_dates.get(path, TODAY)
        body.append(f"  <url>\n    <loc>{absolute(path)}</loc>\n    <lastmod>{lastmod}</lastmod>\n    <changefreq>{freq}</changefreq>\n    <priority>{priority}</priority>\n  </url>")
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
