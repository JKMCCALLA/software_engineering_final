#===================================Library Definitions
from tkinter import *
from tkinter import Canvas, Entry, Button, PhotoImage
from pathlib import Path

class jobFrame(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)
 
            OUTPUT_PATH = Path(__file__).parent
            ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame5")

            #===============Canvas Objects
            canvasJob = Canvas(
                self,
                bg = "#FFFFFF",
                height = 654,
                width = 829,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )

            canvasJob.place(x = 0, y = 0)
            self.imageJob_1 = imageJob_1 = PhotoImage(
               file=ASSETS_PATH / Path("image_1.png"))
            imageJob_1b = canvasJob.create_image(
                572.3466796875,
                140.26365661621094,
                image=imageJob_1
            )

            canvasJob.create_rectangle(
                389.0,
                279.0,
                756.0,
                621.0,
                fill="#FFFFFF",
                outline="")

            self.imageJob_2 = imageJob_2 = PhotoImage(
                file=ASSETS_PATH / Path("image_2.png"))
            imageJob_2b = canvasJob.create_image(
                146.0,
                327.0,
                image=imageJob_2
            )

            canvasJob.create_text(
                402.0,
                283.0,
                anchor="nw",
                text="Job Search",
                fill="#2578A9",
                font=("Kreon Bold", 30 * -1)
            )
            canvasJob.pack()

            #=============Button Declarations (Job Frame)

            self.buttonJob_1 = buttonJob_1 = PhotoImage(
                file=ASSETS_PATH / Path("button_1.png"))
            buttonJob_1b = Button(
                self,
                image=buttonJob_1,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: controller.changePage("postFrame"),
                relief="flat"
            )
            buttonJob_1b.pack()
            buttonJob_1b.place(
                x=509.0,
                y=342.0,
                width=127.5384521484375,
                height=40.875
            )

            self.buttonReturn_Job = buttonReturn_Job = PhotoImage(
                file=ASSETS_PATH / Path("return.png"))
            buttonReturn_Job_b = Button(
                self,
                image=buttonReturn_Job,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: controller.changePage("optionsFrame"),
                relief="flat"
            )
            buttonReturn_Job_b.pack()
            buttonReturn_Job_b.place(
                x=772.0,
                y=16.0,
                width=35.0,
                height=35.0
            )


