 
import sqlite3

def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")       
    cursor.execute("SELECT * FROM `member` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `member` (username, password) VALUES('admin', 'admin')")
        conn.commit() 

def GetJob(user):
    Database()
    cursor.execute(''' SELECT * FROM applied ''')
    rows = cursor.fetchall()
    if (len(rows) > 0):
        cursor.execute("SELECT * FROM applied WHERE student = ?", [(user)])
        listReturn = cursor.fetchall()
        conn.commit()
        cursor.close()
    else:
        print("No applied jobs exist")
    return listReturn

def sendMessage(user, message):
    Database()
    cursor.execute("SELECT * FROM users WHERE user = ? AND status = ?", [(user), "online"])
    rows = cursor.fetchall()
    if (len(rows) > 0):
        cursor.execute("INSERT INTO `messages` (message, user) VALUES(?, ?)", [(message), (user)])
        conn.commit() 
        cursor.close()
    else:
        print("User can not be found or, user is not online")

def getOnlineList():
    Database()
    cursor.execute("SELECT * FROM users WHERE status = ?", ["online"])
    rows = cursor.fetchall()
    return rows

if __name__ == '__main__':
    print(getOnlineList())
