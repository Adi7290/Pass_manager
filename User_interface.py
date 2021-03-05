from tkinter import *
from tkinter import messagebox
import string
import random
from PIL import ImageTk,Image
#________________________________To generate a password_________________________________________________

def generate_pass():

    letters_upper = (string.ascii_uppercase)
    letters_lower = (string.ascii_lowercase)
    symbols = (string.punctuation)
    numbers = (string.digits)


    letter1 = random.choice(letters_upper)
    letter2 = random.choice(letters_upper)
    letter3 = random.choice(letters_upper)    
    letter4 = random.choice(letters_upper)    
    letter5 = random.choice(letters_lower)    
    letter6 = random.choice(letters_lower)    
    letter7 = random.choice(letters_lower)    
    letter8 = random.choice(letters_lower)    

    alph = letter1+letter3+letter6+letter8+letter2+letter4+letter7+letter5
    pass_sym1 = random.choice(symbols)
    pass_sym2 = random.choice(symbols)
    pass_sym = pass_sym1+pass_sym2
    pass_num1 = random.choice(numbers)
    pass_num2 = random.choice(numbers)
    pass_num = pass_num1 + pass_num2
    password = alph + pass_num + pass_sym
    password_entry1.insert(0,password)

def save_pass():
    URLNAME = URLNAME_entry.get
    username = Username_entry.get()
    password_entry= password_entry1.get()

    if URLNAME == 0 or username == 0:
        messagebox.showinfo('Please Check both the Field has some value in it')
    ok = messagebox.askokcancel(title='URL',message= f'These are the details entered \n Username :\t {username} \n Password : \t {password_entry}\n You wish to proceed further?')

    if ok:
        with open("data.txt", "w") as data_file:
            data_file.write(f"'URL '{URLNAME} | 'Username :'{username}| 'Password :'{password_entry}")
            URLNAME_entry.delete(0,END)
            password_entry1.delete(0,END)

window = Tk()
window.configure(background="black")
window.title("Password Manager and Generator")
window.configure(padx = 50, pady=50)
canvas = Canvas(height=250, width =250)
canvas.grid(row=0, column=1)

#Labels

URLNAME_Label = Label(text="Enter Your URL: ")
URLNAME_Label.grid(row=1,column=0)
Username_label = Label(text="Email/Username : ")
Username_label.grid(row=2,column=0)
Password_label = Label(text="Password : ")
Password_label.grid(row=3 , column= 0)


#Entries

URLNAME_entry = Entry(width=53)
URLNAME_entry.grid(row=1, column=1, columnspan=2)
URLNAME_entry.focus()
Username_entry = Entry(width=53)
Username_entry.grid(row=2, column=1, columnspan=2)
Username_entry.insert(0, "")
password_entry1 = Entry(width=35)
password_entry1.grid(row=3, column=1)


generate_password = Button(text="Generate Password", width=14, command=generate_pass)
generate_password.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save_pass)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()

