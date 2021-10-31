from tkinter import *

import password


def button_generate_password():
    outputEntry.delete(0, END)
    generated_password = password.Password(entry.get())
    generated_password.generate_strong_password()
    generated_password.print_password()
    outputEntry.insert(0, generated_password.return_password())


window = Tk()
window.geometry("420x420")
window.title("Password generator")

label = Label(window, text="Entry length of your desired password")
label.pack()
entry = Entry(window)
entry.pack()

button = Button(window, text="Generate password", command=button_generate_password)
button.pack()

outputLabel = Label(window, text="Your password: ")
outputLabel.pack()
outputEntry = Entry(window)
outputEntry.pack()

window.mainloop()

password_length = input("How long password do you require?\n")
