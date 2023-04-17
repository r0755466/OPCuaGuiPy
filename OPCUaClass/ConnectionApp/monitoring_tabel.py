# Monitoring tabel
import tkinter
import tkinter.messagebox
import customtkinter
from time import sleep
import sys
import logging
import asyncio
from time import sleep
from asyncua import Client, ua, Node 
from asyncua.client.ua_file import UaFile
from IPython import embed
from tabulate import tabulate
from connection import Connection 
from pysondb import db
import array
import pandas as pd
import numpy as np 
import openpyxl
#Connection class, for multiple connections 
from connection import Connection 
from euromap import EuroMap63
from dataplot import Mygraph
import matplotlib.pyplot as plt
# For the iamge 
from PIL import Image
import os

import customtkinter
import os
from PIL import Image


class ScrollableCheckBoxFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, item_list, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.command = command
        self.checkbox_list = []
        for i, item in enumerate(item_list):
            self.add_item(item)

    def add_item(self, item):
        checkbox = customtkinter.CTkCheckBox(self, text=item)
        if self.command is not None:
            checkbox.configure(command=self.command)
        checkbox.grid(row=len(self.checkbox_list), column=0, pady=(0, 10))
        self.checkbox_list.append(checkbox)

    def remove_item(self, item):
        for checkbox in self.checkbox_list:
            if item == checkbox.cget("text"):
                checkbox.destroy()
                self.checkbox_list.remove(checkbox)
                return

    def get_checked_items(self):
        return [checkbox.cget("text") for checkbox in self.checkbox_list if checkbox.get() == 1]


class ScrollableRadiobuttonFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, item_list, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.command = command
        self.radiobutton_variable = customtkinter.StringVar()
        self.radiobutton_list = []
        for i, item in enumerate(item_list):
            self.add_item(item)

    def add_item(self, item):
        radiobutton = customtkinter.CTkRadioButton(self, text=item, value=item, variable=self.radiobutton_variable)
        if self.command is not None:
            radiobutton.configure(command=self.command)
        radiobutton.grid(row=len(self.radiobutton_list), column=0, pady=(0, 10))
        self.radiobutton_list.append(radiobutton)

    def remove_item(self, item):
        for radiobutton in self.radiobutton_list:
            if item == radiobutton.cget("text"):
                radiobutton.destroy()
                self.radiobutton_list.remove(radiobutton)
                return

    def get_checked_item(self):
        return self.radiobutton_variable.get()


class ScrollableLabelButtonFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.command = command
        self.radiobutton_variable = customtkinter.StringVar()
        self.label_list = []
        self.button_list = []

    # We use the iteration number as key and the item=config
    def add_item(self, item, i, image=None):
        label = customtkinter.CTkLabel(self, text=item, image=image, compound="left", padx=5, anchor="w")
        
        button = customtkinter.CTkButton(self, text=f"Delete item{i}", width=100, height=24)

        if self.command is not None:
            button.configure(command=lambda: self.command(item, i))

        label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
        button.grid(row=len(self.button_list), column=1, pady=(0, 10), padx=5)

        self.label_list.append(label)
        self.button_list.append(button)

    def remove_item(self, item, i):
        for label, button in zip(self.label_list, self.button_list):
            pint("test........")
            if item == label.cget("text"):
                label.destroy()
                button.destroy()
                self.label_list.remove(label)
                self.button_list.remove(button)
                return

class monitoring(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Monitoring System")
        self.grid_rowconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)

        # create scrollable checkbox frame
        self.scrollable_checkbox_frame = ScrollableCheckBoxFrame(master=self, width=200, command=self.checkbox_frame_event,

                                                                 item_list=[f"item {i}" for i in range(50)])

        self.scrollable_checkbox_frame.grid(row=0, column=0, padx=15, pady=15, sticky="ns")

        self.scrollable_checkbox_frame.add_item("new item")

        # create scrollable radiobutton frame
        self.scrollable_radiobutton_frame = ScrollableRadiobuttonFrame(master=self, width=500, command=self.radiobutton_frame_event,
                                                                       item_list=[f"item {i}" for i in range(100)],
                                                                       label_text="ScrollableRadiobuttonFrame")


        self.scrollable_radiobutton_frame.grid(row=0, column=1, padx=15, pady=15, sticky="ns")
        self.scrollable_radiobutton_frame.configure(width=200)
        self.scrollable_radiobutton_frame.remove_item("item 3")

        # create scrollable label and button frame
        current_dir = os.path.dirname(os.path.abspath(__file__))

        self.scrollable_label_button_frame = ScrollableLabelButtonFrame(master=self, width=300, command=self.label_button_frame_event, corner_radius=0)
        self.scrollable_label_button_frame.grid(row=0, column=2, padx=0, pady=0, sticky="nsew")

        for i in range(20):  # add items with images
            self.scrollable_label_button_frame.add_item(f"image and item {i}")

    def checkbox_frame_event(self):
        print(f"checkbox frame modified: {self.scrollable_checkbox_frame.get_checked_items()}")

    def radiobutton_frame_event(self):
        print(f"radiobutton frame modified: {self.scrollable_radiobutton_frame.get_checked_item()}")

    def label_button_frame_event(self, item):
        print(f"label button frame clicked: {item}")
