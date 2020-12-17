from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import time

def scrape_data():
    webdriver = 'C:/Users/Hneva/OneDrive/Desktop/chromedriver_win32/chromedriver.exe' #Loads in webdriver and binds to chrome
    driver = Chrome(webdriver)
    df = pd.DataFrame(columns= ['Channel', 'Link', 'Subs'])
    chan = pd.read_csv('youtuber_list.csv')
    chan = set(chan['channel_id'])
    wait = WebDriverWait(driver, 10)

    for c in chan:
        youtube_link = 'https://www.youtube.com/channel/' + c + '/videos'
        driver.get(youtube_link)
        try:
            v_channelName = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"yt-formatted-string#text.style-scope.ytd-channel-name"))).text
            v_subs = driver.find_element(By.CSS_SELECTOR, "yt-formatted-string#subscriber-count.style-scope.ytd-c4-tabbed-header-renderer").text
        except:
            v_channelName = -1
            v_subs = -1
        counter = 0
        while counter < 9: #Each 10 loops captures ~200 pieces of data
            # Get old scroll position
            old_position = driver.execute_script(
                    ("return (window.pageYOffset !== undefined) ?"
                     " window.pageYOffset : (document.documentElement ||"
                     " document.body.parentNode || document.body);"))
            # Sleep and Scroll
            time.sleep(1)
            driver.execute_script((
                    "var scrollingElement = (document.scrollingElement ||"
                    " document.body);scrollingElement.scrollTop ="
                    " scrollingElement.scrollHeight;"))
            # Get new position
            new_position = driver.execute_script(
                    ("return (window.pageYOffset !== undefined) ?"
                     " window.pageYOffset : (document.documentElement ||"
                     " document.body.parentNode || document.body);"))
            counter += 1
        try:
            v_link = driver.find_elements(By.CSS_SELECTOR, "a#video-title.yt-simple-endpoint.style-scope.ytd-grid-video-renderer")
        except:
            v_link = -1


        
        for x in v_link:
            try:
                link = x.get_attribute('href')
            except:
                link = -1

            df.loc[len(df)] = [v_channelName, link, v_subs]
            print(v_channelName, link, v_subs) 
        df.to_csv(r'vid_links.csv')

if __name__ == "__main__":
    scrape_data()
    