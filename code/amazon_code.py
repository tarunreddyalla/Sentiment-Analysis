from tokenize import Name
from selenium import webdriver
import os
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.common.exceptions import TimeoutException 
from selenium.webdriver.support import expected_conditions
import time
driver = webdriver.Firefox(executable_path=r'C:\Users\team\Downloads\geckodriver-v0.32.0-win64\geckodriver.exe')
amazon_url = 'https://www.amazon.com/House-Dragon-Complete-First-Season/dp/B0BGMZB6GQ/ref=sr_1_2?crid=202G4M20HC0UI&keywords=House+of+the+Dragon%3A+The+Complete+First+Season+%28DVD%29&qid=1667492291&sprefix=house+of+the+dragon+the+complete+first+season+dvd+%2Caps%2C114&sr=8-2'
driver.get(amazon_url)

# Selecting See All reviews
WebDriverWait(driver, timeout= 100).until(lambda d: d.find_element(By.CSS_SELECTOR,'.a-link-emphasis'))
all_reviews_link = driver.find_element(By.CSS_SELECTOR,'.a-link-emphasis').click()

# Scraping tweets from Amazon

# Creating Element for Amazon Review Text and saving them in a list
WebDriverWait(driver, timeout=30).until(lambda d: d.find_element(By.CSS_SELECTOR, 'div.a-section.celwidget>div:nth-child(5)'))
amazon_review = driver.find_elements(By.CSS_SELECTOR, 'div.a-section.celwidget>div:nth-child(5)')
amazon_reviews = []
print('\nAmazon Reviews :\n')
for reviews in amazon_review:
    amazon_reviews.append(reviews.text) 
    print(reviews.text, '\n')
print(len(amazon_reviews))

# Creating an element for the next page button and scraping the reviews
WebDriverWait(driver, timeout=100).until(lambda d: d.find_element(By.CSS_SELECTOR,'.a-last > a:nth-child(1)'))
next_page_button = driver.find_element(By.CSS_SELECTOR,'.a-last > a:nth-child(1)').click()

WebDriverWait(driver, timeout=30).until(lambda d: d.find_element(By.CSS_SELECTOR, 'div.a-section.celwidget>div:nth-child(5)'))
amazon_review_next = driver.find_elements(By.CSS_SELECTOR, 'div.a-section.celwidget>div:nth-child(5)')
amazon_reviews_next = []
print('\nAmazon Reviews :\n')
for reviews in amazon_review_next:
    amazon_reviews_next.append(reviews.text) 
    print(reviews.text, '\n')
print(len(amazon_reviews_next))
from heapq import merge
reviews_list = list(merge(amazon_reviews, amazon_reviews_next))

os.chdir(r'C:\Users\team\OneDrive\Documents\GitHub\project-deliverable-1-targaryens\data')
# creating a dataframe to store the scraped reviews 
amaz_reviews = pd.DataFrame({"text" : reviews_list})
amaz_reviews.to_csv('Amazon_Reviews_1.csv', index = False)