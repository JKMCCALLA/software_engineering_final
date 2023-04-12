#===================================Library Definitions
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path
from PIL import Image, ImageTk

class undoneFrame(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)
 
            OUTPUT_PATH = Path(__file__).parent
            ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame3")

            #===============Canvas Objects     
            canvasUndone = Canvas(
                self,
                bg = "#FFFFFF",
                height = 654,
                width = 829,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )

            canvasUndone.place(x = 0, y = 0)
            self.imageUndone_1 = imageUndone_1 = PhotoImage(
                file=ASSETS_PATH / Path("image_1.png"))
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

            self.imageUndone_2 = imageUndone_2 = PhotoImage(
                file=ASSETS_PATH / Path("image_2.png"))
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

            #===============Button Objects
            self.buttonReturn_Undone = buttonReturn_Undone = PhotoImage(
                file=ASSETS_PATH / Path("return.png"))
            buttonReturn_Undone_b = Button(
                self,
                image=buttonReturn_Undone,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: controller.changePage("homeFrame"),
                relief="flat"
            )
            buttonReturn_Undone_b.pack()
            buttonReturn_Undone_b.place(
                x=772.0,
                y=16.0,
                width=35.0,
                height=35.0
            )
