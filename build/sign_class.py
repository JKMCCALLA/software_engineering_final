#===================================Library Definitions
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path
from PIL import Image, ImageTk

class signFrame(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)
 
            OUTPUT_PATH = Path(__file__).parent
            ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame4")

            #========Canvas Objects
            canvasSign = Canvas(
                self,
                bg = "#FFFFFF",
                height = 654,
                width = 829,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )

            canvasSign.place(x = 0, y = 0)
            self.imageSign_1 = imageSign_1 = PhotoImage(
                file=ASSETS_PATH / Path("image_1.png"))
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

            self.imageSign_2 = imageSign_2 = PhotoImage(
                file=ASSETS_PATH / Path("image_2.png"))
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
            
            #========Entry Objects
            self.entrySign_1 = entrySign_1 = PhotoImage(
                file=ASSETS_PATH / Path("entry_1.png"))
            entrySign_1b = canvasSign.create_image(
                573.0,
                364.0,
                image = entrySign_1
            )
            entrySign_2 = Entry(
                self,
                bd=0,
                bg="#D9D9D9",
                fg="#000716",
                highlightthickness=0,
                textvariable=controller.USERNAME
            )
            entrySign_2.place(
                x=493.0,
                y=345.0,
                width=160.0,
                height=36.0
            )

            self.entrySign_3 = entrySign_3 = PhotoImage(
                file=ASSETS_PATH / Path("entry_2.png"))
            entrySign_3b = canvasSign.create_image(
                573.0,
                417.0,
                image=entrySign_3
            )
            entrySign_4 = Entry(
                self,
                bd=0,
                bg="#D9D9D9",
                fg="#000716",
                highlightthickness=0,
                textvariable=controller.FIRST
            )
            entrySign_4.place(
                x=493.0,
                y=398.0,
                width=160.0,
                height=36.0
            )

            self.entrySign_5 = entrySign_5 = PhotoImage(
                file=ASSETS_PATH / Path("entry_3.png"))
            entrySign_5b = canvasSign.create_image(
                573.0,
                470.0,
                image=entrySign_5
            )
            entrySign_6 = Entry(
                self,
                bd=0,
                bg="#D9D9D9",
                fg="#000716",
                highlightthickness=0,
                textvariable=controller.LAST
            )
            entrySign_6.place(
                x=493.0,
                y=451.0,
                width=160.0,
                height=36.0
            )

            #========Button Objects
            self.buttonSign_6 = buttonSign_6 = PhotoImage(
                file=ASSETS_PATH / Path("button_1.png"))
            buttonSign_6b = Button(
                self,
                image=buttonSign_6,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: controller.Signup,
                relief="flat"
            )
            buttonSign_6b.pack()
            buttonSign_6b.place(
                x=509.0,
                y=519.0,
                width=127.5384521484375,
                height=40.875
            )

            self.buttonReturn_Sign = buttonReturn_Sign = PhotoImage(
                file=ASSETS_PATH / Path("return.png"))
            buttonReturn_Sign_b = Button(
                self,
                image=buttonReturn_Sign,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: controller.changePage("homeFrame"),
                relief="flat"
            )
            buttonReturn_Sign_b.pack()
            buttonReturn_Sign_b.place(
                x=772.0,
                y=16.0,
                width=35.0,
                height=35.0
            )



