
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from tkinter import *
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/jordanemccalla/Downloads/Software Engineering/softeng_team2023/build/assets/frame1")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#===================================Frame & Canvas Initialization
window = Tk()
window.geometry("829x654")
window.configure(bg = "#FFFFFF")
optionsFrame = Frame(window)
optionsFrame.pack()

canvasOptions = Canvas(
    optionsFrame,
    bg = "#FFFFFF",
    height = 654,
    width = 829,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvasOptions.place(x = 0, y = 0)
imageOptions_1= PhotoImage(
    file=relative_to_assets("image_1.png"))
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

imageOptions_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
imageOptions_2b = canvasOptions.create_image(
    146.0,
    327.0,
    image=imageOptions_2
)

buttonOptions_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
buttonOptions_1b = Button(
    image=buttonOptions_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
buttonOptions_1b.place(
    x=433.0,
    y=369.0,
    width=127.5384521484375,
    height=40.875
)

buttonOptions_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
buttonOptions_2b = Button(
    image=buttonOptions_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
buttonOptions_2b.place(
    x=509.0,
    y=424.0,
    width=127.5384521484375,
    height=40.875
)

buttonOptions_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
buttonOptions_3b = Button(
    image=buttonOptions_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
buttonOptions_3b.place(
    x=573.0,
    y=369.0,
    width=127.5384521484375,
    height=40.875
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

if __name__ == '__main__':
        window.mainloop()