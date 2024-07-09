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
driver = webdriver.Firefox(executable_path=r'C:\Users\team\Downloads\geckodriver-v0.32.0-win64\geckodriver.exe')

# Scraping reviews from IMDB
imdb_url = 'https://www.imdb.com/title/tt11198330/reviews'
driver.get(imdb_url)

# Reviews from IMDB
imdb_reviews = []
flag = True
while flag == True :
    if flag == True :
        try :
            ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
            WebDriverWait(driver, timeout=10000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'div.lister-list>div>div>div>div:nth-child(4)>div.text.show-more__control')))
            imdb_review = driver.find_elements(By.CSS_SELECTOR, 'div.lister-list>div>div>div>div:nth-child(4)>div.text.show-more__control')
            print('\nIMDB Reviews :\n')
            for im in imdb_review:
                imdb_reviews.append(im.text) 
                a = im.text
                print(im.text, '\n')
                #print(len(rt_reviews))

            #WebDriverWait(driver, timeout=100000).until(lambda d: d.find_element(By.CSS_SELECTOR,'nav.prev-next-paging__wrapper:nth-child(6) > button:nth-child(2) > span:nth-child(1)'))
            WebDriverWait(driver, timeout=100000).until(lambda d: d.find_element(By.CSS_SELECTOR,'#load-more-trigger'))
            load_more_button = driver.find_element(By.CSS_SELECTOR,'#load-more-trigger').click()
        except Exception as ex:
            print('Exception Handled')
            flag = False
            break

os.chdir(r'C:\Users\team\OneDrive\Documents\GitHub\project-deliverable-1-targaryens\data')
# Creating a dataframe to store the scraped imdb reviews and saving it as a csv file
im_reviews = pd.DataFrame({"text" : imdb_reviews})
im_reviews.to_csv('IMDB_Reviews.csv', index = False)

