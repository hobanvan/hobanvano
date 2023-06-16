from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# login.txt가 있는지 확인한다. 있을 경우 read하여 ID/PW를 리턴하고 없을 경우 로그인 폼을 띄우고 정보를 받아 login.txt에 저장하고 ID/PW를 리턴하는 함수
def read_logininfo():
    try:
        f = open("login.txt", 'r')
        username = f.readline()
        password = f.readline()
        f.close()
        return username, password
    except FileNotFoundError:
        login_form = Tk()
        login_form.title("Login")
        login_form.geometry("300x200+100+100")
        login_form.resizable(False, False)

        # ID/PW 입력 폼
        username = StringVar()
        password = StringVar()
        Label(login_form, text="ID").grid(row=0, column=0)
        Entry(login_form, textvariable=username).grid(row=0, column=1)
        Label(login_form, text="PW").grid(row=1, column=0)
        Entry(login_form, textvariable=password).grid(row=1, column=1)

        # 로그인 버튼
        def login_btn():
            f = open("login.txt", 'w')
            f.write(username.get() + "\n")
            f.write(password.get() + "\n")
            f.close()
            login_form.destroy()

        Button(login_form, text="Login", command=login_btn).grid(row=2, column=0, columnspan=2)
        login_form.mainloop()

        return username.get(), password.get()
