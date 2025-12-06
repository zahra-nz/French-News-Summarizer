# French-News-Summarizer
### Abstractive & Extractive Text Summarization using Transformers

This project provides a complete **end-to-end French news summarization system** using both **abstractive** and **extractive** NLP techniques.
It is designed as a portfolio-quality project that demonstrates high-value real-world skills in **machine learning, NLP, deep learning, model evaluation, API development, and app deployment**.

---

## Project Overview

The goal of this project is to generate concise and high-quality summaries for French news articles using:

### **Abstractive Summarization**

* Fine-tuned Transformer models
* Candidate models: **mT5**, **BART French**, **T5-fr**
* Generates human-like rewritten summaries

### **Extractive Summarization**

* TextRank
* BERT embeddings + cosine similarity
* KeyBERT-based keyword scoring

A comparison of the two approaches is included, along with evaluation metrics.

---

## 📁 Repository Structure

```
french-news-summarizer/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_train_abstractive.ipynb
│   ├── 04_train_extractive.ipynb
│   └── 05_evaluation.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── preprocess.py
│   ├── train_abstractive.py
│   ├── train_extractive.py
│   ├── evaluate.py
│   └── utils.py
│
├── api/
│   └── main.py        # FastAPI
│
├── app/
│   └── app.py         # Streamlit UI
│
├── models/
│   ├── abstractive/
│   └── extractive/
│
├── requirements.txt
└── README.md
```

---

## Dataset

The project uses French news datasets such as:

### • **MLSUM (French split) – HuggingFace**

Contains:

* Article text
* Summary
* Headline

This dataset is high-quality and ideal for summarization tasks.

---

## Models Used

### **Abstractive**

| Model            | Notes                                |
| ---------------- | ------------------------------------ |
| mT5-small        | Fast, multilingual, great for French |
| BART-base-french | High-quality summarization model     |
| T5-fr            | Already adapted to French            |

### **Extractive**

* TextRank
* BERT embeddings + cosine similarity
* KeyBERT

---

## Evaluation

Metrics used:

* **ROUGE-1**
* **ROUGE-2**
* **ROUGE-L**
* **BLEU** (optional)

Evaluation notebooks are included in the `notebooks/` directory.

---

## API (FastAPI)

Endpoints:

* `POST /summarize_abstractive`
* `POST /summarize_extractive`
* `GET /healthcheck`

Example request:

```json
{
  "text": "Votre article ici..."
}
```

---

## Streamlit App

Features:

* Paste news article text
* Choose extractive or abstractive method
* View summary
* Compare both approaches
* Rouge score examples

Run locally:

```bash
streamlit run app/app.py
```

---

## Deployment

You can deploy the model/app to:

* **HuggingFace Spaces**
* **Render**
* **Railway**
* **Docker**
* **AWS / GCP**

The project is designed to run on CPU as well.

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/your-username/french-news-summarizer
cd french-news-summarizer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Contributing

Pull requests and suggestions are welcome!

---

---

## If you found this project useful, consider giving it a star!
