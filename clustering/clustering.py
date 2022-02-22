import string
import collections

import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
STOPWORDS = set(stopwords.words('english'))

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from sklearn.cluster import KMeans
from sklearn.cluster import Birch
from sklearn.feature_extraction.text import TfidfVectorizer
from pprint import pprint
import hdbscan

def process_text(text, stem=True):
    text = text.translate(str.maketrans('','',string.punctuation))
    tokens = word_tokenize(text)
    if stem:
        stemmer = PorterStemmer()
        tokens = [stemmer.stem(t) for t in tokens]
    return tokens

def cluster_texts_hdbscan(texts, clusters):
    vectorizer = TfidfVectorizer(tokenizer=process_text,
                                 stop_words=stopwords.words('english'),
                                 max_df=0.5,
                                 min_df=0.1,
                                 lowercase=True)
    tfidf_model = vectorizer.fit_transform(texts)
    clusterer = hdbscan.HDBSCAN(clusters)
    label = clusterer.fit_predict(tfidf_model)
    return clusterer.labels_
 
def cluster_texts_kmeans(texts, clusters=3):
    vectorizer = TfidfVectorizer(tokenizer=process_text,
                                 stop_words=stopwords.words('english'),
                                 max_df=0.5,
                                 min_df=0.1,
                                 lowercase=True)
    tfidf_model = vectorizer.fit_transform(texts)
    kmeans = KMeans(clusters, random_state=0).fit(tfidf_model)
    return kmeans.labels_
 
def cluster_texts_birch(texts, clusters):
    vectorizer = TfidfVectorizer(tokenizer=process_text,
                                 stop_words=stopwords.words('english'),
                                 max_df=0.5,
                                 min_df=0.1,
                                 lowercase=True)
    tfidf_model = vectorizer.fit_transform(texts)
    birch = Birch(clusters).fit(tfidf_model)
    return birch.labels_
  
if __name__ == "__main__":
  df = pd.read_csv('')
  text = df["text"].tolist()

  clusters = cluster_texts_hdbscan(text, 3)
  print(clusters)
  clusters = cluster_texts_kmeans(text, 3)
  print(clusters)
  clusters = cluster_texts_birch(text, 3)
  print(clusters)