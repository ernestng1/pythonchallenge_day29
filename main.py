from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def random_password_generate():
    password_list = []

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    for char in range(nr_letters):
      password_list.append(random.choice(letters))
    for char in range(nr_symbols):
      password_list += random.choice(symbols)
    for char in range(nr_numbers):
      password_list += random.choice(numbers)
    random.shuffle(password_list)
    password_field.delete(0, END)
    password_field.insert(0, "".join(password_list))
    pyperclip.copy("".join(password_list))

# ---------------------------- SAVE PASSWORD ------------------------------- #
def password_submission():
    website = website_field_entry.get()
    email = username_field_entry.get()
    password = password_field_entry.get()


    if website == "":
        messagebox.showinfo(title="No website",
                            message="You did not key in any website."
                                    "\nPlease try again")
    elif password == "":
        messagebox.showinfo(title="No password",
                            message="You did not key in any password."
                                    "\nPlease try again")
    elif email == "":
        messagebox.showinfo(title="No email",
                            message="You did not key in any email."
                                    "\nPlease try again")
    else:
        is_okay = messagebox.askokcancel(title=f"{website}", message="These are the details you have provided:"
                                                                     f"\nEmail: {email}"
                                                                     f"\nPassword: {password}"
                                                                     f"\nDo you to save your result?")
        if is_okay:
            with open("data.txt", "a") as f:
              f.write(f"{website} | {email} | {password}\n")
            website_field.delete(0,END)
            password_field.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width = 200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0,column=1)

website_field_entry = StringVar()
username_field_entry = StringVar()
password_field_entry = StringVar()

website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
website_field = Entry(window, width=55, textvariable=website_field_entry)
website_field.grid(row=1,column=1, columnspan=2)
website_field.focus()

username_label = Label(text="Email/Username:")
username_label.grid(row=2,column=0)
username_field = Entry(window, width=55, textvariable=username_field_entry)
username_field.grid(row=2,column=1, columnspan=2)
username_field.insert(0,"abc@edu.sg")


password_label = Label(text="Password:")
password_label.grid(row=3,column=0)
password_field = Entry(window, width=36, textvariable=password_field_entry)
password_field.grid(row=3,column=1)
password_button = Button(window, text = "Generate Password", command = random_password_generate)
password_button.grid(row=3, column=2)



add_button = Button(window, text = "Add", width=47,
                    command = password_submission)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()