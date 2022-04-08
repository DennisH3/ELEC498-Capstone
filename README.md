# ELEC498-Capstone
Repository to store ML code for Recognize.ai project

Recognize.ai is an NLP application that recognizes instances of poor mental health from social media, specifically Reddit, text. In these cases, the application will reach out to users and provide resources they can use. A REST API and UI will be developed to apply this algorithm to live data.

# Data
The data used for this project can be found [here](https://drive.google.com/drive/folders/1u5PmvN_KHCHog4NhvUSrVQYDNFiQgniX)

# Files

## Collection
Contains Pushshift API code to collect Reddit data on select subreddits

## Preprocessing
Contains basic preprocessing and text preprocessing Jupyter notebooks
- train_test_split.ipynb: splits the preprocessed data into training and testing data sets
- Doc2vec.ipynb: example Doc2vec model on some of the collected data

## Clustering
Clustering results with different feature sets, namely just TF-IDF, just Doc2vec, and both TF-IDF and Doc2vec features. Labels are also inverted to check which cluster is the better fit.
The results are in clustering_results_analysis_final.ipynb

## Models
Contains models used for this project:
- FastText
- GPT-2
- XLNet
- Random Forest
- Support Vector Classifier
The results for these models can be seen in classification_results.ipynb, RFC.ipynb, and SVM.ipynb

# Team Members
Nick Gagan – 20068337
Dennis Huynh – 20056402
Christopher Salomons – 20061276
Randy Lee - 20079451