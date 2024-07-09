# importing all the required libraries
import pandas as pd
import os
import matplotlib.pyplot as plt
import regex
import re
import string 
import numpy as np
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import nltk

nltk.download('stopwords')
stemmer = nltk.SnowballStemmer('english')
from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
nltk.download('punkt')

stopword=set(stopwords.words('english'))
os.chdir(r'C:\Users\team\OneDrive\Documents\GitHub\project-deliverable-1-targaryens\data')

# dropping columns that are not required from twitter dataset
twitter_dataset = pd.read_csv('Twitter_Reviews.csv')
amazon_dataset = pd.read_csv('Amazon_Reviews.csv') # Data scraped from amazon website
rt_dataset = pd.read_csv('RT_Reviews.csv') # Data scraped from rotten tomatoes website
imdb_dataset = pd.read_csv('IMDB_Reviews.csv') # Data scraped from IMDB website

twitter_data = twitter_dataset.drop(columns = {'location', 'geo', 'date'}, axis = 1)
# deleting duplicates from the scraped data
tweets_wo_duplicates = twitter_data.drop_duplicates()

def data_clean(tweet_data) :
    remov_tag = str(tweet_data).lower()
    remov_tag = re.sub('^(RT) (@[A-Za-z]*_?[A-Za-z]*?_?[0-9]*?_?)?: -?', "", tweet_data)
    remov_tag = re.sub("^(RT) (@[A-Za-z0-9_]+)?: -?", '', remov_tag)
    remov_tag = re.sub("#[A-Za-z0-9_]+(\'s)?", '', remov_tag)
    #remov_tag = re.sub('http?s?://\S+|www\.\S+', '', remov_tag)
    remov_tag = re.sub('http?s?\\w+://\S+|www\.\S+', '', remov_tag)
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  
        u"\U0001F1E0-\U0001F1FF" 
        u"\U00002500-\U00002BEF"  
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    remov_tag = re.sub(emoj, '', remov_tag)
    remov_tag = re.sub('<.*?>+', '', remov_tag)
    remov_tag = re.sub('[%s]' % re.escape(string.punctuation), '', remov_tag)
    remov_tag = re.sub('\n', '', remov_tag)
    #remov_tag = re.sub('(\n?|#+|/+|\")', '', remov_tag)
    remov_tag = remov_tag.encode('ascii', 'ignore')
    remov_tag = remov_tag.decode()
    remov_tag = re.sub('\w*\d\w*', '', remov_tag)
    remov_tag = [word for word in remov_tag.split(' ') if word not in stopword]
    remov_tag=" ".join(remov_tag)
    remov_tag = [stemmer.stem(word) for word in remov_tag.split(' ')]
    remov_tag=" ".join(remov_tag)
    remov_tag = remov_tag.split()
    remov_tag=" ".join(remov_tag)
    return remov_tag

clean_tweet = [data_clean(tw) for tw in tweets_wo_duplicates['text']]
tweets_wo_duplicates['text'] = tweets_wo_duplicates['text'].apply(data_clean)
tweets_wo_duplicates.to_csv('Clean_Twitter_Dataset.csv', index = False)
clean_twitter_dataset = pd.read_csv('Clean_Twitter_Dataset.csv')
    
# Reading Amazon Reviews dataset that was pulled froam the website using Selenium
amazon_dataset = pd.read_csv('Amazon_Reviews.csv')

# Rotten Tomatoes CSV File
rt_dataset = pd.read_csv('RT_Reviews.csv')
merged_dataset_1 = amazon_dataset.append(rt_dataset)

# IMDB Reviews CSV File
imdb_dataset = pd.read_csv('IMDB_Reviews.csv')
merged_dataset_2 = merged_dataset_1.append(imdb_dataset)
print('Merged dataset of twitter, Amazon, Rotten Tomatoes, IMDB :\n', merged_dataset_2.head())

# Deleting duplicates from the merged data of the three sites other than twitter
merged_wo_duplicate = merged_dataset_2.drop_duplicates()

# merging the raw scraped data of the four sites without any duplicates
combined_data = tweets_wo_duplicates.append(merged_wo_duplicate)

# cleaning the scraped data of three sites other than twitter
def data_clean_other_sites(other_sites_data) :
    global wordcount
    wordcount = {}
    clean = str(other_sites_data).lower()
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    clean = re.sub(emoj, '', clean)
    clean = re.sub('<.*?>+', '', clean)
    clean = re.sub('[%s]' % re.escape(string.punctuation), '', clean)
    clean = clean.encode('ascii', 'ignore')
    clean = clean.decode()
    clean = [word for word in clean.split(' ') if word not in stopword]
    clean=" ".join(clean)
    clean = [stemmer.stem(word) for word in clean.split(' ')]
    clean=" ".join(clean)
    clean = clean.split()
     #   new_text = print(text)
    clean=" ".join(clean)
    return clean

review_clean = [data_clean_other_sites(tw) for tw in merged_wo_duplicate['text']]
merged_wo_duplicate['text'] = merged_wo_duplicate['text'].apply(data_clean_other_sites)
merged_wo_duplicate.to_csv('Clean_Dataset_other.csv', index = False)
clean_dataset_other = pd.read_csv('Clean_Dataset_other.csv')

merged_dataset = clean_twitter_dataset.append(clean_dataset_other)
merged_dataset = merged_dataset.dropna()
merged_dataset.to_csv('Clean_Dataframe.csv', index = False)

# Displaying the most common words before cleaning and transformation
text_data = " ".join(i for i in combined_data.text)
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords = stopwords, background_color="white").generate(text_data)
plt.figure( figsize=(15,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# Displaying the most common words in House of the Dragons reviews after cleaning and transformation
data_text = " ".join(x for x in merged_dataset.text)
stopwords = set(STOPWORDS)
wordcloud_1 = WordCloud(stopwords = stopwords, background_color="white").generate(data_text)
plt.figure( figsize=(15,10))
plt.imshow(wordcloud_1, interpolation='bilinear')
plt.axis("off")
plt.show()

word_frequency = nltk.word_tokenize(data_text) # To find the words in a string
freq_words = FreqDist(word_frequency)
# Get the top 20 most common words for displaying it as a plot
top_20_freq = freq_words.most_common(20)

# using pandas series for plotting
plott = pd.Series(dict(top_20_freq))
sns.set_theme(style="ticks")

sns.barplot(y = plott.index, x = plott.values, color='blue')
# To create any graph figures we are using plotly.express library
import plotly.express as pe

graph = pe.bar(y = plott.index, x = plott.values)
# sorting the values
graph.update_layout(barmode = 'stack', yaxis = {'categoryorder':'total ascending'})

# displaying the plotted graph
graph.show()