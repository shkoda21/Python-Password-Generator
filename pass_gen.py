import string
import random
from tkinter import *
from tkinter import messagebox
import pyperclip


window = Tk()
window.geometry("600x400")
window.resizable(0, 0)
window.title("PASSWORD GENERATOR")
greeting = Label(text="Password Generator", font='arial 16 bold', fg="blue").pack()
passw_string = StringVar()
pass_label = Label(window, text='Password Length', font='arial 12 bold').pack()


len_password = IntVar()
spinbox = Spinbox(window, from_=8, to_=16, textvariable=len_password, width=8).pack()


def gen_password():
    try:
        if 8 <= len_password.get() <= 16 and isinstance(len_password.get(), int):
            password = ''
            password += random.choice(string.ascii_lowercase) + \
                random.choice(string.ascii_uppercase) + \
                random.choice(string.digits) + \
                random.choice(string.punctuation)
            for j in range(len_password.get() - 4):
                password += random.choice(string.ascii_letters + string.digits + string.punctuation)
        else:
            messagebox.showinfo('Error', 'Please, use the number between 8 and 16')
    except TclError:
        messagebox.showinfo('Error', 'Please, use the number between 8 and 16')
    return passw_string.set(password)


button = Button(window, text="Generate Password", command=gen_password)
button.pack(pady=5)
Entry(window, textvariable=passw_string).pack()


def copy_passw():
    pyperclip.copy(passw_string.get())


Button(window, text='Copy to clipboard', command=copy_passw).pack(pady=5)
window.mainloop()
