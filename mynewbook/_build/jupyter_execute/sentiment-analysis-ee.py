***

`## DIA TEAM MEMBER NOTES (DELETE THIS CELL ON CHECKING POINTS BELOW):`

`### Text changes required if using different dataset to Amazon's Fine Food Reviews:`

- `Change title of notebook`
- `Change dataset text in "1. Introduction"`
- `Change dataset text in "2. Data"`

***

# Sentiment Detection within Comments

## 1. Introduction

The purpose of this notebook is to demonstrate *Sentiment Analysis*, a *Natural Language Processing (NLP)* technique. This procedure aims to detect sentiment within text.

A subsample of the *Amazon* fine food reviews [dataset](https://www.kaggle.com/snap/amazon-fine-food-reviews) has been used in this notebook.

### 1.1 Import Libraries

The cell immediately below houses the import statements for this script. Please run the cell and continue to scroll to the next cell where the tutorial will continue.

# Data Analysis
import pandas as pd

# Sentiment Analysis
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

## 2. Data

The cell below shows the top 10 records of the fine foods review dataset which is being used in this demonstration. In this case we are only interested in the 'Text' column.

# Step 1: Read in data and print
df = pd.read_csv('fine-food-reviews-ee.csv')
display(df.head())

# Step 2: Retrieve the top 10 reviews for demonstration purposes
df = df[:10]

# Step 3: Convert 'Text' column to list
review_list = df['Text'].tolist()
# print(review_list)

## 3. Sentiment Analysis

In the following cell, we apply `VADER`, a sentiment analysis tool, to the top 10 reviews in the example dataset.

Once `VADER` is installed, we call the `SentimentIntensityAnalyzer` object. We will use the `polarity_scores()` method to obtain the polarity indices for a given review.

# Step 1: Initialise 'SentimentIntensityAnalyzer' object
analyser = SentimentIntensityAnalyzer()

# Step 2: Classify reviews by sentiment on *compound score*
def sentiment_analyzer_scores(review_comments):
    for i in review_comments:
        score = analyser.polarity_scores(i)
        if score['compound'] >= 0.05:
            print(i, "\n")
            print("Compound Score: ", score)
            print("Overall Sentiment: Positive", "\n")
            print("------------------------------------------------------------------------------------------------")
        elif score['compound'] <= - 0.05:
            print(i, "\n")
            print("Compound Score: ", score)
            print("Overall Sentiment: Negative", "\n")
            print("------------------------------------------------------------------------------------------------")
        else:
            print(i, "\n")
            print("Compound Score: ", score)
            print("Overall Sentiment: Neutral", "\n")
            print("------------------------------------------------------------------------------------------------")

sentiment_scores = sentiment_analyzer_scores(review_list)