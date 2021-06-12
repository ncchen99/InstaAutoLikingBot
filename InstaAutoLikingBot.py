
from selenium import webdriver  # selenium
from time import sleep
from selenium.webdriver.common.keys import Keys
# 匯入 time 模組的 sleep() 函式

# ==============================全慾變數===================================
username = ''
password = ''
loveResources = []
lovePostImg = []

# ===============================找對象====================================


def findNewPost(driver):
    global loveResources, lovePostImg
    try:
        for love in driver.find_elements_by_tag_name("article"):
            if not love.find_elements_by_css_selector(
                    "img")[1].get_attribute("src") in lovePostImg:
                loveResources.append(love)
                lovePostImg.append(love.find_elements_by_css_selector(
                    "img")[1].get_attribute("src"))
                break
    except Exception as e:
        print(e)


# ==============================先登『入』==================================
def signIn(driver):
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password + "\n")


# ==============================開始做愛====================================
def makeLove(driver):
    driver.find_element_by_xpath(
        "//*[contains(text(), 'Not Now')]").click()  # 按先不要
    sleep(3)
    driver.find_element_by_xpath(
        "//*[contains(text(), 'Not Now')]").click()  # 按下斥再說
    sleep(1)
    # 找到貼文，開始案愛心
    loveResources.append(driver.find_element_by_tag_name("article"))
    lovePostImg.append(loveResources[0].find_elements_by_css_selector(
        "img")[1].get_attribute("src"))
    sleep(2)
    count = 0
    while(count < len(loveResources)):
        try:
            try:
                loveResources[count].find_element_by_css_selector(
                    "svg[aria-label='Like']").click()
                print("💝成功")
            except:
                loveResources[count].find_element_by_css_selector(
                    "div[data-testid='post-comment-root']").click()
                print("按過💝了")
            count += 1
            findNewPost(driver)
            sleep(2)
        except Exception as e:
            print(e)
            findNewPost(driver)
            count += 1
            print("skip...")


def main():
    global username, password
    username = input("輸入尼的IG使用者名子：")
    password = input("輸入尼的密碼：")
    url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
    driver = webdriver.Chrome("./chromedriver")  # 建立瀏覽器物件
    driver.get(url)
    driver.maximize_window()   # 將視窗最大化
    sleep(3)
    signIn(driver)  # 登入
    sleep(5)
    makeLove(driver)  # 作愛


if __name__ == "__main__":
    main()
