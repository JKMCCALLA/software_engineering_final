#===================================Library Definitions
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path
from PIL import Image, ImageTk

class skillsFrame(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)
 
            OUTPUT_PATH = Path(__file__).parent
            ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame2")

            #===============Canvas Objects
            canvasSkills = Canvas(
                self,
                bg = "#FFFFFF",
                height = 654,
                width = 829,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )

            canvasSkills.place(x = 0, y = 0)
            self.imageSkills_1 = imageSkills_1 = PhotoImage(
                file=ASSETS_PATH / Path("image_1.png"))
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

            self.imageSkills_2 = imageSkills_2 = PhotoImage(
                file=ASSETS_PATH / Path("image_2.png"))
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

            #===============Button Objects
            self.buttonSkills_1 = buttonSkills_1 = PhotoImage(
                file=ASSETS_PATH / Path("button_1.png"))
            buttonSkills_1b = Button(
                self,
                image=buttonSkills_1,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: controller.changePage("undoneFrame"),
                relief="flat"
            )
            buttonSkills_1b.pack()
            buttonSkills_1b.place(
                x=509.0,
                y=336.0,
                width=127.5384521484375,
                height=40.875
            )

            self.buttonSkills_2 = buttonSkills_2 = PhotoImage(
                file=ASSETS_PATH / Path("button_2.png"))
            buttonSkills_2b = Button(
                self,
                image=buttonSkills_2,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: controller.changePage("undoneFrame"),
                relief="flat"
            )
            buttonSkills_2b.pack()
            buttonSkills_2b.place(
                x=509.0,
                y=393.0,
                width=127.5384521484375,
                height=40.875
            )

            self.buttonSkills_3 = buttonSkills_3 = PhotoImage(
                file=ASSETS_PATH / Path("button_3.png"))
            buttonSkills_3b = Button(
                self,
                image=buttonSkills_3,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: controller.changePage("undoneFrame"),
                relief="flat"
            )
            buttonSkills_3b.pack()
            buttonSkills_3b.place(
                x=509.0,
                y=507.0,
                width=127.5384521484375,
                height=40.875
            )

            self.buttonSkills_4 = buttonSkills_4 = PhotoImage(
                file=ASSETS_PATH / Path("button_4.png"))
            buttonSkills_4b = Button(
                self,
                image=buttonSkills_4,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: controller.changePage("undoneFrame"),
                relief="flat"
            )
            buttonSkills_4b.pack()
            buttonSkills_4b.place(
                x=509.0,
                y=564.0,
                width=127.5384521484375,
                height=40.875
            )

            self.buttonSkills_5 = buttonSkills_5 = PhotoImage(
                file=ASSETS_PATH / Path("button_5.png"))
            buttonSkills_5b = Button(
                self,
                image=buttonSkills_5,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: controller.changePage("undoneFrame"),
                relief="flat"
            )
            buttonSkills_5b.pack()
            buttonSkills_5b.place(
                x=509.0,
                y=450.0,
                width=127.5384521484375,
                height=40.875
            )

            self.buttonReturn_Skills = buttonReturn_Skills = PhotoImage(
                file=ASSETS_PATH / Path("return.png"))
            buttonReturn_Skills_b = Button(
                self,
                image=buttonReturn_Skills,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: controller.changePage("optionsFrame"),
                relief="flat"
            )
            buttonReturn_Skills_b.pack()
            buttonReturn_Skills_b.place(
                x=772.0,
                y=16.0,
                width=35.0,
                height=35.0
            )
