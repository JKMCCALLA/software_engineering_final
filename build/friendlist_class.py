#===================================Library Definitions
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path
from PIL import Image, ImageTk

class friendlistFrame(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)
 
            OUTPUT_PATH = Path(__file__).parent
            ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame7")

            #===============Canvas Objects
            scroll_bar = Scrollbar(self)
            canvasFriendList = Canvas(
                self,
                bg = "#FFFFFF",
                height = 654,
                width = 829,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge",
                yscrollcommand=scroll_bar.set
            )
            
            scroll_bar.pack( side = RIGHT,
                            fill = Y)
            canvasFriendList.place(x = 0, y = 0)
            self.imageSkills_1 = imageSkills_1 = PhotoImage(
                file=ASSETS_PATH / Path("image_1.png"))
            
            imageSkills_1b = canvasFriendList.create_image(
                572.3466796875,
                140.26365661621094,
                image=imageSkills_1
            )

            canvasFriendList.create_rectangle(
                389.0,
                279.0,
                756.0,
                621.0,
                fill="#FFFFFF",
                outline="")

            self.imageSkills_2 = imageSkills_2 = PhotoImage(
                file=ASSETS_PATH / Path("image_2.png"))
            imageSkills_2b = canvasFriendList.create_image(
                146.0,
                327.0,
                image=imageSkills_2
            )

            canvasFriendList.create_text(
                402.0,
                283.0,
                anchor="nw",
                text="Friends",
                fill="#2578A9",
                font=("Kreon Bold", 30 * -1)
            )
            posX = 425
            posY = 350

            canvasFriendList.pack()
            
            scroll_bar.config( command = canvasFriendList.yview )

            #===============Button Objects
            self.message = message = PhotoImage(
                file=ASSETS_PATH / Path("message.png"))
            self.friend_list = list(controller.ConfigLoad()["friends"].values())
            self.line = line = PhotoImage(
                file=ASSETS_PATH / Path("line.png"))
            
            
            self.buttonReturn_Options = buttonReturn_Options = PhotoImage(
                file=ASSETS_PATH / Path("return.png"))
            
            buttonReturn_Options_b = Button(
                self,
                image=buttonReturn_Options,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: controller.changePage("optionsFrame"),
                relief="flat"
            )
            buttonReturn_Options_b.pack()
            buttonReturn_Options_b.place(
                x=772.0,
                y=16.0,
                width=35.0,
                height=35.0
            )
            for friend in self.friend_list:
                button = Button(self,
                                image=message,
                                borderwidth=0,
                                highlightthickness=0,
                                command=lambda: controller.changePage("undoneFrame"),
                                relief="flat"
                            )
                
                canvasFriendList.create_text(
                    posX,
                    posY,
                    anchor="nw",
                    text=friend,
                    fill="black",
                    font=("Kreon Bold", 30 * -1)
                )

                button.place(
                    x = posX + 300, 
                    y = posY
                )
                posY += 75
            '''

            # Add 9-by-5 buttons to the frame
            rows = len(self.friend_list)
            for i in range(0, rows):
                    button = Button(self,
                                image=message,
                                borderwidth=0,
                                highlightthickness=0,
                                command=lambda: controller.changePage("undoneFrame"),
                                relief="flat"
                            )
                    label = Label(self, text=self.friend_list[i])
                    label.grid(row=i, column=0, columnspan=4)
                    button.grid(row=i, column=4, columnspan=1)

            '''
