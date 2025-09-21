# CORD-19 Abstracts Explorer

This project is a simplified data analysis of the [CORD-19 research dataset](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge), focusing on metadata of COVID-19 papers (titles, abstracts, and URLs).  
The goal was to practice **loading real-world data, cleaning it, analyzing text, and building an interactive Streamlit app** for exploration, but i downloaded a simple small covid abstract  from [covid abstract csv](https://www.kaggle.com/datasets/anandhuh/covid-abstracts?select=covid_abstracts.csv)  to work with. 

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Henri2611/plp_python-assignment.git
cd plp_python-assignment/Python-week8
```

### 2. Install dependencies
```
pip install -r requirements.txt
 ```
### 3. Run the Jupyter Notebook
```
pip install -r requirements.txt

```
### 📂 Files in this Repo
```
Frameworks_Assignment/
├─ covid/
│  ├─ covid_abstracts.csv    # original dataset (10,000 rows)
│  └─ metadata_clean.csv     # cleaned dataset (produced in notebook)
├─ notebook.ipynb             # full step-by-step analysis
├─ app.py                     # interactive Streamlit app
├─ requirements.txt           # required Python packages
└─ README.md                  # project documentation

```

### 🔎 Brief Findings

Abstract word counts: Most abstracts range between 150–250 words, with some much longer.

Top sources/domains: Data came primarily from pubmed.ncbi.nlm.nih.gov, with some from other domains.

Frequent words in titles: Common words include vaccine, risk, infection, patients, impact, care.

Dataset limitation: This simplified version lacks publication dates and journal names, so year-wise or journal-wise analysis was not possible.

⚠️ Limitations & Next Steps
---

Limitations

No publish_time or journal columns → can’t analyze publications by year or journal.

Some abstracts truncated.

Only includes a subset (10k rows) of the full dataset.

Next Steps

Enrich data with additional metadata (publication year, journal, authors).

Normalize journal names and domains for consistency.

Perform topic modeling (e.g., LDA) on abstracts.

Add keyword search/filtering in Streamlit app.


✨ Reflection
---
What I learned

How to load and explore messy real-world datasets with pandas.

How to clean and transform text fields (word counts, tokenization, stopword removal).

How to visualize distributions and categorical counts with matplotlib/seaborn.

How to build a simple Streamlit dashboard for interactive data exploration.

Challenges

The dataset lacked important fields like publication dates and journal names.

Needed to adapt the assignment by focusing on text analysis and URL domains instead.

Next Steps

Add richer metadata to enable more traditional analyses (year, journals, authors).

Explore NLP techniques for deeper insights (topic modeling, sentiment).

### 📝 Requirements

Minimal requirements.txt:

pandas
matplotlib
seaborn
streamlit
scikit-learn

### Generate full requirements (optional):

```
pip freeze > requirements.txt
```
### ✅ Repo Tips

Keep app.py in the root directory, not inside covid/.

Place datasets inside covid/.

Always commit both raw (covid_abstracts.csv) and cleaned (metadata_clean.csv) versions for reproducibility.
