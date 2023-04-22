from tkinter import *
from tkinter import messagebox

import base64
import os

def main_screen():
    screen=Tk()
    screen.geometry("357x398")
    
    #icon
    image_icon=PhotoImage(file="keys.png")
    screen.iconphoto(False,image_icon)
    
    screen.title("PctApp")
    screen.mainloop()
    
main_screen()