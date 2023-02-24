#===================================Library Definitions
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path
from PIL import Image, ImageTk

class postFrame(Frame):
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
                textvariable=controller.JOBTITLE,
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
                textvariable=controller.DESCRIPTION,
                font=("Arial-BoldMT", int(25))
            )
            jobDescription_4.place(
                x=493.0,
                y=377.0,
                width=160.0,
                height=36.0
            )

            self.entryPost_5 = entryPost_5 = PhotoImage(
               file=ASSETS_PATH / Path("entry_3.png"))
            entryPost_5b = canvasPost.create_image(
                573.0,
                449.0,
                image=entryPost_5
            )
            employer_6 = Entry(
                self,
                bd=0,
                bg="#D9D9D9",
                fg="#000716",
                highlightthickness=0,
                textvariable=controller.EMPLOYER,
                font=("Arial-BoldMT", int(25))
            )
            employer_6.place(
                x=493.0,
                y=430.0,
                width=160.0,
                height=36.0
            )

            self.entryPost_7 = entryPost_7 = PhotoImage(
                file=ASSETS_PATH / Path("entry_4.png"))
            entryPost_7b = canvasPost.create_image(
                573.0,
                502.0,
                image=entryPost_7
            )
            location_8 = Entry(
                self,
                bd=0,
                bg="#D9D9D9",
                fg="#000716",
                highlightthickness=0,
                textvariable=controller.LOCATION,
                font=("Arial-BoldMT", int(25))
            )
            location_8.place(
                x=493.0,
                y=483.0,
                width=160.0,
                height=36.0
            )

            self.entryPost_9 = entryPost_9 = PhotoImage(
                file=ASSETS_PATH / Path("entry_5.png"))
            entryPost_9b = canvasPost.create_image(
                573.0,
                555.0,
                image=entryPost_9
            )
            salary_10 = Entry(
                self,
                bd=0,
                bg="#D9D9D9",
                fg="#000716",
                highlightthickness=0,
                textvariable=controller.SALARY,
                font=("Arial-BoldMT", int(25))
            )
            salary_10.place(
                x=493.0,
                y=536.0,
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
                command=lambda: controller.PostJob,
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

