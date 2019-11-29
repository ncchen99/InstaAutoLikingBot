from selenium import webdriver  # selenium 的用法可參見 5-7 節
from time import sleep
# 匯入 time 模組的 sleep() 函式

username='***REMOVED***' #在這裡輸入你的userID
password='***REMOVED***' #在這裡輸入你的密碼

def signIn(driver):
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(username) 
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(password + "\n") 

def startFlash(driver):
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click() #按下斥再縮
        driver.implicitly_wait(2)
        url = 'https://www.instagram.com/'+ username
        driver.get(url)
        sleep(2)
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').click()
        for index in range(int(driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').get_attribute('textContent'))):
                sleep(1)
                driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li['+str(index+1)+']/div/div[1]/div').click()#用圖片按follow的人
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
                                print (driver.find_element_by_css_selector("span[class='glyphsSpriteHeart__outline__24__grey_9 u-__7']").get_attribute('textContent'))
                                driver.find_element_by_css_selector("span[class='glyphsSpriteHeart__outline__24__grey_9 u-__7']").get_attribute('textContent')
                                driver.find_element_by_css_selector("span[class='fr66n']").click()
                        except:
                                print("already liked!")
                                
                        try:
                                driver.find_element_by_css_selector("a[class='HBoOv coreSpriteRightPaginationArrow']").click()
                        except:
                                break
                        sleep(2)
                driver.get(url)
                sleep(2)
                driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
                sleep(2)
                        
                
                
def main():
        url = 'https://www.instagram.com/accounts/login/?source=auth_switcher' 
        driver=webdriver.Chrome()  # 建立瀏覽器物件
        driver.get(url)            
        driver.maximize_window()   # 將視窗最大化
        signIn(driver) #登入
        driver.implicitly_wait(2)
        startFlash(driver)
main()
