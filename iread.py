from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# selenium을 통하여 instagram login하는 함수, username과 password을 튜플로 인자를 받는다
def login(driver, id, pw):
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(1)

    # username 입력
    username = driver.find_element_by_name("username")
    username.send_keys(id)
    time.sleep(1)

    # password 입력
    password = driver.find_element_by_name("password")
    password.send_keys(pw)
    time.sleep(1)

    # login 버튼 클릭
    login_btn = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
    login_btn.click()
    time.sleep(3)

