from tkinter import *
from tkinter import messagebox
import pyperclip
import json

FONT = "Arial"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for item in range(nr_letters)]
    password_sym = [random.choice(symbols) for item in range(nr_symbols)]
    password_num = [random.choice(numbers) for item in range(nr_numbers)]

    password_list = password_letter + password_sym + password_num

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    passentry.delete(0,END)
    passentry.insert(END, password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = webentry.get().lower()
    password = passentry.get()
    email = userentry.get()
    new_data = {website:{
        "email":email,
        "password":password
    }}
    if len(website)==0 or len(password)==0 or len(email)==0:
        messagebox.showinfo(title="Error", message="Please make sure none of the inputs are empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it okay?")

        if is_ok:
            try:
                with open("data.json", mode="r") as file:
                    data = json.load(file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)

            else:
                with open("data.json", mode="w") as file:
                    json.dump(data,file,indent=4)

            webentry.delete(0,END)
            passentry.delete(0, END)

# ---------------------------- Search ------------------------------- #

def search():
    website = webentry.get().lower()
    try:
        with open("data.json") as file:
            data = json.load(file)
            result = data[website]
            messagebox.showinfo(title=website.title(), message=f"The credentials for {website.title()} are \nEmail: {result['email']}\nPassword: {result['password']}")

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    except KeyError:
        messagebox.showinfo(title="Error", message="No such data found")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("MyPass - Password Manager")
window.config(padx=50,pady=100)

image_data = PhotoImage(file="logo.png")
canvas = Canvas(height=200,width=200)
canvas.create_image(100,100,image=image_data)
canvas.grid(column=0,row=0,columnspan=3)

# Website name

weblabel = Label(text="Website : ",font=(FONT,12,"normal"),pady=5,padx=0)
weblabel.grid(column=0,row=1)

webentry = Entry(width=30)
webentry.grid(column=1,row=1,columnspan=2,sticky="W")
webentry.focus()

searchBtn = Button(text="Search", highlightthickness=0,width=15,pady=5, command=search)
searchBtn.grid(column=2,row=1)
# Email name

userlabel = Label(text="Email/Username : ",font=(FONT,12,"normal"),pady=5)
userlabel.grid(column=0,row=2)

userentry = Entry(width=50)
userentry.grid(column=1,row=2,columnspan=2,sticky="W")
userentry.insert(END, "zulkar@gmail.com")

# Password

passlabel = Label(text="Password : ",font=(FONT,12,"normal"),pady=5)
passlabel.grid(column=0,row=3)

passentry = Entry(width=30)
passentry.grid(column=1,row=3,sticky="W")

passbutton  = Button(text="Generate Password", highlightthickness=0,pady=5, command=generate_pass)
passbutton.grid(column=2,row=3,sticky="W")

addbutton  = Button(text="Add", highlightthickness=0,width=20,pady=5, command=save)
addbutton.grid(column=1,row=4,columnspan=1)


window.mainloop()