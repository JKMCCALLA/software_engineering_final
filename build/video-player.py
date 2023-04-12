import tkinter as tk
from tkVideoPlayer import TkinterVideo

root = tk.Tk()
root.geometry("829x654")

videoplayer = TkinterVideo(master=root, scaled=True)
videoplayer.load(r"video.mp4")
videoplayer.pack(expand=True, fill="both")

videoplayer.play() # play the video

root.mainloop()