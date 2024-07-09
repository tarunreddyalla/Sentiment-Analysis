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

os.chdir(r'C:\Users\team\OneDrive\Documents\GitHub\project-deliverable-1-targaryens\data')
driver = webdriver.Firefox(executable_path=r'C:\Users\team\Downloads\geckodriver-v0.32.0-win64\geckodriver.exe')

# Scraping reviews from Rotten Tomatoes
rt_url = 'https://www.rottentomatoes.com/tv/house_of_the_dragon/s01'
driver.get(rt_url)

# Creating an element to click on 'Selecting All Audience Reviews' link
WebDriverWait(driver, timeout= 100).until(lambda d: d.find_element(By.CSS_SELECTOR,'.mop-audience-reviews__view-all--link'))
audience_reviews = driver.find_element(By.CSS_SELECTOR,'.mop-audience-reviews__view-all--link').click()

# Reviews from Rotten Tomatoes
# Since there is a next button in every new page writing it in a loop till the last page
flag = True
rt_reviews = []
while flag == True :
    if flag :
        try :
            ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
            WebDriverWait(driver, timeout=10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//p[@data-qa = "review-text"]')))
            rt_review = driver.find_elements(By.XPATH, '//p[@data-qa = "review-text"]')
            print('\nRotten Tomatoes Reviews :\n')
            for rt in rt_review:
                rt_reviews.append(rt.text) 
                a = rt.text
                print(rt.text, '\n')
                #print(len(rt_reviews))

            WebDriverWait(driver, timeout=100000).until(lambda d: d.find_element(By.CSS_SELECTOR,'nav.prev-next-paging__wrapper:nth-child(6) > button:nth-child(2) > span:nth-child(1)'))
            next_button = driver.find_element(By.CSS_SELECTOR,'nav.prev-next-paging__wrapper:nth-child(6) > button:nth-child(2) > span:nth-child(1)').click()
        except Exception as ex:
            print('Exception Handled')
            for rev in rt_reviews :
                if rev == 'The first episode is awesome. Looking forward to the next ones.' :
                    flag = False
                    break

# Creating a dataframe to store the scrapped rotten tomatoes reviews and saving it as a csv file
rott_reviews = pd.DataFrame({"text" : rt_reviews})
#print('length of dataframe is :\n', len(rott_reviews))
rott_reviews.to_csv('RT_Reviews.csv', index = False)      

