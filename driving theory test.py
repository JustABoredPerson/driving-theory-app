import tkinter as tk
from tkinter.constants import END
from PIL import ImageTk, Image
import csv
from tkinter import messagebox

root = tk.Tk()

username_field = tk.Entry(root)
password_field = tk.Entry(root)

reg_username_field = tk.Entry(root)
reg_password_field = tk.Entry(root)
re_enter_password_field = tk.Entry(root)

name = username_field.get()

background = Image.open("/Users/nick/Documents/GitHub/driving-theory-app/background.png")
resized = background.resize((1450, 770), Image.ANTIALIAS)
app_background = ImageTk.PhotoImage(resized)

reg_background = Image.open("/Users/nick/Documents/GitHub/driving-theory-app/reg_background.png")
reg_resized = reg_background.resize((1450, 770), Image.ANTIALIAS)
reg_background = ImageTk.PhotoImage(reg_resized)

topics_background = Image.open("/Users/nick/Documents/GitHub/driving-theory-app/topics_background.png")
topics_resized = topics_background.resize((1450, 770), Image.ANTIALIAS)
topics_background = ImageTk.PhotoImage(topics_resized)



def loginScreen():
    global username_field
    global password_field
    global root
    global name
    
    root.geometry("1450x770")

    canvas = tk.Canvas(root, height=1750, width=770, bd=-2)
    canvas.pack()

    #Resizes the background image to fit the dimentions of the canvas
    background_label = tk.Label(root, image=app_background)
    background_label.place(anchor="nw")

    username_field = tk.Entry(root)
    username_field.place(x=650, y=350, height= 30, width=200)
    
    password_field = tk.Entry(root)
    password_field.place(x=650, y=426, height= 30, width=200)

    submit_button = tk.Button(root, text= "Submit",bg = 'gray' ,padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:[loginProcess(), clearTextboxinLogin()])
    submit_button.place(x=900, y=375, height= 60, width=150)

    reg_new_acc_button = tk.Button(root, text= "Click here to register an account if you dont have one", padx= 60, pady= 20, font=("Helvitca", 18) ,command=lambda:registering_new_acc_Screen())
    reg_new_acc_button.place(x=530, y=575, height= 60, width=450)

    def clearTextboxinLogin():
        username_field.delete(0, END)
        password_field.delete(0, END)
    
    def loginProcess():
        global root
        global name
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
                    name = username_field.get()
                    topicsScreen()
                else:
                    user_bool = False
                    pass_bool = False
                    a+=1
            if user_bool == False and pass_bool == False:
                message_popup('login')
                print("incorrect")

def registering_new_acc_Screen():
    global root
    global name
    for widgets in root.winfo_children():
      widgets.destroy()
    
    reg_background_label = tk.Label(root, image=reg_background)
    reg_background_label.place(anchor="nw")

    reg_username_field = tk.Entry(root)
    reg_username_field.place(x=650, y=280, height= 30, width=200)

    reg_password_field = tk.Entry(root)
    reg_password_field.place(x=650, y=400, height= 30, width=200)

    re_enter_password_field = tk.Entry(root)
    re_enter_password_field.place(x=650, y=520, height= 30, width=200)

    submit_button = tk.Button(root, text= "Submit", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:[uploading_details_and_logging_in(), clearTextboxinReg()])
    submit_button.place(x=670, y=600, height= 30, width=150)

    back_button = tk.Button(root, text= "Back", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:loginScreen())
    back_button.place(x=470, y=580, height= 30, width=100)

    def clearTextboxinReg():
        reg_username_field.delete(0, END)
        reg_password_field.delete(0, END)
        re_enter_password_field.delete(0, END)

    def uploading_details_and_logging_in():
        if reg_password_field.get() == re_enter_password_field.get():
            with open("/Users/nick/Documents/GitHub/driving-theory-app/usernames_passwords.csv",'a', newline='') as f:
                thewriter = csv.writer(f)
                thewriter.writerow([reg_username_field.get(),reg_password_field.get()])
                name = username_field.get()
                topicsScreen()
        else: 
            message_popup('reg')

def topicsScreen():
    global root
    for widgets in root.winfo_children():
      widgets.destroy()
    topics_background_label = tk.Label(root, image=topics_background)
    topics_background_label.place(anchor="nw")

    road_and_traffic_button = tk.Button(root, text= "Road and Traffic signs", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:questionsScreen('road'))
    road_and_traffic_button.place(x=100, y=250, height= 40, width=200)

    attitude_button = tk.Button(root, text= "Attitude", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:questionsScreen('attitude'))
    attitude_button.place(x=470, y=250, height= 40, width=200)

    hazard_awareness_button = tk.Button(root, text= "Hazard Awareness", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:questionsScreen('hazard'))
    hazard_awareness_button.place(x=840, y=250, height= 40, width=200)

    motorway_rules_button = tk.Button(root, text= "Motorwawy Rules", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:questionsScreen('motorway'))
    motorway_rules_button.place(x=1180, y=250, height= 40, width=200)

    alertness_button = tk.Button(root, text= "Alertness", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:questionsScreen('alertness'))
    alertness_button.place(x=100, y=530, height= 40, width=200)

    documents_button = tk.Button(root, text= "Documents", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:questionsScreen('documents'))
    documents_button.place(x=470, y=520, height= 40, width=200)

    incidents_button = tk.Button(root, text= "Incidents", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:questionsScreen('incidents'))
    incidents_button.place(x=850, y=530, height= 40, width=200)

    vulnerable_button = tk.Button(root, text= "Vulnerable Road Users", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:questionsScreen('vulnerable'))
    vulnerable_button.place(x=1190, y=540, height= 40, width=200)

    random_button = tk.Button(root, text= "Random", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:questionsScreen('random'))
    random_button.place(x=1070, y=80, height= 40, width=160)

    welcome_text = tk.Label(root, text= "Hello "+ name + " - Pick the specific topic you would like to practice. \n You can also select Random for a mixture of all the topics", font=("Helvitca", 18))
    welcome_text.place(x=350, y=40, height= 120, width=590)

def questionsScreen(topic):
    print("placeholder")

    global root
    global name

    for widgets in root.winfo_children():
      widgets.destroy()

    if topic == 'road':
        print("placeholder")
    if topic == 'attitude':
        print("placeholder")
    if topic == 'hazard':
        print("placeholder")
    if topic == 'motorway':
        print("placeholder")
    if topic == 'alertness':
        print("placeholder")
    if topic == 'documents':
        print("placeholder")
    if topic == 'incidents':
        print("placeholder")
    if topic == 'road':
        print("placeholder")
    if topic == 'vulnerable':
        print("placeholder")
    if topic == 'random':
        print("placeholder")

def message_popup(reason):
    if reason == 'login':
        messagebox.showerror("Error", "Username and password don't match. Try again.")
    elif reason == 'reg':
        messagebox.showerror("Error", "Password doesn't match. Try again.")

# loginScreen()
topicsScreen()
root.mainloop()
