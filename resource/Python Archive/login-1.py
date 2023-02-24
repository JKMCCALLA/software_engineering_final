from tkinter import *
import sqlite3
#==========================Custom UI Definition==============================
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/jordanemccalla/Downloads/Software Engineering/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

root = Tk()
root.title("InCollege")
width = 400
height = 280
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

canvas = Canvas(
    root,
    bg = "#FFFFFF",
    height = screen_height,
    width = screen_width,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))

image_1 = canvas.create_image(
    183.0,
    38.0,
    image=image_image_1
)
canvas.create_rectangle(
    130.0,
    72.0,
    screen_width,
    screen_height,
    fill="#FFFFFF",
    outline=""
)
image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    44.0,
    88.0,
    image=image_image_2
)
canvas.create_text(
    135.0,
    76.0,
    anchor="nw",
    text="Welcome",
    fill="#2578A9",
    font=("Kreon Bold", 10 * -1)
)

#==============================VARIABLES======================================
USERNAME = StringVar()
PASSWORD = StringVar()

#==============================LABELS=========================================
 
#==============================ENTRY WIDGETS==================================
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    183.5,
    101.5,
    image=entry_image_1
)
username = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    textvariable=USERNAME,
    font=(14)
)
username.place(
    x=135.0,
    y=95.0,
    width=97.0,
    height=11.0
)
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    183.5,
    117.5,
    image=entry_image_2
)
password= Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    textvariable=PASSWORD,
    show="*",
    font=(14)
)
password.place(
    x=135.0,
    y=111.0,
    width=97.0,
    height=11.0
)
#==============================METHODS========================================
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
            HomeWindow()
            USERNAME.set("")
            PASSWORD.set("")
            lambda: print("")
        else:
            print("Invalid username or password")
            USERNAME.set("")
            PASSWORD.set("")   
    cursor.close()
    conn.close()

#==============================BUTTON WIDGETS=================================
#----------------------------------------------Login Button
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
btn_login = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=Login,
    relief="flat"
)
btn_login.place(
    x=137.0,
    y=134.0,
    width=36.0,
    height=11.0
)
btn_login.bind('<Return>', Login)
#---------------------------------------------Signup Button
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
btn_signup = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("SignUp Button clicked"),
    relief="flat"
)
btn_signup.place(
    x=182.0,
    y=134.0,
    width=36.0,
    height=11.0
)
#================================HOME PAGE
def HomeWindow():
    global Home
    root.withdraw()
    Home = Toplevel()
    Home.title("InCollege")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.resizable(0, 0)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    lbl_home = Label(Home, text="Successfully Login!", font=('times new roman', 20)).pack()
    btn_back = Button(Home, text='Back', command=Back).pack(pady=20, fill=X)
 
def Back():
    Home.destroy()
    root.deiconify()

#==============================INITIALIATION
if __name__ == '__main__':
    root.mainloop()