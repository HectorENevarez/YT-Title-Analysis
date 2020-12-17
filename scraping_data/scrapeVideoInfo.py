from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import time

def scrape_vid():
    df = pd.read_csv('vid_links.csv')
    
    webdriver = 'C:/Users/Hneva/OneDrive/Desktop/chromedriver_win32/chromedriver.exe' #Loads in webdriver and binds to chrome
    driver = Chrome(webdriver)
    wait = WebDriverWait(driver, 10)
    new_df = pd.DataFrame(columns=['Channel', 'Subs', 'Title', 'Views', 'Link', 'Likes', 'Dislikes', 'Description'])
    for index, row in df.iterrows():
        driver.get(row['Link'])
        try:
            v_description = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div#description yt-formatted-string"))).text
        except:
            v_description = -1
        try:
            v_title = driver.find_element(By.XPATH, '//*[@id="container"]/h1/yt-formatted-string').text
        except:
            v_title = -1
        try:
            v_text = driver.find_elements(By.XPATH, '//*[@id="text"]')
        except:
            v_text = -1
        try:
            v_views = driver.find_element(By.XPATH, '//*[@id="count"]/yt-view-count-renderer/span[1]').text
        except:
            v_views = -1

        v_dislikes = v_likes = -1

        try:
            if v_text[4].text == 'SHARE':
                v_likes = v_text[2].text
                v_dislikes = v_text[3].text
        except:
            v_dislikes = v_likes = -1

        new_df.loc[len(new_df)] = [row['Channel'], row['Subs'], v_title, v_views, row['Link'], v_likes, v_dislikes, v_description]
        
        print(v_title, v_views, v_dislikes, v_likes)
        new_df.to_csv(r'full_data.csv')
    

if __name__ == "__main__":
    scrape_vid()