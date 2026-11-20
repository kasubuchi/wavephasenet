# How Well Biosignal Foundation Models Transfer to Emotion, Affect and Stress Recognition (as of Nov 2026)

> **Method note (read first):** This session could not open arxiv.org, eurekalert.org or themoonlight.io directly (DNS blocked). So every number below comes from search-engine extracts of the papers' text and tables, not from tables I read myself. Several extracts were garbled, and the search tool itself flagged column-alignment problems in some of them. I attach a confidence level to each number. Before quoting a number externally, check it against the original PDF. Several arXiv IDs are from 2026 (26xx.xxxxx); I report what the search results showed and could not check them independently.

## Q1. Which FM papers evaluate on affect/stress datasets, and what metrics vs. baselines?

### Takeaway
- **EEG (strongest evidence):** foundation models such as CBraMod and LaBraM are routinely tested on FACED, SEED, SEED-IV, SEED-V and DEAP. They beat earlier EEG foundation models by small margins, but absolute performance on cross-subject emotion stays low: SEED-V 5-class kappa is about 0.25 and FACED 9-class kappa about 0.50.
- **PPG:** foundation models are tested mostly on WESAD stress. Pulse-PPG, which was pretrained on field data, consistently comes out on top, and PaPaGei lags.
- **Multimodal wearable models (Google LSM-2, NormWear):** they report stress or anxiety tasks but give few public numbers specific to affect.

### Cited Findings
**EEG foundation models**
- CBraMod (ICLR 2025) evaluates on FACED (9-class) and SEED-V (5-class) and reports state-of-the-art results on both. Its Cohen's kappa vs. the best baseline, LaBraM: **0.5041 vs. 0.4698 on FACED** and **0.2569 vs. 0.2386 on SEED-V**. — [CBraMod arXiv](https://arxiv.org/html/2412.07236v2); [ICLR 2025 PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/bbbd6d915cb90be21c1254a82d45cedd-Paper-Conference.pdf) (confidence: high; the text states these numbers explicitly)
- Baseline rows in the CBraMod tables (moderate confidence, from table extracts):
  - LaBraM: FACED balanced accuracy 0.5273 / kappa 0.4698; SEED-V balanced accuracy 0.3976 / kappa 0.2386.
  - BIOT: FACED balanced accuracy 0.5118 / kappa 0.4476; SEED-V balanced accuracy 0.3837 / kappa 0.2261.
  - CBraMod variant: FACED balanced accuracy about 0.551 / kappa 0.504.
  — [OpenReview PDF](https://openreview.net/notes/edits/attachment?id=jG9IatiQoT&name=pdf)
- CBraMod used the 16-subject open release of SEED-V, while LaBraM used the 20-subject private release. The SEED-V numbers in the two papers are therefore not directly comparable. — [CBraMod arXiv](https://arxiv.org/html/2412.07236v2)
- A third-party leaderboard lists SEED-V results as CBraMod 40.29 balanced accuracy / 0.257 kappa and LaBraM 40.1 / 0.2563, so the two are almost tied. — [SOTA2 SEED-V leaderboard](https://www.sota2.com/research/sota/emotion-recognition-on-seed-v-balanced-accuracy-cohen-s-kappa) (low–moderate confidence; aggregator site)
- In EEG-FM-Bench, CBraMod gets SEED balanced accuracy 70.83±0.28 (3-class). — [EEG-FM-Bench, ResearchGate](https://www.researchgate.net/publication/394940447_EEG-FM-Bench_A_Comprehensive_Benchmark_for_the_Systematic_Evaluation_of_EEG_Foundation_Models); [arXiv 2508.17742](https://arxiv.org/pdf/2508.17742)
- **OmniEEG-Bench (2026):**
  - Scope: 10 EEG foundation models (BENDR, BIOT, LaBraM, CBraMod, BrainOmni, FEMBA, Neuro-GPT, NeuroLM, EEGMamba, REVE) across 54 datasets. Emotion is covered by DEAP (binary valence/arousal), the SEED family (3–7 classes) and FACED.
  - Primary protocol: linear probing.
  - Under full fine-tuning the top three by average rank are CBraMod 4.51, LaBraM 4.88 and FEMBA 5.42. CBraMod is described as especially strong on cognition and emotion.
  - Conclusion: frozen representations remain limited under linear probing.
  — [OmniEEG-Bench](https://arxiv.org/html/2606.00815v1)
- "LaBraM at Scale" (2611.03165) follows the OmniEEG-Bench protocol. The extract shows CBraMod at SEED 57.32 (fine-tuning) / 54.02 (linear probe), SEED-IV 25.66 / 32.49 and SEED-V 26.53 / 23.92. — [LaBraM at Scale](https://arxiv.org/html/2611.03165) (**low confidence:** column labels were ambiguous in the extract. SEED-IV is 4-class, so ~25% would be near chance.)
- **EEG-FM-Compass** (formerly "EEG Foundation Models: Progresses, Benchmarking, and Open Problems"; published in National Science Review 2026):
  - Scope: 12 open-source EEG foundation models plus specialist models trained from scratch, across 13 datasets and 9 paradigms, including emotion. Settings cover cross-subject generalization and few-shot adaptation.
  - Full fine-tuning beats linear probing for almost all models.
  - Specialist models trained from scratch remain competitive and often match or beat fine-tuned foundation models.
  - I did not get a breakdown of the emotion results specifically.
  — [NSR article](https://academic.oup.com/nsr/advance-article/doi/10.1093/nsr/nwag466/8750569); [arXiv 2601.17883](https://arxiv.org/html/2601.17883v3)
- MSBraM (2026) slightly beats CBraMod-small on SEED-V but trails it on FACED. — [MSBraM](https://arxiv.org/pdf/2607.21402)
- Specialist (non-foundation) emotion models report much higher cross-subject numbers. For example, an EmotionCLIP-style contrastive method reports 88.69% cross-subject accuracy on SEED (3-class). — [Cross-domain EEG ER with contrastive learning](https://arxiv.org/html/2511.05293v2) (protocols differ, so this is not directly comparable)

**PPG foundation models**
- Pulse-PPG (open source, pretrained on field data): on WESAD binary stress, logistic regression on its frozen features reaches **F1 0.8759** vs. 0.4065 for a naive model. On WESAD 4-class affect it is much weaker; one comparison shows ResNet-26 at F1 0.1998 there. — [Pulse-PPG](https://arxiv.org/pdf/2502.01108) (moderate confidence; the search summary of the 4-class comparison was ambiguous)
- A 2026 paper on a PPG foundation model trained with multimodal physiological supervision (2606.07365) reports WESAD stress, 2-class, as MF1 / Acc / AUC:

  | Model | MF1 | Acc | AUC |
  |---|---|---|---|
  | Pulse-PPG | 0.81 | 0.86 | 0.92 |
  | PaPaGei-P | 0.65 | 0.79 | 0.80 |
  | PaPaGei-S | 0.67 | 0.78 | 0.76 |
  | Proposed model | 0.83 | 0.88 | 0.94 |

  Within-subject scores are higher than across-subject ones (stress 0.90 vs. 0.83). — [arXiv 2606.07365](https://arxiv.org/html/2606.07365v1)
- In the SIGMA-PPG comparison, Pulse-PPG remains the best model for both stress and emotion on WESAD, against PaPaGei, AnyPPG and GPT-PPG. — [SIGMA-PPG](https://arxiv.org/html/2601.21031v1)
- **PPG-Bench (2026), emotion balanced accuracy:** AnyPPG .515, Pulse-PPG .465, PaPaGei-S .387, PaPaGei-P .365. The ranking differs from the WESAD stress papers. — [PPG-Bench](https://arxiv.org/html/2610.13435) (moderate confidence; I could not confirm the exact dataset and protocol)
- Apple's PPG/ECG foundation model was trained on about 141K Apple Watch users with contrastive learning. It is closed source, and I found no public results on affect or stress. — [Large-scale Training of FMs for Wearable Biosignals](https://arxiv.org/html/2312.05409v1)

**Multimodal wearable foundation models**
- **Google LSM-2** (with Adaptive and Inherited Masking): with only a linear probe it outperforms supervised baselines on binary **anxiety** and hypertension classification, and is the best self-supervised method there. The labels come from the Metabolics study, about 1,250 labeled users. Removing nighttime biosignals lowered anxiety and hypertension accuracy. — [Google Research blog](https://research.google/blog/lsm-2-learning-from-incomplete-wearable-sensor-data/); [ResearchGate](https://www.researchgate.net/publication/392466785_LSM-2_Learning_from_Incomplete_Wearable_Sensor_Data) (I did not get the exact numbers.)
- LSM is trained on aggregated per-minute features, not raw waveforms; the pretraining scale cited is 40M hours from 165K people. — [StressLLM (NSF PAR)](https://par.nsf.gov/servlets/purl/10665612)
- **NormWear:**
  - Pretraining: PPG, ECG, EEG, GSR and IMU.
  - Evaluation: 18 downstream tasks under linear probing and zero-shot inference (through text alignment), compared against baselines including Chronos.
  - Venue: ACM Transactions on Computing for Healthcare, 2026.
  - WESAD: the extract suggests NormWear-Medium ≈74 vs. a Chronos row ≈66, but the column alignment is unclear.
  — [ACM DL](https://dl.acm.org/doi/10.1145/3803808); [arXiv](https://arxiv.org/html/2412.09758v1) (low confidence on these numbers)

### Inferences
- **EEG:** foundation models beat each other by about 1–3 points of kappa or balanced accuracy on emotion. In absolute terms, cross-subject emotion decoding stays weak: SEED-V 5-class balanced accuracy is about 40%.
- **PPG:** the domain of the pretraining data seems to matter for stress more than model size or design. Pulse-PPG was pretrained on field data and beats PaPaGei, which was pretrained on clinical data. This is my interpretation of the consistent ranking across papers, not a finding any paper states.
- **Binary vs. multi-class:** binary stress on WESAD is close to solved (F1 above 0.8). Finer-grained affect (4-class, valence/arousal) stays poor for every model.

### Gaps
- I could not get per-model emotion tables from OmniEEG-Bench or EEG-FM-Compass because arXiv was blocked. Of particular interest is whether specialist from-scratch models such as EEGNet or Conformer beat the foundation models on emotion specifically.
- I did not get exact LSM-2 anxiety numbers.
- I found no foundation-model results on CASE, AMIGOS, MAHNOB-HCI or DREAMER, except BrainGPT, which uses DREAMER as a held-out dataset (see Q5).
- I found no published affect results for Apple's model, LSM-1 or SensorLM.

## Q2. Label efficiency, few-shot, cross-subject generalization, and personalization

### Takeaway
Claims that foundation models are label-efficient mostly come from non-affect tasks, such as activity recognition and health endpoints. The evidence specific to affect is thin and mixed. Cross-subject generalization remains the main bottleneck, and personalization still helps.

### Cited Findings
- **LSM (Scaling Wearable Foundation Models):** reports high label efficiency, but its few-shot evaluation is on activity recognition, not emotion. — [arXiv 2410.13638](https://arxiv.org/pdf/2410.13638)
- **SensorFM (2026):** reports few-shot label efficiency on health endpoints, not emotion. — [SOTA Papers summary](https://www.sotapapers.com/article/2026/07/sensor-foundation-model-scales-across-wearable-health-tasks-2605-22759)
- **FEEL (2026):** quantifies how heterogeneous physiological emotion recognition data is across datasets.
  - Label regimes tested: few-shot (5% of labels), low-resource (25%) and partial-participant (50%).
  - Zero-shot CLSP (contrastive language–signal pretraining) models are sometimes best on EDA.
  - Results vary widely by dataset and modality.
  — [FEEL](https://arxiv.org/html/2604.05926)
- **Within- vs. across-subject:** in the PPG multimodal-supervision paper, within-subject stress scores (0.90) are higher than across-subject ones (0.83). — [arXiv 2606.07365](https://arxiv.org/html/2606.07365v1)
- **Retrieval-augmented personalization** (Simon & Chetouani, 2026, ACM DOI 10.1145/3776591.3836729):
  - Method: frozen, out-of-domain foundation models retrieve similar segments from a user's history. These form a personalized embedding that modulates a lightweight transformer, replacing per-user fine-tuning.
  - Using only the user's own prior samples performs almost as well as full intra-user retrieval.
  - Cold start: retrieving from K-EmoCon to WESAD comes close to the non-personalized baseline and beats inter-user retrieval within WESAD.
  - The authors note that WESAD (15 subjects) is too small to pretrain user embeddings.
  - I did not get the exact gain figures.
  — [arXiv 2606.24985](https://arxiv.org/abs/2606.24985)
- **OmniEEG-Bench** includes cross-subject transfer and few-shot label-efficiency settings. — [OmniEEG-Bench](https://arxiv.org/html/2606.00815v1)
- **EEG-FM-Compass** evaluates cross-subject and few-shot settings and finds that specialist models remain competitive. — [NSR](https://academic.oup.com/nsr/advance-article/doi/10.1093/nsr/nwag466/8750569)

### Inferences
- I found no evidence that foundation models remove the need for personalization in affect recognition. The newest work, the 2026 retrieval-augmented personalization paper, keeps the foundation model frozen and still adds a personalization step. That suggests the field is treating foundation models as a feature extractor plus a personalization layer, not as a replacement for personalization.

### Gaps
- I found no published learning curves for emotion (accuracy vs. % labels) that compare foundation models with handcrafted HRV/EDA features plus a random forest. FEEL may contain them, but I could not open its tables.
- I found no quantified evidence that foundation models reduce the number of calibration samples needed per user for affect.

## Q3. Do general-purpose LLMs or time-series foundation models (Chronos, MOMENT, etc.) work for affect from physiology?

### Takeaway
- **LLMs on raw or summarized signals:** weak at zero-shot stress detection, with some improvement from few-shot prompting.
- **Generic time-series foundation models:** their frozen embeddings can do reasonably well on WESAD binary stress, but the evidence comes from low-rigor sources.
- **Specialized physiological foundation models:** in NormWear's comparison, they seem to beat Chronos-style models.

### Cited Findings
- **StressLLM (NSF PAR):**
  - Tested GPT-4, GPT-3.5 and others on WESAD with zero-shot, few-shot and chain-of-thought prompting.
  - Zero-shot accuracy was very low when the ground truth was "no stress"; few-shot generally did better.
  - I did not get the exact GPT-4 figure.
  — [StressLLM](https://par.nsf.gov/servlets/purl/10665612)
- **Mental-health forecasting from smartphone sensing (2026):** a comparison of classical ML, deep learning and LLMs. — [arXiv 2601.03603](https://arxiv.org/pdf/2601.03603) (details not retrieved)
- **Hackathon project (2026, low rigor):** MOMENT-1-base frozen embeddings reach macro-F1 0.90 ± 0.04 over 5 folds on WESAD stress. — [GitHub nealp](https://github.com/nealp/foundationalModelsForWearableTech) (indicative only; I could not verify the leakage controls)
- **bioRxiv 2026 preprint:** compares zero-shot and fine-tuned Amazon Chronos on WESAD EDA against a BiLSTM and TabPFN, with subject-independent cross-validation. — [bioRxiv](https://www.biorxiv.org/content/10.64898/2026.07.24.740621v2.full.pdf) (numbers not retrieved)
- **Generalist vs. specialist time-series foundation models on PPG health tasks:** a dedicated comparison paper exists. — [arXiv 2510.14254](https://arxiv.org/pdf/2510.14254) (affect results not retrieved)
- **NormWear:** includes Chronos-type baselines, and the WESAD extract suggests NormWear is ahead (≈74 vs. ≈66; low confidence). — [NormWear arXiv](https://arxiv.org/html/2412.09758v1)
- **For reference, non-foundation-model WESAD results:**
  - The original WESAD paper reports up to about 93% binary accuracy.
  - A CNN-LSTM on chest signals reaches about 92% binary accuracy under leave-one-subject-out evaluation (personal repo).
  — [GitHub Praruj](https://github.com/Praruj/stress-detection)

### Inferences
- WESAD binary stress is close to saturated even for simple models. So the claim that "time-series foundation model X works" on WESAD binary stress does not tell us much. Transfer is better judged on harder affect tasks (valence/arousal, field data).

### Gaps
- I found no rigorous peer-reviewed benchmark of Chronos, MOMENT or TimesFM on multi-class emotion datasets such as DEAP, CASE or AMIGOS.
- I did not retrieve SensorLM or Health-LLM results on stress.

## Q4. Known limitations specific to affective use

### Takeaway
The main open problems are:
- small datasets, which also differ in how emotion is labeled;
- leakage, both between pretraining and evaluation data and between subjects;
- evaluation protocols that are not comparable across papers;
- frozen embeddings that perform poorly, so full fine-tuning is needed, which costs more;
- a gap between lab-elicited stress and stress in daily life.

### Cited Findings
- **Pretraining–evaluation leakage:** LaBraM uses SEED during pretraining, so EMOD excludes LaBraM's SEED results for fairness. — [EMOD](https://arxiv.org/pdf/2511.05863)
- **Subject splits:** EEG-FM-Bench enforces subject-independent splits and notes that subject-dependent splits inflate metrics. — [EEG-FM-Bench](https://www.researchgate.net/publication/394940447_EEG-FM-Bench_A_Comprehensive_Benchmark_for_the_Systematic_Evaluation_of_EEG_Foundation_Models)
- **Terminology:** LibEER notes that "subject-independent" and "cross-subject" are used interchangeably in prior work, which muddies comparisons. — [LibEER](https://arxiv.org/pdf/2410.09767)
- **Dataset variants:** different releases of the same dataset (SEED-V with 16 vs. 20 subjects) block direct comparison. — [CBraMod](https://arxiv.org/html/2412.07236v2)
- **Label schemes:** DEAP labels emotion on continuous dimensions (valence/arousal), while SEED and FACED use discrete emotion categories. This complicates joint pretraining and transfer. — [mdJPT](https://arxiv.org/pdf/2510.22197)
- **Channel layouts:** SEED has 62 EEG channels and DEAP has 32, so unifying them needs a channel schema. — [Universal pretraining 2511.08444](https://arxiv.org/html/2511.08444)
- **Stressor type matters:** cross-dataset stress generalization depends on what kind of stressor was used. — [Stressor Type Matters!](https://arxiv.org/pdf/2405.09563)
- **Physiological heterogeneity across datasets** limits how well emotion recognition generalizes. — [FEEL](https://arxiv.org/html/2604.05926)
- **Small datasets:** WESAD has 15 subjects, too few to pretrain user embeddings. — [RAG personalization](https://arxiv.org/abs/2606.24985)
- **Frozen embeddings are weak:** under linear probing, EEG foundation model representations stay limited. — [OmniEEG-Bench](https://arxiv.org/html/2606.00815v1); [EEG-FM-Compass](https://arxiv.org/html/2601.17883v3)
- **On-device compute:** PPG-Distill distils PPG foundation models for efficiency. — [PPG-Distill](https://arxiv.org/html/2509.19215v1) (I did not get affect-specific numbers.)
- **Missing data in the wild:** LSM-2 is designed for incomplete real-world wearable data; nighttime data matters for anxiety. — [Google blog](https://research.google/blog/lsm-2-learning-from-incomplete-wearable-sensor-data/)
- **Benchmark-identity shortcuts:** a negative-control protocol for clinical EEG foundation-model benchmarks tests whether models exploit dataset identity. — [arXiv 2607.24519](https://arxiv.org/pdf/2607.24519) (clinical, not affect; included as related methodology)

### Inferences
- Results reported by foundation-model authors on SEED and FACED are probably optimistic relative to deployment, for three reasons:
  - possible overlap between pretraining and evaluation data;
  - lab elicitation with film clips;
  - labels assigned per stimulus rather than per person.
- I found no source that directly quantifies the validity of emotion labels, demographic bias, or the on-device latency and energy cost of affect foundation models. These need to be raised as known unknowns.

### Gaps
- Bias and fairness audits of affect foundation models (by sex, age, skin tone for PPG): none found.
- Quantified lab-to-field transfer for affect foundation models: none found. Pulse-PPG claims to work in both lab and field, but I found no affect-specific field-validation numbers.

## Q5. Affect-specific foundation models and emotion-focused pretraining (2025–2026)

### Takeaway
Since late 2025 a cluster of EEG emotion-specific pretraining efforts has appeared. They pool many emotion EEG datasets and report large gains over general EEG foundation models in their own evaluations. As of the end of 2026 I found no peer-reviewed independent benchmark confirming those gains.

### Cited Findings
- **mdJPT** (multi-dataset joint pretraining of emotion EEG):
  - Transfers from DEAP to the SEED family and FACED.
  - Claims to beat the second-best model, EEGPT, by **17.05%** on SEED.
  — [arXiv 2510.22197](https://arxiv.org/pdf/2510.22197)
- **Universal pretraining across heterogeneous emotion EEG datasets** ("One Model for All"):
  - Pretrains on SEED, DEAP and DREAMER with a unified channel schema.
  - Claims significant transfer to datasets not seen in pretraining.
  — [arXiv 2511.08444](https://arxiv.org/html/2511.08444)
- **EMOD:**
  - Pretrained on 8 public EEG emotion datasets with contrastive learning guided by valence/arousal.
  - Evaluated on FACED, SEED-V and SEED.
  - Removing temporal tokens lowers FACED by 4.49% and SEED-V by 2.05%.
  — [arXiv 2511.05863](https://arxiv.org/pdf/2511.05863)
- **BrainGPT** (autoregressive EEG generalist foundation model):
  - Evaluates emotion on DEAP, FACED, SEED-IV and SEED-V.
  - DREAMER is held out of pretraining and tested as 4-class (high/low valence × arousal).
  — [arXiv 2410.19779](https://arxiv.org/html/2410.19779v2)
- **Other emotion-focused models:** EEG-FM-Compass lists emotion-focused foundation models such as mdJPT and MEET. — [arXiv 2601.17883](https://arxiv.org/html/2601.17883v3)
- **Physiological emotion with language alignment:** FEEL evaluates CLSP models, which can do zero-shot emotion recognition. — [FEEL](https://arxiv.org/html/2604.05926)
- **Non-foundation-model cross-dataset adaptation remains active:**
  - [Source-free UDA 2606.28202](https://arxiv.org/pdf/2606.28202)
  - [PRISM 2607.00358](https://arxiv.org/pdf/2607.00358)
  - [Graph learning cross-population 2609.22103](https://arxiv.org/pdf/2609.22103)

### Inferences
- The trend is toward pretraining on data from a single domain (emotion EEG only), not on general EEG. This implies the field believes general EEG foundation models transfer only modestly to emotion, which matches the low SEED-V and FACED absolute scores in Q1.
- Gains like "+17% vs. EEGPT" are measured against general foundation models under the authors' own protocols. They need independent replication, for example in OmniEEG-Bench.

### Gaps
- I found no affect-specific peripheral-signal foundation model (PPG + EDA + skin temperature pretrained on emotion data) with a public benchmark, beyond CLSP-type models in FEEL.
- I found no evidence that any affect foundation model has been validated in the field or deployed on a device.
