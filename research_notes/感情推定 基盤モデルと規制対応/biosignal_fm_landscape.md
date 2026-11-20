# Foundation Models for Physiological / Wearable Biosignals: Landscape as of Nov 2026

Method note: this is based on WebSearch results only. Direct page fetches failed because arxiv.org and research.google are blocked by the session's network allowlist. Figures come from search snippets of primary sources (arXiv, ICLR/NeurIPS pages, GitHub, PMC, company blogs) and from secondary coverage, and are marked where they come only from secondary sources. Items labelled "(unverified, prior knowledge)" are not sourced in this session and should not be stated as fact without checking.

## Q1. What are the major models? (catalogue: data scale, SSL objective, architecture, size, openness, organization)

### Takeaway
By late 2026 the field has split into three groups:
- **Big-tech closed models** trained on proprietary cohorts of 10^5 to 10^6+ people: Apple AHMS models, Google LSM, LSM-2 and SensorFM, and Samsung xMAE/HiMAE.
- **Academic open-weight models** trained on public data, roughly 10^4 to 10^5 hours. Examples are PaPaGei, Pulse-PPG, NormWear, AnyPPG, ECG-FM, HuBERT-ECG and the EEG models (LaBraM, CBraMod, EEGPT, NeuroLM, REVE).
- **A 2026 "open science" push** that reimplements the closed big-tech recipes on large public cohorts: OpenMHC and Inertia-1.

### Cited Findings

**Multi-sensor wearable models (consumer smartwatch / ring data)**
- **Apple, "Large-scale Training of Foundation Models for Wearable Biosignals"** (Abbaspourazad et al., ICLR 2024):
  - Self-supervised pretraining on Apple Watch PPG and ECG from the Apple Heart and Movement Study (AHMS), about 141K participants (141,207) over about 3 years.
  - Method: contrastive learning with participant-level positive pairs, stochastic augmentation, and a regularized contrastive loss with momentum training.
  - The embeddings encode demographics and health conditions. The authors claim it is the first FM built on large-scale consumer-wearable PPG/ECG. Closed, no weights. — [arXiv 2312.05409](https://arxiv.org/pdf/2312.05409); [ICLR 2024 poster](https://iclr.cc/virtual/2024/poster/17787)
- A 2026 paper describes the Apple Watch PPG FM as later extended to 213K participants. This is a secondary citation and was not verified on Apple's own pages. — [AnyPPG / related search result](https://arxiv.org/pdf/2511.01747)
- **Apple + USC, Wearable Behavior Model (WBM)**, "Beyond Sensor Data: Foundation Models of Behavioral Data from Wearables Improve Health Predictions" (ICML 2025):
  - Data: about 162K AHMS participants. The arXiv text says "over 15 billion hourly measurements"; press coverage says "2.5 billion hours". These are different units and are not reconciled here.
  - Input: 27 HealthKit quantities aggregated hourly over weekly (168-hour) windows. Evaluated on 57 tasks.
  - It matches or beats a sensor baseline and complements the PPG FM. The best results are on behavior-driven tasks such as sleep. Press reports "up to 92% accuracy", for example on pregnancy detection. Closed. — [arXiv 2507.00191](https://arxiv.org/html/2507.00191v1); [9to5Mac](https://9to5mac.com/2025/07/10/study-apple-ai-model-flags-health-conditions-with-up-to-92-accuracy/); [MacRumors](https://www.macrumors.com/2025/07/11/apple-watch-ai-model-can-reveal-health-conditions/)
- **Wearable accelerometer FM via knowledge distillation** from a PPG teacher (arXiv 2412.11276): 20M minutes of multimodal sensor data from about 172K participants. — [arXiv 2412.11276](https://arxiv.org/pdf/2412.11276). The Apple/AHMS affiliation is from prior knowledge and is unverified.
- **Apple Hypertension Notifications** (Sept 2025): a shipped Apple Watch feature in which an ML feature extractor turns raw PPG into general features, followed by linear risk models. It is for users aged 22+ without a prior diagnosis. — [Apple validation paper](https://www.apple.com/health/pdf/Hypertension_Notifications_Validation_Paper_September_2025.pdf). Apple's PDF does not label this an "FM". The design (pretrained general PPG feature extractor plus linear heads) matches an FM-style deployment, but that reading is an inference.
- **Google LSM-1, "Scaling Wearable Foundation Models"** (Narayanswamy et al., ICLR 2025; arXiv Oct 2024):
  - Data: up to 40M hours of per-minute data from more than 165,000 people. Signals: heart rate, HRV, accelerometer, EDA, skin temperature and altimeter (Fitbit/Pixel).
  - Model: ViT with masked-autoencoding-style SSL. Scaling laws were measured for imputation, interpolation and extrapolation. Closed. — [UW Ubicomp page](https://ubicomplab.cs.washington.edu/publications/lsm_iclr25); [Google Research blog](https://research.google/blog/scaling-wearable-foundation-models/); [ICLR 2025](https://iclr.cc/virtual/2025/poster/27713)
- **Google LSM-2, "Learning from Incomplete Wearable Sensor Data"** (arXiv 2506.05321, June 2025):
  - Pretrained on 40M hours of day-long multimodal recordings.
  - Introduces Adaptive and Inherited Masking (AIM): learnable mask tokens handle both natural missingness and artificial masks, with no imputation step.
  - Evaluated on classification, regression and generation. It degrades much less than imputation-based baselines when sensors or time windows are missing. Closed. — [arXiv 2506.05321](https://arxiv.org/pdf/2506.05321); [Google Research blog](https://www.research.google/blog/lsm-2-learning-from-incomplete-wearable-sensor-data/)
- **Google SensorFM** (blog July 2026; arXiv 2605.22759 per a secondary site):
  - Data: more than 1 trillion minutes (more than 2 billion hours) of minute-resolution signals from about 5 million people. Covers more than 100 countries, all 50 US states, and more than 20 Fitbit/Pixel Watch models.
  - Builds on the LSM-2/AIM approach.
  - Beat bespoke supervised baselines on 34 of 35 tasks covering cardiovascular, metabolic, sleep, mental health, lifestyle and demographics.
  - Presented as a "general intelligence and interface" for wearable data, with LLM-facing health summaries.
  - No public API, no product feature and no shipping timeline announced. Closed. — [Google Research blog](https://research.google/blog/sensorfm-towards-a-general-intelligence-and-interface-for-wearable-health-data/); [MarkTechPost](https://www.marktechpost.com/2026/07/10/google-research-introduces-sensorfm-a-wearable-health-foundation-model-pretrained-on-one-trillion-minutes-of-sensor-data/); [The Decoder](https://the-decoder.com/sensorfm/); [chatppg (arXiv id)](https://chatppg.com/research/papers/sensorfm-google-2026)
- **Samsung Research America, xMAE (ICML) and HiMAE (ICLR)**:
  - Masked-autoencoder biosignal FMs.
  - xMAE links two cardiac signals that measure related activity through different mechanisms (likely PPG and ECG; inferred).
  - HiMAE uses a hierarchical multi-timescale design that supports classification, regression and generation. Samsung claims it runs in under 1 ms on a smartwatch-class CPU.
  - Publicized in Japan in Sept 2026 as a "ヘルス基盤モデル" (health foundation model) by Samsung Electronics Japan. Weights status unknown. — [AI News](https://www.artificialintelligence-news.com/news/samsung-health-ai-models-analyse-wearable-biosignal-data/); [ケータイ Watch](https://k-tai.watch.impress.co.jp/docs/news/2141045.html); [Kyodo PR](https://www.kyodo.co.jp/pr/2026-09-15_4035244/)
- **NormWear** (UCSD Mobile Sensing & UbiComp Lab; arXiv 2412.09758; ACM Trans. Computing for Healthcare 2026):
  - Multivariate, channel-aware FM over PPG, ECG, EEG, GSR/EDA and IMU.
  - Data: 2.5M segments, 14,943 hours, all from public datasets.
  - Code and checkpoint released. — [arXiv](https://arxiv.org/html/2412.09758v1); [GitHub](https://github.com/Mobile-Sensing-and-UbiComp-Laboratory/NormWear); [ACM DL](https://dl.acm.org/doi/10.1145/3803808)
- **OpenMHC** (Stanford Ashley Lab; arXiv 2607.16235, July 2026 with later revisions):
  - Data: more than 60M hours of wearable data, 19 sensor channels and up to 169 linked variables from 11,894 My Heart Counts participants.
  - Benchmark tracks: downstream prediction, imputation and forecasting.
  - Open reimplementations of Apple's WBM (a Mamba2 contrastive encoder) and Google's LSM-2 (ViT MAE).
  - The dataset is to be hosted on Harvard Dataverse for qualified researchers once the paper is accepted. Release status is unconfirmed. — [arXiv](https://arxiv.org/html/2607.16235v2); [GitHub AshleyLab/OpenMHC](https://github.com/AshleyLab/OpenMHC)
- **FemWear** (arXiv 2608.08244): a parameter-efficient women's-health wearable FM built on the OpenMHC backbone. — [arXiv](https://arxiv.org/pdf/2608.08244)

**PPG-specific models**
- **PaPaGei** (Nokia Bell Labs; ICLR 2025):
  - Data: more than 57,000 hours, 20M unlabeled PPG segments from about 13.5K participants, public datasets only.
  - Method: morphology-aware contrastive SSL.
  - Open code and weights under BSD-3-Clause. The GitHub repo was archived (read-only) on Sep 14, 2026.
  - Results include AUROC 0.77 for hypertension and 0.70 for sleep-disordered breathing. — [arXiv 2410.20542](https://arxiv.org/abs/2410.20542); [ICLR proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/file/7871f51d332c8661cc729539d7987b21-Paper-Conference.pdf); [GitHub](https://github.com/nokia-bell-labs/papagei-foundation-model)
- **Pulse-PPG** (arXiv 2502.01108):
  - Model: a 12-block ResNet1D trained with contrastive learning.
  - Data: raw wearable PPG from a 100-day field study with 120 participants.
  - Open-source, and argues that field-trained models beat models trained on clinical data. Total hours not found. — [arXiv](https://arxiv.org/pdf/2502.01108)
- **AnyPPG** (Peking University, Shenda Hong group; arXiv 2511.01747):
  - Method: ECG-guided cross-modal PPG–ECG alignment.
  - Data: 109,909 hours from 58,796 subjects (v1). Later versions say "over 100,000 hours from six sources".
  - Open code and weights. — [arXiv](https://arxiv.org/pdf/2511.01747); [GitHub per paper](https://github.com/PKUDigitalHealth/AnyPPG)
- Further 2026 PPG FM papers:
  - Wavelet-driven masked multiscale reconstruction (2601.12215).
  - SIGMA-PPG generative masking (2601.21031).
  - CAP, with patient-level supervision (2606.15284).
  - RAE-PPG (2609.36794).
  - Cross-modal PPG–ECG "Biosignal Fingerprinting" (2605.09579).
  - Structured pruning plus about 1% parameter fine-tuning of PPG FMs (2610.33788).
  - Benchmark of open-source PPG FMs for biological-age prediction (2603.14030).
  - Abstract-level only; results not verified. — [2601.12215](https://arxiv.org/pdf/2601.12215); [2601.21031](https://arxiv.org/pdf/2601.21031); [2606.15284](https://arxiv.org/pdf/2606.15284); [2609.36794](https://arxiv.org/pdf/2609.36794); [2605.09579](https://arxiv.org/pdf/2605.09579); [2610.33788](https://arxiv.org/html/2610.33788); [2603.14030](https://arxiv.org/pdf/2603.14030)
- Applied use: PPG FM embeddings used for cardiovascular screening of people living with HIV in Vietnam. — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12868744/)
- Other adjacent models: BCG-FM for ambient cardiac sensing (2606.07692), MorphologyFM for ECG plus pulse oximetry (2607.09749), SOTER as a generative wearable-physiology time-series FM (2609.16804), and UNIPHY+ from ICU to home (2509.16348). — [BCG-FM](https://arxiv.org/pdf/2606.07692); [MorphologyFM](https://arxiv.org/pdf/2607.09749); [SOTER](https://arxiv.org/pdf/2609.16804); [UNIPHY+](https://arxiv.org/pdf/2509.16348)

**Accelerometer / IMU / EMG models**
- **Inertia-1** (UCLA, Duke and JHU, Yuzhe Yang et al.; NeurIPS 2026; arXiv 2607.06617):
  - A "fully open" study of wearable motion FMs that compares 10 pretraining methods under shared data and evaluation.
  - Tests downsampling to 20, 5, 1 and 0.2 Hz. Wrist-pretrained models transfer to other body placements.
  - Code is public. Weights are not confirmed. — [arXiv](https://arxiv.org/pdf/2607.06617); [NeurIPS 2026](https://neurips.cc/virtual/2026/poster/153477)
- "Physical activities enable scalable foundation modelling for broad-spectrum health prediction" (arXiv 2607.06954): an activity-based FM. Details not verified. — [arXiv](https://arxiv.org/html/2607.06954)
- **Meta Reality Labs, sEMG wristband** (Nature 645:702–711, 2025):
  - Generic decoding models (not branded an "FM") trained on data from thousands of participants.
  - Hardware: 16 bipolar channels (48 electrode pins).
  - Generalizes out of the box across people. Personalization improved handwriting decoding by 16%.
  - Released more than 100 hours of sEMG from 300 participants, plus code (facebookresearch/generic-neuromotor-interface). — [The Register](https://www.theregister.com/2025/07/23/meta_wristband_ui_control/); [RePEc/Nature](https://ideas.repec.org/a/nat/nature/v645y2025i8081d10.1038_s41586-025-09255-w.html); [Scimex](https://www.scimex.org/newsfeed/could-you-swap-your-mouse-and-keyboard-for-a-smart-bracelet)

**ECG models**
- **ECG-FM** (University Health Network/Toronto per prior knowledge; JAMIA Open):
  - Transformer trained with masked reconstruction plus contrastive learning on about 1.5M 12-lead ECGs. arXiv v1 said 2.5M.
  - Open weights, code and benchmark. — [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12530324/)
- **HuBERT-ECG**: a transformer using HuBERT-style masked prediction, pretrained on 9.1M 12-lead ECGs from 4 countries. 97.2M parameters (base). Weights are on Hugging Face under CC BY-NC 4.0, which is non-commercial. — [medRxiv](https://www.medrxiv.org/content/10.1101/2024.11.14.24317328.full.pdf); [HF model card](https://huggingface.co/Edoardo-BS/hubert-ecg-base)
- **ECGFounder**: a CNN of 33.8M parameters, trained with supervised (not SSL) learning on about 10M (10.7M) ECGs from HEEDB, a single site, covering 150 conditions. Weights released. The Harvard/MGH affiliation is not verified here. — [arXiv 2509.25095](https://www.arxiv.org/pdf/2509.25095); [FOUND-AF](https://arxiv.org/html/2608.03597)
- **ECG-JEPA**: a transformer of 87.2M parameters trained with a JEPA objective. — [FOUND-AF](https://arxiv.org/html/2608.03597)
- **Benchmarks:**
  - ECG FM rankings depend on the task. In FOUND-AF (atrial fibrillation), ECGFounder ranks first, ECG-JEPA and ST-MEM form the second tier, and HuBERT-ECG is lowest.
  - Elsewhere HuBERT-ECG is strong on PTB-XL. "Reality check" benchmark papers show FMs do not uniformly beat supervised baselines. — [FOUND-AF](https://arxiv.org/html/2608.03597); [Benchmarking ECG FMs: reality check](https://www.arxiv.org/pdf/2509.25095); [post-training strategy](https://arxiv.org/pdf/2509.12991); [rare-disease transfer](https://arxiv.org/pdf/2607.03009); [OpenECG 1.2M public records](https://arxiv.org/pdf/2503.00711)

**EEG models**
- **LaBraM**: about 2,500 hours from about 20 datasets. Variants Base, Large and Huge have 5.8M, 46M and 369M parameters. Method: VQ neural tokenizer plus masked token prediction (method from prior knowledge). ICLR 2024 per prior knowledge; venue not confirmed in this search. — [EEG FM critical review](https://arxiv.org/html/2507.11783v3)
- **CBraMod**: criss-cross spatial/temporal attention with masked reconstruction, on about 9,000 cleaned hours of TUEG and about 4–5M parameters. One source says 27,000 hours, which looks like an outlier. ICLR 2025 per prior knowledge. — [ResearchGate](https://www.researchgate.net/publication/386964759_CBraMod_A_Criss-Cross_Brain_Foundation_Model_for_EEG_Decoding); [review](https://arxiv.org/html/2507.11783v3)
- **EEGPT**: reported figures conflict. One source gives 25M parameters on about 246 hours from 5 datasets; others give 10M, or a 4.7M "Tiny" variant. — [search snippets via review/benchmarks](https://arxiv.org/html/2507.11783v3)
- **NeuroLM**: an LLM-based EEG model with up to 1.7B parameters (250M and 500M variants also exist), trained on about 25,000 hours. — [review](https://arxiv.org/html/2507.11783v3)
- **REVE** (NeurIPS 2025): masked autoencoding on more than 60,000 hours from 92 datasets. An audit counts 61,415 hours, 89 of the datasets named. Handles arbitrary electrode setups. Open code and weights. — [NeurIPS paper](https://papers.neurips.cc/paper_files/paper/2025/file/20a917f77773ac0fa8bea2bdd6606b66-Paper-Conference.pdf); [EmergentMind](https://www.emergentmind.com/papers/2510.21585)
- **LUNA**: topology-agnostic, scaling linearly with channel count, trained on more than 21,000 hours (TUEG plus Siena). Weights status unknown. **CSBrain**: cross-scale spatiotemporal model on about 9,000 hours of TUEG. — [arXiv 2606.20074](https://arxiv.org/pdf/2606.20074); [CSBrain](https://arxiv.org/pdf/2506.23075)
- Other EEG FMs named in the review: BrainBERT, Neuro-GPT, Brant, BIOT, EEGFormer, Mentality, FoME and BrainWave. Also ALFEE, MAGE, and LEAD (Alzheimer's).
  - 2026 work suggests "your vision FM is secretly an EEG FM" (2611.17031).
  - The EEGDash Corpus (2611.06356) offers a training-ready public EEG pretraining corpus.
  - Sources: [review](https://arxiv.org/html/2507.11783v3); [ALFEE](https://arxiv.org/pdf/2505.06291); [MAGE](https://arxiv.org/pdf/2611.09928); [LEAD](https://arxiv.org/html/2502.01678v4); [2611.17031](https://arxiv.org/pdf/2611.17031); [EEGDash](https://arxiv.org/pdf/2611.06356)
- **EEG benchmarks:** EEG-FM-Bench (2508.17742; v1 covers BIOT, BENDR, LaBraM, EEGPT and CBraMod; v2 adds CSBrain, REVE, Mantis and Moment, across 14 tasks), OmniEEG-Bench (10 FMs on 54 datasets), AdaBrain-Bench, EEG-Bench (ETH), and a negative-control protocol for clinical EEG FM benchmarks. — [EEG-FM-Bench](https://arxiv.org/html/2508.17742v2); [OmniEEG-Bench](https://arxiv.org/pdf/2606.00815); [AdaBrain-Bench](https://arxiv.org/pdf/2507.09882); [EEG-Bench](https://www.alphaxiv.org/abs/2512.08959.md); [negative-control](https://arxiv.org/pdf/2607.24519)

**Emotion/stress (brief, covered elsewhere)**
- Retrieval-augmented personalization with FMs for wearable stress detection (2606.24985). FEEL quantifies physiological heterogeneity for generalizable emotion recognition (2604.05926). NormWear and PaPaGei also report stress/affect downstream tasks (inferred from their task suites; not verified here). — [2606.24985](https://arxiv.org/pdf/2606.24985); [FEEL](https://arxiv.org/pdf/2604.05926)

### Inferences
- **SSL objectives by group:**
  - Contrastive learning dominates the PPG/ECG models trained on individual waveforms: Apple 2024, PaPaGei, Pulse-PPG and the WBM contrastive encoder.
  - Masked autoencoding / masked prediction dominates multi-channel minute-level wearable models (LSM, LSM-2, SensorFM, Samsung xMAE/HiMAE) and EEG models (LaBraM, CBraMod, REVE).
  - Cross-modal alignment (PPG↔ECG) is a 2025–26 growth area: AnyPPG, Biosignal Fingerprinting and xMAE.
- **Openness splits by organization.** Every big-tech model with the largest data (Apple, Google, Samsung) is closed. Open-weight models come from Nokia Bell Labs and academia.
- **PaPaGei is archived.** That may signal Nokia Bell Labs is stepping back from maintaining it. This is speculative.
- **Size gap.** Wearable FMs are small next to LLMs: typically 1M to 100M parameters, with EEG's NeuroLM at 1.7B as the outlier. The scale lever is data hours, not parameters.

### Gaps
- Could not fetch full papers (arxiv.org and research.google are blocked), so these are not verified:
  - parameter counts for LSM-2 and SensorFM;
  - whether Pulse-PPG has a total-hours figure;
  - LUNA and CSBrain weight availability;
  - Inertia-1 pretraining data scale and weights.
- **BIOT** (NeurIPS 2023, cross-data biosignal transformer; prior knowledge), **BENDR**, **Brant** and **Moment/Chronos-style general time-series FMs** applied to biosignals were not looked up in detail.
- **Apple's 2025–2026 follow-up models were not found on Apple ML Research.** This includes the claimed 213K-participant PPG FM extension and any PPG+accelerometer joint FM.
- **Google PH-LLM / the Fitbit personal health LLM / Gemini coach integration was not researched.** These are LLMs over wearable data, not sensor FMs proper.

## Q2. Which companies are productizing (Apple, Google/Fitbit, Samsung, Oura, WHOOP, Meta, Nokia Bell Labs; Japan)?

### Takeaway
- **Apple** ships PPG-ML features: Hypertension Notifications, Sept 2025.
- **Google** has the largest research model (SensorFM) but no announced product integration.
- **Samsung** positions HiMAE as on-device.
- **Meta's** sEMG wristband is the clearest consumer-interface use.
- **Oura and WHOOP:** no public FM papers found.
- **Japan:** no Japanese company or academic biosignal FM was found in this search.

### Cited Findings
- **Apple:** Hypertension Notifications use a PPG ML feature extractor plus linear models, for adults 22 and over (Sept 2025). — [Apple validation paper](https://www.apple.com/health/pdf/Hypertension_Notifications_Validation_Paper_September_2025.pdf). The research FMs come from the AHMS cohort (141K to 162K participants). — [arXiv 2312.05409](https://arxiv.org/pdf/2312.05409); [arXiv 2507.00191](https://arxiv.org/html/2507.00191v1)
- **Google:** SensorFM was trained only on Fitbit/Pixel Watch data. There is no public API, consumer feature or timeline. — [The Decoder](https://the-decoder.com/sensorfm/); [MarkTechPost](https://www.marktechpost.com/2026/07/10/google-research-introduces-sensorfm-a-wearable-health-foundation-model-pretrained-on-one-trillion-minutes-of-sensor-data/)
- **Samsung:** Samsung Research America's Digital Health team built xMAE and HiMAE. HiMAE is claimed at under 1 ms on a watch-class CPU, i.e. on-device. The work was promoted around Galaxy Unpacked (July 2026) and in Japanese PR in Sept 2026. Samsung also runs a cognitive-change study with UCSF Neuroscape using Galaxy Watch. — [AI News](https://www.artificialintelligence-news.com/news/samsung-health-ai-models-analyse-wearable-biosignal-data/); [ケータイ Watch](https://k-tai.watch.impress.co.jp/docs/news/2141045.html)
- **Oura:** launched a Brain Health Check-In with Cambridge Cognition that pairs cognitive tests with ring data (up to 45,000 members). No Oura FM paper was found. **WHOOP:** no FM source was found. — [AI News](https://www.artificialintelligence-news.com/news/samsung-health-ai-models-analyse-wearable-biosignal-data/)
- **Meta:** sEMG wristband generic models trained on thousands of participants and published in Nature in 2025. The wristband is understood to ship with Meta Ray-Ban Display glasses (prior knowledge, unverified here). — [The Register](https://www.theregister.com/2025/07/23/meta_wristband_ui_control/)
- **Nokia Bell Labs:** PaPaGei is open under BSD-3. The repository was archived in Sept 2026. — [GitHub](https://github.com/nokia-bell-labs/papagei-foundation-model)
- **Academic hubs:**
  - Stanford (OpenMHC);
  - UCLA, Duke and JHU (Inertia-1);
  - UCSD (NormWear);
  - Peking University (AnyPPG);
  - Google with the University of Washington (LSM);
  - USC with Apple (WBM). — sources above
- **Japan:**
  - The only items found are Samsung Electronics Japan's PR and a METI-supported wireless EEG-plus-vitals measurement device by Rexam (レクザム), Osaka University and PGV. That is hardware, not an FM. — [Kyodo PR](https://www.kyodo.co.jp/pr/2026-09-15_4035244/); [METI 中小企業庁](https://www.chusho.meti.go.jp/sapoin/index.php/cooperation/project/detail/5001)

### Inferences
- Productization is going mainly through two routes: (a) FM-derived embeddings feeding narrow regulated or notification features (Apple), and (b) FMs as a sensor-to-LLM "interface" for health coaching (Google SensorFM framing). On-device efficiency (Samsung HiMAE) is a differentiator.
- Japan looks like a white space for biosignal FMs, but that rests on one Japanese-language search and should be checked further.

### Gaps
- No primary sources were checked for WHOOP, Oura, Garmin, Huawei or Xiaomi FM efforts.
- Japanese players (Sony, Omron, NTT, Hitachi, NEC, Kyocera, PGV, university labs) were not searched individually, so absence is not proven.
- Whether Samsung or Google has shipped any FM-based feature by Nov 2026 is unconfirmed.

## Q3. Scaling laws for sensor data

### Takeaway
- **Google:** LSM-1 found that total hours matter more than the number of subjects, with diminishing returns between roughly 10^5 and 10^7 hours. LSM-2 reports that performance has not plateaued at 40M hours, and SensorFM pushed to about 2B hours from about 5M people.
- **EEG:** scaling is weak or unclear across model size and data diversity.
- **ECG:** systematic scaling studies emerged in 2026.

### Cited Findings
- LSM-1 established scaling laws for imputation, interpolation and extrapolation. Total hours matter more than subject count. Gains slow beyond about 10^5 hours and diminish around 10^7 hours. Larger models (ViT-110M) keep gaining beyond 1M hours. A secondary review puts saturation near 10^7 hours, so the summaries disagree. — [Google blog](https://research.google/blog/scaling-wearable-foundation-models/); [ICLR 2025](https://mlanthology.org/iclr/2025/narayanswamy2025iclr-scaling)
- LSM-2 keeps improving with more data and does not plateau, whereas LSM-1 appeared to level off. — [Google blog](https://www.research.google/blog/lsm-2-learning-from-incomplete-wearable-sensor-data/)
- SensorFM scales to more than 1 trillion minutes from about 5M people. — [MarkTechPost](https://www.marktechpost.com/2026/07/10/google-research-introduces-sensorfm-a-wearable-health-foundation-model-pretrained-on-one-trillion-minutes-of-sensor-data/)
- **EEG:**
  - The critical review reports unclear scaling between model size, data volume and performance. — [review](https://arxiv.org/html/2507.11783v3)
  - OmniEEG-Bench finds weak correlations between performance and pretraining diversity or model size. — [OmniEEG-Bench](https://arxiv.org/pdf/2606.00815)
  - A REVE retrain on its public subset reached comparable results. — [emergentmind](https://www.emergentmind.com/papers/2510.21585)
- **ECG:** "Pretraining Strategies and Scaling for ECG Foundation Models: A Systematic Study" (2605.12241). Findings not retrieved. — [arXiv](https://arxiv.org/pdf/2605.12241)
- **Accelerometer:** Inertia-1 studies the trade-off between sampling rate and pretraining. — [arXiv](https://arxiv.org/pdf/2607.06617)

### Inferences
- Clean scaling has been shown mainly on dense, minute-level, multi-channel consumer data at huge scale (Google). Public-data waveform FMs (EEG, PPG) do not show reliable scaling yet. This points to data quality, diversity and benchmark noise as the bottlenecks, not model size.

### Gaps
- No quantitative scaling exponents were retrieved.
- Apple's scaling results (if any) and the ECG scaling-study conclusions are unknown.

## Q4. Overall 2025–2026 trend direction

### Takeaway
The trends:
- Data scale is moving from 10^7 to 10^9+ hours at big tech.
- Missing-data-native pretraining (AIM).
- Behavior-level plus sensor-level fusion (WBM).
- Cross-modal PPG–ECG alignment.
- On-device efficiency.
- Coupling FMs to LLMs as an "interface".
- A strong 2026 counter-movement toward open, reproducible public datasets and benchmarks that show FMs do not uniformly beat supervised or general time-series baselines.

### Cited Findings
- **Missing-data robustness as a core design goal:** LSM-2's AIM. — [arXiv 2506.05321](https://arxiv.org/pdf/2506.05321)
- **Behavioral-level FMs complement raw-sensor FMs:** Apple's WBM. — [arXiv 2507.00191](https://arxiv.org/html/2507.00191v1)
- **Sensor FM as general intelligence plus an interface for LLM summaries:** Google SensorFM. — [Google blog](https://research.google/blog/sensorfm-towards-a-general-intelligence-and-interface-for-wearable-health-data/)
- **Open-science push:**
  - OpenMHC notes prior wearable FMs were built and evaluated only on proprietary data, and provides public reimplementations. — [OpenMHC](https://arxiv.org/html/2607.16235)
  - Inertia-1 runs a fully open comparison. — [Inertia-1](https://arxiv.org/pdf/2607.06617)
  - The EEGDash Corpus is a public pretraining corpus. — [EEGDash](https://arxiv.org/pdf/2611.06356)
  - OpenECG is a public benchmark of 1.2M records. — [OpenECG](https://arxiv.org/pdf/2503.00711)
- **Benchmark "reality checks":**
  - ECG FMs vary by task. — [2509.25095](https://www.arxiv.org/pdf/2509.25095)
  - EEG-specific FMs rarely beat general time-series FMs. This comes from an aggregator and is unverified. — [benchmarklist](https://benchmarklist.com/benchmarks/neuroatlas_benchmarking_foundation_models_for_clinical_eeg_and_brain_computer_interfaces/)
  - Proposals of negative-control protocols. — [2607.24519](https://arxiv.org/pdf/2607.24519)
- **Three survey-identified directions:** training from scratch on biosignals, adapting general time-series FMs, and multimodal LLMs. The survey also notes the field lacks a cohesive roadmap. — [TechRxiv survey](https://www.techrxiv.org/doi/10.36227/techrxiv.175606236.62808131)
- **Efficiency and specialization:** structured pruning with about 1% of parameters fine-tuned for PPG FMs (2610.33788), and HiMAE on-device. — [2610.33788](https://arxiv.org/html/2610.33788); [AI News](https://www.artificialintelligence-news.com/news/samsung-health-ai-models-analyse-wearable-biosignal-data/)
- **Device- and topology-agnostic models:** NormWear (channel-aware), REVE (any electrode setup), LUNA (topology-agnostic). — [ACM DL](https://dl.acm.org/doi/10.1145/3803808); [REVE](https://papers.neurips.cc/paper_files/paper/2025/file/20a917f77773ac0fa8bea2bdd6606b66-Paper-Conference.pdf)

### Inferences
- For a company without proprietary cohorts, the realistic path is one of these:
  - open-weight backbones (PaPaGei under BSD-3, AnyPPG, NormWear, ECG-FM, REVE), keeping licenses in mind: HuBERT-ECG is non-commercial;
  - public large cohorts (OpenMHC, once released);
  - parameter-efficient adaptation.
- Big tech's moat is data volume, not methods. OpenMHC-style reimplementations make the methods replicable.

### Gaps
- Not covered here: regulatory status (FDA/PMDA) of FM-derived features; the licenses of NormWear, AnyPPG and REVE; and whether OpenMHC data has actually been released by Nov 2026.
