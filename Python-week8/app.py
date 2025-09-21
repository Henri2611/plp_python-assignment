# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.parse import urlparse
from collections import Counter
import re

st.set_page_config(layout="wide")
st.title("CORD-19 Data Explorer (customized)")
st.write("Exploration of your simplified `covid/covid_abstract.csv` dataset")

@st.cache_data
def load_data(path="covid/metadata_clean.csv"):
    df = pd.read_csv(path, dtype=str)

    # Word counts
    df['title_word_count'] = df['title'].fillna("").astype(str).apply(lambda x: len(x.split()))
    df['abstract_word_count'] = df['abstract'].fillna("").astype(str).apply(lambda x: len(x.split()))

    # Domain from URL
    df['domain'] = df['url'].apply(lambda x: urlparse(str(x)).netloc if pd.notna(x) else "Unknown")

    return df

df = load_data()

# Domain filter
domains = ['All'] + list(df['domain'].value_counts().head(15).index)
domain_choice = st.sidebar.selectbox("Filter by domain (top 15)", domains)

# Apply filter
df_view = df.copy()
if domain_choice != 'All':
    df_view = df_view[df_view['domain'] == domain_choice]

#Summary stats
st.header("Summary statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Papers (in view)", len(df_view))
col2.metric("Avg abstract words", int(df_view['abstract_word_count'].mean() if len(df_view) > 0 else 0))
col3.metric("Avg title words", int(df_view['title_word_count'].mean() if len(df_view) > 0 else 0))

#Abstract length distribution
st.header("Distribution of Abstract Lengths")
fig, ax = plt.subplots()
sns.histplot(df_view['abstract_word_count'], bins=50, kde=True, ax=ax)
ax.set_xlabel("Number of words in abstract")
ax.set_ylabel("Number of papers")
st.pyplot(fig)

# Top domains
st.header("Top Domains (sources)")
top_domains = df_view['domain'].value_counts().head(15)
fig, ax = plt.subplots()
sns.barplot(y=top_domains.index, x=top_domains.values, ax=ax)
ax.set_xlabel("Number of papers")
ax.set_ylabel("Domain")
st.pyplot(fig)

# Frequent words in titles
st.header("Frequent Words in Titles")
titles = df_view['title'].fillna("").astype(str)
stopwords = set(['the','and','of','in','a','for','on','with','to','from','by','an',
                 'is','are','using','use','at','via','study','studies',
                 'covid','covid-19','covid19','sars-cov-2','sars','coronavirus'])
words = Counter()
pattern = re.compile(r"[A-Za-z0-9']+")
for t in titles:
    for w in pattern.findall(t.lower()):
        if w in stopwords or len(w) <= 2:
            continue
        words[w] += 1
common_words = words.most_common(15)

if common_words:
    word_df = pd.DataFrame(common_words, columns=["Word", "Count"])
    fig, ax = plt.subplots()
    sns.barplot(y="Word", x="Count", data=word_df, ax=ax)
    st.pyplot(fig)
else:
    st.write("No words found.")

# Sample papers 
st.header("Sample Papers")
st.dataframe(df_view[['title','abstract','url']].head(50))
