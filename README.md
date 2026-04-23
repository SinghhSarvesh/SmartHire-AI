# SmartHire-AI

![ML-powered](https://img.shields.io/badge/ML--powered-blue) ![Open Dataset](https://img.shields.io/badge/Open%20Dataset-green) ![NLP](https://img.shields.io/badge/NLP-purple) ![Similarity Scoring](https://img.shields.io/badge/Similarity%20Scoring-teal) ![Rule-based](https://img.shields.io/badge/Rule--based-orange)

A structured dataset of resumes and job descriptions for computing candidate–job similarity scores using machine learning and rule-based techniques. Designed for building, evaluating, and benchmarking AI-powered hiring pipelines.

---

## At a Glance

| Metric | Value |
|---|---|
| Candidate records | 12,000+ |
| Job descriptions | 3,400 |
| Parse accuracy | 98% |
| Scoring methods | 2 (ML + Rule-based) |

---

## What's Inside

### Structured Resume Data
Parsed fields including skills, work experience, education, certifications, and years of experience — extracted from raw resume text.

### Job Description Embeddings
Structured job descriptions with required skills, seniority level, domain tags, and precomputed vector embeddings for similarity search.

### Similarity Scores & Labels
Precomputed cosine similarity scores paired with human-reviewed fit labels (`Strong` / `Partial` / `Low`) for model training and evaluation.

---

## Schema

| Field | Type | Description |
|---|---|---|
| `candidate_id` | `string` | Unique identifier per resume |
| `skills` | `list[str]` | Extracted technical & soft skills |
| `experience_years` | `int` | Total years of work experience |
| `education_level` | `string` | Highest degree attained |
| `job_id` | `string` | Linked job description ID |
| `similarity_score` | `float` | Cosine similarity (0.0 – 1.0) |
| `fit_label` | `string` | `Strong` / `Partial` / `Low` — human-reviewed |

---

## Pipeline

```
01. Parse resume  →  02. Embed text  →  03. Score similarity  →  04. Rank & label
```

---

## Quick Start

```python
# load the dataset
from datasets import load_dataset

ds = load_dataset("smarthire-ai/main")

# compute cosine similarity
from sklearn.metrics.pairwise import cosine_similarity

score = cosine_similarity(candidate_vec, job_vec)
```

---

## Use Cases

- **Resume screening** — Automate shortlisting by ranking candidates against job requirements at scale.
- **Model benchmarking** — Evaluate NLP and embedding models against human-reviewed fit labels.
- **Bias analysis** — Audit scoring fairness across demographic groups and job categories.
- **ATS integration** — Use as training data to fine-tune fit prediction in applicant tracking systems.

---

## License

This dataset is released for research and non-commercial use. See [LICENSE](LICENSE) for details.
