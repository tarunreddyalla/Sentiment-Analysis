# importing all the required libraries
import pandas as pd
import numpy as np
import os
from textblob import TextBlob

os.chdir(r'C:\Users\haric\OneDrive\Documents\GitHub\project-deliverable-2-targaryens\data')

final_dataset = pd.read_csv('Clean_Dataframe.csv')
# Defining the sentiment using TextBlob
# TextBlob returns polarity
# Polarity lies between [-1,1], -1 defines a negative sentiment and 1 defines a positive sentiment.
senti_tex = [TextBlob(values) for values in final_dataset['text']]
senti_tex[0].polarity, senti_tex[0]

# Creating a list of polarity values and reviews text
senti_val = [[values.sentiment.polarity, str(values)] for values in senti_tex]

# Create a dataframe for each review against its polarity using TextBlob 
sentiment_data = pd.DataFrame(senti_val, columns=["polarity", "text"])
# Adding a new variable 'Positive/Negative/neutral' to the existing dataframe
sentiment_data.loc[sentiment_data['polarity'] < 0, 'Positive/Negative/neutral'] = 'Negative'
sentiment_data.loc[sentiment_data['polarity'] == 0, 'Positive/Negative/neutral'] = 'Neutral'
sentiment_data.loc[sentiment_data['polarity'] > 0, 'Positive/Negative/neutral'] = 'Positive'
sentiment_data.to_csv('dataset_with_Polarity.csv', index = False)

# Number of negative reviews
neg_count = (sentiment_data['Positive/Negative/neutral'] == 'Negative').sum()
print('Negative : ', neg_count)
# Number of Neutral reviews
neu_count = (sentiment_data['Positive/Negative/neutral'] == 'Neutral').sum()
print('Neutral : ', neu_count)
# Number of Positive reviews
pos_count = (sentiment_data['Positive/Negative/neutral'] == 'Positive').sum()
print('Positive : ', pos_count, '\n')

if (pos_count > neg_count) and (pos_count > neu_count) :
        print("Majority of the audience have POSITIVE response towards the show")
elif (neg_count > pos_count) and (neg_count > neu_count) :
        print("Majority of the audience have NEGATIVE response towards the show")
else :
        print("Majority of the audience have NEUTRAL response towards the show")

count_list = [pos_count, neu_count, neg_count]

resp_list = ['Positive', 'Neutral', 'Negative']

resp_count = pd.DataFrame({"Pos/Neu/Neg" : resp_list, "NumberofReviews" : count_list})
response_count = resp_count.to_csv("dataset_count.csv", index = False )
response_count = resp_count.to_csv("dataset_count.txt", sep = "\t" )

# Determing the number of reviews given in each website for data visualization purpose
twitter_data = pd.read_csv('Twitter_Reviews.csv')
amazon_data = pd.read_csv('Amazon_Reviews.csv') 
rt_data = pd.read_csv('RT_Reviews.csv') 
imdb_data = pd.read_csv('IMDB_Reviews.csv') 

twitter_data = twitter_data.drop(columns = {'location', 'geo', 'date'}, axis = 1)
# deleting duplicates from the scraped raw data
tweets_wo_duplicates = twitter_data.drop_duplicates()
amazon_wo_duplicates = amazon_data.drop_duplicates()
rt_wo_duplicates = rt_data.drop_duplicates()
imdb_wo_duplicates = imdb_data.drop_duplicates()

tweet_count = len(tweets_wo_duplicates.text)
ama_count = len(amazon_wo_duplicates.text)
rt_count = len(rt_wo_duplicates.text)
imdb_count = len(imdb_wo_duplicates.text)

# Adding the number of reviews given in each website to a list
sum_count = [tweet_count, ama_count, rt_count, imdb_count]
# Adding the website name to a list
web_names = ['Twitter', 'Amazon', 'Rotten Tomatoes', 'IMDB']

review_count = pd.DataFrame({"Website" : web_names, "Total_Reviews" : sum_count})
response_count = review_count.to_csv("website_rev_count.csv", index = False )
