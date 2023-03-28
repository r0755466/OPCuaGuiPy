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

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Connectivity application")
        self.geometry(f"{1100}x{650}")



        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=150, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Tabel connection", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=1, padx=20, pady=(20, 10))

        # We wanna add an add device button
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        # It is placed in an grid 
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(15, 15))

        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create textbox
        # We can what is in the text box using functions like state="disabled"
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # create slider and progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        # Establsich connection
        self.sidebar_button_1 = customtkinter.CTkButton(self.slider_progressbar_frame, text="Establsich connection", command=self.establisched)
        self.sidebar_button_1.grid(row=2, column=0, padx=20, pady=10)

        # create tabview
        self.tabview = customtkinter.CTkTabview(self.sidebar_frame, width=250 , height=450)
        # the grid inside the main grid (where we have the containement)
        self.tabview.grid(row=0, column=1, padx=(10, 0), pady=(10, 0), sticky="nsew")
        self.tabview.add("Arburg")
        self.tabview.add("Fanuc")
        self.tabview.add("Otto Vision")
        self.tabview.add("Bruder")
        self.tabview.tab("Arburg").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Fanuc").grid_columnconfigure(0, weight=1)
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Arburg"), text="Session configuration")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

    

        # create main entry and button
        self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("Arburg"),
                                                    values=["host_computer"])
        self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))

        self.combobox_2 = customtkinter.CTkComboBox(self.tabview.tab("Arburg"),
                                                    values=[" "])
        self.combobox_2.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.combobox_3 = customtkinter.CTkComboBox(self.tabview.tab("Arburg"),
                                                    values=["opc.tcp://10.210.40.215:4880/Arburg"])
        self.combobox_3.grid(row=3, column=0, padx=20, pady=(10, 10))

        self.combobox_4 = customtkinter.CTkComboBox(self.tabview.tab("Arburg"),
                                                    values=["opc.tcp://10.210.40.215:4880/Arburg"])
        self.combobox_4.grid(row=3, column=0, padx=20, pady=(10, 10))

        self.sidebar_button_1 = customtkinter.CTkButton(self.tabview.tab("Arburg"), text="Add Machine", command=self.addmachine_event)
        self.sidebar_button_1.grid(row=4, column=0, padx=20, pady=(10, 10))
        
        self.combobox_1.set("Set the username")
        self.combobox_2.set("Set the paswwords")
        self.combobox_3.set("Set the endpoint")
        # We wanna set it correctly, soo it works.
        self.combobox_4.set("Folder with namespaces id")

        # Loading when it is getting the data 
        self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")

        # set default values

        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

        # We can start or stop de progress bar:: 
        self.progressbar_1.configure(mode="indeterminnate")
        self.progressbar_1.start()
        self.progressbar_1.stop()

        # using * 20 you can add many times the same line code cool 
        self.textbox.insert("0.0", "Connection output\n\n" + "Once the connection is establisched data is gone apear below: \n\n")

      
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    
    def addmachine_event(self):
        print("Adding an machine")

        #We best read the size we wanna store, soo we get the best result. 
        # Read table, read all 
    

            

            # We need to read how many elements and than we can add the new one on the correct index 

        def createtable(self): 
            # Create multiple lists

            machinetype = ["Arburg"]
            Protocol = ["OPC UA"]
            username = [self.combobox_3.get()]
            endpoint = [self.combobox_4.get()]
            password = [' ']
            columns=['Machinetype','Protocol','username','password', 'endpoint']

            # Create DataFrame from multiple lists
            df = pd.DataFrame(list(zip(machinetype,Protocol,username, password, endpoint)), columns=columns)

            print(df)
            # We wanna first read the table and write one more than the last index.

            Amount_saved_configs = read_csv_file()
            print("test", Amount_saved_configs)

            df.to_excel('tabel.xlsx', index=Amount_saved_configs + 1)
            self.textbox.insert("0.0", "Arburg\n\n")

            # We have  to make ur table and than be able to retrive the data: 
            # We add than every time and index more than the last. 
            
        #read_csv_file()
        createtable(self)
        #read_csv_file()
        #get_data()

        # We coud call an other function 

        # Before we load the tabel already esxiting

        # We select an csv file we wanna add
        # We read it
        # We add one position more

        # We load the new table

        
    def establisched(self): 
        # we wanna call connection class
        print("Trying to connect")


if __name__ == "__main__":
    app = App()
    app.mainloop()


# Woud be nice we can manage every connection we load an select if we wanna get data or not, like stop process or continue. 
# Like switches, also secuirty to log in the application. 

# We have an configuration box, where we go and add the config. 
# Like type of machine , protocol is than specific per machine. 
# All the machines we add they are visualised on the left side. 

# we can see how many machines.


# We need to add the data in an csv file and we call the dat that we have added inside of it.