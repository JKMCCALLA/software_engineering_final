#===================================Library Definitions
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path
from PIL import Image, ImageTk

class friendFrame(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)
 
            OUTPUT_PATH = Path(__file__).parent
            ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame6")

            #===============Canvas Objects
            canvasPost = Canvas(
                self,
                bg = "#FFFFFF",
                height = 654,
                width = 829,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )

            canvasPost.place(x = 0, y = 0)
            self.imagePost_1 = imagePost_1 = PhotoImage(
                 file=ASSETS_PATH / Path("image_1.png"))
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

            self.imagePost_2 = imagePost_2 = PhotoImage(
                file=ASSETS_PATH / Path("image_2.png"))
            imagePost_2b = canvasPost.create_image(
                146.0,
                327.0,
                image=imagePost_2
            )

            canvasPost.create_text(
                507.0,
                258.0,
                anchor="nw",
                text="Find a Friend",
                fill="#2578A9",
                font=("Kreon Bold", 30 * -1)
            )

            canvasPost.create_text(
                373.0,
                332.0,
                anchor="nw",
                text="First",
                fill="#2578A9",
                font=("Kreon Bold", 20 * -1)
            )

            canvasPost.create_text(
                365.0,
                384.0,
                anchor="nw",
                text="Last",
                fill="#2578A9",
                font=("Kreon Bold", 20 * -1)
            )
            canvasPost.pack()

            #===========Entry Objects
            self.entryPost_1 = entryPost_1 = PhotoImage(
                file=ASSETS_PATH / Path("entry_1.png"))
            entryPost_1b = canvasPost.create_image(
                573.0,
                343.0,
                image=entryPost_1
            )
            jobTitle_2 = Entry(
                self,
                bd=0,
                bg="#D9D9D9",
                fg="#000716",
                highlightthickness=0, 
                textvariable=controller.FIRST,
                font=("Arial-BoldMT", int(25))
            )
            jobTitle_2.place(
                x=493.0,
                y=324.0,
                width=160.0,
                height=36.0
            )

            self.entryPost_3 = entryPost_3 = PhotoImage(
               file=ASSETS_PATH / Path("entry_2.png"))
            entryPost_3b = canvasPost.create_image(
                573.0,
                396.0,
                image=entryPost_3
            )
            jobDescription_4 = Entry(
                self,
                bd=0,
                bg="#D9D9D9",
                fg="#000716",
                highlightthickness=0,
                textvariable=controller.LAST,
                font=("Arial-BoldMT", int(25))
            )
            jobDescription_4.place(
                x=493.0,
                y=377.0,
                width=160.0,
                height=36.0
            )

            #=======Button Objects

            self.buttonFrame_1 = buttonFrame_1 = PhotoImage(
                file=ASSETS_PATH / Path("button_1.png"))
            buttonFrame_1b = Button(
                self,
                image=buttonFrame_1,
                borderwidth=0,
                highlightthickness=0,
                command=controller.FindPerson,
                relief="flat"
            )
            buttonFrame_1b.pack()
            buttonFrame_1b.place(
                x=507.0,
                y=593.0,
                width=127.5384521484375,
                height=40.875
            )

            self.buttonReturn_Post = buttonReturn_Post = PhotoImage(
               file=ASSETS_PATH / Path("return.png"))
            buttonReturn_Post_b = Button(
                self,
                image=buttonReturn_Post,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: controller.changePage("jobFrame"),
                relief="flat"
            )
            buttonReturn_Post_b.pack()
            buttonReturn_Post_b.place(
                x=772.0,
                y=16.0,
                width=35.0,
                height=35.0
            )

