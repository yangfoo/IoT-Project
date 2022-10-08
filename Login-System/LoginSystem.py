import tkinter as tk
from tkinter import *
import os

class Main:
    def __init__(self, window):
        self.window = window
        self.window.geometry('300x260')
        self.window.title('Login Page')
        Label(text="Login or Register", bg="#b1abf1", fg="white",
          width="300", height="2", font=("Calibri", 13)).pack(padx=20, pady=23 )
        Button(text="LOGIN", height="2", width="15", fg="#c0ecc0",command=self.login).pack(padx=1, pady=20)
        Button(text="REGISTER", height="2", width="15",fg="#D8BFD8", command=self.register).pack(padx=1, pady=5)

    def register(self):
        register_screen = RegisterPage(self.window)

    def login(self):
        login_screen = LoginPage(self.window)
        
    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')

class RegisterPage:
    def __init__(self, window):
        self.window = Toplevel(window)
        self.window.title("Register")
        self.window.geometry("320x350")
        self.username = StringVar()
        self.password = StringVar()

        Label(self.window, text="Enter Details Below to Login!",bg="#D8BFD8", fg="black",
            width="300", height="2",font=("Calibri", 13)).pack(padx=20, pady=23 )
        Label(self.window, text="").pack()

        unLabel = Label(self.window, text="Username",fg="black", bg="#D8BFD8")
        unLabel.pack(pady=5)

        unEntry = Entry(self.window, textvariable=self.username)
        unEntry.pack()

        passLabel = Label(self.window, text="Password",fg="black" , bg="#D8BFD8")
        passLabel.pack(pady=5)

        passEntry = Entry(self.window,textvariable=self.password, show='*')
        passEntry.pack()

        Label(self.window, text="").pack()
        Button(self.window, text="Register", width=10, height=1, fg="black", command=self.register_user).pack()
    
    def register_user(self):
        username_info = self.username.get()
        password_info = self.password.get()

        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()

        Label(self.window, text="Registration Success", fg="green", font=("calibri", 11)).pack()

class LoginPage:
    def __init__(self, window):
        self.window = Toplevel(window)
        self.window.title("Login")
        self.window.geometry("320x350")
        Label(self.window,text="Enter Details Below to Login!",bg="#c0ecc0", fg="black",
            width="300", height="2",font=("Calibri", 13)).pack(padx=20, pady=23 )
        Label(self.window, text="").pack()

        global username_verify
        global password_verify

        username_verify = StringVar()
        password_verify = StringVar()

        global username_login_entry
        global password_login_entry

        Label(self.window, text="Username",fg="black", bg="#c0ecc0").pack()
        username_login_entry = Entry(self.window, textvariable=username_verify)
        username_login_entry.pack(pady=5)

        Label(self.window, text="").pack()
        Label(self.window, text="Password",fg="black", bg="#c0ecc0").pack(pady=5)

        password_login_entry = Entry(self.window, textvariable=password_verify, show='*').pack()

        Label(self.window, text="").pack()
        Button(self.window, text="Login",width=10,fg="black" ,height=1, command=self.login_verify).pack()

    def login_verify(self):
        username1 = username_verify.get()
        password1 = password_verify.get()

        list_of_files = os.listdir()
        if username1 in list_of_files:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                self.login_sucess()
            else:
                self.password_not_recognised()
        else:
            self.user_not_found()
    
    def login_sucess(self):
        self.login_success_screen = Toplevel(self.window)
        self.login_success_screen.title("Success")
        self.login_success_screen.geometry("150x100")
        Label(self.login_success_screen, text="Login Success").pack()
        Button(self.login_success_screen, text="OK", command=self.delete_login_success).pack()

    def password_not_recognised(self):
        self.password_not_recog_screen = Toplevel(self.window)
        self.password_not_recog_screen.title("ERROR")
        self.password_not_recog_screen.geometry("150x100")
        Label(self.password_not_recog_screen, text="Invalid Password").pack()
        Button(self.password_not_recog_screen, text="OK", command=self.delete_password_not_recognised).pack()

    def user_not_found(self):
        self.user_not_found_screen = Toplevel(self.window)
        self.user_not_found_screen.title("ERROR")
        self.user_not_found_screen.geometry("150x100")
        Label(self.user_not_found_screen,fg="red", text="User Not Found!").pack(pady=20)
        Button(self.user_not_found_screen, text="OK", command=self.delete_user_not_found_screen).pack()

    def delete_login_success(self):
        self.login_success_screen.destroy()

    def delete_password_not_recognised(self):
        self.password_not_recog_screen.destroy()

    def delete_user_not_found_screen(self):
        self.user_not_found_screen.destroy()

def page():
    window = Tk()
    Main(window)
    window.mainloop()


if __name__ == '__main__':
    page()
    # main_acc()