#ig bot
#compatible with Google Chrome browser
#runs a script to like and follow on 
# post found via a hashtag, runs with credentials.py where username and password is required

#from your termanal/bash check for the following dependancies as they are needed to run script
#random-- allows for random choices in hashtag list found at the bottom of the script
#time--allows system to lapse time before next task is executed
#webdriver-- controls the chrome window the bot operates in--this has to be updated locally 
# when chrome updates
#selenim is a webdriver dependency

import random
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from J_credentials import pw, username



#creates IGBot class that logs into IG, no need to change
class InstagramBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome(executable_path= "/Applications/chromedriver")
        self.driver.get("https://instagram.com")
        # self.username = username
        time.sleep(3)
    #this fills in userame
        self.driver.find_element(By.XPATH,("//input[@name= 'username']"))\
           .send_keys(username)
    #this fills in password
        self.driver.find_element(By.XPATH,("//input[@name= 'password']"))\
           .send_keys(pw)
    #this clicks submit
        self.driver.find_element(By.XPATH,("//button[@type= 'submit']"))\
            .click()
        #this sleeps time for 3 seconds
        time.sleep(3)
        #this should close the "Not Now" box if it appears, if it doesnt, it'll keep rolling
        self.driver.find_element(By.XPATH,("//button[contains(text(), 'Not Now')]"))\
           .click()
        time.sleep(3)
       
       
    #         ig.get_photos(tag)
    #this defines the script that navigates to the hashtags(please see bottom for list of hashtags, line 133)
    def get_photos(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(5)

        pic_hrefs = []
        for i in range(1, 7):
            try: 
                # driver.execute_script("window.scrollIntoView(document.querySelector("#react-root > section > main > article > div:nth-child(3)")")

                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
            #searching for the pic link
                
                pic_hrefs_view = driver.find_elements_by_tag_name('a')
                pic_hrefs_view = [elem.get_attribute('href') for elem in pic_hrefs_view
                            if '.com/p/' in elem.get_attribute('href')]
                [pic_hrefs.append(href) for href in pic_hrefs_view if href not in pic_hrefs]
                print(hashtag + ' photos: ' + str(len(pic_hrefs)))
            except Exception:
               continue
        
        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(2)
            try:
               # follow button
                # self.driver.find_element_by_class_name("oW_lN.sqdOP.yWX7d.y3zKF ")\
                    # .click()

                time.sleep(4)
                #like post
                
                # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                self.driver.find_element_by_class_name("_8-yf5 ")\
                    .click()

                time.sleep(2)
               #Message option could initiate here

            # Comment

                comment_box = self.driver.find_element(By.XPATH,("/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea"))\
                    .send_keys('Lovely ✨')
                comment_box.send_keys(Keys.ENTER)
                time.sleep(3)
                # comm_prob = randint(1,10)
                # comment_box = self.driver.find_element(By.XPATH,("/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea"))
                # if (comm_prob < 7):
                #         comment_box.send_keys('Drippy 💧!')
                #         time.sleep(1)
                # elif (comm_prob > 6) and (comm_prob < 9):
                #     comment_box.send_keys('Lovely ✨ :)')
                #     time.sleep(1)
                # elif comm_prob == 9:
                #     comment_box.send_keys('✨✨')
                #     time.sleep(1)
                # elif comm_prob == 9:
                #     comment_box.send_keys('Beautiful.')
                #     time.sleep(1)

                # elif comm_prob == 10:
                #     comment_box.send_keys('Lovely')
                #     time.sleep(1)
                # # Enter to post comment
                # comment_box.send_keys(Keys.ENTER)
                time.sleep(randint(22,28))
                for second in reversed(range(0, random.randint(7,10))):
                    print("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                                    + " | Sleeping " + str(second))
                    time.sleep(2)
                time.sleep(20)
            except Exception as e:
                time.sleep(2)
                unique_photos -= 1

if __name__ == "__main__":

    

    ig = InstagramBot(username, pw)
    
   
   #list of hashtags, code can be ran with minimun one hastag to test that it works
    hashtag = ['accessories', 'fashionable', 'fashionaddict', 'fashiondiaries','fashiongram','instastyle',
                'jewelry', 'trendy', 'trend', 'instaFashion', 'Fashionista', 'ootd']

   
    while True:
        try:
            #Choose a random tag from the list of tags
            tag = random.choice(hashtag)
            ig.get_photos(tag)
        except Exception:
            ig.closeBrowser()
            time.sleep(60)
            ig = InstagramBot(username, pw)
            

