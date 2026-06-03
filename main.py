from tkinter import *
from random import choice, randint, shuffle

def password_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

def save():
    web_site = Website_entry.get()
    e_mail = email_entry.get()
    Pass_word = password_entry.get()
    
    with open("mypassword.txt", "a") as file:
        file.write(f"{web_site} | {e_mail} | {Pass_word}\n")
        Website_entry.delete(0, END)
        password_entry.delete(0, END)

window = Tk()
window.title("Password Generate")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

Website = Label(text="Web site Name")
Website.grid(row=1, column=0)
email = Label(text="Enter Email ID")
email.grid(row=2, column=0)
Password = Label(text="Password")
Password.grid(row=3, column=0)

Website_entry = Entry(width=35)
Website_entry.grid(row=1, column=1, columnspan=2)
Website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "anil@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

password_generate_button = Button(text="Generate Password", command=password_generate)
password_generate_button.grid(row=3, column=2)
add = Button(text="add", width=36, command=save)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
