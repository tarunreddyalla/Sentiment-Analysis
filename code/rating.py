# this python file is to scrape ratings from Amazon, IMDB, Rotten Tomatoes websites for data visualization purpose
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
driver = webdriver.Firefox(executable_path=r'C:\Users\haric\Downloads\geckodriver-v0.32.0-win64\geckodriver.exe')
IMDB_url = 'https://www.imdb.com/title/tt11198330/'
driver.get(IMDB_url)
WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH,'/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[1]/a/div/div/div[2]/div[1]/span[1]'))
rating = driver.find_element(By.XPATH,'/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[1]/a/div/div/div[2]/div[1]/span[1]')
hotd = rating.text
a=print("IMDB rating:",hotd)

rt_url1 = 'https://www.rottentomatoes.com/tv/house_of_the_dragon'
driver.get(rt_url1)
WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[3]/div[1]/section/div[1]/section/section/div[2]/h2/a/span/span[2]'))
ratingrt = driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[3]/div[1]/section/div[1]/section/section/div[2]/h2/a/span/span[2]')
hotdrt = ratingrt.text
b=print("rotten tomatoes rating:",hotdrt)

rt_url = 'https://www.amazon.com/House-Dragon-Complete-Blu-ray-Digital/dp/B0BGMYKYBN'
driver.get(rt_url)
WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[5]/div[5]/div[4]/div[3]/div/span[1]/span/span[1]/a/i[1]/span'))
lst_of_ratings = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div[5]/div[5]/div[4]/div[3]/div/span[1]/span/span[1]/a/i[1]/span')
for value in lst_of_ratings:
    rating = value.get_attribute('textContent')
c=print("amazon rating:",rating)
# Adding the website name to a list
rating_list = [hotd, hotdrt, rating]
# Adding the rating of each website to a list
webs_list = ['IMDB', 'Rotten Tomatoes', 'Amazon']
rating_count = pd.DataFrame({"Website_Name" : webs_list, "Rating" : rating_list})
rating_val = rating_count.to_csv("dataset_with_Rating.csv", index = False )