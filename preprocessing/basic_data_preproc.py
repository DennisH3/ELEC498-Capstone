#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Imports
import pandas as pd
import os


# In[2]:


"""
Desc: Basic preprocessing function
Input: f (string) - file name
Output: Cleaned csv file saved to clean_data folder
        and prints basic statistics to console
"""
def basic_data_preproc(f):
    
    try:
        # Load submissions
        df = pd.read_csv(f, 
                         usecols = ['id', 'author', 'created_utc', 'link_flair_text', 'num_comments',
                                    'score', 'selftext', 'subreddit', 'title', 'total_awards_received'])
    except:
        try:
             # Load submissions (data was missing link_flair_text)
            df = pd.read_csv(f, 
                             usecols = ['id', 'author', 'created_utc', 'num_comments',
                                        'score', 'selftext', 'subreddit', 'title', 'total_awards_received'])

            df['link_flair_text'] = ""
        except:
             # Load submissions (data was missing total_awards_received)
            df = pd.read_csv(f, 
                             usecols = ['id', 'author', 'created_utc', 'link_flair_text', 'num_comments',
                                        'score', 'selftext', 'subreddit', 'title'])

            df['total_awards_received'] = 0

    # Remove rows with deleted authors and deleted/removed selftext
    df = df[df['author'] != "[deleted]"]
    df = df[df['selftext'] != "[deleted]"]
    df = df[df['selftext'] != "[removed]"]

    # Keep rows in created_utc if it is int
    df = df.loc[df['created_utc'].apply(type) == int]

    # Replace NaNs in selftext, title, and link_flair with empty string
    df['selftext'] = df['selftext'].fillna("")
    df['title'] = df['title'].fillna("")
    df['link_flair_text'] = df['link_flair_text'].fillna("")

    # Replace NaNs in total_awards_received with 0
    df['total_awards_received'] = df['total_awards_received'].fillna(0)

    # Check how many are 0 in total awards received and the percentage
    print("Number of total awards = 0:", len(df[df['total_awards_received'] == 0]))
    print("Percentage of total awards = 0:",
          len(df[df['total_awards_received'] == 0])/len(df.index))

    # Convert created_utc to date (DD/MM/YYYY)
    df['date'] = pd.to_datetime(df['created_utc'], unit='s').dt.strftime('%d/%m/%Y')

    # Concatenate title and selftext column together
    df['text'] = df['title'] + " " + df['selftext']

    # Remove rows where text is empty
    df = df[df['text'] != ""]

    # Reset index
    df = df.reset_index(drop=True)

    # Select columns to keep and reorder them
    df = df[['subreddit', 'date', 'author', 'id', 'num_comments', 
             'score', 'text', 'link_flair_text']]

    # Print how many flairs are empty and the percentage
    print("Number of empty flairs:", len(df[df['link_flair_text'] == ""]))
    print("Percentage of empty flairs:",
          len(df[df['link_flair_text'] == ""])/len(df.index))

    # Print number of unique authors
    print("Number of unique authors", len(df.author.unique()))

    # Display and print size
    print(df.head())
    print(len(df.index))
    print("")

    # Save to csv with subreddit name and year
    df.to_csv("./clean_data/clean_{}_{}_submission_data.csv".format(df['subreddit'][0],
                                                                    f[-8:-4]),
              index=False)
    


# In[3]:


# If the clean_data forlder does not exist, create it
if not os.path.exists("./clean_data/"):
    os.mkdir("./clean_data/")

# Read the CSV files into a list
try:
    # List of csv files
    csvs = [f.name for f in os.scandir("./raw_data/") if f.name.endswith(".csv")]
    
    # Remove hidden directories
    csvs = [f for f in csvs if not f.startswith('.')]
    
    # Append directory as prefix to strings in list
    csvs = ['./raw_data/' + f for f in csvs]
    
    print(csvs)
except:
    print("The raw_data folder does not exist")


# In[4]:


# Apply basic preprocessing to each csv file
for c in csvs:
    print(c)
    basic_data_preproc(c)


# In[ ]:




