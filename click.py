from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains #下面這兩個後來沒用到ㄌ
import pyautogui #下面這兩個後來沒用到ㄌ

site = webdriver.ChromeOptions()
# site

browser = webdriver.Chrome(options=site) 

url = 'https://popcat.click' #給網址
browser.get(url) #抓網址
browser.maximize_window() #視窗最大話
sleep(2)#怕有人網頁還沒跑好，所以睡個兩秒

while 1:
    browser.find_element_by_xpath('//*[@id="app"]/img').click() #我是抓標題POPCAT的xpath來點
    browser.find_element_by_xpath('//*[@id="app"]/img').click()
    sleep(0.01) #睡覺
