from tkinter import*
import pyperclip
import random
color = "#F6F1F1"
window = Tk()
window.title("Password generator")
window.config(padx=20, pady=20, bg=color)
canva = Canvas(height=200, width=200, bg=color)
img = PhotoImage(file="hrx.png")
canva.create_image(100, 100, image=img)
canva.grid(column=0, row=0)
pass_len = IntVar()
pass_str = StringVar()
pass_len.set(0)


def generate():
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
             '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
             '*', '(', ')']
    password = ""
    for _ in range(pass_len.get()):
        password = password+random.choice(pass1)
    pass_str.set(password)


def copy():
    random_password = pass_str.get()
    pyperclip.copy(random_password)


label= Label(text="Tyagi password Generator Service",font="Times 20 bold italic").grid(column=1,row=0)
label1 = Label(text="Enter password length", font="Times 12 bold")
label1.grid(column=0, row=1)
but = Button(text="Generate password", command=generate)
but.grid(column=1, row=2)
label2 = Label(text="copy to cl")
button = Button(text="copy to clipboard", command=copy)
button.grid(column=1, row=3)


lab_entry = Entry(width=20, textvariable=pass_len)
lab_entry.grid(column=1, row=1)
x = Entry(textvariable=pass_str)
x.grid(column=0, row=3)
window.mainloop()
