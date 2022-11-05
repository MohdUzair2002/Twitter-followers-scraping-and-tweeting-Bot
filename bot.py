from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import csv
name=input("Enter the name of twitter username")
no_of_folowers=input("Enter the no of followers you need to scrap and tweet")
chrome_options =webdriver.ChromeOptions()
s=Service(ChromeDriverManager().install())
chrome_options.add_argument("user-data-dir=C:/Users/User/AppData/Local/Google/Chrome/User Data")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=s,options=chrome_options)
wait=WebDriverWait(driver, 60)
url=f'https://twitter.com/{name}/followers'
driver.get(url)
followers_count=0
list_followers=[]
while(len(list_followers)<int(no_of_folowers)*2):
    time.sleep(10)
    followers_scraping=driver.find_elements(By.XPATH,"//div[@class='css-1dbjc4n r-1wbh5a2 r-dnmrzs']//span")
    i=0
    while(i<len(followers_scraping)):
        print(followers_scraping)
        if followers_scraping[i].text not in list_followers:
         list_followers.append((followers_scraping[i]).text)
        else:
            pass
        i+=1
    driver.execute_script("arguments[0].scrollIntoView();", followers_scraping[-1])
    followers_count=int(len(followers_scraping))

# for i in followers_scraping:
#  print( i.text)
# list_followers.append(followers_scraping)
driver.get("https://twitter.com")
# driver.execute_script("arguments[0].click();", tweet)
time.sleep(5)
print(list_followers)
j=0
while(j+10<len(list_followers)):
    tweet= wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']")))
    tweet=driver.find_element(By.XPATH,"//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']")
    tweet.send_keys(str(list_followers[j:j+10]))
    tweet= wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='css-901oao r-1awozwy r-jwli3a r-6koalj r-18u37iz r-16y2uox r-1qd0xha r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0']")))
    tweet_button=driver.find_element(By.XPATH,"//div[@class='css-901oao r-1awozwy r-jwli3a r-6koalj r-18u37iz r-16y2uox r-1qd0xha r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0']")
    driver.execute_script("arguments[0].click();", tweet_button)
    j+=1
time.sleep(30)


