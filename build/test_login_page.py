#===================================Library Definitions
from tkinter import *
import sqlite3
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path
from PIL import Image, ImageTk
import pytest
#===================================Assets Declaration
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame0")
ASSETS_PATH_1 = OUTPUT_PATH / Path(r"./assets/frame1")

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

#==============================================Variables
USERNAME = StringVar()
PASSWORD = StringVar()


#==================================================Methods
def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")       
    cursor.execute("SELECT * FROM `member` WHERE `username` = 'admin' AND `password` = 'admin'")
    test = len(list(cursor.execute('SELECT * FROM member'))) == 44
    if (len(list(cursor.execute('SELECT * FROM member'))) >= 5): 
        print("All permitted accounts have been created, please come back later")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `member` (username, password) VALUES('admin', 'admin')")
        conn.commit()
    return test

def Login(user, password):
    Database()
    #messagePrompt = True
    if user == "" or password == "":
        print("Please complete the required field!")
        messagePrompt = "Enter again!"
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?", (user, password))
        if cursor.fetchone() is not None:
            #messagePrompt = "found you"
            messagePrompt = "YES"
            #user.set("")
            #password.set("")
            lambda: print("")
        else:
            print("Invalid username or password")
            messagePrompt = False
            #user.set("")
            #password.set("")   
    cursor.close()
    conn.close()
    return messagePrompt 

def Signup(user, first, last):
     Database()
     cursor.execute("SELECT * FROM member")
     rows = cursor.fetchall()
     print(rows)
     if (len(rows) < 5):
         if (user == "" or first == "" or last == ""):
             print("Please complete the required field!")
             return 0
         else:
             sql = ''' INSERT INTO member(user, first, last) VALUES (?,?,?) '''
             task = (user, first, last)
             cursor.execute(sql, task)
             conn.commit()
             return 1
         cursor.close()
         conn.close()
     else:
         print("Maximum number of records in database \n")
         return -1, rows


def PostJob(job, title, employer, location, salary):
    Database()
    cursor.execute("SELECT * FROM jobs")
    rows = cursor.fetchall()
    ret = 1
    if (len(rows) < 5):
        if (job == "" or title == "" or employer == "" or
            location == "" or salary == ""):
            ret = 0 
        else:
            return 1
        cursor.close()
        conn.close()
    else:
        ret = 1
    return ret

def testcase_jobpost():
    Database()
    response = PostJob("test", "test", "test", "test", "test")
    assert response == 1
def testcase_empty_jobpost():
    response = PostJob("", "", "", "", "")
    assert response == 0

def testcase_sign_up_limit():
    response, rows = Signup("test", "test", "test")
    print(rows)
    assert response == -1

def testcase_invalid():
    USERNAME = "tilak"
    PASSWORD = "whaete"
    pass1 = Login(USERNAME, PASSWORD)
    assert pass1 == False
#This testcase should pass because the username and password is in the database 
def testcase_valid():
    USERNAME = 'bob'
    PASSWORD = 'easybob'
    pass2 = Login(USERNAME, PASSWORD) 
    assert pass2 == 'YES'

def test_connection():
    # Test to make sure that there are items in the database
    cursor = Database()
    #test = len(list(cursor.execute('SELECT * FROM member'))) == 5
    assert cursor == False

def testcase_passinvalid1():
    USERNAME = 'admin'
    PASSWORD = 'ad'
    pass3 = Login(USERNAME, PASSWORD)
    assert len(PASSWORD) < 5                 #This testcase is invalid, password must  be minimum of 8 characters

def testcase_passinvalid2():
    USERNAME = 'bob'
    PASSWORD = 'easybobeasybob'
    pass4 = Login(USERNAME, PASSWORD)
    assert len(PASSWORD) == 14                 #This testcase is invalid, password must be max of 12 characters

def testcase_passvalid1():
    USERNAME = 'admin'
    PASSWORD = 'adminadmin'
    pass5 = Login(USERNAME, PASSWORD)
    assert len(PASSWORD) == 10                #Testcase is valid, password must be in range of 8 to 12 characters

def testcase_passinvalid3():
    USERNAME = 'admin'
    PASSWORD = 'adminadmin'
    pass5 = Login(USERNAME, PASSWORD)
    length = len(PASSWORD)
    for char in PASSWORD[0:length:1]:
        if char.isupper()==True:                #Testcase invalid, no capital letter involved
            break
        else:
            continue 

    assert pass5 == False

def testcase_passvalid2():
    USERNAME = 'admin'
    PASSWORD = 'adminAdmin'
    pass5 = Login(USERNAME, PASSWORD)
    length = len(PASSWORD)
    for char in PASSWORD[0:length:1]:                   #Testcase valid, has at least one capital letter
        if char.isupper()==True:
            break
        else:
            continue 

    assert pass5 == True


def testcase_passinvalid4():
    USERNAME = 'bob'
    PASSWORD = 'easybobeasyb'
    length = len(PASSWORD)
    pass6 = Login(USERNAME, PASSWORD)
    for char in PASSWORD[0:length:1]:                   #Testcase invalid, does not have at least one digit
        if char.isdigit()==True:
            break
        else:
            continue
    assert pass6 == False
def testcase_passvalid5():
    USERNAME = 'bob'
    PASSWORD = 'easybobeasy12'
    length = len(PASSWORD)
    pass6 = Login(USERNAME, PASSWORD)
    for char in PASSWORD[0:length:1]:                   #Testcase valid, has at least one digit
        if char.isdigit()==True:
            break
        else:
            continue
    assert pass6 == True


#==============================================Main Method
def loginPage():

    if __name__ == '__main__':
        homeFrame.tkraise()
        window.mainloop()

loginPage()