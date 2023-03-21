#===================================Library Definitions
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path
from PIL import Image, ImageTk

class optionsFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame1")

        #===============Canvas Objects
        
        canvasOptions = Canvas(
            self,
            bg = "#FFFFFF",
            height = 654,
            width = 829,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvasOptions.place(x = 0, y = 0)
        self.imageOptions_1 = imageOptions_1 = PhotoImage(
            file=ASSETS_PATH / Path("image_1.png"))
        imageOptions_1b = canvasOptions.create_image(
            572.3466796875,
            140.26365661621094,
            image=imageOptions_1)
        canvasOptions.create_rectangle(
            389.0,
            279.0,
            757.0,
            528.0,
            fill="#FFFFFF",
            outline="")

        self.imageOptions_2 = imageOptions_2 = PhotoImage(
            file=ASSETS_PATH / Path("image_2.png"))
        imageOptions_2b = canvasOptions.create_image(
            146.0,
            327.0,
            image=imageOptions_2
        )

        canvasOptions.create_text(
            534.0,
            313.0,
            anchor="nw",
            text="Hi {User}",
            fill="#000000",
            font=("Kreon Bold", 20 * -1)
        )
        canvasOptions.pack() 

        #==============Button Objects

        self.buttonOptions_1 = buttonOptions_1 = PhotoImage(
            file=ASSETS_PATH / Path("button_1.png"))
        buttonOptions_1b = Button(
            self,
            image=buttonOptions_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.changePage("jobFrame"),
            relief="flat"
        )
        buttonOptions_1b.pack()
        buttonOptions_1b.place(
            x=433.0,
            y=369.0,
            width=127.5384521484375,
            height=40.875
        )

        self.buttonOptions_2 = buttonOptions_2 = PhotoImage(
                file=ASSETS_PATH / Path("button_2.png"))
        buttonOptions_2b = Button(
            self,
            image=buttonOptions_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.changePage("skillsFrame"),
            relief="flat"
        )
        buttonOptions_2b.pack()
        buttonOptions_2b.place(
            x=509.0,
            y=424.0,
            width=127.5384521484375,
            height=40.875
        )
        self.buttonOptions_3 = buttonOptions_3 = PhotoImage(
                file=ASSETS_PATH / Path("button_3.png"))
        buttonOptions_3b = Button(
            self,
            image=buttonOptions_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.changePage("undoneFrame"),
            relief="flat"
        )
        buttonOptions_3b.pack()
        buttonOptions_3b.place(
            x=573.0,
            y=369.0,
            width=127.5384521484375,
            height=40.875
        )

        self.buttonReturn_Options = buttonReturn_Options = PhotoImage(
                file=ASSETS_PATH / Path("return.png"))
        buttonReturn_Options_b = Button(
            self,
            image=buttonReturn_Options,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.changePage("homeFrame"),
            relief="flat"
        )

        buttonReturn_Options_b.pack()
        buttonReturn_Options_b.place(
            x=772.0,
            y=16.0,
            width=35.0,
            height=35.0
        )

        # Adrian changes start here downward
        # Add buttonOptions_4 (profile button)
        self.buttonOptions_4 = buttonOptions_4 = PhotoImage(
            # Needs its own png generated that says "Profile"
            file=ASSETS_PATH / Path("button_3.png"))
        buttonOptions_4b = Button(
            self,
            image=buttonOptions_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.changePage("profileFrame"),
            relief="flat"
        )
        buttonOptions_4b.pack()

        # Calculate the positions for the buttons
        button_width = 127.5384521484375
        button_height = 40.875
        horizontal_padding = 20
        vertical_padding = 20
        start_x = (1150 - (2 * button_width + horizontal_padding)) / 2
        start_y = (800 - (2 * button_height + vertical_padding)) / 2

        # Place the buttons at the calculated positions
        buttonOptions_1b.place(x=start_x, y=start_y, width=button_width, height=button_height)
        buttonOptions_3b.place(x=start_x + button_width + horizontal_padding, y=start_y, width=button_width, height=button_height)
        buttonOptions_2b.place(x=start_x, y=start_y + button_height + vertical_padding, width=button_width, height=button_height)
        buttonOptions_4b.place(x=start_x + button_width + horizontal_padding, y=start_y + button_height + vertical_padding, width=button_width, height=button_height)