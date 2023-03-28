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

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class EuroMap63:
        #What is not working for the moment accessing the folder on the server 
        # We make an Session file. That calls the job file 
        # Later we can scale it for for multiple differant session names
        # We write in the correct folder 
        # We can again make an tabel where we have the address to the file 
        #162.109.54.99//
        #string_in_string = "Shepherd {} is on duty.".format(shepherd)

        def export_csv(data): 
      
            description = data[0]
            values = data[1]

            description_ = description.split(',')
            values_ = values.split(',')

            for i in range(len(values_)):
                print(description_[i],"Values:", values_[i])
            
            return description , values
        
        # get all the ids just reading the MachineInit file. 
        # We give an feedback in function of it and we generate an tabel. 
        # Tabel

        # We save locally ur structures for ur files: 
        # We need to specify wich machine
        # If we get an response we have an connection ? 
        #Data not equal to 0 ? Just the Data is readble? 
        def sessionStart(machine):
            #server = "162.109.54.99//"
            #with open( '{}M614/SESS0000.req'.format(server), 'w') as f:
            with open( 'C:\EM63\{}\SESS0000.req'.format(machine), 'w') as f:
                f.write('REQ_0000 EXECUTE "C:\EM63\{}\REPORT0001.job";'.format(machine))

        
        # If it does not exist make one other wise don't, first we look for the file 
        def makeJob(machine): 
            with open('C:\EM63\{}\REPORT0001.job'.format(machine), 'w') as f:
                f.write('JOB Report0001 RESPONSE "REPORT0001.LOG";\n')
                f.write('REPORT Report0001 REWRITE "REPORT0001.DAT"\n')
                f.write('START IMMEDIATE\n')
                f.write('STOP NEVER\n')
                f.write('CYCLIC TIME 00:00:10\n')
                f.write('PARAMETERS\n')
                f.write('DATE,\n')
                f.write('ActStrCsh[1],\n')
                f.write('ActTimFill[1],\n')
                f.write('ActTimPlst[1],\n')
                f.write('ActPrsMachSpecMax,\n')
                f.write('ActTimCyc,\n')
                f.write('@ActExtStartPos,\n')
                f.write('ActTmpBrlZn[1,1],\n')
                f.write('ActTmpBrlZn[1,2],\n')
                f.write('ActTmpBrlZn[1,3],\n')
                f.write('ActTmpBrlZn[1,4],\n')
                f.write('ActTmpBrlZn[1,5],\n')
                f.write('ActTmpBrlZn[1,6],\n')
                f.write('ActTmpBrlZn[1,7],\n')
                f.write('ActTmpBrlZn[1,8],\n')
                f.write('ActStrXfr[1],\n')
                f.write('@ActTmpHRZn[1],\n')
                f.write('ActStsMach,\n')
                f.write('ActCntCycRej,    \n')
                f.write('ActCntCyc,           \n')
                f.write('ActPrsXfrSpec[1],  \n')
                f.write('ActStrPlst[1],           \n')
                f.write('@ActExtTorque6,           \n')
                f.write('@ActInjPeakTime,           \n')
                f.write('@ActInjPeakPos,           \n')
                f.write('@ActEjeDevTrq,           \n')
                f.write('@ActClampOpenTime,           \n')
                f.write('@ActEjectTime,           \n')
                f.write('@ActCloseTime,           \n')
                f.write('@ActPickupTime,           \n')
                f.write('@ActResidenceTime,           \n')
                f.write('@ActInjStartPrs,           \n')
                f.write('@ActFillingPrs,           \n')
                f.write('@ActPackEndPrs,           \n')
                f.write('@ActPackEndPos,           \n')
                f.write('@ActCmpDst,           \n')
                f.write('@ActCmpPrs,           \n')
                f.write('@ActFlowPeak,          \n')
                f.write('@ActBackFlow,          \n')
                f.write('@ActLockUpTime,          \n')
                f.write('@ActEjeCmpPos,          \n')
                f.write('@ActEjePeakTrq,          \n')
                f.write('@ActEjeAvrDevTrq,          \n')
                f.write('@ActConsumpPower,          \n')
                f.write('@ActConsumpServo,          \n')
                f.write('@ActConsumpSrvRe,          \n')
                f.write('@ActConsumpHeater,          \n')
                f.write('@ActConsumpOther,          \n')
                f.write('@ActScrewMTLoad,          \n')
                f.write('@ActclampMTLoad,          \n')
                f.write('@ActExtruderMTLoad,          \n')
                f.write('@ActScrewRev,          \n')
                f.write('@Set_SB_MaxInjectionPressure,          \n')
                f.write('@Set_SB_MaxInjectionTime,          \n')
                f.write('@Set_SB_InjectionPressureAlarm,          \n')
                f.write('@Set_SB_PackPressure1,          \n')
                f.write('@Set_SB_PackTime1,          \n')
                f.write('@Set_SB_PackPressure2,          \n')
                f.write('@Set_SB_PackPressure3,          \n')
                f.write('@Set_SB_PackTime2,          \n')
                f.write('@Set_SB_PackTime3,          \n')
                f.write('@Set_SB_PackStep,          \n')
                f.write('@ActInjPeakVol,          \n')
                f.write('@Set_SB_Barrel1Temperature,          \n')
                f.write('@Set_SB_Barrel2Temperature,          \n')
                f.write('@Set_SB_Barrel3Temperature,          \n')
                f.write('@Set_SB_Barrel4Temperature,          \n')
                f.write('@Set_SB_FeedThroatTemperature,          \n')
                f.write('@Set_SB_UpperLimitOfBarrel1Temperature,          \n')
                f.write('@Set_SB_UpperLimitOfBarrel2Temperature,          \n')
                f.write('@Set_SB_UpperLimitOfBarrel3Temperature,          \n')
                f.write('@Set_SB_UpperLimitOfBarrel4Temperature,          \n')
                f.write('@Set_SB_UpperLimitOfFeedThroatTemperature,          \n')
                f.write('@Set_SB_LowerLimitOfBarrel1Temperature,          \n')
                f.write('@Set_SB_LowerLimitOfBarrel2Temperature,          \n')
                f.write('@Set_SB_LowerLimitOfBarrel3Temperature,          \n')
                f.write('@Set_SB_LowerLimitOfBarrel4Temperature,          \n')
                f.write('@Set_SB_LowerLimitOfFeedThroatTemperature          \n')
                f.write(';          \n')
            
        # The dat file has the data we wanna read
        # Using the next commands we overwrite it. 

        def ReadDat(machine):
            with open('C:\EM63\{}\REPORT0001.dat'.format(machine)) as f:
                lines = f.readlines()
                #print(lines)

                # 50% description other 50% values 
                data = []
                data.append(lines)
                #print("This is data", data)
                # We get only the values 
                data_datfile = np.array(data[0])
                data_np1 = np.array(data)
                #print(data_np)
                #print(data_np.size
        
                #print("Description", data_datfile[0])
                #print("Values", data_datfile[1])d

                descr, valuesm614 = EuroMap63.export_csv(data_datfile)
           
                # We need to get inside the first array
                #We wanna split the file .dat and read the values. Maybe a Graph or something similar. 
                # [array([''], [''])]
            return descr, valuesm614   

        def machine_init():
             with open('C:\EM63\MACHINE_inc.ini') as f:
                lines = f.readlines()
               
                data = []
                data.append(lines)

                data_np = np.array(data[0])

                test = data[0]
                values_ =  test.split(',')

                print(values_)
          
    

        def makingconnection(cycletime, machine):
            # we call the session every 10 seconds 
            #EuroMap63.machine_init()
            print("Starting session")
            EuroMap63.makeJob(machine)
            EuroMap63.sessionStart(machine)
            print("Reading data")
            descr, valuesm614 = EuroMap63.ReadDat(machine)
            

            return descr, valuesm614

        def inputInterface(): 
            print("Welkom to this Euromap63 demo!\r\n")
            val = input("Type Start to run de demo \r\n" )

            if val == "start" or val == "Start" or val == "start " or val == " start":
                return True

            elif val == "stop" : 
                return False
            print(val)



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()


        # configure window
        self.title("Connectivity application")
        self.geometry(f"{1500}x{650}")

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
        self.textbox = customtkinter.CTkTextbox(self, width=450)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

                # We can what is in the text box using functions like state="disabled"
        self.textbox1 = customtkinter.CTkTextbox(self.sidebar_frame, width=100)
        self.textbox1.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create slider and progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        # Establsich connection
        self.sidebar_button_1 = customtkinter.CTkButton(self.slider_progressbar_frame, text="Establsich connection", command=self.establisched)
        self.sidebar_button_1.grid(row=2, column=0, padx=20, pady=10)

        self.sidebar_button_1 = customtkinter.CTkButton(self.slider_progressbar_frame, text="Delete Config", command=self.deleteconfig)
        self.sidebar_button_1.grid(row=2, column=2, padx=20, pady=10)

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
        self.combobox_2_2.set("get data every (s) Standard 10s")

        self.sidebar_button_1 = customtkinter.CTkButton(self.tabview.tab("Fanuc"), text="Add Machine", command=self.addmachine_event)
        self.sidebar_button_1.grid(row=5, column=0, padx=20, pady=(10, 10))
        
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
 

        # using * 20 you can add many times the same line code cool 
        self.textbox.insert("0.0", "Connection output\n\n" + "Once the connection is establisched data is gone apear below: \n\n")

        # We load the data first
        df = pd.read_excel('tabel.xlsx')
        print(df)

        self.textbox.delete("0.2", "end")

        # Before printing we clean the output 
        for i in range(100): 
                try:
                    # We extract the row 
                    index_list = [i]
                    df.loc[df.index[index_list]]
                    print(index_list) #we get an list of how many elements 
                    #print(df.loc[index_list,:])
                    # We print all the elements from the list 
                    self.textbox.insert('1.0', df.loc[index_list,:])
                
                except: 
                    print("Configurations saved", index_list )
                    break


        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="Delete")
        self.scrollable_frame.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        # Make an array with all the swutches 
        self.scrollable_frame_switches = []

        for m in range(i):
            switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"Remove setting {m}")
            switch.grid(row=m, column=0, padx=10, pady=(0, 20))
            # We add all the switches 
            self.scrollable_frame_switches.append(switch)
            print("Out of range")
        
            
            
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def deleteconfig(self): 
        # Need to add feature to erase file 
        
        # We also empty the data 
        self.textbox.delete("0.2", "end")

    
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


        

            # Before we remake the table we write 0 
            self.scrollable_frame_switches = []

            for m in range(i):
                switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"Remove setting {m}")
                switch.grid(row=m, column=0, padx=10, pady=(0, 20))
                # We add all the switches 
                self.scrollable_frame_switches.append(switch)

            # We need to read how many elements and than we can add the new one on the correct index 

        def createtableFanuc(self):
            # Create multiple lists
            machinetype = ["Fanuc"]
            Protocol = ["OPC UA"]
            username = [self.combobox_1.get()]
            endpoint = [self.combobox_3.get()]
            addressNs = [self.combobox_4.get()]
            password = [' ']

            columns=['Machinetype','Protocol','Username','Password', 'Endpoint', 'AddressNs']

            newdf = pd.DataFrame(list(zip(machinetype,Protocol,username, password, endpoint, addressNs)), columns=columns)

            Olddf = read_csv_file()

            df_row_merged = pd.concat([Olddf, newdf], ignore_index=True)

            df_row_merged.to_excel('tabel.xlsx', index=None)

    

        def createtableArburg(self): 
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
            
           
            # Wanna remove an configuration click on remove

            # We have  to make ur table and than be able to retrive the data: 
            # We add than every time and index more than the last. 
        
        createtable(self)
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
        self.progressbar_1.start()
    

        # Make an array with connections , Detecting the OPCUA 
        # We read the table, we iterate in function of the protocol we connect. 

        connections = []

         # We load the data first
        df = pd.read_excel('tabel.xlsx')
        
        # Maybe we can add an m.. to the machine

        # columns=['Machinetype','Protocol','Username','Password', 'Endpoint', 'AddressNs']


        # Before printing we clean the output 
        for i in range(100):  
                  
                        # We extract the row 
                        # if OPCUA ? THAN WE make the connection 
                        self.textbox.insert("0.0", " \n\n" * 3) # add on the end 

                        print("test ....", df.loc[ i ,"Protocol"])

                        if df.loc[ i ,"Protocol"] == "OPC UA":
                            # Starting connection OPC UA 
                            print("Starting connection")
                            username = df.loc[ i ,"Username"]
                            user_pas = df.loc[ i ,"Password"]
                            endpoint =  df.loc[ i ,"Endpoint"]
                            addressNs = df.loc[ i ,"AddressNs"]
                            done, dataframe = connection = asyncio.get_event_loop().run_until_complete(Connection.Get_all_data(endpoint, username, user_pas, addressNs))
                            print("from main", dataframe)

                            for m in range(15):
                                # Show the first 30 data tpyes
                                self.textbox.insert("0.0", dataframe.loc[m,:])
                        
        self.progressbar_1.stop()



        # For loop connection and we change the parameters in an loop.
        

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