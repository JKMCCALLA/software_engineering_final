from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path
from PIL import Image, ImageTk
import sqlite3

class profileFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame7")

        # Create StringVar variables for name and tagline
        self.name_text = StringVar()
        self.tagline_text = StringVar()

        # Name and tagline labels
        self.name_label = Label(self, textvariable=self.name_text, font=("Kreon Bold", 24 * -1), bg="#FFFFFF")
        self.name_label.place(x=30, y=30)
        self.tagline_label = Label(self, textvariable=self.tagline_text, font=("Kreon Regular", 20 * -1), bg="#FFFFFF")
        self.tagline_label.place(x=30, y=70)

        #===============Canvas Objects

        canvasProfile = Canvas(
            self,
            bg = "#FFFFFF",
            height = 654,
            width = 829,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvasProfile.place(x = 0, y = 0)

        #==============Text Objects

        canvasProfile.create_text(
            30,
            30,
            anchor="nw",
            text="Student Name",
            fill="#000000",
            font=("Kreon Bold", 24 * -1)
        )

        canvasProfile.create_text(
            30,
            70,
            anchor="nw",
            text="Tagline",
            fill="#000000",
            font=("Kreon Regular", 20 * -1)
        )

        #==============Button Objects

        buttonSavedJobs_b = Button(
            self,
            text="Saved Jobs",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.changePage("savedJobsFrame"),
            relief="flat",
            font=("Kreon Regular", 16)
        )
        buttonSavedJobs_b.pack()
        buttonSavedJobs_b.place(x=30, y=120, width=200, height=40)

        buttonEditProfile_b = Button(
            self,
            text="Edit Profile",
            borderwidth=0,
            command=self.make_editable,
            highlightthickness=0,
            # command=lambda: controller.changePage("editProfileFrame"),
            relief="flat",
            font=("Kreon Regular", 16)
        )
        buttonEditProfile_b.pack()
        buttonEditProfile_b.place(x=30, y=180, width=200, height=40)

        #==============Return Button

        buttonReturn_Profile_b = Button(
            self,
            text="Return",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.changePage("optionsFrame"),
            relief="flat",
            font=("Kreon Regular", 16)
        )

        buttonReturn_Profile_b.pack()
        buttonReturn_Profile_b.place(x=600.0, y=16.0, width=200.0, height=40.0)

        self.save_button = Button(
            self,
            text="Save",
            borderwidth=0,
            highlightthickness=0,
            command=self.save_profile,
            relief="flat",
            font=("Kreon Regular", 16)
        )
        self.save_button.pack()
        self.save_button.place(x=30, y=250, width=200, height=40)
        # Hide button initially
        self.save_button.lower()

    def make_editable(self):
        self.name_label.destroy()
        self.tagline_label.destroy()

        self.name_entry = Entry(self, textvariable=self.name_text, font=("Kreon Bold", 24 * -1))
        self.name_entry.place(x=30, y=30)

        self.tagline_entry = Entry(self, textvariable=self.tagline_text, font=("Kreon Regular", 20 * -1))
        self.tagline_entry.place(x=30, y=70)
        # Show save button
        self.save_button.lift()

    def Database(self):
        global conn, cursor
        conn = sqlite3.connect("pythontut.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT, name TEXT, tagline TEXT)")       
        cursor.execute("SELECT * FROM `member` WHERE `username` = 'admin' AND `password` = 'admin'")
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO `member` (username, password) VALUES('admin', 'admin')")
            conn.commit()

    def save_profile(self):
        # Update the profile in the database
        self.Database()
        cursor.execute("UPDATE member SET username = ?, tagline = ? WHERE mem_id = 1", (self.name_text.get(), self.tagline_text.get()))
        conn.commit()

        # Hide the save button and show the labels after saving
        self.save_button.lower()

        # Create new labels for name and tagline
        self.name_label = Label(self, text=self.name_text.get(), font=("Kreon Bold", 24 * -1), bg="#FFFFFF")
        self.name_label.place(x=30, y=30)
        self.tagline_label = Label(self, text=self.tagline_text.get(), font=("Kreon Regular", 20 * -1), bg="#FFFFFF")
        self.tagline_label.place(x=30, y=70)

        self.name_entry.destroy()
        self.tagline_entry.destroy()

        cursor.close()
        conn.close()