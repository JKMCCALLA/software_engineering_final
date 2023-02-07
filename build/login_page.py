#===================================Library Definitions
from tkinter import *
import sqlite3
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path
from PIL import Image, ImageTk
#===================================Assets Declaration
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/jordanemccalla/Downloads/Software Engineering/softeng_team2023/build/assets/frame0")
ASSETS_PATH_1 = OUTPUT_PATH / Path(r"/Users/jordanemccalla/Downloads/Software Engineering/softeng_team2023/build/assets/frame1")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def relative_to_assets_1(path: str) -> Path:
    return ASSETS_PATH_1 / Path(path)

window = Tk()
window.geometry("829x654")
window.configure(bg = "#FFFFFF")

#===================================Frame & Canvas Initialization (Login Page)
homeFrame = Frame(window)
optionsFrame = Frame(window)

for frame in (homeFrame, optionsFrame):
    frame.grid(row=0,column=0, sticky='nsew')

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
    file=relative_to_assets("image_1.png"))
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
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    146.0,
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
    file=relative_to_assets_1("image_1.png"))
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
    file=relative_to_assets_1("image_2.png"))
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

#==============================================Variables
USERNAME = StringVar()
PASSWORD = StringVar()

#==============================================Form-Entry Objects
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
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
    file=relative_to_assets("entry_2.png"))
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

#==================================================Methods
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
            nextPage()
            USERNAME.set("")
            PASSWORD.set("")
            lambda: print("")
        else:
            print("Invalid username or password")
            USERNAME.set("")
            PASSWORD.set("")   
    cursor.close()
    conn.close()

#======================================================Button Declarations (Login Page)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
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
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    homeFrame,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
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
    file=relative_to_assets_1("button_1.png"))
buttonOptions_1b = Button(
    optionsFrame,
    image=buttonOptions_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
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
    file=relative_to_assets_1("button_2.png"))
buttonOptions_2b = Button(
    optionsFrame,
    image=buttonOptions_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
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
    file=relative_to_assets_1("button_3.png"))
buttonOptions_3b = Button(
    optionsFrame,
    image=buttonOptions_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
buttonOptions_3b.pack()
buttonOptions_3b.place(
    x=573.0,
    y=369.0,
    width=127.5384521484375,
    height=40.875
)

#================================================Home Page
def nextPage():
    optionsFrame.tkraise()
    print("Next page is displayed")

# def Back():
#     Home.destroy()
#     window.deiconify()

#==============================================Main Method
def loginPage():

    if __name__ == '__main__':
        homeFrame.tkraise()
        window.mainloop()

loginPage()