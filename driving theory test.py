from tkinter import *
import tkinter as tk
from tkinter.constants import END
from PIL import ImageTk, Image
import csv
from tkinter import messagebox

score = 0

root = tk.Tk()

vara1 = IntVar()
vara2 = IntVar()
vara3 = IntVar()
vara4 = IntVar()

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

class road_questions:
            def __init__(self, q, a1, a2, a3, a4, pic):
                self.q = q
                self.a1 = a1
                self.a2 = a2
                self.a3 = a3
                self.a4 = a4
                self.pic = pic

roadsq1 = road_questions("When may you use hazard warning lights while you're driving?", "Instead of sounding the horn in a \n built-up area between 11.30pm and 7.00am", "On rural routes, after \n a sign warniing of animals", "On a motorway or undrestricted rual \n carridgeway, to warn of a hazard ahead", "On the approach to toucan crossings, \n where cyclists are waiting to cross", "/Users/nick/Documents/GitHub/driving-theory-app/road-question-images/hazard_lights.png")
roadsq2 = road_questions("What does this sign mean?", "No entry for traffic turning left", "Turn left for parking area", "Turn left for ferry terminal", "No through road on the left", "/Users/nick/Documents/GitHub/driving-theory-app/road-question-images/no_through_road.png")
roadsq3 = road_questions("What does this traffic sign mean?", "Advisory maximum speed Limit", "Compulstory maximum speed limit", "Advised seperation distance", "Compulsory minimum speed limit", "/Users/nick/Documents/GitHub/driving-theory-app/road-question-images/speedlimit.png")
roadsq4 = road_questions("What should you do when you're approaching traffic lights that have red and amber showing together?", "Pass the lights if the road is clear", "Wait for the green light", "Stop because the lights are changing to red", "Take care becuase there's a fault with the lights", "/Users/nick/Documents/GitHub/driving-theory-app/road-question-images/red_yellow.png")
roadsq5 = road_questions("You're in a tunnel and you see this sign, What does it mean?", "Beware of pedestrians crossing ahead", "Beware of pedestrians: no footpath ahead", "Diretions to an emergrency pedestrian exit", "No access for pedestrians", "/Users/nick/Documents/GitHub/driving-theory-app/road-question-images/exit.png")


# THESE ARE PICTURES FOR THE ROAD QUESTIONS
imgRoad1 = Image.open(roadsq1.pic)
resizedRoad1 = imgRoad1.resize((400, 300), Image.ANTIALIAS)
img_Road_1 = ImageTk.PhotoImage(resizedRoad1)

imgRoad2 = Image.open(roadsq2.pic)
resizedRoad2 = imgRoad2.resize((400, 300), Image.ANTIALIAS)
img_Road_2 = ImageTk.PhotoImage(resizedRoad2)

imgRoad3 = Image.open(roadsq3.pic)
resizedRoad3 = imgRoad3.resize((400, 300), Image.ANTIALIAS)
img_Road_3 = ImageTk.PhotoImage(resizedRoad3)

imgRoad4 = Image.open(roadsq4.pic)
resizedRoad4 = imgRoad4.resize((400, 300), Image.ANTIALIAS)
img_Road_4 = ImageTk.PhotoImage(resizedRoad4)

imgRoad5 = Image.open(roadsq5.pic)
resizedRoad5 = imgRoad5.resize((400, 300), Image.ANTIALIAS)
img_Road_5 = ImageTk.PhotoImage(resizedRoad5)


class attitude_questions:
            def __init__(self, q, a1, a2, a3, a4, pic):
                self.q = q
                self.a1 = a1
                self.a2 = a2
                self.a3 = a3
                self.a4 = a4
                self.pic = pic

attitudesq1 = attitude_questions("What's the minimum time gap you should leave when following a vehicle on a wet road?", "One second", "Four seconds", "Three Seconds", "Two seconds", "/Users/nick/Documents/GitHub/driving-theory-app/attitudes-question-images/wet_road.png")
attitudesq2 = attitude_questions("When should you leave a two-second gap between your vehicle and the one in front?", "When it's icy", "When it's foggy", "When it's dry", "When it's raining", "/Users/nick/Documents/GitHub/driving-theory-app/attitudes-question-images/time_gap.png")
attitudesq3 = attitude_questions("You're approaching a zebra crossing. What should you do if pedestrians are waiting to cross", "Use your headlights to iindicate they can cross", "Slow down and prepare to stop", "Wave at them to cross the road", "Give way to older and infirm people only", "/Users/nick/Documents/GitHub/driving-theory-app/attitudes-question-images/pedestrians_crossing.png")
attitudesq4 = attitude_questions("You're waiting in a traffic queue at night. How can you avoid dazzliing drivers behind you?", "Keep your foot on the footbrake", "Use the parking brake and the footbrake together", "Use the parking brake and release the footbrake", "Balance the clutch with the accelerator","/Users/nick/Documents/GitHub/driving-theory-app/attitudes-question-images/night_traffic.png")
attitudesq5 = attitude_questions("What style of driving causes increased risk to everyone?", "Responsible", "Considerate", "Defensive", "Competative", "/Users/nick/Documents/GitHub/driving-theory-app/attitudes-question-images/car_road.png")

imgAttitude1 = Image.open(attitudesq1.pic)
resizedAttitude1 = imgAttitude1.resize((400, 300), Image.ANTIALIAS)
img_Attitude_1 = ImageTk.PhotoImage(resizedAttitude1)

imgAttitude2 = Image.open(attitudesq2.pic)
resizedAttitude2 = imgAttitude2.resize((400, 300), Image.ANTIALIAS)
img_Attitude_2 = ImageTk.PhotoImage(resizedAttitude2)

imgAttitude3 = Image.open(attitudesq3.pic)
resizedAttitude3 = imgAttitude3.resize((400, 300), Image.ANTIALIAS)
img_Attitude_3 = ImageTk.PhotoImage(resizedAttitude3)

imgAttitude4 = Image.open(attitudesq4.pic)
resizedAttitude4 = imgAttitude4.resize((400, 300), Image.ANTIALIAS)
img_Attitude_4 = ImageTk.PhotoImage(resizedAttitude4)

imgAttitude5 = Image.open(attitudesq5.pic)
resizedAttitude5 = imgAttitude5.resize((400, 300), Image.ANTIALIAS)
img_Attitude_5 = ImageTk.PhotoImage(resizedAttitude5)

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

    global vara1
    global vara2 
    global vara3 
    global vara4
    global score
    global root
    global name

    for widgets in root.winfo_children():
      widgets.destroy()

    if topic == 'road':

        def checkIfRight(questionNum):

            global score
            global vara1
            global vara2 
            global vara3 
            global vara4
            global score
            global root
            

            if questionNum == 1:

                if  vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara3.get() == 1 and vara1.get() == 0 and vara2.get() == 0 and vara4.get() == 0:
                    score +=1 
                    question2()
                else: 
                    question2()

            elif questionNum == 2: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara4.get() == 1 and vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0:
                    score +=1 
                    question3()
                else: 
                    question3()
            
            elif questionNum == 3: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara2.get() == 1 and vara1.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    score +=1 
                    question4()
                else: 
                    question4()

            elif questionNum == 4: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara2.get() == 1 and vara1.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    score +=1 
                    question5()
                else: 
                    question5()

            elif questionNum == 5: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara3.get() == 1 and vara1.get() == 0 and vara2.get() == 0 and vara4.get() == 0:
                    score +=1 
                    resultsScreen()
                else: 
                    resultsScreen()
        
        def displayQuestion(q, a1, a2, a3, a4, questionNum):

            global root
            global img_background_label
            
            def q1():

                global root
                global img_Road_1 

                canvasRoad = tk.Canvas(root, height=500, width=500, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Road_1)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=0, y=50, height= 100, width=1700)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(1))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q2():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=500, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Road_2)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=0, y=50, height= 100, width=1700)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(2))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q3():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Road_3)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(3))
                next_button.place(x=1300, y=680, height= 30, width=100)
            
            def q4():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Road_4)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(4))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q5():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Road_5)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(5))
                next_button.place(x=1300, y=680, height= 30, width=100)

            if questionNum == 1:
                q1()
            
            if questionNum == 2:
                q2()
            
            if questionNum == 3:
                q3()

            if questionNum == 4:
                q4()
            
            if questionNum == 5:
                q5()

        def question1():
            displayQuestion(roadsq1.q, roadsq1.a1, roadsq1.a2, roadsq1.a3, roadsq1.a4, 1)
        
        def question2():
            displayQuestion(roadsq2.q, roadsq2.a1, roadsq2.a2, roadsq2.a3, roadsq2.a4, 2)

        def question3():
            displayQuestion(roadsq3.q, roadsq3.a1, roadsq3.a2, roadsq3.a3, roadsq3.a4, 3)

        def question4():
            displayQuestion(roadsq4.q, roadsq4.a1, roadsq4.a2, roadsq4.a3, roadsq4.a4, 4)
        
        def question5():
            displayQuestion(roadsq5.q, roadsq5.a1, roadsq5.a2, roadsq5.a3, roadsq5.a4, 5)

    if topic == 'attitude':

        def checkIfRight(questionNum):

            global score
            global vara1
            global vara2 
            global vara3 
            global vara4
            global score
            global root
            

            if questionNum == 1:

                if  vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara2.get() == 1 and vara1.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    score +=1 
                    question2()
                else: 
                    question2()

            elif questionNum == 2: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara3.get() == 1 and vara1.get() == 0 and vara2.get() == 0 and vara4.get() == 0:
                    score +=1 
                    question3()
                else: 
                    question3()
            
            elif questionNum == 3: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara2.get() == 1 and vara1.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    score +=1 
                    question4()
                else: 
                    question4()

            elif questionNum == 4: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara3.get() == 1 and vara1.get() == 0 and vara2.get() == 0 and vara4.get() == 0:
                    score +=1 
                    question5()
                else: 
                    question5()

            elif questionNum == 5: 

                if vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0 and vara4.get() == 0:
                    message_popup('select')
                elif vara4.get() == 1 and vara1.get() == 0 and vara2.get() == 0 and vara3.get() == 0:
                    score +=1 
                    resultsScreen()
                else: 
                    resultsScreen()
    
        def displayQuestion(q, a1, a2, a3, a4, questionNum):

            global root
            global img_background_label
            
            def q1():

                global root
                global img_attitudes_1 

                canvasRoad = tk.Canvas(root, height=500, width=500, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Attitude_1)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=0, y=50, height= 100, width=1700)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(1))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q2():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=500, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Attitude_2)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=0, y=50, height= 100, width=1700)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(2))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q3():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Attitude_3)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(3))
                next_button.place(x=1300, y=680, height= 30, width=100)
            
            def q4():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Attitude_4)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(4))
                next_button.place(x=1300, y=680, height= 30, width=100)

            def q5():

                global root
                global img_background_label

                canvasRoad = tk.Canvas(root, height=500, width=400, bd=-2)
                canvasRoad.pack()

                
                img_background_label = tk.Label(root, image=img_Attitude_5)
                img_background_label.place(x=500, y=200)

                questionLabel = tk.Label(root, text = q, font=("Helvitca", 25))
                questionLabel.place(x=50, y=50, height= 100, width=1000)

                checkboxa1 = Checkbutton(root, text = a1, font=("Helvitca", 18), variable = vara1)
                checkboxa1.deselect()
                checkboxa1.place(x=200, y=540, height= 40, width=400)
                
                checkboxa2 = Checkbutton(root, text = a2, font=("Helvitca", 18), variable = vara2)
                checkboxa2.deselect()
                checkboxa2.place(x=200, y=640, height= 40, width=400)
                
                checkboxa3 = Checkbutton(root, text = a3, font=("Helvitca", 18), variable = vara3)
                checkboxa3.deselect()
                checkboxa3.place(x=800, y=540, height= 40, width=500)

                checkboxa4 = Checkbutton(root, text = a4, font=("Helvitca", 18), variable = vara4)
                checkboxa4.deselect()
                checkboxa4.place(x=800, y=640, height= 40, width=500)

                next_button = tk.Button(root, text= "Next", padx= 60, pady= 20,font=("Helvitca", 18) ,command=lambda:checkIfRight(5))
                next_button.place(x=1300, y=680, height= 30, width=100)

            if questionNum == 1:
                q1()
            
            if questionNum == 2:
                q2()
            
            if questionNum == 3:
                q3()

            if questionNum == 4:
                q4()
            
            if questionNum == 5:
                q5()

        def question1():
            displayQuestion(attitudesq1.q, attitudesq1.a1, attitudesq1.a2, attitudesq1.a3, attitudesq1.a4, 1)
        
        def question2():
            displayQuestion(attitudesq2.q, attitudesq2.a1, attitudesq2.a2, attitudesq2.a3, attitudesq2.a4, 2)

        def question3():
            displayQuestion(attitudesq3.q, attitudesq3.a1, attitudesq3.a2, attitudesq3.a3, attitudesq3.a4, 3)

        def question4():
            displayQuestion(attitudesq4.q, attitudesq4.a1, attitudesq4.a2, attitudesq4.a3, attitudesq4.a4, 4)
        
        def question5():
            displayQuestion(attitudesq5.q, attitudesq5.a1, attitudesq5.a2, attitudesq5.a3, attitudesq5.a4, 5)


        question1()
        

        
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

def resultsScreen():
    print("placeholder")

def message_popup(reason):
    if reason == 'login':
        messagebox.showerror("Error", "Username and password don't match. Try again.")
    elif reason == 'reg':
        messagebox.showerror("Error", "Password doesn't match. Try again.")
    elif reason == 'select':
        messagebox.showerror("Error", "You have not selected an answer")

# loginScreen()
topicsScreen()
root.mainloop()
