import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as tk_fdialog
import numpy as np
from .controller import Controller

class View():
    def __init__(self, window_size=(1024, 768)):
        ### todo: move widget styles to style_config file ###
        my_style = {"bg_btn": "white",
                    "font_btn": "sans 10 bold",
                    "bg_log": "white",
                    "font_log": "sans 10 bold"}
        bg_btn,font_btn,bg_log,font_log ="white","sans 10 bold","white","sans 10 bold"
        ### ###

        self.window_size = self.get_window_resolution(window_size[0], window_size[1])

        # root
        self.root = tk.Tk()
        #self.root.configure(background="black")
        self.root.title("Koudou mk2")
        self.root.geometry(self.make_geometry_string(window_size))
        self.root.resizable(False, False)
        self.controller = None
        self.button = {}

    def set_controller(self,controller):
        self.controller = controller

    ## main methods ##
    def main_loop(self):
        self.root.mainloop()

    def close(self):
        self.root.destroy()

    ## screen positioning methods ##
    def get_window_resolution(self, window_width, window_height):
        width = 1024
        height = 768

        # If a width contains a "%", the window size is relative to the screen size
        # if it contains only a int, its an absolute value

        if isinstance(window_width, str) and window_width[-1] == "%":
            scale = int(window_width[:-1])/100
            width = self.root.winfo_screenwidth() * scale
        elif isinstance(window_width, int):
            width = window_width

        if isinstance(window_height, str) and window_height[-1] == "%":
            scale = int(window_height[:-1])/100
            height = self.root.winfo_screenheight() * scale
        elif isinstance(window_height, int):
            height = window_height

        return (width, height)
    def get_center_screen(self, window_size):
        # get the screen dimension
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - window_size[0]/2)
        center_y = int(screen_height/2 - window_size[1]/2)

        return center_x, center_y
    def make_geometry_string(self, window_size):
        self.center_x, self.center_y = self.get_center_screen(window_size)
        return f"{window_size[0]}x{window_size[1]}+{self.center_x}+{self.center_y}"