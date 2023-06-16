from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import login
import iread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager


def open_brower():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver

# selenium driver 생성, chrome driver를 사용한다. 없을 경우 알아서 다운로드
driver = open_brower()
driver.implicitly_wait(3)

# 메인 윈도우 생성 800*600
root = Tk()
root.title("Auto Insta")
root.geometry("800x600+100+100")
root.resizable(False, False)

logininfo = login.read_logininfo()
iread.login(driver, logininfo[0], logininfo[1])

# 메인 윈도우 실행
root.mainloop()










