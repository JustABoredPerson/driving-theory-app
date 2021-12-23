import tkinter as tk
from tkinter.constants import END
from PIL import ImageTk, Image
import csv

def login():

    with open("/Users/nick/Documents/GitHub/driving-theory-app/usernames_passwords.csv", 'r') as csv_file:

        usernames = []
        passwords = []

        csv_reader = csv.reader(csv_file)

        next(csv_reader)

        for line in csv_reader:
            usernames.append(line[0])
            passwords.append(line[1])
        
        user_bool = False
        pass_bool = False
        a = 0

        for x in range(0, len(usernames)):

            if username_field.get() == usernames[a]:
                user_bool = True
            
            if password_field.get() == passwords[a]:
                pass_bool = True

            if pass_bool and user_bool:
                registering_new_acc()
            else:
                user_bool = False
                pass_bool = False
                a+=1
        if user_bool == False and pass_bool == False:
            print("incorrect")

def registering_new_acc():
    print("you are now registering a new account")

def topics():
    print("your now in topics")

def register_acc():
    print("your now registering an account")

def clearTextbox():
    username_field.delete(0, END)
    password_field.delete(0, END)

root = tk.Tk()
root.geometry("1450x770")

canvas = tk.Canvas(root, height=1750, width=770, bd=-2)
canvas.pack()

#Resizes the background image to fit the dimentions of the canvas
background = Image.open("/Users/nick/Documents/GitHub/driving-theory-app/background.png")
resized = background.resize((1450, 770), Image.ANTIALIAS)
app_background = ImageTk.PhotoImage(resized)

background_label = tk.Label(root, image=app_background)
background_label.place(anchor="nw")

username_field = tk.Entry(root)
username_field.place(x=650, y=350, height= 30, width=200)

password_field = tk.Entry(root)
password_field.place(x=650, y=426, height= 30, width=200)

submit_button = tk.Button(root, text= "Submit", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:[login(), clearTextbox()])
submit_button.place(x=900, y=375, height= 60, width=150)

reg_new_acc_button = tk.Button(root, text= "Click here to register an account if you dont have one", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:register_acc())
reg_new_acc_button.place(x=530, y=575, height= 60, width=450)

root.mainloop()
