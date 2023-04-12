#===================================Library Definitions
from tkinter import *
from tkinter import Canvas, Entry, Button, PhotoImage
from pathlib import Path

class homeFrame(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)

            OUTPUT_PATH = Path(__file__).parent
            ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame0")

            #===============Canvas Objects
            canvas = Canvas(
                self,
                bg = "#FFFFFF",
                height = 654,
                width = 829,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )
            canvas.place(x = 0, y = 0)

            self.image_image_1 = image_image_1 = PhotoImage(
                file=ASSETS_PATH / Path("image_1.png"))
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

            self.image_image_2 = image_image_2 = PhotoImage(
                 file=ASSETS_PATH / Path("image_2.png"))
            image_2 = canvas.create_image(
                180,
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

            #===========Form Entry Objects
            self.entry_image_1 = entry_image_1 = PhotoImage(
                file=ASSETS_PATH / Path("entry_1.png"))
            entry_bg_1 = canvas.create_image(
                573.8876647949219,
                369.01800537109375,
                image=entry_image_1
            )
            entry_1 = Entry(
                self,
                bd=0,
                bg="#D9D9D9",
                fg="#000716",
                highlightthickness=0,
                textvariable=controller.USERNAME,
                font=("Arial-BoldMT", int(25))
            )

            entry_1.place(
                x=402.06500244140625,
                y=344.8645935058594,
                width=343.64532470703125,
                height=46.30682373046875
            )

            self.entry_image_2 = entry_image_2 = PhotoImage(
                file=ASSETS_PATH / Path("entry_2.png"))
            entry_bg_2 = canvas.create_image(
                573.8876647949219,
                428.04888916015625,
                image=entry_image_2
            )
            entry_2 = Entry(
                self,
                bd=0,
                bg="#D9D9D9",
                fg="#000716",
                highlightthickness=0,
                textvariable=controller.PASSWORD,
                show="*",
                font=("Arial-BoldMT", int(25))
                )
            entry_2.place(
                x=402.06500244140625,
                y=403.8954772949219,
                width=343.64532470703125,
                height=46.30682373046875
            )

            #===============Button Objects
            self.button_image_1 = button_image_1 = PhotoImage(
                file=ASSETS_PATH / Path("button_1.png"))
            button_1 = Button(
                self,
                image=button_image_1,
                borderwidth=0,
                highlightthickness=0,
                command=controller.Login,
                relief="flat"
            )
            button_1.pack()
            button_1.place(
                x=402.06500244140625,
                y=478.4608154296875,
                width=127.5384521484375,
                height=40.875
            )
            self.bind('<Return>', controller.Login)

            self.button_image_2 = button_image_2 = PhotoImage(
                file=ASSETS_PATH / Path("button_2.png"))
            button_2 = Button(
                self,
                image=button_image_2,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: controller.changePage("signFrame"),
                relief="flat"
            )
            button_2.pack()
            button_2.place(
                x=555.4299926757812,
                y=478.4608154296875,
                width=127.5384521484375,
                height=40.875
            )

