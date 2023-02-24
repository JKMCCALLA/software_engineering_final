#===================================Library Definitions
from tkinter import *
import sqlite3
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path
from PIL import Image, ImageTk
#===================================Assets Declaration
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame0")
ASSETS_PATH_1 = OUTPUT_PATH / Path(r"./assets/frame1")
ASSETS_PATH_2 = OUTPUT_PATH / Path(r"./assets/frame2")
ASSETS_PATH_3 = OUTPUT_PATH / Path(r"./assets/frame3")
ASSETS_PATH_4 = OUTPUT_PATH / Path(r"./assets/frame4")
ASSETS_PATH_5 = OUTPUT_PATH / Path(r"./assets/frame5")
ASSETS_PATH_6 = OUTPUT_PATH / Path(r"./assets/frame6")

def relative_to_assets(path: str, pos: int) -> Path:
    if (pos == 0):
        return ASSETS_PATH / Path(path)
    elif (pos == 1):
        return ASSETS_PATH_1 / Path(path)
    elif (pos == 2):
        return ASSETS_PATH_2 / Path(path)
    elif (pos == 3):
        return ASSETS_PATH_3 / Path(path)
    elif (pos == 4):
        return ASSETS_PATH_4/ Path(path)
    elif (pos == 5):
        return ASSETS_PATH_5/ Path(path)
    elif (pos == 6):
        return ASSETS_PATH_6/ Path(path)

window = Tk()
window.geometry("829x654")
window.configure(bg = "#FFFFFF")

homeFrame = Frame(window)
optionsFrame = Frame(window)
skillsFrame = Frame(window)
undoneFrame = Frame(window)
signFrame = Frame(window)
jobFrame = Frame(window)
postFrame = Frame(window)

for frame in (homeFrame, optionsFrame, skillsFrame, undoneFrame, signFrame, jobFrame, postFrame):
    frame.grid(row=0,column=0, sticky='nsew')

#===================================Frame & Canvas Initialization (Login Page)
canvas = Canvas(
    homeFrame,
    bg = "#FFFFFF",
    height = 654,
    width = 829,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png", 0))
image_1 = canvas.create_image(
    572.3466796875,
    140.26365661621094,
    image=image_image_1
)
canvas.create_rectangle(
    389.0,
    279.0,
    757.0,
    528.0,
    fill="#FFFFFF",
    outline="")

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png", 0))
image_2 = canvas.create_image(
    180,
    327.0,
    image=image_image_2
)

canvas.create_text(
    402.0,
    283.0,
    anchor="nw",
    text="Welcome",
    fill="#2578A9",
    font=("Kreon Bold", 30 * -1)
)
canvas.pack()

#=============================Frame & Canvas Initialization (Options Page)
canvasOptions = Canvas(
    optionsFrame,
    bg = "#FFFFFF",
    height = 654,
    width = 829,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvasOptions.place(x = 0, y = 0)
imageOptions_1= PhotoImage(
    file=relative_to_assets("image_1.png", 1))
imageOptions_1b = canvasOptions.create_image(
    572.3466796875,
    140.26365661621094,
    image=imageOptions_1)
canvasOptions.create_rectangle(
    389.0,
    279.0,
    757.0,
    528.0,
    fill="#FFFFFF",
    outline="")

imageOptions_2 = PhotoImage(
    file=relative_to_assets("image_2.png", 1))
imageOptions_2b = canvasOptions.create_image(
    146.0,
    327.0,
    image=imageOptions_2
)

canvasOptions.create_text(
    534.0,
    313.0,
    anchor="nw",
    text="Hi {User}",
    fill="#000000",
    font=("Kreon Bold", 20 * -1)
)
canvasOptions.pack() 

#=============================Frame & Canvas Initialization (Skills Page)
canvasSkills = Canvas(
    skillsFrame,
    bg = "#FFFFFF",
    height = 654,
    width = 829,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvasSkills.place(x = 0, y = 0)
imageSkills_1 = PhotoImage(
    file=relative_to_assets("image_1.png", 2))
imageSkills_1b = canvasSkills.create_image(
    572.3466796875,
    140.26365661621094,
    image=imageSkills_1
)

canvasSkills.create_rectangle(
    389.0,
    279.0,
    756.0,
    621.0,
    fill="#FFFFFF",
    outline="")

imageSkills_2 = PhotoImage(
    file=relative_to_assets("image_2.png", 2))
imageSkills_2b = canvasSkills.create_image(
    146.0,
    327.0,
    image=imageSkills_2
)

canvasSkills.create_text(
    402.0,
    283.0,
    anchor="nw",
    text="Skills",
    fill="#2578A9",
    font=("Kreon Bold", 30 * -1)
)
canvasSkills.pack()

#===========================Frame & Canvas Initialization (Undone Page)
canvasUndone = Canvas(
    undoneFrame,
    bg = "#FFFFFF",
    height = 654,
    width = 829,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvasUndone.place(x = 0, y = 0)
imageUndone_1 = PhotoImage(
    file=relative_to_assets("image_1.png", 3))
imageUndone_1b = canvasUndone.create_image(
    572.3466796875,
    140.26365661621094,
    image=imageUndone_1
)

canvasUndone.create_rectangle(
    389.0,
    279.0,
    757.0,
    528.0,
    fill="#FFFFFF",
    outline="")

imageUndone_2= PhotoImage(
    file=relative_to_assets("image_2.png", 3))
imageUndone_2b = canvasUndone.create_image(
    146.0,
    327.0,
    image=imageUndone_2
)

canvasUndone.create_text(
    486.0,
    375.0,
    anchor="nw",
    text="Under Construction",
    fill="#2578A9",
    font=("Kreon Bold", 30 * -1)
)
canvasUndone.pack()
#===========================Frame & Canvas Initialization (SignUp Page)
canvasSign = Canvas(
    signFrame,
    bg = "#FFFFFF",
    height = 654,
    width = 829,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvasSign.place(x = 0, y = 0)
imageSign_1 = PhotoImage(
    file=relative_to_assets("image_1.png", 4))
imageSign_1b = canvasSign.create_image(
    572.3466796875,
    140.26365661621094,
    image=imageSign_1
)

canvasSign.create_rectangle(
    364.0,
    279.0,
    773.0,
    530.0,
    fill="#FFFFFF",
    outline="")

imageSign_2 = PhotoImage(
    file=relative_to_assets("image_2.png", 4))
imageSign_2b = canvasSign.create_image(
    146.0,
    327.0,
    image=imageSign_2
)

canvasSign.create_text(
    521.0,
    279.0,
    anchor="nw",
    text="Sign Up",
    fill="#2578A9",
    font=("Kreon Bold", 30 * -1)
)

canvasSign.create_text(
    373.0,
    353.0,
    anchor="nw",
    text="Username",
    fill="#2578A9",
    font=("Kreon Bold", 20 * -1)
)

canvasSign.create_text(
    390.0,
    405.0,
    anchor="nw",
    text="First",
    fill="#2578A9",
    font=("Kreon Bold", 20 * -1)
)

canvasSign.create_text(
    391.0,
    457.0,
    anchor="nw",
    text="Last ",
    fill="#2578A9",
    font=("Kreon Bold", 20 * -1)
)
canvasSign.pack()
#============================= Frame & Canvas Initialization (Job Search Options Page)

canvasJob = Canvas(
    jobFrame,
    bg = "#FFFFFF",
    height = 654,
    width = 829,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvasJob.place(x = 0, y = 0)
imageJob_1= PhotoImage(
    file=relative_to_assets("image_1.png", 5))
imageJob_1b = canvasJob.create_image(
    572.3466796875,
    140.26365661621094,
    image=imageJob_1
)

canvasJob.create_rectangle(
    389.0,
    279.0,
    756.0,
    621.0,
    fill="#FFFFFF",
    outline="")

imageJob_2 = PhotoImage(
    file=relative_to_assets("image_2.png", 5))
imageJob_2b = canvasJob.create_image(
    146.0,
    327.0,
    image=imageJob_2
)

canvasJob.create_text(
    402.0,
    283.0,
    anchor="nw",
    text="Job Search",
    fill="#2578A9",
    font=("Kreon Bold", 30 * -1)
)
canvasJob.pack()
#===================================== Frame & Canvas Initialization (Post Job Screen Page)
canvasPost = Canvas(
    postFrame,
    bg = "#FFFFFF",
    height = 654,
    width = 829,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvasPost.place(x = 0, y = 0)
imagePost_1 = PhotoImage(
    file=relative_to_assets("image_1.png", 6))
imagePost_1b = canvasPost.create_image(
    572.3466796875,
    140.26365661621094,
    image=imagePost_1
)

canvasPost.create_rectangle(
    364.0,
    258.0,
    773.0,
    587.0,
    fill="#FFFFFF",
    outline="")

imagePost_2 = PhotoImage(
    file=relative_to_assets("image_2.png", 6))
imagePost_2b = canvasPost.create_image(
    146.0,
    327.0,
    image=imagePost_2
)

canvasPost.create_text(
    507.0,
    258.0,
    anchor="nw",
    text="Post a Job",
    fill="#2578A9",
    font=("Kreon Bold", 30 * -1)
)

canvasPost.create_text(
    373.0,
    332.0,
    anchor="nw",
    text="Job Title",
    fill="#2578A9",
    font=("Kreon Bold", 20 * -1)
)

canvasPost.create_text(
    365.0,
    384.0,
    anchor="nw",
    text="Description",
    fill="#2578A9",
    font=("Kreon Bold", 20 * -1)
)

canvasPost.create_text(
    370.0,
    436.0,
    anchor="nw",
    text="Employer",
    fill="#2578A9",
    font=("Kreon Bold", 20 * -1)
)

canvasPost.create_text(
    373.0,
    488.0,
    anchor="nw",
    text="Location",
    fill="#2578A9",
    font=("Kreon Bold", 20 * -1)
)

canvasPost.create_text(
    381.0,
    541.0,
    anchor="nw",
    text="Salary",
    fill="#2578A9",
    font=("Kreon Bold", 20 * -1)
)
canvasPost.pack()
#==============================================Variables
USERNAME = StringVar()
PASSWORD = StringVar()
FIRST = StringVar()
LAST = StringVar()
JOBTITLE = StringVar()
DESCRIPTION = StringVar()
EMPLOYER = StringVar()
LOCATION = StringVar()
SALARY = StringVar()
#==============================================Form-Entry Objects (Home Page/ Login Page)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png", 0))
entry_bg_1 = canvas.create_image(
    573.8876647949219,
    369.01800537109375,
    image=entry_image_1
)
entry_1 = Entry(
    homeFrame,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    textvariable=USERNAME,
    font=("Arial-BoldMT", int(25))
)

entry_1.place(
    x=402.06500244140625,
    y=344.8645935058594,
    width=343.64532470703125,
    height=46.30682373046875
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png", 0))
entry_bg_2 = canvas.create_image(
    573.8876647949219,
    428.04888916015625,
    image=entry_image_2
)
entry_2 = Entry(
    homeFrame,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    textvariable=PASSWORD,
    show="*",
    font=("Arial-BoldMT", int(25))
    )
entry_2.place(
    x=402.06500244140625,
    y=403.8954772949219,
    width=343.64532470703125,
    height=46.30682373046875
)

#======================================================= Form-Entry Objects (SignUp Page)
entrySign_1 = PhotoImage(
    file=relative_to_assets("entry_1.png", 4))
entrySign_1b = canvasSign.create_image(
    573.0,
    364.0,
    image = entrySign_1
)
entrySign_2 = Entry(
    signFrame,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    textvariable=USERNAME
)
entrySign_2.place(
    x=493.0,
    y=345.0,
    width=160.0,
    height=36.0
)

entrySign_3 = PhotoImage(
    file=relative_to_assets("entry_2.png", 4))
entrySign_3b = canvasSign.create_image(
    573.0,
    417.0,
    image=entrySign_3
)
entrySign_4 = Entry(
    signFrame,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    textvariable=FIRST
)
entrySign_4.place(
    x=493.0,
    y=398.0,
    width=160.0,
    height=36.0
)

entrySign_5 = PhotoImage(
    file=relative_to_assets("entry_3.png", 4))
entrySign_5b = canvasSign.create_image(
    573.0,
    470.0,
    image=entrySign_5
)
entrySign_6 = Entry(
    signFrame,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    textvariable=LAST
)
entrySign_6.place(
    x=493.0,
    y=451.0,
    width=160.0,
    height=36.0
)
#==========Form-Entry Objects (Post Job Screen Page)

entryPost_1 = PhotoImage(
    file=relative_to_assets("entry_1.png", 6))
entryPost_1b = canvasPost.create_image(
    573.0,
    343.0,
    image=entryPost_1
)
jobTitle_2 = Entry(
    postFrame,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0, 
    textvariable=JOBTITLE,
    font=("Arial-BoldMT", int(25))
)
jobTitle_2.place(
    x=493.0,
    y=324.0,
    width=160.0,
    height=36.0
)

entryPost_3 = PhotoImage(
    file=relative_to_assets("entry_2.png", 6))
entryPost_3b = canvasPost.create_image(
    573.0,
    396.0,
    image=entryPost_3
)
jobDescription_4 = Entry(
    postFrame,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    textvariable=DESCRIPTION,
    font=("Arial-BoldMT", int(25))
)
jobDescription_4.place(
    x=493.0,
    y=377.0,
    width=160.0,
    height=36.0
)

entryPost_5 = PhotoImage(
    file=relative_to_assets("entry_3.png", 6))
entryPost_5b = canvasPost.create_image(
    573.0,
    449.0,
    image=entryPost_5
)
employer_6 = Entry(
    postFrame,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    textvariable=EMPLOYER,
    font=("Arial-BoldMT", int(25))
)
employer_6.place(
    x=493.0,
    y=430.0,
    width=160.0,
    height=36.0
)

entryPost_7 = PhotoImage(
    file=relative_to_assets("entry_4.png", 6))
entryPost_7b = canvasPost.create_image(
    573.0,
    502.0,
    image=entryPost_7
)
location_8 = Entry(
    postFrame,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    textvariable=LOCATION,
    font=("Arial-BoldMT", int(25))
)
location_8.place(
    x=493.0,
    y=483.0,
    width=160.0,
    height=36.0
)

entryPost_9 = PhotoImage(
    file=relative_to_assets("entry_5.png", 6))
entryPost_9b = canvasPost.create_image(
    573.0,
    555.0,
    image=entryPost_9
)
salary_10 = Entry(
    postFrame,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    textvariable=SALARY,
    font=("Arial-BoldMT", int(25))
)
salary_10.place(
    x=493.0,
    y=536.0,
    width=160.0,
    height=36.0
)
#==================================================Methods
def nextPage(choice: int):
    if (choice == 0):
        optionsFrame.tkraise()
    elif (choice == 1):
        skillsFrame.tkraise()
    elif (choice == 2):
        undoneFrame.tkraise()
    elif (choice == 3):
        signFrame.tkraise()
    elif (choice == 4):
        homeFrame.tkraise()
    elif (choice == 5):
        jobFrame.tkraise()
    elif (choice == 6):
        postFrame.tkraise()

def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")       
    cursor.execute("SELECT * FROM `member` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `member` (username, password) VALUES('admin', 'admin')")
        conn.commit()

def Login(event=None):
    Database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        print("Please complete the required field!")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            nextPage(0)
            USERNAME.set("")
            PASSWORD.set("")
            lambda: print("")
        else:
            print("Invalid username or password")
            USERNAME.set("")
            PASSWORD.set("")   
    cursor.close()
    conn.close()

def Signup(event=None):
    Database()
    cursor.execute("SELECT * FROM member")
    rows = cursor.fetchall()
    if (len(rows) < 5):
        if (USERNAME.get() == "" or FIRST.get() == "" or LAST.get() == ""):
            print("Please complete the required field!")
        else:
            if (isSignupInfoValid()):
                sql = ''' INSERT INTO member(username, first, last) VALUES (?,?,?) '''
                task = (USERNAME.get(), FIRST.get(), LAST.get())
                cursor.execute(sql, task)
                conn.commit()
                nextPage(4)
        cursor.close()
        conn.close()
    else:
        print("Maximum number of records in database \n")
        cursor.close()
        conn.close()

def PostJob(event=None):
    Database()
    cursor.execute("SELECT * FROM jobs")
    rows = cursor.fetchall()
    if (len(rows) < 5):
        if (JOBTITLE.get() == "" or DESCRIPTION.get() == "" or EMPLOYER.get() == "" or
            LOCATION.get() == "" or SALARY.get() == ""):
            print("Please complete the required field!")
        else:
            sql = ''' INSERT INTO jobs(title, description, employer, location, salary) VALUES (?,?,?,?,?) '''
            task = (JOBTITLE.get(), DESCRIPTION.get(), EMPLOYER.get(), LOCATION.get(), SALARY.get())
            cursor.execute(sql, task)
            conn.commit()
        cursor.close()
        conn.close()
    else:
        print("Maximum number of records in database \n")

def isSignupInfoValid():
     
     password = PASSWORD.get()
     containsUpper = False
     containsNumber = False
     containsSpecialCharacter = False
     finalBool = False

     for letter in password:
         if letter.isupper():
             containsUpper = True
         if letter.isdigit():
             containsNumber = True
         if letter.isalnum() != True:
             containsSpecialCharacter = True

     if len(password) < 8 or len(password) > 12:
         print('Password is either too long or too short')
         finalBool = False
     if containsUpper != True:
         print('Password must contain uppercase letter')
         finalBool = False
     if containsNumber != True:
         print('Passowrd must contain a number')
         finalBool = False
     if containsSpecialCharacter != True:
         print('Password doesn\'t contain a special character')
         finalBool = False

    #  return finalBool // Enabled when the SignUp option has a password field added
     return True 
#======================================================Button Declarations (Login Page)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png", 0))
button_1 = Button(
    homeFrame,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=Login,
    relief="flat"
)
button_1.pack()
button_1.place(
    x=402.06500244140625,
    y=478.4608154296875,
    width=127.5384521484375,
    height=40.875
)
window.bind('<Return>', Login)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png", 0))
button_2 = Button(
    homeFrame,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: nextPage(3),
    relief="flat"
)
button_2.pack()
button_2.place(
    x=555.4299926757812,
    y=478.4608154296875,
    width=127.5384521484375,
    height=40.875
)

#=========================================Button Declarations (Options Page)
buttonOptions_1 = PhotoImage(
    file=relative_to_assets("button_1.png", 1))
buttonOptions_1b = Button(
    optionsFrame,
    image=buttonOptions_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: nextPage(5),
    relief="flat"
)
buttonOptions_1b.pack()
buttonOptions_1b.place(
    x=433.0,
    y=369.0,
    width=127.5384521484375,
    height=40.875
)

buttonOptions_2 = PhotoImage(
    file=relative_to_assets("button_2.png", 1))
buttonOptions_2b = Button(
    optionsFrame,
    image=buttonOptions_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: nextPage(1),
    relief="flat"
)
buttonOptions_2b.pack()
buttonOptions_2b.place(
    x=509.0,
    y=424.0,
    width=127.5384521484375,
    height=40.875
)
buttonOptions_3 = PhotoImage(
    file=relative_to_assets("button_3.png", 1))
buttonOptions_3b = Button(
    optionsFrame,
    image=buttonOptions_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: nextPage(2),
    relief="flat"
)
buttonOptions_3b.pack()
buttonOptions_3b.place(
    x=573.0,
    y=369.0,
    width=127.5384521484375,
    height=40.875
)

buttonReturn_Options = PhotoImage(
    file=relative_to_assets("return.png", 0))
buttonReturn_Options_b = Button(
    optionsFrame,
    image=buttonReturn_Options,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: nextPage(4),
    relief="flat"
)

buttonReturn_Options_b.pack()
buttonReturn_Options_b.place(
    x=772.0,
    y=16.0,
    width=35.0,
    height=35.0
)

#=========================================Button Declarations (Skills Page)
buttonSkills_1 = PhotoImage(
    file=relative_to_assets("button_1.png", 2))
buttonSkills_1b = Button(
    skillsFrame,
    image=buttonSkills_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: nextPage(2),
    relief="flat"
)
buttonSkills_1b.pack()
buttonSkills_1b.place(
    x=509.0,
    y=336.0,
    width=127.5384521484375,
    height=40.875
)

buttonSkills_2 = PhotoImage(
    file=relative_to_assets("button_2.png", 2))
buttonSkills_2b = Button(
    skillsFrame,
    image=buttonSkills_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: nextPage(2),
    relief="flat"
)
buttonSkills_2b.pack()
buttonSkills_2b.place(
    x=509.0,
    y=393.0,
    width=127.5384521484375,
    height=40.875
)

buttonSkills_3 = PhotoImage(
    file=relative_to_assets("button_3.png", 2))
buttonSkills_3b = Button(
    skillsFrame,
    image=buttonSkills_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: nextPage(2),
    relief="flat"
)
buttonSkills_3b.pack()
buttonSkills_3b.place(
    x=509.0,
    y=507.0,
    width=127.5384521484375,
    height=40.875
)

buttonSkills_4 = PhotoImage(
    file=relative_to_assets("button_4.png", 2))
buttonSkills_4b = Button(
    skillsFrame,
    image=buttonSkills_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: nextPage(2),
    relief="flat"
)
buttonSkills_4b.pack()
buttonSkills_4b.place(
    x=509.0,
    y=564.0,
    width=127.5384521484375,
    height=40.875
)

buttonSkills_5 = PhotoImage(
    file=relative_to_assets("button_5.png", 2))
buttonSkills_5b = Button(
    skillsFrame,
    image=buttonSkills_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: nextPage(2),
    relief="flat"
)
buttonSkills_5b.pack()
buttonSkills_5b.place(
    x=509.0,
    y=450.0,
    width=127.5384521484375,
    height=40.875
)

buttonReturn_Skills = PhotoImage(
    file=relative_to_assets("return.png", 0))
buttonReturn_Skills_b = Button(
    skillsFrame,
    image=buttonReturn_Skills,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: nextPage(0),
    relief="flat"
)
buttonReturn_Skills_b.pack()
buttonReturn_Skills_b.place(
    x=772.0,
    y=16.0,
    width=35.0,
    height=35.0
)
#=========Button Declarations (SignUp Page)
buttonSign_6 = PhotoImage(
    file=relative_to_assets("button_1.png", 4))
buttonSign_6b = Button(
    signFrame,
    image=buttonSign_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Signup(),
    relief="flat"
)
buttonSign_6b.pack()
buttonSign_6b.place(
    x=509.0,
    y=519.0,
    width=127.5384521484375,
    height=40.875
)

buttonReturn_Sign = PhotoImage(
    file=relative_to_assets("return.png", 0))
buttonReturn_Sign_b = Button(
    signFrame,
    image=buttonReturn_Sign,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: nextPage(4),
    relief="flat"
)
buttonReturn_Sign_b.pack()
buttonReturn_Sign_b.place(
    x=772.0,
    y=16.0,
    width=35.0,
    height=35.0
)
#===============================Button Declarations (Undone Frame)

buttonReturn_Undone = PhotoImage(
    file=relative_to_assets("return.png", 0))
buttonReturn_Undone_b = Button(
    undoneFrame,
    image=buttonReturn_Undone,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: nextPage(4),
    relief="flat"
)
buttonReturn_Undone_b.pack()
buttonReturn_Undone_b.place(
    x=772.0,
    y=16.0,
    width=35.0,
    height=35.0
)

#=============Button Declarations (Job Frame)

buttonJob_1 = PhotoImage(
    file=relative_to_assets("button_1.png", 5))
buttonJob_1b = Button(
    jobFrame,
    image=buttonJob_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: nextPage(6),
    relief="flat"
)
buttonJob_1b.pack()
buttonJob_1b.place(
    x=509.0,
    y=342.0,
    width=127.5384521484375,
    height=40.875
)

buttonReturn_Job = PhotoImage(
    file=relative_to_assets("return.png", 0))
buttonReturn_Job_b = Button(
    jobFrame,
    image=buttonReturn_Job,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: nextPage(0),
    relief="flat"
)
buttonReturn_Job_b.pack()
buttonReturn_Job_b.place(
    x=772.0,
    y=16.0,
    width=35.0,
    height=35.0
)
#=============Button Declarations (Post Frame)
buttonFrame_1 = PhotoImage(
    file=relative_to_assets("button_1.png", 6))
buttonFrame_1b = Button(
    postFrame,
    image=buttonFrame_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: PostJob(),
    relief="flat"
)
buttonFrame_1b.pack()
buttonFrame_1b.place(
    x=507.0,
    y=593.0,
    width=127.5384521484375,
    height=40.875
)

buttonReturn_Post = PhotoImage(
    file=relative_to_assets("return.png", 0))
buttonReturn_Post_b = Button(
    postFrame,
    image=buttonReturn_Post,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: nextPage(5),
    relief="flat"
)
buttonReturn_Post_b.pack()
buttonReturn_Post_b.place(
    x=772.0,
    y=16.0,
    width=35.0,
    height=35.0
)
#==============================================Main Method
def loginPage():

    if __name__ == '__main__':
        homeFrame.tkraise()
        window.mainloop()

loginPage()