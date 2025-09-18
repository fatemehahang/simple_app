from tkinter import *
import tkinter.messagebox as msg
from data_access.database_manage import save_user
from tools.validation import *

def save_button():
    try:
        username_validator(username.get())
        password_validator(password.get())
        nickname_validator(nickname.get())
        save_user(username.get(), password.get(), nickname.get(),locked.get())
        msg.showinfo("saved", f"User saved")
        username.set("")
        password.set("")
        nickname.set("")
    except Exception as e:
        msg.showerror("Error", f"{e}")

window = Tk()
window.title("user profile")
window.geometry("500x300")
#Username
username = StringVar()
Label(window, text="username", bg="yellow", fg="black").pack(x=20, y=20)
Entry(window, textvariable=username).pack(x=100, y=40)
#Password
password = StringVar()
Label(window, text="password", bg="yellow", fg="black").pack(x=20, y=60)
Entry(window, show="*", textvariable=password).pack(x=100, y=60)
#nickname
nickname = StringVar()
Label(window, text="nickname", bg="yellow", fg="black").place(x=20, y=100)
Entry(window, textvariable=nickname).pack(x=100, y=100)
#Locked
locked = BooleanVar(value=True)
Label(window, text="locked").place(x=20, y=200)
Checkbutton(window, variable=locked).pack(x=100, y=200)

Button(window, text="save", width=15, command=save_button).pack(x=70, y=240)
window.mainloop()
