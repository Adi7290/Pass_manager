from tkinter import *
import string
import random
from SQLAlchemy import all

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
    print(password)

generate_pass()

def save_pass():
    pass

# from tkinter import *
# from tkinter import messagebox
# import random
# import pyperclip
# # ---------------------------- PASSWORD GENERATOR ------------------------------- #
# def generate_password():
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#                'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
#                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#     nr_letters = random.randint(8, 10)
#     nr_symbols = random.randint(2, 4)
#     nr_numbers = random.randint(2, 4)

#     password_letters = [random.choice(letters) for _ in range(nr_letters)]
#     password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
#     password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

#     password_list = password_letters + password_numbers + password_symbols
#     random.shuffle(password_list)

#     password = "".join(password_list)

#     password_entry.insert(0, password)

#     pyperclip.copy(password)





# # ---------------------------- SAVE PASSWORD ------------------------------- #

# def save():

#     website = website_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()

#     if len(website) == 0 or len(password) == 0:
#         messagebox.showinfo(title="Oops", message="Please make sure that each and every field is filled up")

#     is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered : \nEmail: {email} \nPassword: {password} \nAre you sure you want to save this? " )

#     if is_ok:
#         with open("data.txt", "a") as data_file:
#             data_file.write(f"{website} | {email} | {password}\n")
#             website_entry.delete(0, END)
#             password_entry.delete(0, END)






# # ---------------------------- UI SETUP ------------------------------- #

# window = Tk()
# window.title("Password Manager")
# window.config(padx=50, pady=50)

# canvas = Canvas(height=200, width=200)
# logo_img = PhotoImage(file="logo.png")
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(row=0, column=1)

# # labels
# website_label = Label(text="Website :")
# website_label.grid(row=1, column=0)
# email_label = Label(text="Email/Username :")
# email_label.grid(row=2, column=0)
# password_label = Label(text="Password :")
# password_label.grid(row=3, column=0)

# # Entries
# website_entry = Entry(width=53)
# website_entry.grid(row=1, column=1, columnspan=2)
# website_entry.focus()
# email_entry = Entry(width=53)
# email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(0, "mgonugondlamanikanta@gmail.com")
# password_entry = Entry(width=35)
# password_entry.grid(row=3, column=1)

# # Buttons
# generate_password = Button(text="Generate Password", width=14, command=generate_password)
# generate_password.grid(row=3, column=2)
# add_button = Button(text="Add", width=36, command=save)
# add_button.grid(row=4, column=1, columnspan=2)

# window.mainloop()