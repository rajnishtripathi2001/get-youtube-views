import time
import random
from selenium import webdriver

def getView(link,views):

    browser = webdriver.Chrome('chromedriver.exe') 

    for i in range(views+1):
        browser.get(link)
        sleep_time=random.randint(45,50)
        #sleep_time = 20

        print("running the video for {} time".format(i))
        print("sleep time is ",sleep_time)
        print("------------------------------------------------")

        time.sleep(sleep_time)

    browser.quit()
        


