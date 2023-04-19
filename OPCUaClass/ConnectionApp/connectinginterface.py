import tkinter
import tkinter.messagebox
import customtkinter
from time import sleep
import sys
import logging
import asyncio

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

#My classes 
from connection import Connection 
from euromap import EuroMap63
from dataplot import Mygraph

from monitoring_tabel import monitoring
from monitoring_tabel import ScrollableLabelButtonFrame

import matplotlib.pyplot as plt
import os

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


# Paramters that can be added for later ?? 
#OPCUA 
#Duty Cycle 10
#reconnect interval 5s 
#watchdog interval 5s 

#Eu63 

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Connectivity application")
        self.geometry(f"{1500}x{650}")
        

        # Declare attribute done for OPCUA use
        self.done = ""

        self.server = True
        # configure grid layout  (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=100, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Tabel connection", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=1, padx=20, pady=(20, 10))

        # We wanna add an add device button
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=1, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        # It is placed in an grid 
        self.appearance_mode_optionemenu.grid(row=6, column=1, padx=20, pady=(15, 15))

        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=1, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=1, padx=20, pady=(10, 20))

        # create textbox
        # We can what is in the text box using functions like state="disabled"
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # We can what is in the text box using functions like state="disabled"


        # create slider and progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)

        # We can add switches for every connection to give an feedback.

      

        # Start the server 
        self.sidebar_button_1 = customtkinter.CTkButton(self.slider_progressbar_frame, text="Start the Server", command=self.establisched)
        self.sidebar_button_1.grid(row=0, column=2, padx=10, pady=10)

        self.sidebar_button_1 = customtkinter.CTkButton(self.slider_progressbar_frame, text="Stop the Server", command=self.stoptheserver)
        self.sidebar_button_1.grid(row=1, column=2, padx=10, pady=10)

        # Start monitoring data
        self.sidebar_button_1 = customtkinter.CTkButton(self.slider_progressbar_frame, text="Monitoring Data", command=self.monitoring)
        self.sidebar_button_1.grid(row=2, column=2, padx=10, pady=10)
      
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

        # For the ARBURG 
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
                                                    values=["dataSS.csv"])
        self.combobox_4.grid(row=4, column=0, padx=20, pady=(10, 10))

        self.sidebar_button_1 = customtkinter.CTkButton(self.tabview.tab("Arburg"), text="Add Machine", command=self.addmachine_event)
        self.sidebar_button_1.grid(row=5, column=0, padx=20, pady=(10, 10))

        # For the Fanuc 
        self.combobox_1_1 = customtkinter.CTkComboBox(self.tabview.tab("Fanuc"),
                                                    values=["M614"])
        self.combobox_1_1.grid(row=1, column=0, padx=20, pady=(10, 10))

        self.combobox_2_2 = customtkinter.CTkComboBox(self.tabview.tab("Fanuc"),
                                                    values=["10"])
        self.combobox_2_2.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.sidebar_button_1 = customtkinter.CTkButton(self.tabview.tab("Arburg"), text="Add Machine", command=self.addmachine_event)
        self.sidebar_button_1.grid(row=5, column=0, padx=20, pady=(10, 10))


        #For the Fanuc 
        self.combobox_1_1.set("Machine-description")


        self.sidebar_button_1 = customtkinter.CTkButton(self.tabview.tab("Fanuc"), text="Add Machine", command=self.addmachine_event)
        self.sidebar_button_1.grid(row=5, column=0, padx=20, pady=(10, 10))
        

        # For the Arburg pannel 
        self.combobox_1.set("Set the username")
        self.combobox_2.set("Set the paswwords")
        self.combobox_3.set("Set the endpoint")
        # We wanna set it correctly, soo it works.
        self.combobox_4.set("Folder with namespaces id")

        # Server loading 
        #self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        #self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")

        # Settings vieuw app 
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

        # We can start or stop de progress bar:: 
        #self.progressbar_1.configure(mode="indeterminnate")
 

        # using * 20 you can add many times the same line code cool 
        self.textbox.insert("0.0", "Connection output\n\n" + "Once the connection is establisched data is gone apear below: \n\n")

        # We load the data first
        df = pd.read_excel('tabel.xlsx')
        print(df)

        self.textbox.delete("0.2", "end")

         # create scrollable frame
        
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="Delete")
        self.scrollable_frame.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        self.scrollable_label_button_frame = ScrollableLabelButtonFrame(master=self.scrollable_frame, width=50, command=self.delete_config, corner_radius=0)
        self.scrollable_label_button_frame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
        
        for i in range(100): 
                try:
                    # We extract the row 
                    index_list = [i]
                    df.loc[df.index[index_list]]
                    print(index_list) #we get an list of how many elements 
                    #print(df.loc[index_list,:])
                    # We print all the elements from the list 
                    self.textbox.insert('1.0', df.loc[index_list,:])
                    
                    self.scrollable_label_button_frame.add_item("Config", i)
                                            
                except: 
                    print("Configurations saved", index_list )
                    self.tabelsize = i
                    break


    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)


    def monitoring(self): 
        # We start the application where we show ur differant connections
        # We can than click every connection and get a vieuws of the data. We iterate around it. 
        # Some alarms if it goes of, we get direct feedback. 
        monitor = monitoring()
        monitor.mainloop()


    def stoptheserver(self):
        self.server = False
        print("Stop server", self.server)
        return self.server

    def delete_config(self, item, index):
        print(f"label button frame clicked: {index}")  
        # We can decide witch item we wanna delete 
        # We read the csv file and we delete the row with id itme, pop out 
        # We also empty the data 
        # We read the file, we get the current structure. 
        # We make a dataframe of the current structure. 

        def read_csv_file(): 
            df = pd.read_excel('tabel.xlsx')
            print(df)
            return df

            self.scrollable_label_button_frame.remove_item("Config",0) 

        # We remove the row we want 
        # We make an new datafram 
        def removerow(item): 
            df = read_csv_file()
            
            df = df.drop(item)
            return df
        
        # We overwrite the old dataframe with the new data
        def overwirtetable(item):
            df = pd.read_excel('tabel.xlsx')

            # We iterate every colum and we rempalce it with emptyness
            columns=['Machinetype','Protocol','Username','Password', 'Endpoint', 'AddressNs', 'mdescription', 'IP' ]
            
            for column in df.columns:
                 df[column] = df[column].replace(r'\W',"")

            df.to_excel("tabel.xlsx")
            # We wirte the tabel with the newframe with the removed frame
            
            newdf = removerow(item)

        

            # We wanna drop the column unamed using an desctructor 
            newdf = newdf.loc[:, ~newdf.columns.str.contains('^Unnamed')]
            print("New dataframe", newdf)

            newdf.to_excel("tabel.xlsx")

            for i in range(100): 
                    try:
                        # We extract the row 
                        index_list = [i]
                        newdf.loc[newdf.index[index_list]]
                        print(index_list) #we get an list of how many elements 
                        #print(df.loc[index_list,:])
                        # We print all the elements from the list 
                        self.textbox.insert('1.0', newdf.loc[index_list,:])
                    
                    except: 
                        print("Configurations saved", index_list )
                        break
            
            # We delete the button with the correspondig id 

            self.textbox.delete(f"0.{str(i)}", "end")
        
        overwirtetable(index)


    def addmachine_event(self):
        print("Adding an machine")

        #We best read the size we wanna store, soo we get the best result. 
        # Read table, read all  
        def read_csv_file(): 
            df = pd.read_excel('tabel.xlsx')
            print(df)
            return df

        def print_tabel(self):
            df = pd.read_excel('tabel.xlsx')
            print(df)
    
            self.textbox.delete("0.0", "end")

            # Before printing we clean the output 
            for i in range(100): 
                        # We extract the row 
                        index_list = [i]
                        df.loc[df.index[index_list]]
                        print("ELEMENTS in tabel", index_list) 
                        
                        #we get an list of how many elements 
                        #print(df.loc[index_list,:])
                        # We print all the elements from the list 
                        # We want to reverse what we show:  
                        # We store in an array and we reverse the elements


                        self.textbox.insert("0.0", df.loc[index_list,:])

                        self.scrollable_label_button_frame.add_item("Config", i)


            # We need to read how many elements and than we can add the new one on the correct index 

        def createtableFanuc(self):
            print("Adding Fanuc")
            # Create multiple lists
            mdescription = [self.combobox_1_1.get()]
            machinetype = ["Fanuc"]
            Protocol = ["EU 63"]
            IP = ["x.x.x.x.x"]
          
            columns=['mdescription','Machinetype','Protocol','IP']
            newdf = pd.DataFrame(list(zip(mdescription, machinetype, Protocol, IP)), columns=columns)
            Olddf = read_csv_file()
            df_row_merged = pd.concat([Olddf, newdf], ignore_index=True)
            df_row_merged.to_excel('tabel.xlsx', index=None)
            

        def createtableArburg(self): 
            print("Adding Arburg")
            # Create multiple lists
            machinetype = ["Arburg"]
            Protocol = ["OPC UA"]
            username = [self.combobox_1.get()]
            endpoint = [self.combobox_3.get()]
            addressNs = [self.combobox_4.get()]
            password = [' ']
            columns=['Machinetype','Protocol','Username','Password', 'Endpoint', 'AddressNs']

            # Create DataFrame from multiple listss
            newdf = pd.DataFrame(list(zip(machinetype,Protocol,username, password, endpoint, addressNs)), columns=columns)

            # We wanna first read the table and write one more than the last index.

            Olddf = read_csv_file()

            # We add the old data frame to the new one:
        
            df_row_merged = pd.concat([Olddf, newdf], ignore_index=True)

            df_row_merged.to_excel('tabel.xlsx', index=None)

            # After we add an table, we also print it 
            
            print(self.tabview.get())
           
            # Wanna remove an configuration click on remove

            # We have  to make ur table and than be able to retrive the data: 
            # We add than every time and index more than the last. 
        
        if (self.tabview.get() == "Arburg" ): 
            print("if Arburg")
            createtableArburg(self)
            print_tabel(self)
            #read_csv_file()
            #get_data()

        elif (self.tabview.get() == "Fanuc" ):
            print("if Fanuc")
            createtableFanuc(self)
            print_tabel(self)
            #read_csv_file()
            #get_data()


        # We coud call an other function 
        # Before we load the tabel already esxiting
        # We select an csv file we wanna add
        # We read it
        # We add one position more
        # We load the new table


    # We load the data from the tabel on the start 
      
    def establisched(self): 
        # We show how many connections we have
        # Show data
        # Catch for the connection        
        #self.progressbar_1.start()


        # Make an array with connections , Detecting the OPCUA 
        # We read the table, we iterate in function of the protocol we connect. 

        connections = []

         # We load the data first
        df = pd.read_excel('tabel.xlsx')
        
        # Maybe we can add an m.. to the machine

        # columns=['Machinetype','Protocol','Username','Password', 'Endpoint', 'AddressNs']

        print("status self.server:", self.server)

        # We coud add to the table the status of the server ?
        # The status of multiple Machines ? 

        serverStart = True

        while(serverStart):
            # Before printing we clean the output
            # Max  200 machines 
            
            # Stop the server 
            # We wanna only read in function of the size of the # * rows. 

            # +1 to give one iteration time to execute the code before stoping the server

            for i in range(self.tabelsize): 
                        try: 
                          
                            # We extract the row 
                            # if OPCUA ? THAN WE make the connection 
                            self.textbox.insert("0.0", " \n\n" * 3) # add on the end 
                            username = df.loc[ i ,"Username"]
                            user_pas = df.loc[ i ,"Password"]
                            endpoint =  df.loc[ i ,"Endpoint"]
                            addressNs = df.loc[ i ,"AddressNs"]
                            print("Reading the the protocol: ", df.loc[ i ,"Protocol"])


                            # Try OPC UA 
                            try: 
                                
                                done, dataframe, output = connection = asyncio.get_event_loop().run_until_complete(Connection.Get_all_data(endpoint, username, user_pas, addressNs))
                                print("from main", dataframe)
                    
                                # Later we need to take it from an class 
                                x = input_ds
                                # corresponding y axis values
                                y = output
                    
                                # plotting the points 
                                plt.plot(x, y)
                                
                                # naming the x axis
                                plt.xlabel('x - axis')
                                # naming the y axis
                                plt.ylabel('y - axis')
                                
                                # giving a title to my graph
                                plt.title('Arbrg OPC Ua data')

                                # We coud iterate pictures of differant machines, we save a picture for every machine .. 
                                plt.savefig('Graph.png')

                                plt.show()

                                
                                #self.progressbar_1.stop()

                            # Try OPC UA anonymous 
                            except: 

                                done, dataframe, output, input_ds = connection = asyncio.get_event_loop().run_until_complete(Connection. Get_all_data_anonymous(endpoint, addressNs))
                                
                                self.done = done 

                                if self.done =="wrong network": 
                                    # We stop the server, and we give the feedback to the user 
                                    serverStart = False
                                    print("The Network is wrong, we can't get to the machine")
                                    self.textbox.insert("0.0", "The Network is wrong, we can't get to the machine\n\n" ) # add on the end 
                               
                                print("from main", dataframe)
                                self.textbox.insert("0.0", "The OPC Ua connection with endpoint\n\n" + df.loc[ i ,"Endpoint"] + " is anonymous\n\n"  ) # add on the end
                                # Mygraph.drawgraph(output, machineID, machineType
                                #Mygraph.drawgraph(self, output, input_ds, i, "Arburg")
                                
                                t = []
                                s = []
                                #To get all the data from the 
                                print("From main", dataframe)

                                for i in range(71):
                                    
                                    if (i == 38 or i ==  41 or i == 44 or i == 47 or i == 50 ): 
                                        t.append(input_ds[i])
                                        s.append(output[i])
                                   
                                    x = t
                                    # corresponding y axis values
                                    y = s
                    
                                # plotting the points 
                                plt.plot(x, y)
                                
                                # naming the x axis
                                plt.xlabel('x - axis')
                                # naming the y axis
                                plt.ylabel('y - axis')
                                
                                # giving a title to my graph
                                plt.title('Arburg OPC Ua')
                                
                                # function to show the plot
                                plt.savefig('Graph.png')

                                #Show image 
                                plt.show()

                                #self.Graph_img = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Graph.png")), size=(500, 150))
                                #self.home_frame_large_image_label = customtkinter.CTkLabel(self.slider_progressbar_frame, text="", image=self.Graph_img)
                                #self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)


                                for m in range(15):
                                    # Show the first 30 data tpyes
                                    self.textbox.insert("0.0", dataframe.loc[m,:])

                                #self.progressbar_1.stop()
                          

    
                        except: 
                            #There as problem with this expetation 

                            #self.textbox.insert("0.0", " \n\n" * 2) # add on the end 
                            #self.textbox.insert("0.0", "Something is wrong with the OPCUA connection\n\n" + df.loc[ i ,"Endpoint"] + "\n\n" ) # add on the end 
                            #self.textbox.insert("0.0", "Check if you are in the right netwok(igonre if other connections work)\n\n" ) # add on the end 
                            print("Jumping to next connection: " + str(i) )

                            # We can repeat the process every 10 seconds

                        # Try EU63 
                        try: 
                            if df.loc[ i ,"Protocol"] == "EU 63":
                                # Starting connection OPC UA 
                                # data
                                m_name = df.loc[i, "mdescription"]
                                print("Connecting to:  " + m_name)
                                print("from main", dataframe)

                                try: 
                                    descr, valuesm614 = EuroMap63.makingconnection(m_name)
                                except:
                                    self.textbox.insert("0.0", "Something went wrong with EU 63 - Machine\n\n" + df.loc[ i ,"mdescription"] + "\n\n" ) # add on the end 
                                    
                                for m in range(15):
                                    # Show the first 30 data tpyes
                                    self.textbox.insert("0.0", dataframe.loc[m,:])

                            elif (df.loc[ i ,"Protocol"] != "EU 63" and  df.loc[ i ,"Protocol"] != "OPC UA"): 
                                print("No data in the tabel")

                        except:
                            print("Something is wrong with the EU63 ftp files")
                            print("Shutting down server")
                            self.textbox.insert("0.0", " \n\n" * 2) # add on the end 
                            self.textbox.insert("0.0", " Something is wrong with the EU63 ftp files\n\n" ) # add on the end
                
            print("Tabel size from server", self.tabelsize)
        
            serverStart = False
            
            # We check if somone pressed on server Stop 
            #if self.server == True: 
               # serverStart = True

            #elif self.server == False:
                #serverStart = False
            

          
            

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
