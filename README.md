## SENTIMENT ANALYSIS ON HOUSE OF THE DRAGON SHOW

![image](https://user-images.githubusercontent.com/111839058/205789252-39e77d58-a691-4e06-a9b0-1a6875576e0d.png)


**Table of Contents**

Summary………………………………………………………………………..…………4

Statement of Scope …………….………………………………………………….………4

Project Objectives…….……………………………………………………………….……..4

Unit of Analysis………………………………………………………………….………………5

Variables……………………………………………………………………………..5

Project Schedule……………………………………..………………………………………………6

Fig 1: GANTT Chart…………………………………………………….…….6

Data Preparation…………………………………………………………………………….6

Data Access………………………………………………………………………….6

Fig2:- HBO House of the Dragon……………….….………………….…………..8

Fig3:- Twitter Search………………………………………………….….………….8

Fig3.1:- Rotten Tomatoes…………………………………………..………………8

Fig3.2:- IMDB Search………………………………………………………..…….9

Fig3.3:- Amazon Search………………………………………………………….…10

Data Consolidation………………………………………………………………………10

Figure 4: KeyWord Search(Hashtags) …………………………………………….10

Data Cleaning……………………………………………………………………………10

Fig5: Data cleansing with RegEx…………………………………………..……….11

Fig6: Stemming of Tweets………………….………………….…………………..11

Data Reduction……….………………………………………………………………….13

Data Transformation……………………………………………………………………..13

Fig7: Data Transformation.…….…………………………………………………..13

Fig8: Most used words…………………………………………...………………...13

Fig9: Before transformations……….…………..…………………………………..14

Fig10: After transformations ………………………………………………………..14

Data Sets……………………………………………………………………………..15

Data Dictionary………………..…………………………………………………….15

Table 1: Scraped-Level Data…………………..……………………………… 17

Sentiment analysis ……………………..…………………..……………………………… 17

Fig11: Sentiment analysis 1 ………………………………………………………..17

Fig11.1: Sentiment analysis 2 ………………………………………………………..18

Fig11.2: Sentiment analysis 3 ………………………………………………………..18

Fig12: Sentiment analysis output ………………………………………………………..18

 Data visualization…………………..……………………………………………………… 19

Fig13: Data visualization 1 ………………………………………………………..20

Fig14: Data visualization 2 ………………………………………………………..21

Fig15: Data visualization 3 ………………………………………………………..22

Fig16: comparing Data visualization 3 & 4 ………………………………………………………..23

## Executive Summary

In this project we are performing an analysis of audience feedback and responses to HBO Max's House of the Dragon program. House of Dragons is a big-budget HBO Max show that serves as a precursor to the hugely acclaimed Game of Thrones series. As a result, there are high expectations for this show. Although social media platforms are important for allowing users to express their opinions on a variety of topics, most users choose to use Twitter but there are several other media platforms than Twitter, like IMDB, Rotten Tomatoes, and Amazon where people may share their thoughts on movies or television series. The financial opportunity for this study is in the screenplay adjustments that must be made depending on audience response for the series to be successful, as well as if the program continues for several seasons. As social networks continue to increase in popularity, sentiment analysis is increasingly being utilized to examine user attitudes. Such analysis will assist us in determining where the program falls short, what attracts viewers to the show, and what aspects of the show people love. For sentiment analysis, we first retrieved all of the tweets and reviews from the major social media platforms mentioned above, then we performed data cleaning and data transformation on the data sets containing all of the raw tweets and reviews, and finally we merged all of the clean data into a single data frame. With this data set we have performed sentiment analysis Sentiment Analysis can help us decipher the mood and emotions of the audience regarding the context. Sentiment Analysis is a process of analyzing data and classifying it based on the need of the research. With sentiment analysis we generated polarities for every tweet and for that tweets we have determined the emotion and saved that into a data set. We generated data visualizations on the sentiment values (positive, negative, and neutral) and ratings of the program from various media platforms once sentiment analysis was completed. Using data visualization, we also anticipated which social media platforms the audience would be most likely to utilize to provide their feedback.


## Statement of Scope
Social media sites such as Twitter, IMDb, Rotten Tomatoes, and Amazon are widely utilized in many nations to express their opinions and thoughts about this web series. For each social media network, we will have four data sets. So, we're analyzing and doing sentiment analysis to determine whether the majority of users are on positive or negative note about this program.

## Project Objectives: 
The House of the Dragon is now one of HBO's most popular series. It is so popular that individuals who have seen the Game of Thrones Web series were highly eager about this series. This is a collection of social media reviews and thoughts. So, I want to utilize Python to assess people's feelings regarding House of the Dragons sentiment analysis. we will be analyzing data from twitter and other websites such as Amazon, Rotten Tomatoes and IMDB as follows:
How people reacted to this show.
How these tweets affected the show.
## Unit of Analysis:
We'd be analyzing tweets from Twitter, IMDB, Rotten Tomatoes, and Amazon, concentrating on hashtags and tweet content that represent opinions towards the House of the Dragon show.
## Variables:
**Source:** The tweet in which the html formatted text is utilized, the primary value of tweets, and social media platforms reviews

**Tweet_text:** This is the primary variable that we will use to scrape data.

**created_at:** We would be collecting the date and time details of the tweet by the user.

**geo:** We will extract the tweet in order to determine where it originated and to limit the tweets.

**hashtags:** In order to collect tweets, we will utilize #HouseOfTheDargon or #HouseOfTheDragonHBO hashtags.


## Project Schedule
![WhatsApp Image 2022-12-14 at 16 54 54](https://user-images.githubusercontent.com/111839058/207737112-0c2587a1-7282-4938-a898-bc72178cf893.jpg)


							Fig1: Gantt Chart

## Data Preparation
### Data Access
Data Access:
We scraped data from the below-mentioned websites: 
* https://developer.twitter.com/en/portal/ - We used the Twitter API to gather twitter tweets of the users.

->	We used the Twitter API and tokens for app access, and we ran into problems retrieving tweets with Essential access (default access provided by Twitter developer account), so we requested elevated access to retrieve tweets. Then we were granted elevated access and attempted to get about 1000 tweets, however we only received 455 unique tweets.

->	We utilized Twitter API to search for tweets using the hashtags #HouseOfTheDargon or #HouseOfTheDragonHBO in order to gather tweets and relevant data for our project report analysis. We also used libraries such as pandas, NumPy, and many more to our data scraping. So, after scarping the tweets from Twitter, we obtained roughly 450 tweets, which we believe would not be enough for sentiment analysis, so we scarped the show's reviews from other social media platforms such as Amazon, IMDB, and Rotten Tomatoes too.
* Code for Scraping Twitter Data :- [twitter_API.py](code/twitter_API.py)

* https://www.rottentomatoes.com/tv/house_of_the_dragon/s01 " To get reviews from rotten tomatoes, we browsed directly to display reviews and pulled audience reviews from there using selenium in python (firefox web driver), which is python's dynamic web scraping. We received around 3000 reviews in all, 2800 of which were unique."
* Code for Scraping Rotten Tomatoes Data :- [rotten_Tomatoes_Code.py](code/rotten_Tomatoes_Code.py)

* https://www.imdb.com/title/tt11198330/reviews "We used Python's selenium library to navigate to the show's reviews page and grab all of the user reviews, which we then saved in a data set, in order to obtain reviews from IMDB. We collected almost 50000 reviews overall, of which only 1425 were unique."
* Code for Scraping IMDB Data :- [imdb_Code.py](code/imdb_Code.py)

* https://www.amazon.com/House-Dragon-Complete-First-Season/dp/B0BGMZB6GQ/ref=sr_1_2?crid=202G4M20HC0UI&keywords=House+of+the+Dragon%3A+The+Complete+First+Season+%28DVD%29&qid=1667492291&sprefix=house+of+the+dragon+the+complete+first+season+dvd+%2Caps%2C114&sr=8-2 "The same selenium in Python approach was used to retrieve Amazon reviews. For Amazon, we extracted xxx reviews, of which we identified xxx were distinctive."

* Code for Scraping Amazon Data :- [amazon_code.py](code/amazon_code.py)

- We accessed the data from the mentioned social media networks via tweets and reviews.
- We also scraped ratings data from the aforementioned social media sites, such as IMDB, Amazon, and Rotten Tomatoes in addition to audience reviews and tweets.
* Code for Scraping Ratings Data :- [rating.py](code/rating.py)

![image](https://user-images.githubusercontent.com/111839058/205790240-dd00e9b1-3832-4ec2-916d-cd59fad44911.png)

 							Fig2: HBO House Of The Dragon



![image](https://user-images.githubusercontent.com/111839058/205797959-251c18dc-ef0b-4a6d-8b8c-3dcbdba72d85.png)

 
							Fig 3: Twitter Search


![image](https://user-images.githubusercontent.com/111839058/205790336-e68de847-5b5b-4e5f-bafa-72c766a84a85.png) 

							Fig 3.1: Rotten Tomatoes Reviews

![image](https://user-images.githubusercontent.com/111839058/205798024-eedb33ea-99f2-4a14-96f5-01f0855e7fae.png)

							Fig 3.2 IMDB search

![image](https://user-images.githubusercontent.com/111839058/205790382-b3f9626d-6791-4e5c-be1e-9e7732f52d9a.png)
 
							Fig 3.3 Amazon Search

## Data Consolidation:
We stored the tweets that are extracted from the two hashtags #HouseOfTheDragons, #HouseOfTheDragonHBO into one data frame. This is converted to csv file to keep track of all the columns involved in the extraction and find out the useful columns to implement our analysis.

![image](https://user-images.githubusercontent.com/111839058/205790527-26d4f009-1a97-4973-a5cd-49d40b224417.png)

							Fig 4: Keyword Search (Hashtags)

### Data Cleaning
So, after data extraction tweets with emojis and numerical values are not necessary for our sentiment analysis, we eliminated all duplicate tweets, un-wanted tweets, and special characters from the data after retrieving it from Twitter. After cleaning, we added every tweet that was cleaned to a new data frame. Other social media sites, such as rotten tomatoes, IMDB, and Amazon reviews are in alternative data frames, which we have developed. Then, we cleaned up each batch of data and combined all the reviews into a totally new data frame. We now have accurate, cleaned house of the dragon show reviews and tweets in two separate data sets for Twitter and other social media sites
We cleaned the data with RegEx

**"http?s?://\S+|www\.\S+"** - We removed the links containing http data. 

**"^(RT) (@[A-Za-z0-9_]+)?: -?"** –  We removed the data starting with <RT and Usernames which are Retweets.  

**"#[A-Za-z0-9_]+"** –  we removed the Hashtags from the tweet texts.

**"emoj"** - We removed the data that contained emojis.

**"[%s]"** – to remove a single character from a list.

**"\n"** –   To remove the new line text and move it to the previous line.

![image](https://user-images.githubusercontent.com/111839058/205790611-2c5b7b26-2f3d-42d8-9d8d-7958ce7dd02f.png)

							Fig 5: Data cleansing with RegEx

After cleaning the text from the tweets, developing morphological variations of a root/base word using stemming algorithms or stemmers. The words are reduced via a stemming algorithm. For example, “playing," "plays," or "played." to the root word "play,"
 
![image](https://user-images.githubusercontent.com/111839058/205790632-b52956da-95cd-404a-9d43-3a604f1ce255.png)

							Fig 6: Stemming of Tweets


### Data Transformation
We used the built-in libraries to create the graph of the most common words used in tweets and show reviews. We created a graph plot that displays the top twenty most commonly used words and the number of times they were repeated. We used plotly.express library to represent these plots. 

![image](https://user-images.githubusercontent.com/111839058/205791276-aae4a47b-bcc2-4ef2-b726-9d647b13e855.png)

							Fig 7: Data Transformation

![image](https://user-images.githubusercontent.com/111839058/205791319-7a542bcd-de51-4e66-92e2-feda54080f93.png)

							Fig 8: Most used words

We utilized WORDCLOUD to portray the most frequently used words in tweet text in a more effective and visually appealing manner. To execute this for all the integrated tweets and reviews from all social networking sites, we used wordcloud and libraries. Here, you can see that the most frequently used words are greater in size than others. We have provided a word cloud of textual data before and after cleaning and transformation. In the pictures below, you can see that some of the characters are not necessary before and after changes.

**Before Transformation:**
![image](https://user-images.githubusercontent.com/111839058/205791388-437fc818-d385-4071-aa8f-f73cc5a9de58.png)

![image](https://user-images.githubusercontent.com/111839058/205791424-6c8466ac-a616-43b2-b428-ef622d414a15.png)

							Fig 9:- Before Transformations

**After Transformation:**
![image](https://user-images.githubusercontent.com/111839058/205791468-aa069b5f-3236-402d-930c-5a02dc32fe68.png)
![image](https://user-images.githubusercontent.com/111839058/205791503-2623b413-9870-41a4-a105-146faa1931b6.png)

							Fig 10:- After Transformations

**Data Sets:**

  Data Set of Twitter, Rotten Tomatoes, IMBD, Amazon before cleaning:-

![image](https://user-images.githubusercontent.com/111839058/205792509-d184499a-c80d-4996-9d66-ed8c55ccc128.png)
![image](https://user-images.githubusercontent.com/111839058/205792585-4409d578-39d0-456d-9781-8c1c597e705f.png)
![image](https://user-images.githubusercontent.com/111839058/205792601-6e389d9d-bc94-4044-af25-36f0a1945808.png)
![image](https://user-images.githubusercontent.com/111839058/205792616-2a7989bb-ad38-401b-a20e-fc9ec340c404.png)

**Data set of Twitter Tweets after cleaning:** -

![image](https://user-images.githubusercontent.com/111839058/205792721-e6f88add-71b6-4c14-9809-5e83b4e294d9.png)

Data set of Amazon, Rotten Tomatoes, IMBD Tweets and reviews combined after cleaning:-

![image](https://user-images.githubusercontent.com/111839058/205792747-ba102a63-1c56-4e17-8272-89c3c8b8968c.png)

Data set of merged Twitter, Amazon, Rotten Tomatoes, IMBD Tweets and reviews after cleaning : 

![image](https://user-images.githubusercontent.com/111839058/205792783-563657bd-26b2-41b4-bf28-24b7e72ac43c.png)
	
Data set for review count in each website:

* [website_rev_count.csv](data/website_rev_count.csv)

Data set for reviews with polarity and sentiment values:

* [dataset_with_Polarity.csv](data/dataset_with_Polarity.csv)

Data set for sentiment Count:
	
* [Dataset_count.csv](data/dataset_count.csv)

Data set for rating given in Social websites:

* [dataset_with_Rating.csv](data/dataset_with_Rating.csv)

**Data Reduction**

We initially extracted 3 columns of data from the tweets i.e Text, geo, create_at. We used drop function to drop geo and created_ at columns as we observed they are not of use for our analysis. 

We then reduced the size of all tweets obtained from Twitter. In addition, we deleted the stop words and created a new data frame containing relevant terms. This capability was applied to all of the tweets and reviews from all of the social media channels that we utilised. We also eliminated any data that was empty. Further data cleanup and data minimization will be performed in order to provide a more precise analysis of our project.

 ### Data Dictionary


| Attribute Name | Description | Data Type | Source |
|:---|:---|:---:|:---|
| GOT | sequel of  series House of The Dragons | char | https://twitter.com |
| House of The Dragon | series for which we are doing sentiment analysis| char |https://twitter.com|
| Targaryen | family in the series HOTD | char | https://twitter.com |
| ep | episode| char |https://twitter.com|
| tweet_text | variable for data scraped  from twitter | char | https://twitter.com |
| rott_reviews | variable for data scraped  from rotten tomatoes| char |[https://twitter.com](https://www.rottentomatoes.com/tv/house_of_the_dragon/s01)|
| finale | final episode of the show HOTD| char |[https://twitter.com](https://www.rottentomatoes.com/tv/house_of_the_dragon/s01 | https://twitter.com)|
| reeHBO | streaming platform of HOTD in United States| char |(https://www.rottentomatoes.com/tv/house_of_the_dragon/s01 | https://twitter.com)|
| rating | people rating the show on the scale of 10| char/int |House of the Dragon (TV Series 2022– ) - House of the Dragon (TV Series 2022– ) - User Reviews - IMDb|
| amaz_reviews | variable for data scraped  from amazon| char |Amazon.com: House of the Dragon: The Complete First Season (DVD) : Miguel Sapochnik, Kevin Lau, Ryan Condal, Alexis Raben, Karen Wacker, George R.R. Martin, Ron Schmidt, Jocelyn Diaz, Sara Hess, Vince Gerardis, Greg Yaitanes, Paddy Considine, Matt Smith, Olivia Cooke, Emma D’Arcy, Fabien Frankel, Rhys Ifans, Steve Toussaint, Eve Best, Sonoya Mizuno, George R.R. Martin: Movies & TV|
| Im_reviews | variable for data scraped  from IMBD| char |House of the Dragon (TV Series 2022– ) - House of the Dragon (TV Series 2022– ) - User Reviews - IMDb|
| sentiment | sentiment of a word based on polarity| char |from our project|
| positive | the score of sentiment positive using polarity| int |from our analysis|
| negative | the score of sentiment negative using polarity| int |from our analysis|
| neutral | the score of sentiment neutral using polarity| int |from our analysis|
| textblog | a library used in R | char |R.Studio|
	
 ##Sentiment Analysis
We used the cleaned dataset to do text mining and sentiment analysis on tweets and reviews data to examine audience's emotions, feelings, and attitude towards the House of the Dragon show.To work on the sentiment polarity for our dataset, we installed the 'textblob' package. We successfully determined the polarity of each cleaned review using textblob, the polarity of a sentence is returned by TextBlob. Polarity is defined as [-1,1], where -1 represents a negative sentiment and 1 represents a positive sentiment. Once the polarity value is calculated we have merged these values with the reviews into a new data frame (dataset with polarity). So, based on the polarity values assigned to each review, we determined the emotion as follows: - 

  If the polarity value is less than zero, the review is considered as negative.

  If the polarity value is greater than zero, the review is considered as positive.

  If the polarity value is 0, the review is considered as neutral.
  
We have now built a new column in the data frame (dataset with polarity) and integrated these feelings into it.

We estimated the number of negative, positive, and neutral reviews from this data set and determined the show sentiment using an else if statement.

* Code for Sentiment Analysis:- [sentiment_analysis.py](code/sentiment_analysis.py)

![Screenshot (327)](https://user-images.githubusercontent.com/111839448/207773521-c23758bd-8093-409c-947a-6463d44c0de8.png)
	
							Fig 11:- sentiment analysis


![Screenshot (328)](https://user-images.githubusercontent.com/111839448/207773555-417d625c-9964-48c7-bf76-d5b918b0192b.png)
	
							Fig 11.1:- sentiment analysis


![Screenshot (329)](https://user-images.githubusercontent.com/111839448/207773586-77477121-66ee-4b68-adc3-b23d04d96087.png)
	
							Fig 11.2:- sentiment analysis
	
![Sentiment_Analysis_Result](https://user-images.githubusercontent.com/111839448/207776966-3af81236-4ec1-4b53-8bda-f6a02cb659f8.png)
	
							Fig 12.:- sentiment analysis output




  ## Data Visualization
  Data visualization is the process of putting information into a visual framework, such as graphs, so that all the investors, customers and supervisors can more easily grasp and draw conclusions from it, through insightful data visualizations. Data visualization positively impacts an organization's decision-making process. Due to the ability to evaluate data in graphical or visual forms, businesses can now see trends more quickly. We created visualizations for the three emotions—positive, negative, and neutral—that our sentiment analysis revealed. The ggplot library was installed for visualization. We created four distinct visualizations to quickly grasp the entire project in order to make the analysis and observation clear and understandable.

* Code for Data Visulaization:- 
[data_visualization.R](code/data_visualization.R)
 
**Visualization 1**
 
A bar plot of the data below offers information on the number of positive, negative, and neutral reviews. As soon as we finished the sentiment analysis and determined the quantity of reviews, we decided on this visualization.so that we can gauge the audience's opinion of the House of the Dragon show with positivity and negativity. As we can see, there are over 3000 positive ratings and approximately 850 negative reviews. We utilized the y axis to indicate the amount of reviews, and the x axis to represent positive, negative and neutral. So, with this bar plot visualization, we can confirm that this show is a hit show, but there are also bad reviews, so the directors and investors should also focus on what went wrong in season one and must fix in future seasons.

![Bar_plot_1_Num_rev](https://user-images.githubusercontent.com/111839448/207773721-9e6b43aa-c55e-4eca-a5d3-8785e80111d8.png)
		
							Fig 13:- Visualization 1


	
**Visualization 2**
 
A donut plot of the data below shows which social media platforms the audience has preferred to express feedback on the House of the Dragon series. As soon as we finished the data cleaning and determined on which social media website audience gave more reviews, we decided to do this visualization. As we can see, about 60% of the audience has preferred to provide the review in rotten tomatoes,30% in IMDB,7% in twitter and 0.5% in amazon website. While scraping the twitter tweets we have observed most the feedback were provided in the form of Picture, so we were not able to scrape them but most of the textual feedback has provided in rotten tomatoes. So, we should include this as a primary factor because doing sentiment analysis just on Twitter data may result in incorrect results.

![plot_web_rev](https://user-images.githubusercontent.com/111839448/207773754-244eb049-6dd9-4cce-a6db-628084eccba4.png)
		
							Fig 14:- Visualization 2
  
  **Visualization 3**
   
A bar plot of the data below offers information on the rating of the house of the dragon show in various social media platforms like amazon, rotten tomatoes and IMDB. As soon as we finished the data extraction for ratings of this show, we decided to do this visualization. As we can see, audience rated this show about 88% in amazon (4.4 out of 5),85% in IMDB (8.5 out of 10) and 82% in Rotten tomatoes. With this visualization we surely say that it is one the top television series because IMDB rating is above 8.5.We utilized the y axis to indicate the rating percentage, and the x axis to represent social media websites(IMDB, Amazon and Rotten Tomatoes).

![Bar_plot_2_web_rating](https://user-images.githubusercontent.com/111839448/207773795-148ffc83-97f8-4e19-9873-b3a171e6e5aa.png)
		
							Fig 15:- Visualization 3

 **Visualization 4**
 
We created this Visualization for our study, in which we compared the ratings offered by the biggest social media platforms to our analysis percentage, allowing us to confirm our findings. Therefore, we took the visualization 3 as one of the visualizations and built an other pie chart visualization based on positive, negative and neutral reviews from the 5000 cleaned reviews dataset. As we can see from the image below, we are quite close to the ratings offered by the biggest social media networks. The computed rating is 68% which we have generated. There may be some disparities between the ratings we computed and the ratings on the biggest social media platforms because the audience may only submit the rating without providing feedback in the comment area. 

![Pie_plot_percent_rev](https://user-images.githubusercontent.com/111839448/207774138-66d7ff36-4d4a-4d1d-ab24-6e13574c9424.jpg)

![Bar_plot_2_web_rating](https://user-images.githubusercontent.com/111839448/207773832-455d0f83-a0f8-41d6-9aa0-f145c7306420.png)

							Fig 16:- comparing Visualization 3 & Visualization 4


  ## Conclusion and Discussion
 We scraped roughly 50000 tweets and reviews for the House of the Dragon show using Selenium in Python and from Twitter using the Twitter API (Elevated Access). We finalized 4635 tweets and reviews in total after cleaning the raw tweets and reviews.
So, while extracting tweets or reviews in the first stage, we discovered that the opinions on this show were neutral, and when we extracted more tweets for subsequent episodes, we discovered that positivity on the show increased gradually when we finally extracted tweets or reviews of the season 1 finale episode, audience were satisfied with the first season. We ran into a problem while scraping the data since we couldn't extract more than 50 to 60 tweets or reviews from a single episode. This may be problematic for sentiment analysis, so we retrieved all the tweets and reviews for whole season. So, when doing sentiment analysis, we had the thought to scrape the ratings as well, so we scraped the ratings from IMDB, Amazon, and Rotten Tomatoes and utilized them to compare our calculated rating to those ratings. HBO and Disney+ Hotstar are the platforms that will benefit the most from this analysis as these two streaming services/ OTT platforms are airing the show in United States and India respectively.
