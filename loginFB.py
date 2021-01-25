from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

#1. Khai bao bien browser
browser = webdriver.Chrome(executable_path="./chromedriver")

#2. Mo thu Web
browser.get("http://facebook.com")

#2a. Dien thong tin User
print ("NameUser: ")
usr = input()
usrname = browser.find_element_by_id("email")
usrname.send_keys(usr)

print ("PassUser: ")
pawd =input()
usrpawd = browser.find_element_by_id("pass")
usrpawd.send_keys(pawd)

#2b. Login Account
usrpawd.send_keys(Keys.ENTER)

#3. Dung chuong trinh 5s
sleep(5)

#4. Dong trinh duyet
browser.close()
