from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
  global password_entry
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_list = []

  password_list += [ random.choice(letters) for char in range(nr_letters)]
  password_list += [ random.choice(numbers) for char in range(nr_symbols)]
  password_list += [ random.choice(symbols) for char in range(nr_numbers)]

  random.shuffle(password_list)

  password = "".join(password_list)
  password_entry.insert(0, password)
  pyperclip.copy(password)
  # print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
  website=website_entry.get()
  email = email_entry.get()
  password = password_entry.get()
  if len(website)==0 or len(password) == 0:
    messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
  else:
    is_ok = messagebox.askokcancel(title=website, message=f" Please Confirm the details: \n Email: {email}\n Password: {password}")

    if is_ok:
      with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="E")
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky="E")
password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="E")

website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()


email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "dummy@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="E")


generate_password_button = Button(text="Generate Password", width=20, command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="W")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
