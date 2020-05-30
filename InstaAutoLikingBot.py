from selenium import webdriver  # selenium 的用法可參見 5-7 節
from time import sleep
from selenium.webdriver.common.keys import Keys
# 匯入 time 模組的 sleep() 函式

username='***REMOVED***' #在這裡輸入你的userID
password='***REMOVED***' #在這裡輸入你的密碼

def signIn(driver):
        driver.find_element_by_name('username').send_keys(username) 
        driver.find_element_by_name('password').send_keys(password + "\n") 

def startFlash(driver):
        driver.find_element_by_xpath("//*[contains(text(), 'Not Now')]").click() #按下斥再說
        sleep(1)
        driver.implicitly_wait(2)
        url = 'https://www.instagram.com/'+ username
        driver.get(url)
        sleep(2)
        max = int(driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').get_attribute('textContent'))
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').click()
        
#        followersList = driver.find_element_by_css_selector('div[role=\'dialog\'] ul')
#        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
#        followersList.click()
#        actionChain = webdriver.ActionChains(driver)
#        while (numberOfFollowersInList < max):
#            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
#            numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
#            print(numberOfFollowersInList)
        for index in range(int(driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').get_attribute('textContent'))):
                sleep(1)
                # /html/body/div[4]/div/div[2]/ul/div/li[1]/div/div[2]/div[1]/div/div/a
                # /html/body/div[4]/div/div[2]/ul/div/li[2]/div/div[1]/div
                driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li['+str(index+1)+']/div/div[1]/div').click()#用圖片按follow的人
                #/html/body/div[3]/div/div[2]/ul/div/li[1]/div/div[1]/div[2]/div[1]/a
                driver.implicitly_wait(2)
                try: 
                        driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div/section/header/div/div[1]/div/div/div/a').click() #如果跑出現時就在按進去
                except:
                    print("already in page")
                driver.implicitly_wait(2)
                #點開貼文，開始案愛心
                try:
                        firstPost=driver.find_element_by_css_selector("div[class='v1Nh3 kIKUG  _bz0w']")
                except:
                        print("NO post")
                        driver.get(url)
                        sleep(2)
                        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
                        sleep(2)
                        continue
                print(firstPost)
                firstPost.click()
                sleep(2)
                while True:
                        try:
                                driver.find_element_by_css_selector("span[class='fr66n']").click()
                        except:
                                print("already liked!")
                        sleep(1)
                        try:
                                driver.find_element_by_css_selector("a[class='HBoOv coreSpriteRightPaginationArrow']").click()
                        except:
                                break
                        sleep(1.5)
                driver.get(url)
                sleep(2)
                driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
                sleep(2)
                        
                
                
def main():
        url = 'https://www.instagram.com/accounts/login/?source=auth_switcher' 
        driver=webdriver.Chrome("/home/ncc/桌面/InstaAutoLikingBot/chromedriver")  # 建立瀏覽器物件
        driver.get(url)            
        driver.maximize_window()   # 將視窗最大化
        sleep(2)
        signIn(driver) #登入
        sleep(3)
        startFlash(driver)
main()
