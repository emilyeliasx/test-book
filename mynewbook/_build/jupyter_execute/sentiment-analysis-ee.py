# Detecting Emotion within Discussion Comments 
 
The ability to automatically detect the sentiment expressed in textual data will provide Cath's Cabs with a greater insight into the nuance of the comments associated with research notes. This functionality will support further analysis into the correlation between a comment and a researcher's notes. For example, a comment that has a positive sentiment may be linked to a user gaining valuable information from such note and could contribute to a ranking system in terms of usefulness of research notes. Such a feature could greatly innovate Cath's Cabs's software. 

Sentiment Analysis is an area of NLP which aims to automatically identify and extract opinions within a given text by gauging the attitude, sentiment, evaluation and emotion of a speaker/writer based on the computational treatment of the text.

## Sentiment Analysis

For the purposes of the concept work herein, we use an *Amazon* fine food reviews dataset.

# Step 1: Read in data and print
df = pd.read_csv('fine-food-reviews-ee.csv')
display(df.head())

# Step 2: Retrieve the top 10 reviews for demonstration purposes
df = df[:10]

# Step 3: Convert 'Text' column to list
review_list = df['Text'].tolist()
# print(review_list)


The demonstration reports the results of VADER and the Tone Analyzer classifications for the five example comments. Both VADER and IBM's Tone Analyzer produce a score which correlates to the associated sentiment/emotion. As mentioned above, VADER's score is based off of three different thresholds in relation to the compound score whereas the Tone Analyzer is on a scale of zero to one. A score of 0.75 or higher means it's likely that the emotional indicators are spot-on.

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

The given examples clearly express sentiments and emotions. It is important to note that if a comment were to express two sentiments, for example, "I found these notes really helpful, but they could have included a little more information" then more sophisticated techniques may be required such as IBM's Tone Analyzer. Overall, the results from VADER and the Tone Analyzer are in line with our pragmatic competence as human readers which allows us to interpret that these are intuitive results.