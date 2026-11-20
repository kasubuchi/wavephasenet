# Regulatory landscape for AI emotion recognition / affect inference (status as of 20 Nov 2026)

Method note: research done on 2026-11-20 by web search plus fetches. Many law-firm and Japanese law-firm hosts (gibsondunn.com, skadden.com, tmi.gr.jp, miyake.gr.jp, aigl.blog) could not be reached from this session, so several 2026 developments rest on search-result summaries of those pages, not on full-text reads. Points marked **[KNOWN TEXT]** come from the statute text as published in the Official Journal or the legislature, which the researcher knows well. They link to the primary source but were not re-fetched in this session. Status labels: **ENACTED/IN FORCE**, **ENACTED, NOT YET APPLICABLE**, **PROPOSED/PENDING**, **SOFT LAW**.

---

## 1. EU AI Act (Regulation (EU) 2024/1689): prohibition, high-risk, transparency, timelines, penalties

### Takeaway
Since 2 Feb 2025, the EU has banned emotion inference from biometric data (face, voice, physiological and behavioural signals) in workplaces and educational institutions, with narrow medical and safety exceptions. Penalties for this ban have applied since 2 Aug 2025. Outside those settings, biometric emotion recognition is Annex III high-risk. The 2026 Digital Omnibus deferred high-risk obligations for Annex III systems to **2 Dec 2027**. The Art. 50(3) duty to inform people exposed to emotion recognition applies from **2 Aug 2026**. Emotion inference from non-biometric data, such as text, is outside both the ban and the Art. 3(39) definition.

### Cited Findings
**Definitions [KNOWN TEXT]** — [EUR-Lex, Reg. 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- Art. 3(39): an "emotion recognition system" is "an AI system for the purpose of identifying or inferring emotions or intentions of natural persons on the basis of their biometric data."
- Art. 3(34): "biometric data" is personal data resulting from specific technical processing relating to the physical, physiological or behavioural characteristics of a natural person. The AI Act definition does not require that the data allow or confirm unique identification, unlike the GDPR's Art. 4(14) definition. Commentators read this as pulling physiological and behavioural signals into scope — [William Fry](https://www.williamfry.com/knowledge/the-time-to-ai-act-is-now-a-practical-guide-to-emotion-recognition-systems-under-the-ai-act/); [Bird & Bird](https://www.twobirds.com/en/insights/2024/global/what-is-an-emotion-recognition-system-under-the-eus-artificial-intelligence-act-part-1)
- Recital 18 (known text): emotions include happiness, sadness, anger, surprise, disgust, embarrassment, excitement, shame, contempt, satisfaction and amusement. Physical states such as pain or fatigue are excluded, as is the mere detection of readily apparent expressions, gestures or movements (e.g., a smile) unless they are used to infer emotions. The recital gives the example of detecting fatigue in professional pilots or drivers to prevent accidents.

**Art. 5(1)(f) prohibition [KNOWN TEXT]** — [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- Prohibits placing on the market, putting into service for this specific purpose, or using AI systems "to infer emotions of a natural person in the areas of workplace and education institutions, except where the use of the AI system is intended to be put in place or into the market for medical or safety reasons."
- This prohibition has applied since **2 Feb 2025** (Art. 113(a)). Penalties have applied since **2 Aug 2025**.

**Commission Guidelines on prohibited AI practices (C(2025) 884, published 4 Feb 2025; non-binding)** (secondary summaries; full text not fetched in this session)
- Workplace emotion recognition is prohibited except for medical or safety reasons. The guidelines give as a prohibited example a call centre that uses webcams and voice recognition to track employees' emotions such as anger — [Lewis Silkin](https://www.lewissilkin.com/insights/2025/02/17/understanding-the-eu-ai-acts-prohibited-practices-key-workplace-and-advertising-102k011); [HCA Mag](https://www.hcamag.com/ca/specialization/employment-law/eus-new-ai-act-restricts-emotion-recognition-systems-in-workplaces/524292)
- The medical and safety exception is read narrowly. Fatigue detection for pilots or drivers falls under safety. An AI system to detect burnout or depression at the workplace or in education would **not** fall under the exception and remains prohibited — [Orrick](https://www.orrick.com/en/Insights/2025/04/EU-Commission-Publishes-Guidelines-on-the-Prohibited-AI-Practices-under-the-AI-Act); [Inside Global Tech (Covington)](https://www.insideglobaltech.com/2025/06/04/european-commission-guidelines-on-prohibited-ai-practices-under-the-eu-artificial-intelligence-act/)
- Physical states such as pain or tiredness are not "emotions or intentions." Fatigue detection for accident prevention is therefore not emotion recognition at all — [Lewis Silkin](https://www.lewissilkin.com/insights/2025/02/17/understanding-the-eu-ai-acts-prohibited-practices-key-workplace-and-advertising-102k011); [WSGR](https://www.wsgrdataadvisor.com/2025/02/eu-commission-issues-guidelines-on-prohibited-ai-practices-under-eu-ai-act/)
- AI systems that infer emotions or sentiment **not** on the basis of biometric data, such as written text, are not prohibited. A search-result summary reports that the guidelines count inference from keystrokes, body postures or movements as biometric-based. This came from a single source and should be verified against paras. 240–260 of the guidelines — [William Fry](https://www.williamfry.com/knowledge/the-time-to-ai-act-is-now-a-practical-guide-to-emotion-recognition-systems-under-the-ai-act/); [Freshfields](https://technologyquotient.freshfields.com/post/102kfql/eu-ai-act-unpacked-25-european-commission-releases-critical-ai-act-implementati)
- The guidelines are not legally binding. Authoritative interpretation rests with the CJEU — [Orrick](https://www.orrick.com/en/Insights/2025/04/EU-Commission-Publishes-Guidelines-on-the-Prohibited-AI-Practices-under-the-AI-Act)

**High-risk (Annex III) [KNOWN TEXT]** — [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- Annex III point 1(c): AI systems intended to be used for emotion recognition, insofar as their use is permitted under Union or national law, are high-risk.
- Annex III point 4 (employment: recruitment, monitoring and evaluating the performance and behaviour of workers) and point 3 (education) can also apply.
- High-risk obligations include Arts. 9–15: risk management, data governance, technical documentation, logging, human oversight, accuracy and robustness. They also include conformity assessment, CE marking and EU database registration. Under Art. 26(7), deployers must inform workers before workplace use.

**Art. 50 transparency [KNOWN TEXT]**
- Art. 50(3): deployers of an emotion recognition or biometric categorisation system must inform the natural persons exposed to it of its operation and process personal data in line with the GDPR. There is a carve-out for law enforcement. The original application date is 2 Aug 2026 — [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- After the Omnibus, Art. 50 duties other than 50(2) watermarking keep the **2 Aug 2026** date. Art. 50(2) machine-readable marking was pushed to **2 Dec 2026** — [CSA research note](https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-omnibus-vii-deadline-delay-20260/); [Usercentrics](https://usercentrics.com/knowledge-hub/eu-ai-act-high-risk-delay-article-50-transparency-consent/)

**Digital Omnibus on AI (proposed 19 Nov 2025 → ENACTED 2026)**
- Political agreement was reached on 7 May 2026. Parliament approved it on 16 June 2026 and the Council gave final adoption on 29 June 2026 — [Sidley Data Matters](https://datamatters.sidley.com/2026/06/22/eu-lawmakers-reach-provisional-agreement-to-delay-key-eu-ai-act-obligations/); [SecurePrivacy](https://secureprivacy.ai/blog/eu-ai-act-digital-omnibus-the-new-high-risk-ai-deadlines-after-council-approval); [Hogan Lovells](https://www.hlc.com/en/publications/eu-legislators-agree-to-delay-for-highrisk-ai-rules)
- One source reports publication as **Regulation (EU) 2026/1744**, published in the OJ on 24 July 2026 and in force from 27 July 2026. This is single-source and the regulation number is unverified — [aiacto.eu](https://www.aiacto.eu/en/blog/digital-omnibus-ai-act-report-2027)
- New application dates: **2 Dec 2027** for standalone Annex III high-risk systems, which covers emotion recognition under Annex III 1(c) and employment and education uses, and **2 Aug 2028** for Annex I product-embedded systems — [CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-omnibus-vii-deadline-delay-20260/); [Gibson Dunn (title/snippet only)](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/); [VerifyWise](https://verifywise.ai/blog/eu-ai-act-omnibus-what-changed)
- No source found indicates that the Omnibus changed the Art. 5(1)(f) prohibition or its Feb 2025 application date.

**Penalties [KNOWN TEXT]** — Art. 99, [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- Breach of Art. 5 prohibitions: up to €35m or 7% of worldwide annual turnover, whichever is higher.
- Breach of most other obligations, including high-risk and Art. 50 duties: up to €15m or 3%.
- Supplying incorrect information to authorities: up to €7.5m or 1%.
- For SMEs, each cap is the lower of the two amounts.

### Inferences
- For a product that estimates emotion from physiological signals (HRV, EDA, EEG, respiration), voice or face, the AI Act test is: (a) are the inputs "biometric data" in the Art. 3(34) sense? Physiological signals almost certainly are. (b) Is the output an *emotion or intention*, or a *physical state*? Fatigue, drowsiness and pain are excluded. "Stress" is borderline and depends on framing: physiological arousal or strain reads as a physical state, while anxiety or frustration reads as an emotion. (c) Is the deployment context a workplace or education institution?
- B2B deployments to employers, such as wellbeing dashboards, call-centre QA, burnout or stress scoring, or attention or engagement in classrooms, are the highest-risk use cases. Absent a narrowly framed safety purpose, they are banned in the EU now.
- Consumer and B2C or healthcare uses, such as wellness apps, automotive driver monitoring outside an employment context, and research, are not banned. They are high-risk under Annex III 1(c) from 2 Dec 2027. Art. 50(3) disclosure applies to deployers now, from 2 Aug 2026.
- Medical devices with emotion or affect inference may be Annex I (MDR) high-risk from 2 Aug 2028.

### Gaps
- Exact paragraph numbers and wording of the Commission guidelines on physiological signals (heart rate, EEG) and "stress" could not be fetched. Verify in C(2025) 884, section 7.
- The OJ reference for the Omnibus (2026/1744) is single-source and unverified. Grace periods for systems already on the market and Art. 50 transitional periods for legacy systems were not confirmed.
- No information was found on whether the Commission has issued Art. 50 transparency guidelines or a code of practice covering emotion recognition disclosure by late 2026.

---

## 2. GDPR interplay and EDPB views

### Takeaway
Emotion recognition from face, voice or physiology will usually involve special-category data under GDPR Art. 9. That happens either as biometric data processed to uniquely identify a person, or because the inferences reveal health, for example stress or depression. An explicit Art. 9(2) ground is then needed, typically explicit consent, which is hard to rely on in employment. A DPIA (Art. 35) is effectively mandatory. EU regulators have argued since 2021 for a general ban on emotion recognition.

### Cited Findings
- **[KNOWN TEXT]** GDPR Art. 4(14) defines biometric data as data from specific technical processing of physical, physiological or behavioural characteristics "which allow or confirm the unique identification." Art. 9(1) prohibits processing of biometric data "for the purpose of uniquely identifying" a person and of data concerning health, unless an Art. 9(2) exception applies. Art. 22 restricts solely automated decisions with legal or similarly significant effects — [EUR-Lex GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- **[KNOWN TEXT]** AI Act Art. 50(3) itself requires emotion recognition deployers to process personal data in line with the GDPR. Art. 5 and Annex III operate "without prejudice" to the GDPR — [EUR-Lex AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- The AI Act definition of biometric data is broader than the GDPR's because it does not require identification capability. Data can therefore be "biometric" for AI Act purposes without being Art. 9 biometric data under the GDPR — [William Fry](https://www.williamfry.com/knowledge/the-time-to-ai-act-is-now-a-practical-guide-to-emotion-recognition-systems-under-the-ai-act/)

### Inferences
- Emotion and stress inferences derived from physiological signals are likely to be treated as "data concerning health" when they reveal mental-health state. That triggers Art. 9 even if the signals are not used for identification.
- In employment, consent is generally not considered freely given because of the power imbalance (EDPB consent guidelines). Workplace affect inference therefore lacks a lawful basis under both the GDPR and AI Act Art. 5.

### Gaps
- The EDPB-EDPS Joint Opinion 5/2021 on the AI Act proposal called for a ban on emotion-recognition AI, with exceptions for certain health and research uses. This comes from the researcher's background knowledge and was not re-fetched: [EDPB](https://www.edpb.europa.eu/our-work-tools/our-documents/edpbedps-joint-opinion/edpb-edps-joint-opinion-52021-proposal_en). Confirm the wording before quoting.
- No 2025–2026 EDPB guideline specifically on emotion recognition was found. Whether the EDPB/AI Act interplay guidelines, on the work programme for 2025–26, were published was not verified.

---

## 3. Japan: APPI (2026 amendment), AI推進法, AI事業者ガイドライン, camera guidance

### Takeaway
Japan has no prohibition on emotion recognition. Regulation runs through the APPI and soft law. The **2026 APPI amendment (令和8年法律第56号)** was enacted on 10 July 2026 and promulgated on 17 July 2026. It creates a new category of **特定生体個人情報** ("specified biometric personal information", centred on face feature data). For that category it requires notice of handling, eases data subjects' stop-use requests, and bans opt-out third-party transfers. It will be fully in force by July 2028 at the latest. The AI推進法 (AI Promotion Act) has been fully in force since 1 Sep 2025. It is non-punitive, and neither it nor the AI事業者ガイドライン v1.2 (31 Mar 2026) addresses emotion inference specifically in any source found.

### Cited Findings
- **APPI amendment status: ENACTED, mostly NOT YET IN FORCE.** It passed the House of Councillors on 10 July 2026, was promulgated on 17 July 2026 as 令和8年法律第56号, and takes effect on a cabinet-order date within 2 years of promulgation (i.e., by 17 July 2028). Penalty-related provisions take effect earlier, reported as 6 months after promulgation, around 17 Jan 2027 — [ScanNetSecurity](https://scan.netsecurity.ne.jp/article/2026/07/29/55805.html); [契約ウォッチ](https://keiyaku-watch.jp/media/hourei/202807-kojinjohohogohou-kaisei/); [Rocket Boys](https://rocket-boys.co.jp/security-measures-lab/japan-privacy-law-2026-amendment-passes-house). Sources disagree on the House of Representatives date (21 May committee vs 26 May plenary).
- The amendment covers AI and data use (third-party provision without consent for statistics-creation purposes, including AI development), administrative fines (課徴金), biometric information rules and protection of minors — [公明党 解説](https://www.komei.or.jp/km/otsu-sato-hiroshi/2026/09/08/%E5%80%8B%E4%BA%BA%E6%83%85%E5%A0%B1%E4%BF%9D%E8%AD%B7%E6%B3%95%E3%81%8C%E5%A4%A7%E3%81%8D%E3%81%8F%E5%A4%89%E3%82%8F%E3%82%8A%E3%81%BE%E3%81%99-%E3%80%8C%E7%B7%A9%E3%82%81%E3%82%8B/); [三宅法律事務所 解説 (成立版; not fetched)](https://www.miyake.gr.jp/wp-content/uploads/2026/07/令和8年改正個人情報保護法_解説レジュメ_成立版.pdf)
- 特定生体個人情報 obligations: (i) notice of handling matters (周知義務), (ii) eased requirements for 利用停止 (stop-use) requests, and (iii) a ban on third-party provision by opt-out, so consent is required. The background is concern that face feature data can be collected en masse without the person's knowledge. Search results cite new provisions 16条5項 and 21条の2 — [池田・染谷 I&S Insight](https://www.ikedasomeya.com/insight/26543); [TMI 連載第6回 (title only)](https://www.tmi.gr.jp/eyes/blog/2026/18449.html); [J-Trust解説](https://jtrustc.co.jp/knowledge/hogohou-kaisei-2601/)
- Camera images: the regulatory focus is face feature data and other 個人識別符号 (individual identification codes), not video as such — [OPTiM](https://www.optim.co.jp/media/cat-guide/aic_2610-01)
- カメラ画像利活用ガイドブック (総務省・経産省, IoT推進コンソーシアム; ver2.0 Mar 2018; later ver3.0 exists) recommends extracting feature data, discarding the original images and ensuring attribute estimates such as sex or age cannot identify individuals. It does not specifically address emotion estimation — [総務省 PDF ver2.0](https://www.soumu.go.jp/main_content/000542668.pdf)
- **AI推進法** (人工知能関連技術の研究開発及び活用の推進に関する法律) was promulgated on 4 June 2025, with Chapters 3–4 in force from 1 Sep 2025. It is promotional, imposes effort duties only and has no penalties. The AI基本計画 was adopted by cabinet in Dec 2025, and the 適正性指針 (appropriateness guideline) was decided on 19 Dec 2025 — [White & Case](https://www.whitecase.com/sites/default/files/2026-04/japan-first-ai-legislation-becomes-law.pdf); [AIST AIQMI資料](https://aiqm-initiative.cons.aist.go.jp/pdf/20260330_AIQMI_WG1_SIG_Regulation_Law.pdf)
- **AI事業者ガイドライン v1.2** (published 31 Mar 2026; soft law) adds treatment of AI agents and physical AI, human-in-the-loop operation and training-data traceability — [AI総研](https://www.ai-souken.com/article/ai-generation-guidelines-introduction); [AIST](https://aiqm-initiative.cons.aist.go.jp/pdf/20260330_AIQMI_WG1_SIG_Regulation_Law.pdf)

### Inferences
- Under the current APPI, emotion estimates about an identifiable person are ordinary personal information. They are not 要配慮個人情報 (sensitive information) unless they amount to health information, for example a diagnosis. That means the purpose of use must be specified and disclosed (APPI Arts. 17, 21), and appropriate acquisition is required (Art. 20). PPC Q&A states that profiling-type inference requires purpose disclosure; this is background knowledge, not re-verified.
- If a product extracts face feature data (or possibly voiceprints, depending on the cabinet-order and PPC rule scope) to run emotion estimation on identified individuals, the 特定生体個人情報 rules will likely apply from 2028. That means notice, stop-use handling and no opt-out sharing. Raw physiological signals such as HRV or EDA that are not used as identifiers are probably outside 特定生体個人情報.
- In workplace monitoring, Japanese practice relies on labour-law fairness and the MHLW 雇用管理分野 Q&A on personal information rather than any affect-specific rule. This is background only and not verified in this session.

### Gaps
- The exact statutory definition of 特定生体個人情報 (face only, or also voiceprint, iris, gait) and whether emotion or attribute *inference* is regulated could not be confirmed, because the Japanese law-firm PDFs were unreachable.
- No PPC, METI or MIC document specifically on 感情認識/感情推定 was found. Whether the 第Ⅱ期 AI基本計画 (one source cites a 14 Jul 2026 cabinet decision) mentions emotion AI is unverified.
- No current Japanese guidance on AI workplace monitoring was found.

---

## 4. United States

### Takeaway
There is no federal emotion-AI law. Risk comes from (1) biometric statutes, chiefly Illinois BIPA, when face or voice geometry is captured; (2) state "neural data" amendments to privacy laws in CO, CA, MT and CT, which cover EEG and possibly peripheral nervous-system signals; (3) state AI/ADMT laws, where Colorado repealed and replaced its AI Act in May 2026 with a narrower ADMT law effective 1 Jan 2027; and (4) FTC Section 5 enforcement against unsubstantiated or unfair AI and biometric practices.

### Cited Findings
**Illinois BIPA (ENACTED; amended 2024)**
- SB 2979 was signed on 2 Aug 2024. It makes violations of Sections 15(b) and 15(d) accrue once per person rather than per scan, while the damages amounts stay at $1,000 for negligent and $5,000 for intentional or reckless violations. It also permits electronic signatures for written releases. Whether it applies retroactively was left to the courts — [Kilpatrick](https://ktslaw.com/insights/alert/2024/5/illinois-legislature-passes-bill-amending-bipa-violation-accrual-standards); [Baker Donelson](https://www.bakerdonelson.com/bipa-amendments-passed-by-illinois-legislature-what-companies-need-to-know); [Shook Hardy](https://www.shb.com/intelligence/client-alerts/pds/may-2024-bipa-amendment-wolfe-searle)
- **[KNOWN TEXT]** BIPA covers "biometric identifiers", which include voiceprints and scans of face geometry. It requires written notice, a written release, a public retention policy and a ban on profiting from the data, and it gives a private right of action — [ILGA 740 ILCS 14](https://www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=3004&ChapterID=57)

**Colorado AI Act (SB 24-205): REPEALED AND REPLACED**
- SB 25B-004 (Aug 2025 special session) had delayed the effective date from 1 Feb 2026 to 30 June 2026. On 14 May 2026, Governor Polis signed **SB 26-189**. It replaces the high-risk AI framework with an "automated decision-making technology" (ADMT) framework, and the repeal and replacement take effect on **1 Jan 2027** — [Davis Wright Tremaine](https://www.dwt.com/blogs/privacy--security-law-blog/2026/05/colorado-ai-act-repeal-new-transparency-law); [Skadden (title/snippet)](https://www.skadden.com/insights/publications/2026/06/colorado-repeals-and-replaces-its-ai-act)
- SB 26-189 drops the duty of care, risk-management programmes and impact assessments. It keeps developer documentation duties and consumer notice and human-review rights. The Attorney General filed proposed rules on 11 Aug 2026 and held a hearing on 26 Oct 2026. These two points come from secondary or aggregator sources — [legaldesire](https://legaldesire.com/colorado-ai-act/); [imiel.dev](https://imiel.dev/explore/us-ai-legislation-2026/colorado/)
- xAI sued on 9 Apr 2026 to block SB 24-205, and the AG agreed to pause enforcement. Accounts of the stay's current scope conflict — [Lawfuel](https://www.lawfuel.com/colorado-ai-act-2026-sb-26-189/); [intellisee](https://intellisee.com/intelligence/colorado-ai-act-sb-24-205-repeal-2026-compliance-briefing/)

**Neural data laws (ENACTED)**
- Colorado HB 24-1058 (2024) was the first state law to add neural and biological data to a comprehensive privacy law as sensitive data requiring opt-in consent — [Hunton](https://www.hunton.com/privacy-and-information-security-law/colorado-amends-privacy-act-with-h-b-1058-adding-new-protections-for-biological-and-neural-data)
- California **SB 1223** was signed on 28 Sep 2024. It adds "neural data" to CCPA "sensitive personal information" and defines it as "information that is generated by measuring the activity of a consumer's central or peripheral nervous system, and that is not inferred from nonneural information". The rights model is limit-use, which is opt-out style — [Baker Botts](https://ourtake.bakerbotts.com/post/102jkp7/california-extends-privacy-law-to-cover-neural-data); [Tech Policy Press](https://techpolicy.press/neural-data-and-consumer-privacy-californias-new-frontier-in-data-protection-and-neurorights)
- Montana (SB 163, 2025) and Connecticut (SB 1295; most provisions effective 1 July 2026) followed. Connecticut covers only the central nervous system, while CA and MT also reach the peripheral nervous system. Colorado and Connecticut require opt-in consent — [Cooley (Feb 2026)](https://www.cooley.com/news/insight/2026/2026-02-23-your-brain-their-rules-the-growing-patchwork-of-neural-data-regulation); [FPF](https://fpf.org/blog/the-neural-data-goldilocks-problem-defining-neural-data-in-u-s-state-privacy-laws/); [RM Magazine](https://www.rmmagazine.com/articles/article/2026/02/24/state-of-mind--the-new-landscape-of-neural-data-privacy-laws)
- **PENDING:** In early 2026, nine neural-data bills were introduced in six states (AL, CA, IL, NY, VT, VA). The federal **MIND Act**, which would have the FTC study neural data, has not passed — [Cooley](https://www.cooley.com/news/insight/2026/2026-02-23-your-brain-their-rules-the-growing-patchwork-of-neural-data-regulation); [Captain Compliance](https://captaincompliance.com/news/emerging-u-s-regulation-of-neural-data-risks-and-compliance-strategies-for-privacy-officers/); [Vermont H.814 testimony](https://legislature.vermont.gov/Documents/2026/Workgroups/Senate%20Health%20and%20Welfare/Bills/H.814/Witness%20Testimony/H.814~Ashley%20Collins~US%20State%20Legislation%20to%20Protect%20Neural%20Data~4-9-2026.pdf)
- Sources conflict on the scope of Colorado's neural-data definition: one says it applies only when the data is used for identification, another calls it broader — [Captain Compliance](https://captaincompliance.com/news/emerging-u-s-regulation-of-neural-data-risks-and-compliance-strategies-for-privacy-officers/) vs [FPF](https://fpf.org/blog/the-neural-data-goldilocks-problem-defining-neural-data-in-u-s-state-privacy-laws/)

**FTC**
- **[KNOWN]** In the Rite Aid order (Dec 2023), the FTC barred Rite Aid from using AI facial recognition for 5 years over an inadequate-safeguards finding. It is the leading federal precedent on biometric AI fairness and accuracy duties — [FTC press release](https://www.ftc.gov/news-events/news/press-releases/2023/12/rite-aid-banned-using-ai-facial-recognition-after-ftc-says-retailer-deployed-technology-without-reasonable-safeguards)

### Inferences
- Voice or face-based emotion estimation that extracts face geometry or voiceprints from Illinois residents carries BIPA class-action risk even if the purpose is not identification. Courts have focused on whether a biometric identifier is captured, not on the use.
- EEG and fNIRS products, and arguably HRV or EDA under California's and Montana's peripheral-nervous-system language, trigger sensitive-data duties. California's carve-out for data "inferred from nonneural information" means camera-based affect inference is not neural data.
- Employment uses of affect AI are likely to fall within state ADMT and AI-in-hiring rules, such as Colorado SB 26-189 from 2027, California CPPA ADMT regulations, Illinois HB 3773 (AI in employment, effective 1 Jan 2026) and NYC Local Law 144. Those were not researched in this session.

### Gaps
- No US state law found specifically bans emotion recognition. Specific FTC enforcement against emotion AI in 2025–26 was not found.
- California CPPA ADMT and risk-assessment regulations (finalised 2025) and Illinois HB 3773 were not verified in this session.
- Whether the federal AI preemption push of 2025–26 (executive order and moratorium proposals) affects these state laws was not researched.

---

## 5. China, UK, South Korea

### Takeaway
- **China** regulates emotional-companion ("anthropomorphic") AI services through CAC-led Interim Measures in force since 15 July 2026, plus the PIPL's sensitive-information rules for biometrics. **No** EU-style workplace ban was found.
- **UK**: the ICO has warned since Oct 2022 that biometric emotion analysis is "immature" and possibly never workable. There is no statutory ban.
- **South Korea**: the AI Basic Act has been in force since 22 Jan 2026. Its "high-impact" categories cover biometric analysis in criminal investigation and decisions such as hiring, but no specific emotion-recognition rule was found.

### Cited Findings
**China**
- The Interim Measures for the Administration of Anthropomorphic (Humanised) AI Interaction Services were adopted on 10 Apr 2026 and in force from 15 July 2026. They were jointly issued by the CAC with NDRC, MIIT and others; sources say four or five bodies. They target services that provide sustained emotional interaction simulating human personality. The final text narrowed the Dec 2025 draft by excluding customer-service bots and productivity tools. The measures focus on curbing user dependency, data safeguards and protection of minors — [Science and Technology Daily](https://stdaily.com/web/English/2026-07/28/content_554571.html); [MLex](https://www.mlex.com/mlex/articles/2464392/china-sets-rules-for-companionship-ai-balances-oversight-with-innovation); [Digital Policy Alert](https://digitalpolicyalert.org/event/39272-interim-measures-for-the-administration-of-anthropomorphic-artificial-intelligence-interaction-services-including-artificial-intelligence-authority-governance-enter-into-force); [China Briefing](https://china-briefing.com/news/china-ai-regulation-2026-new-laws-rules)
- **[KNOWN TEXT]** PIPL Art. 28 treats biometric data and medical/health data as sensitive personal information. Art. 29 requires separate consent, and processing requires necessity and a PIA — [NPC PIPL (English)](http://en.npc.gov.cn.cdurl.cn/2021-12/29/c_694559.htm)

**UK**
- In Oct 2022 the ICO warned that emotion analysis technologies are "immature… They may not work yet, or indeed ever". It cited risks of systemic bias, inaccuracy and discrimination, called them "far more risky" than other biometrics, and said organisations failing expectations "will be investigated" — [ICO press release](https://cy.ico.org.uk/about-the-ico/media-centre/news-and-blogs/2022/10/immature-biometric-technologies-could-be-discriminating-against-people-says-ico-in-warning-to-organisations); [Computer Weekly](https://www.computerweekly.com/news/252526548/ICO-warns-against-using-biometrics-for-emotional-analysis)
- The ICO's biometric data guidance followed in 2024. UK GDPR Art. 9 applies. The Data (Use and Access) Act 2025 did not add an emotion-AI ban. Both points are background knowledge, not verified this session.

**South Korea**
- The Framework Act on AI Development and Establishment of Trust and its Enforcement Decree took effect on 22 Jan 2026. Fines are subject to a grace period. High-impact AI domains include biometric analysis for criminal investigation (face and voice matching) and significant decisions such as hiring and lending. Falling within a domain does not automatically make a system high-impact — [Cooley](https://www.cooley.com/news/insight/2026/2026-01-27-south-koreas-ai-basic-act-overview-and-key-takeaways); [Stimson](https://www.stimson.org/2026/south-koreas-ai-basic-act-seeking-balance-between-industry-innovation-and-social-risk/); [BHRRC](https://www.business-humanrights.org/ja/最新ニュース/s-korea-draft-decree-for-ai-basic-act-spark-backlash-over-limited-scope-and-delayed-penalties)
- One source reports an amending act and amended decree entering into force on 21 July 2026, including watermarking rules. This is unverified — [babl.ai](https://babl.ai/?p=9368)
- Civil society compared Korea unfavourably with the EU for not banning high-risk uses such as emotion recognition — [BHRRC](https://www.business-humanrights.org/ja/最新ニュース/s-korea-draft-decree-for-ai-basic-act-spark-backlash-over-limited-scope-and-delayed-penalties)

### Inferences
- A Korean deployment of emotion AI in hiring would likely be high-impact. That brings risk management, explanation and human oversight duties, and generative or "AI interaction" notice duties may apply. Korea's PIPA sensitive-information rules also apply to biometric data.
- Chinese companion or emotional-support products using affect inference fall under the 2026 Interim Measures in addition to the PIPL and the generative-AI and deep-synthesis rules.

### Gaps
- The official Chinese text of the Interim Measures was not reviewed, so it is unknown whether it explicitly regulates emotion *recognition* as opposed to emotional *interaction*.
- The current ICO position as of 2026 on emotion AI, and any UK AI bill, was not verified.
- Korean decree text on biometric or emotion categories was not reviewed.

---

## 6. Standards (IEEE, ISO/IEC)

### Takeaway
**IEEE 7014-2024**, "Ethical Considerations in Emulated Empathy in Autonomous and Intelligent Systems", is the dedicated standard for emotion AI. It was published on 28 June 2024 and is free via the IEEE GET Program. ISO/IEC 42001 (AI management systems) and ISO/IEC 23894 (AI risk management) are the general frameworks most relevant for AI Act conformity, pending harmonised standards from CEN-CENELEC JTC 21.

### Cited Findings
- IEEE 7014-2024 was approved in May 2024 and published on 28 June 2024. It covers systems that identify, measure, respond to or simulate emotional and cognitive states, including affective computing and emotion AI, across development, deployment and decommissioning, to protect wellbeing and guard against bias, abuse and exploitation. The working group is paused but may revise it — [IEEE SA](https://standards.ieee.org/ieee/7014/7648/); [IEEE P7014 WG](https://sagroups.ieee.org/7014); [IEEE Xplore](https://ieeexplore.ieee.org/document/10576666)

### Inferences
- Aligning with IEEE 7014 plus ISO/IEC 42001 is a defensible governance baseline for an emotion-estimation foundation model ahead of Annex III obligations in Dec 2027.

### Gaps
- No ISO/IEC standard specific to emotion recognition was confirmed. ISO/IEC JTC 1/SC 37 covers biometrics generally, and ISO/IEC 30150-series affective-computing work exists but its status was not verified.
- The status of CEN-CENELEC harmonised standards for the AI Act as of Nov 2026 was not researched.

---

## Practical summary for builders of emotion estimation from physiological signals, voice or face (synthesis of the above)

| Jurisdiction | Workplace / education | Other uses | Key dates |
|---|---|---|---|
| EU | **Prohibited** (Art. 5(1)(f)) unless medical/safety; burnout/depression detection is not exempt; fatigue ≠ emotion | High-risk Annex III 1(c); Art. 50(3) notice; GDPR Art. 9/DPIA | Ban 2 Feb 2025; fines 2 Aug 2025; Art. 50 2 Aug 2026; Annex III 2 Dec 2027; Annex I 2 Aug 2028 |
| Japan | No ban; APPI purpose disclosure; labour-law fairness | 特定生体個人情報 rules for face features (consent for third-party sharing, notice, stop-use) | AI推進法 in force 1 Sep 2025; APPI amendment promulgated 17 Jul 2026, in force by Jul 2028 |
| US | No ban; BIPA (IL); state ADMT/hiring laws | Neural data = sensitive (CO, CA, MT, CT); FTC §5 | CT neural data 1 Jul 2026; Colorado SB 26-189 1 Jan 2027 |
| China | No ban found; PIPL sensitive data | Anthropomorphic AI Interim Measures | In force 15 Jul 2026 |
| UK | No ban; ICO warns emotion AI "immature" | UK GDPR Art. 9 | ICO warning Oct 2022 |
| Korea | Hiring = high-impact domain | AI Basic Act transparency | In force 22 Jan 2026 |
