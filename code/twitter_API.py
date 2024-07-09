# Scraping tweets data using Twitter API
# 
# 
# Installed and importing the following libraries :
# pandas, tweepy
# 
# Tweepy is a library used to read tweets.
# 

# get_ipython().system('pip install pandas')
import pandas as pd
import os
# get_ipython().system('pip install tweepy')
import tweepy as tw

# importing config.py file that contains the API keys
import config

# API Keys added in config.py file will be ignored while pushing to GitHub

# Referencing to config.py file for authentication to Twitter

# add your api keys while running this code and change the below code as follows :

#accesstoken = xxxxxxxxxx  
#accesstokensecret = xxxxxxxxx
#apikey = xxxxxxxx
#apisecretkey = xxxxxxxx
# auth = tw.OAuthHandler(apikey, apisecretkey) 
# auth.set_access_token(accesstoken, accesstokensecret)

auth = tw.OAuthHandler(config.apikey, config.apisecretkey) #calling OAuthHandler required for authantication with Twitter
auth.set_access_token(config.accesstoken, config.accesstokensecret)

# calling tweepy's API function
api = tw.API(auth,wait_on_rate_limit=False)

# Extracting tweets using the Hashtags
keyword_search = '#HouseOfTheDragon OR #HouseOfTheDragonHBO'

#creating a tweepy item iterator tweets for searching by calling tw.Cursor func, pulling only 1000 records
tweets = tw.Cursor(api.search_tweets,q = keyword_search, lang ='en').items(1000)

# text : tweet text
# user.location : location of the user
# geo : location of where the tweet is done from
# created_at : date and time of the tweet
twitter_review_col = [[tweet.text, tweet.user.location, tweet.created_at, tweet.geo]for tweet in tweets]

# Creating a dataframe with the required column names
tweet_text = pd.DataFrame(data = twitter_review_col, columns=['geo', 'text', 'location', 'date'])
# pd.set_option('max_colwidth',800)
tweet_text.to_csv('Twitter_Reviews.csv', index = False)