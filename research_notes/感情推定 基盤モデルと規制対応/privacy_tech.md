# Privacy-Preserving Technologies for AI Emotion/Affect/Stress Estimation and Business Implications (as of Nov 2026)

Research note. Method: web search, about 20 queries. arxiv.org, fpf.org and uctoday.com could not be fetched from this session because those hosts are blocked. Most arXiv-derived numbers therefore come from search-result abstracts and snippets, not full texts. Verify them before quoting in a client deliverable.

## 1. On-device / edge inference and TinyML for affect and stress

### Takeaway
Stress classification from HR, HRV, EDA and PPG fits on microcontrollers. Published models run from kilobytes to a few hundred KB of RAM, with reported accuracy of about 88–94% on lab datasets. Biosignal foundation models are being distilled for wearables: the PPG-Distill paper reports 7x faster inference and 19x less memory. Major platforms (Apple, Samsung) market local or encrypted health processing. Public technical documentation on where stress and mood inference actually runs is thin.

### Cited Findings
- A Micro-Attention CNN for wearable biosignal stress detection has about 3.8K parameters. It uses structured pruning, selective quantization-aware training and post-training quantization, and keeps BatchNorm and attention in full precision. — [MDPI Technologies 2025](https://www.mdpi.com/2227-7080/14/5/300)
- An LSTM on raw noisy PPG runs on an STM32H7 Cortex-M7 with TFLite (QAT, pruning, PTQ). It needs about 170 KB RAM (about 12x smaller) at 87.76% accuracy. — [Real-Time Stress Detection from Raw Noisy PPG (TinyML), 2024](https://bohrium.dp.tech/paper/arxiv/5984cfe20bd89110395f53eed8084378b671098a95b160875c9fc76d7374a0a1)
- A PPG + CWT CNN was pruned and post-training-quantized from 19.3 MB to fit an STM32H743. It reports 93.7% on-device accuracy. — [arXiv 2410.19776](https://export.arxiv.org/pdf/2410.19776)
- Kanjo et al. (IEEE Micro) run two TinyML DNNs on one low-cost MCU. A HR+EDA stress model reaches 88% and an activity model 98%. The activity model is used to suppress motion artifacts. — [NTU repository](https://irep.ntu.ac.uk/id/eprint/50321)
- HRV-based stress and sleep TinyML runs on a Raspberry Pi Pico (RP2040). — [MDPI Eng. Proc.](https://www.mdpi.com/2673-4591/78/1/3)
- Foundation-model compression:
  - PPG-Distill (Emory, 2025) uses prediction-, feature- and patch-level distillation from a PPG foundation model. Students improve by up to 21.8%, with 7x faster inference and 19x less memory. The tasks were HR estimation and AF detection, not stress. — [arXiv 2509.19215](https://arxiv.org/pdf/2509.19215)
  - Apple distilled a self-supervised PPG encoder into low-power accelerometer encoders, using data from the Apple Heart and Movement Study. — [arXiv 2412.11276](https://arxiv.org/pdf/2412.11276)
  - Apple trained PPG and ECG foundation models on Apple Watch data from about 141K participants over about 3 years. — [Apple ML Research](https://machinelearning.apple.com/research/large-scale-training)
- Samsung's Galaxy Watch estimates stress from HR plus HRV, and Samsung says health data is stored safely with Samsung Knox. These are marketing claims with no public detail on on-device vs. cloud inference. Users reported spurious high-stress alerts after One UI 8 Watch. — [Android Authority](https://www.androidauthority.com/how-does-galaxy-watch-measure-stress-3234828); [Android Central](https://www.androidcentral.com/wearables/samsung-galaxy-watch-rogue-stress-alerts-signal-a-larger-problem-with-smartwatches); [eWeek: Samsung health AI runs directly on smartwatches](https://www.eweek.com/news/samsung-health-ai-smartwatches/)
- Apple has no native stress score. Its "State of Mind" is a self-reported emotional check-in, not an inference. Apple claims end-to-end encryption of health data, including in iCloud, and inaccessibility while the device is locked. Researchers note that users still have to trust Apple to maintain this. — [WatchWitch, arXiv 2507.07210](https://arxiv.org/html/2507.07210v1); [privacy app comparison blog (secondary)](https://www.sanolabs.eu/blog/best-privacy-first-health-apps-2026/)

### Inferences
- Apple's design choice is to log self-reported mood and HRV but not infer emotion. This lowers both regulatory exposure (it avoids "emotion recognition from biometric data") and false-positive risk. It is a relevant design pattern.
- MCU-level stress models are technically mature for binary stress vs. no-stress classification on lab protocols such as WESAD. Real-world validity is the bottleneck, not compute. The Samsung false-alert reports illustrate this.
- On-device inference supports GDPR data minimization: raw biosignals never leave the device and only a score or event leaves. It does not by itself change AI Act classification, because a prohibited use stays prohibited wherever the model runs.

### Gaps
- No primary Apple or Samsung documentation was found that states where stress or mood models execute. Google/Fitbit's "Body Response" (cEDA) processing location was not verified.
- No published distillation of a foundation model specifically for stress or emotion onto an MCU was found. PPG-Distill covers HR and AF.

## 2. Federated learning (FL) for emotion recognition

### Takeaway
FL for stress (WESAD), speech emotion and EEG emotion is an active academic field with many personalized and clustered variants. Plain FL usually underperforms per-user or centralized models, and personalization narrows the gap. FL alone is not private: inference attacks on shared updates are documented. No real commercial FL deployment for affect was found.

### Cited Findings
- On smartwatch stress detection (WESAD-type data), FL could not reach the performance of either individual or centralized learning. Per-user models averaged 0.9998 accuracy and 0.9996 F1, which suggests a heavily subject-dependent setup. — [J Pers Med 2022, PMC9605246](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9605246/)
- A federated DNN on WESAD wrist EDA reached 86.82% accuracy. — [Sensors 2023, PMC10146352](https://pmc.ncbi.nlm.nih.gov/articles/PMC10146352)
- Clustered FL with Mahalanobis distance was evaluated on WESAD and K-EmoCon against cosine FedAvg. — [JIPS](https://jips-k.org/full-text/1783)
- FedSub uses class-aware prototypes and subnetworks for personalized FL in ubiquitous systems and includes WESAD. Its authors report SOTA improvements. — [arXiv 2411.08699](https://arxiv.org/html/2411.08699v1)
- EEG:
  - Xu et al. (2022) were the first FL on DEAP and SEED, at 90.74%. Local-only training was 29.31% lower than FL. — [Electronics 2022](https://mdpi.com/2079-9292/11/20/3316)
  - FedKDC (IEEE JBHI 2025) uses clustered knowledge distillation for personalized FL and reaches a peak of 85.2% on the SEED family. — [TUM portal](https://portal.fis.tum.de/en/publications/fedkdc-consensus-driven-knowledge-distillation-for-personalized-f/)
  - HeteFedEEG (IEEE TCDS, 2026) uses prototype transfer across heterogeneous client models, about +2.7% on SEED and DEAP. — [XJTU](https://scholar.xjtu.edu.cn/en/publications/hetefedeeg-prototype-transfer-heterogeneous-federated-learning-fo/)
- Speech:
  - Semi-FedSER (Feng & Narayanan, Interspeech 2022) — [arXiv 2203.08810](https://arxiv.org/abs/2203.08810v1)
  - Tan et al. (2024) show speaker-property inference attacks remain possible in federated SER. — [arXiv 2410.13221](https://www.arxiv.org/abs/2410.13221)
  - FedVCPL-Diff (2026) is prototype-learning FL with diffusion. — [TUM portal](https://portal.fis.tum.de/en/publications/fedvcpl-diff-a-federated-convolutional-prototype-learning-framewo/)
  - Asynchronous FL on SER gave up to 10x faster convergence but worsened fairness and privacy disparities (IJCNN 2025). — [arXiv 2505.07041](https://arxiv.org/html/2505.07041v1)
  - CSIRO paper on FL for SER applications — [CSIRO](https://research.csiro.au/dss/paper-federated-learning-for-speech-emotion-recognition-applications)

### Inferences
- FL fits B2B2C settings where several hospitals or OEMs cannot pool data. For single-vendor wearables, on-device personalization (fine-tuning the last layers locally) is simpler and achieves similar privacy goals.
- Accuracy figures are not comparable across papers because of differing subject-dependent vs. LOSO protocols. Treat claims above 90% with caution.

### Gaps
- No verified production FL deployment for affect or stress was found, at Apple, Google, Samsung or anyone else. Google's FL deployments, such as Gboard, are not affect-related.
- Interspeech 2024–2025 FL-SER papers were not confirmed. The ISCA archive could not be searched.

## 3. Differential privacy (DP) on physiological and emotion data

### Takeaway
DP is mostly applied in combination: DP-SGD inside FL, DP-GAN synthetic data, or noise added only to identity-revealing components. Published utility-vs-epsilon curves for affect are scarce. Available results show noticeable quality loss at strong privacy.

### Cited Findings
- Benouis, André & Can (JMIR Mental Health 2024) combine multitask learning, DP and FL on physiological signals. Emotion recognition reached about 90% while re-identification accuracy was limited to 47%. Noise is added only to the identity-recognition task branch. — [JMIR Ment Health 2024;11:e60003](https://mental.jmir.org/2024/1/e60003); [PMC11684349](https://pmc.ncbi.nlm.nih.gov/articles/PMC11684349/)
- A Leipzig master's thesis (Degenkolb) studies DP on WESAD stress detection, with a baseline of 91.89% average accuracy. The author says the relationship to epsilon is difficult to assess. — [Thesis PDF](https://dbs.uni-leipzig.de/file/MA_borislav_degenkolb.pdf)
- DP-GAN synthetic WESAD data (see §5): synthetic data quality is significantly impacted when privacy requirements increase. — [Lange, Wenzlitschke & Rahm, arXiv 2401.13327 / Sensors 2024](https://arxiv.org/pdf/2401.13327)

### Inferences
- A practical pattern is "privacy for identity, utility for affect": target DP or adversarial suppression at the re-identification channel rather than at the whole model. This is a stronger story for GDPR, because biosignals are biometric (see §4).

### Gaps
- No source tabulated stress or emotion accuracy against epsilon (e.g., ε = 1, 4, 8) on WESAD, speech or EEG. The specific utility-loss numbers requested could not be sourced and should not be invented.

## 4. Emotion/identity removal, voice anonymization, and biosignal re-identification risk

### Takeaway
Two complementary directions exist:
- Strip identity or demographics but keep emotion. This is mature: adversarial learning, disentanglement, and the VoicePrivacy Challenge 2024, which explicitly required emotion preservation.
- Strip emotion but keep content. This is less studied (voice-conversion normalization, machine unlearning).

ECG and PPG are effectively biometric, so "anonymized" biosignal datasets carry real re-identification risk.

### Cited Findings
- VoicePrivacy Challenge 2024 (third edition) required anonymization that conceals speaker identity while preserving linguistic content and emotional state. It added emotion-labelled data, protocols and SER-based emotion metrics. It evaluated 6 baselines and 36 participant systems. The results paper (Tomashenko et al.) was posted to arXiv in Jan 2026 and is listed as accepted in Computer Speech & Language. — [arXiv 2601.11846](https://arxiv.org/abs/2601.11846v1); [EURECOM](https://www.eurecom.edu/en/node/4909714)
- Jaiswal & Mower Provost (Univ. Michigan) use adversarial "unlearning" of identity and demographic attributes from speech representations before storage, then train SER on the stripped representations. Performance was maintained or slightly decreased. — [U-M IT news](https://michigan.it.umich.edu/news/?p=18019)
- Ali et al. built an edge-deployable adversarial framework that hides demographic information in speech representations without significantly harming SER. — [arXiv 2103.17139](https://arxiv.org/pdf/2103.17139)
- Aloufi et al. use voice conversion to normalize sensitive paralinguistics, including emotion, while keeping content. This reduces SOTA emotion-recognition accuracy. — [arXiv 1908.03632](https://pdf.arxiv.org/pdf/1908.03632)
- Aloufi et al. use disentangled representations to give users configurable privacy for emotion, gender and health attributes. — [arXiv 2007.15064](https://arxiv.org/pdf/2007.15064v1.pdf)
- Anonymization of HuBERT-type utterance embeddings was evaluated on speaker ID (privacy) and on emotion and depression (utility). — [arXiv 2310.17194](https://arxiv.org/pdf/2310.17194v1.pdf)
- Machine unlearning in SER using only the forget set (2025). Relevant to GDPR erasure requests on trained affect models. — [arXiv 2510.04251](https://arxiv.org/html/2510.04251v2)
- Biosignal re-identification:
  - A study of five real-world ECG datasets (223 participants) finds ECG vulnerable to linkage attacks across public and private datasets. — [arXiv 2408.10228](https://arxiv.org/pdf/2408.10228)
  - In the PRI-Attack, PPG-derived HR and breathing rate plus gesture context re-identified users at up to 71% from HIPAA-compliant wearable data. — [arXiv 2106.11900](https://arxiv.org/abs/2106.11900)
  - A systematic review of 72 studies finds substantial re-identification risk from sensors not usually thought identifying. It asks whether de-identified wearable data gives a false sense of security. — [medRxiv 2022](https://medrxiv.org/content/10.1101/2022.10.04.22280658.full.pdf)
  - Press summary: "your heartbeat could reveal your identity, even in anonymized datasets". — [Help Net Security](https://www.helpnetsecurity.com/?p=341468)

### Inferences
- Under GDPR, raw ECG and PPG should be presumed personal (often biometric) data even after removing names. Anonymization claims for biosignal datasets need a re-identification risk assessment.
- VPC-style anonymization (identity removed, emotion kept) is the most product-ready privacy layer for voice-based affect, e.g. call analytics on customers. It does not make a prohibited workplace use lawful.
- Emotion-removal tech could itself be a product: an "affect firewall" that strips emotional cues before voice data is sent to third-party ASR or LLM services. This is a niche with little competition, flagged as speculative.

### Gaps
- VPC 2024 per-system numbers (EER vs. emotion UAR) were not retrieved because arXiv is blocked here. VPC 2026 status is unknown.
- Few 2024–2026 papers specifically remove emotion from physiological signals; none were found.

## 5. Other PETs: TEE, homomorphic encryption, synthetic data, data minimization, consent UX

### Takeaway
Homomorphic encryption for stress inference is now reported at near-zero accuracy loss and sub-second latency on GPU (WESAD). DP-GAN synthetic WESAD data is usable but degrades under strong DP. No affect-specific TEE work or deployment was found; this is a gap. Aggregate or team-level outputs and user-controlled consent are design patterns argued in commentary, but they do not rescue workplace inference under the AI Act.

### Cited Findings
- A CKKS homomorphic-encryption system for real-time emotion and stress inference on encrypted physiological data (IACR ePrint 2025/2058):
  - WESAD accuracy is 0.966 plaintext vs. 0.967 ciphertext. Hide-and-Seek is 0.868 for both.
  - Latency is 333 ms (general model) and 455 ms (personalized model) on GPU.
  — [IACR ePrint 2025/2058](https://eprint.iacr.org/2025/2058)
- Paillier-encrypted EEG classification keeps inference in milliseconds. — [Applied Sciences 2021](https://www.mdpi.com/2076-3417/11/16/7360/html). A heavier HE vision model needed 7.1 s per prediction, which shows HE cost scales with model size. — [arXiv 2104.09164](https://arxiv.org/pdf/2104.09164.pdf)
- Synthetic data: GAN-generated smartwatch stress data reached about 91% train-on-synthetic, test-on-real and about 93% when augmenting real WESAD. DP-GAN quality drops at stronger privacy. Code is public. — [arXiv 2401.13327](https://arxiv.org/pdf/2401.13327); [GitHub](https://github.com/luckyos-code/privacy-preserving-smartwatch-health-data-generation-using-dp-gans). A 2025 review compares GANs and diffusion (e.g., BioDiffusion) on WESAD, SWELL and CASE for ECG and EDA. — [Sensors 24(10):3052](https://mdpi.com/1424-8220/24/10/3052)
- Consent and ethics frameworks:
  - The Hume Initiative's empathic-AI guidelines set six principles, including Scientific Legitimacy, Transparency and Consent, and rate use cases as supported, conditionally supported or unsupported. — [Hume Initiative](https://hume-initiative-website.pages.dev/guidelines)
  - The Commission's guidelines carve out workplace emotion recognition for training purposes. Critics note this could still let a provider report training completion to the employer. — [Oliver Patel](https://oliverpatel.substack.com/p/emotion-recognition-and-the-eu-ai)

### Inferences
- HE is now viable for small tabular or feature-level biosignal models, i.e. cloud-side scoring without the vendor seeing data. It remains impractical for large audio or video foundation models.
- TEEs (Apple Private Cloud Compute-style, confidential GPUs) are the likely practical path for larger affect models server-side. No affect-specific source was found, so this is unverified.
- Aggregate or team-level outputs reduce GDPR risk but very likely do not avoid AI Act Art. 5(1)(f). The prohibition targets inferring emotions of natural persons, and team aggregates are computed from individual inferences. The regulation researcher should confirm this.

### Gaps
- No public TEE or confidential-computing deployments for emotion AI were found.
- No empirical consent-UX studies specific to affect wearables were found in this pass.

## 6. Commercial examples and vendor pivots after AI Act Art. 5(1)(f)

### Takeaway
The clearest documented retreat predates the AI Act. In 2022 Microsoft retired Azure Face emotion recognition, citing lack of scientific consensus. Automotive (Smart Eye/Affectiva) keeps emotion and state sensing inside safety-regulated driver monitoring (EU GSR, Euro NCAP). No reliable named-vendor report of an EU withdrawal of workplace emotion AI after Feb 2025 was found. Commentary says some vendors still sell such features.

### Cited Findings
- In June 2022, under its Responsible AI Standard, Microsoft stopped offering emotion inference in Azure Face. It also retired gender, age, smile and similar attributes, which became unavailable to new customers immediately and to existing customers from 30 June 2023. Facial recognition was gated behind an application process. — [Gizmodo](https://gizmodo.com/microsoft-shutting-down-azure-facial-emotion-recognitio-1849090511); [Reuters via StreetInsider](https://www.streetinsider.com/Reuters/Microsoft+stops+selling+emotion-reading+tech%2C+limits+face+recognition/20237155.html)
- Smart Eye acquired Affectiva for $73.5M (closed 2021). Affectiva's Emotion AI is integrated into Smart Eye Automotive Interior Sensing, which reads mood and emotions and detects states such as road rage and fear. Smart Eye claims compliance with Euro NCAP, EU GSR and China GB/T DMS standards, and says it is trusted by 21 large OEMs including BMW, Geely and Polestar (vendor claims). The EU GSR mandates ADDW driver monitoring. — [MIT Media Lab](https://www.media.mit.edu/articles/emotion-detection-software-startup-affectiva-acquired-for-73-5m/); [Smart Eye DMS](https://smarteye.se/solutions/automotive/driver-monitoring-system/); [Affectiva](https://go.affectiva.com); [Wikipedia](https://wikipedia.com/wiki/Smart_Eye)
- Commentary (UC Today) asks why vendors are still selling workplace emotion recognition, which implies that market withdrawal is incomplete. The article itself could not be fetched. — [UC Today](https://www.uctoday.com/workplace-management/eu-ai-act-shock-emotion-recognition-is-now-illegal-at-work-so-why-is-your-vendor-still-selling-it/)
- The Commission guidelines narrow the exceptions:
  - Medical means CE-marked or approved medical devices, not general wellbeing.
  - Stress or burnout monitoring of workers is not covered.
  - Safety means life and health, not property.
  - Penalties reach €35M or 7% of turnover, and the rule applies by place of use.
  — [sota.io](https://sota.io/blog/eu-ai-act-emotion-recognition-prohibition-2026-workplace-hr-saas); [Technology's Legal Edge](https://www.technologyslegaledge.com/2025/04/eu-ai-act-spotlight-on-emotional-recognition-systems-in-the-workplace/); [CDT](https://cdt.org/insights/eu-ai-act-brief-pt-4-ai-at-work/)
- The Nov 2025 Commission review / Digital Omnibus reportedly made no change to Art. 5(1)(f) or Art. 50(3). A reported deferral of stand-alone high-risk obligations to 2 Dec 2027 is not verified against an official source. — [Oliver Patel](https://oliverpatel.substack.com/p/emotion-recognition-and-the-eu-ai); [arXiv 2608.00936](https://arxiv.org/pdf/2608.00936)
- California workplace emotion-AI restrictions from 2027 are reported by a secondary blog and not verified. — [shadowaipolicy.com](https://shadowaipolicy.com/blog/ai-emotion-recognition-at-work-eu-california)

### Inferences
- The observable pattern is to reframe "emotion" as "state", meaning drowsiness, distraction, fatigue or impairment, tied to a safety regulation (GSR, Euro NCAP), or as a CE-marked medical device. Commentary says general "wellbeing/stress" framing does not qualify for the exception in the workplace.
- Customer-facing uses such as call-centre customer sentiment and marketing are not prohibited but fall under transparency and high-risk rules. Employee-facing uses of the same system are prohibited. Vendors therefore must architect per-party separation, e.g. analysing only the customer channel. This needs confirmation by the regulation researcher.

### Gaps
- No verified named examples were found of HR-tech, call-centre (Cogito, etc.) or meeting-tool vendors disabling emotion features in the EU after Feb 2025.
- HireVue's earlier drop of facial analysis (reported around 2021) was not confirmed in this search.

## 7. Business implications: open markets and compliance design patterns

### Takeaway
Markets remain open where emotion or state inference is tied to:
- medical device pathways
- safety mandates (automotive DMS, possibly aviation and heavy industry fatigue)
- consumer self-use wellness outside work and education

Privacy tech (on-device, HE, anonymization) is a differentiator for GDPR and biometric-data risk. It is not a legal bypass of AI Act prohibitions.

### Cited Findings
- Exceptions are limited to medical (approved devices) and safety (life and health) reasons. Wellbeing and stress monitoring at work is excluded. — [sota.io](https://sota.io/blog/eu-ai-act-emotion-recognition-prohibition-2026-workplace-hr-saas); [Technology's Legal Edge](https://www.technologyslegaledge.com/2025/04/eu-ai-act-spotlight-on-emotional-recognition-systems-in-the-workplace/)
- Outside the workplace and education, emotion recognition is high-risk or transparency-regulated, not banned. — [mmoww.net summary](https://mmoww.net/ai/laws/eu-ai-act-emotion-recognition-rules/); [regumatrix](https://regumatrix.eu/compliance/emotion-recognition-ai)
- Automotive DMS is mandated by EU GSR (ADDW), which creates regulatory pull. — [Wikipedia: Smart Eye](https://wikipedia.com/wiki/Smart_Eye)
- Consumer wearables (Samsung stress, Apple State of Mind) operate as self-use wellness. — [Android Authority](https://www.androidauthority.com/how-does-galaxy-watch-measure-stress-3234828)

### Inferences (design patterns; synthesis, not sourced claims)
1. **Self-use, on-device by default.** Inference and raw data stay on the user's device, and only user-initiated exports leave it. This minimizes GDPR Art. 9 exposure and suits the consumer wellness market.
2. **Purpose binding to safety or medical use.** Define the output as a physiological or behavioural state (drowsiness, distraction, acute stress physiology) tied to a safety function or CE-marked clinical claim, not as a discrete emotion label.
3. **Identity-stripped affect pipelines.** Use VPC-style voice anonymization or adversarial identity removal before cloud processing, and re-identification testing of biosignal datasets, since ECG and PPG are biometric.
4. **Cryptographic cloud scoring.** CKKS HE for small biosignal models, about 0.3–0.5 s and roughly lossless per the ePrint 2025/2058 result. TEEs are assumed for larger models.
5. **FL or on-device personalization** for multi-institution medical consortia and OEM fleets, with DP or secure aggregation added, because FL alone leaks.
6. **Party separation in B2B contexts.** Never infer on employees or students. Analyse only consenting customers or patients, with Art. 50 disclosure.
7. **Synthetic or DP data** for training and benchmark sharing, accepting a utility drop under strong DP.
8. **Unlearning capability** to honour erasure requests on trained affect models (arXiv 2510.04251).

### Gaps
- No market-size data was gathered on privacy-first affect segments.
- No evidence was found on whether buyers pay a premium for PETs in affect products.
- Cross-jurisdiction differences (Japan APPI, US state biometric laws such as BIPA) were not researched here.
