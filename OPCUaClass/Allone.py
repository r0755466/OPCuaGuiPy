
# pip install -r req.txt

import PySimpleGUI as sg
#Import for OPC Ua uses
import sys
sys.path.insert(0, "..")
import logging

import asyncio

from time import sleep

from asyncua import Client, ua, Node
#For file reading purposes 
from asyncua.client.ua_file import UaFile

from IPython import embed

from tabulate import tabulate


from pysondb import db

import array

import math 
import numpy as np 
import pandas as pd

_logger = logging.getLogger(__name__)



"""
    def opcua_client(self, path_certificate, path_key, username, password): 
        if __name__ == "__main__":
    
            client = Client('opc.tcp://10.210.40.215:4880/Arburg')

            # clit = Client("opc.tcp://admin@localhost:4840/freeopcua/server/") #connect using a user
            # opc.tcp://10.210.40.215:4880/Arburg
            # opc.tcp://host_computer@10.210.40.215:4880/Arburg
            # We try to start an session 
            # We call ur set function 
            #set_user()
            #set_password()
            #Added for session try 
            try:
                
                client.set_user(username)
                client.set_password(password)
                client.load_client_certificate(path_certificate)
                client.load_private_key(path_key)

                    #Set SecureConnection mode. String format:
                    #Policy,Mode,certificate,private_key[,server_private_key]
                    #where Policy is Basic128Rsa15, Basic256 or Basic256Sha256,
                    #Mode is Sign or SignAndEncrypt
                    #certificate, private_key and server_private_key are
                    #paths to .pem o .der files
                    #Call this before connect()

                #set_security(policy, certificate_path, private_key_path,server_certificate_path=None,mode=ua.MessageSecurityMode.SignAndEncrypt):
                client.set_security(None, path_certificate, path_key, server_certificate_path=None, mode=None)
                print("Start connecting ")
                sleep(0.5)
                client.connect()
                print("Done connecting")
                sleep(0.5)
        finally:
             client.disconnect()
    """

class Connection:
        async def Opcua_using_async(end, user, user_pass):  
            #handler = subhandler.subHandler()

            #How much do i wanna wait before to read the data
            ReadEvery = 10
            ReadStatus = True

            while ReadStatus:
                client = Client(url=end)
                # client = Client(url="opc.tcp://localhost:53530/OPCUA/SimulationServer/")

                # We need to set the user and password for verification
                client.set_user(user)
                client.set_password(user_pass)


                #Can connect and get the datum
                try:
                    async with client:
                        _logger.warning("Connected")
                        #subscription = await client.create_subscription(500, handler)
                        #Scan the server for structures: 
                        # .
                        
                        print("Getting Machine parameters from MachineData")

                        # Can place it later in an apart class, calles like MachineDataStructs
    
                               #f80001
                        struct1 =  client.get_node("ns=2;i=117622")
                        f80001_value = await struct1.read_value()

                        #f9000
                        struct2 =  client.get_node("ns=2;i=117672")
                        ff9000_value = await struct2.read_value()

                        #f9000A
                        struct3 =  client.get_node("ns=2;i=117682")
                        f9000A_value = await struct3.read_value()

                        #f9001
                        struct4 =  client.get_node("ns=2;i=117692")
                        f9001_value = await struct4.read_value()

                        #f9002
                        struct5 =  client.get_node("ns=2;i=117692")
                        f9002_value = await struct5.read_value()

                        #t007
                        struct6 =  client.get_node("ns=2;i=117522")
                        t007_value = await struct6.read_value()

                        #t008
                        struct7 =  client.get_node("ns=2;i=117532")
                        t008_value = await struct7.read_value()

                        #t009
                        struct8 =  client.get_node("ns=2;i=117532")
                        t009_value = await struct8.read_value()

                        #t010
                        struct9 =  client.get_node("ns=2;i=117552")
                        t010_value = await struct9.read_value()

                        #t9000
                        struct10 =  client.get_node("ns=2;i=117572")
                        t9000_value = await struct10.read_value()

                        #We have ur label 
                        #Create data


                        # Tabel herbruiken, de structuur. Dan kan je het veranderen. 
                        # Manueel invoegen: 
                        # Manueel, meerdere variables herhalend voor uitbreding. 


                        data = [["f80001", f80001_value, " "], 
                                ["f9000", ff9000_value," "], 
                                ["f9000A", f9000A_value," "], 
                                ["f9001", f9001_value," "],
                                ["f9002", f9002_value," "],
                                ["t007", t007_value," "],
                                ["t007", t008_value," "],
                                ["t008", t009_value," "],
                                ["t009", t010_value," "],
                                ["t0010", t9000_value," "],
                                ["t9000", 88," "],
                                ["t9001", 88," "],
                                ["t9002", 88," "],
                                ["t99128", 88," "]]

                        # Save in an database under the name: 
                        

                        #define header names
                        col_names = ["f-value", "Value", "Description-level-higher"]
                        #tabelValue = tabulate(data, headers=col_names)
                        #display 
                        print("Parameters inside MachineData")
                        #print(tabulate(data, headers=col_names))

                        #Getting the data every 10 seconds 
                        sleep(0.5)

                        tabel = tabulate(data, headers=col_names)
                        #client.disconnect()


                    # print("BEFORE", f80001_value)
                        #print("BEFORE", ff9000_value)

                    #Read it making an request 
                    #For the moment it is hard coded to have an structure 
                       

                    while True:
                            #Change to 10 seconds 
                            sleep(1)

                            #We just wanna disconnect 
                            #client.disconnect()  # Throws a exception if connection is lost"""

                        #To get out of the while    
                    
                    ReadStatus = False
    
                
                except (ConnectionError, ua.UaError):
                    sleep(1)
                    #display 
            
            return tabel

        async def Get_all_data(end, user, user_pass, file_address):
            
            def get_namespacedata(file_address): 
                    dotcomma = []
                    quotionmarks = []
                    namespace = np.loadtxt(file_address,delimiter=";", dtype=str, usecols= (1))
                    indexNf = np.loadtxt(file_address,delimiter=";", dtype=str, usecols= (2))
                    description = np.loadtxt(file_address,delimiter=";", dtype=str, usecols= (3))

                    namespacedata = np.array(namespace)
                    indexNfdata = np.array(indexNf)
                    descrdata = np.array(description)
                    # We need to fill an array with lenght namespacedata with ; 
                    
                    for i in range(indexNfdata.size):
                        dotcomma.append(";")
                        #print(dotcomma)
                
                    for q in range(indexNfdata.size):
                        quotionmarks.append('"')
                        #print(dotcomma)

                    first = np.core.defchararray.add(quotionmarks,namespacedata)
                    sumdata = np.core.defchararray.add(first,dotcomma)
                    last = np.core.defchararray.add(sumdata,indexNfdata)
                    Result = np.core.defchararray.add(last,quotionmarks)

                    # No quatations 
                    qua = np.core.defchararray.add(namespacedata, dotcomma )
                    qua1 = np.core.defchararray.add(qua,indexNfdata)

                    np.char.strip(qua1)
                   
                    #print(namespace, indexNfdata, Result)
                    list_qua1 = qua1.tolist()
                    listdescr = descrdata.tolist()
                   # print(list_qua1) 
                    size_ = indexNfdata.size
                    return list_qua1, listdescr, size_, dotcomma

            ReadEvery = 10
            ReadStatus = True
            
            input_ns, input_ds, size_, dotcomma = get_namespacedata(file_address)

            while ReadStatus:
                    client = Client(url=end)
                    # client = Client(url="opc.tcp://localhost:53530/OPCUA/SimulationServer/")

                    # We need to set the user and password for verification
                    client.set_user(user)
                    client.set_password(user_pass)

                    #Can connect and get the datum
                    try:
                        async with client:
                            _logger.warning("Connected")
                            #subscription = await client.create_subscription(500, handler)
                            #Scan the server for structures: 
                            
                            print("Getting Machine parameters from MachineData")

                            # Can place it later in an apart class, calles like MachineDataStructs

                            #print(input_ns)

                            ouput = []

                            for i in range(size_):

                                # 23 of 71 = 23/71 are unreable 
                                if i == 6 or i == 9 or i == 10 or i == 11 or i == 18 or i == 26 or i == 27 or i == 28 or i == 29 or i == 56 or i == 57 or i == 58 or i == 59 or i == 60 or i == 61 or i == 62 or i == 63 or i == 64 or i == 66  or i == 67  or i == 68  or i == 69  or i == 70:
                                    ouput.append("none")
                                    continue

                                struct = client.get_node(input_ns[i])
                                data_struct= await struct.read_value()

                                ouput.append(data_struct)

                            #Json 
                            # {value: ouput[i], description: input_ds[i]}, 

                            # Just a column 
                            sumdata = np.core.defchararray.add(ouput, dotcomma)
                            sum_ = np.core.defchararray.add(sumdata, input_ds)

                            # Csv
                            # Store it in a csv file 
                            # convert array into dataframe

                            #We need to add on the top (i , value, description )
                            print(sum_)
                            DF = pd.DataFrame(sum_)
                        
                            # save the dataframe as a csv file
                            DF.to_csv("result.csv")
                            print("Done csv")
                            
                            #print(sum_)
            

                        print("ReadStatus False")
                        ReadStatus = False
                        done = "tt"
                        
                                  
                    except (ConnectionError, ua.UaError):
                        sleep(1)
                        print("Something with the connextion went wrong")
                        #display 
                        

                
            return done
                    




# Log in with password and encryt ? 
# To make safe the data 

#Json database to save the config

#First time we need to use the command 
a = db.getDb('configGUI.json')

endpoint1 = "opc.tcp://10.210.40.215:4880/Arburg"
username1 = "host_computer"
user_pas1 = ' '

endpoint2 = "opc.tcp://10.210.40.215:4880/Arburg"
username2 = "host_computer"
user_pas2 = ' '

endpoint3 = "opc.tcp://10.210.40.215:4880/Arburg"
username3 = "host_computer"
user_pas3 = ' '

# Server 1
servername = " "
groupname = " "

# Server 2
servername2 = " "
groupname2 = " "

# Server 3
servername3 = " "
groupname3 = " "

sg.theme('DarkBrown')   # Add a touch of color

#We are adding some menus 
menu_def = [['add certficates', ['certificate', 'key',]],
                ['Help', 'About...'],
                ['app', 'close'],
                
                ]

# All the stuff inside your window.
tab1_layout =  [[sg.T('feedback console')]]

connection_layout = [
[sg.Text('Server-name'), sg.InputText(servername)],
[sg.Text('Group'), sg.InputText(groupname)],
[sg.Button('Create'), sg.Button('Cancel')],
]

# We save the server name in an array an we call it or in an database
# We have max 3 configurations: but we need to be able to change every server name, update with the id 

layout1 = [
  [sg.Text('Server-name'), sg.InputText(servername)],
  [sg.Text('Group'), sg.InputText(groupname)],
  [sg.Text('Enter the endpoint address'), sg.InputText(endpoint1)],
  [sg.Text('Enter username'), sg.InputText(username1)],
  [sg.Text('Enter password'), sg.InputText(user_pas1)],
  [sg.Button('connect'), sg.Button('Cancel')],
]

# Maybe can use it later pysondb convert --c file.csv --d file.json
# TKinter function to display and edit value in cell
def edit_cell(window, key, row, col, justify='left'):

        global textvariable, edit, text

        def callback(event, row, col, text, key):
            global edit
            # event.widget gives you the same entry widget we created earlier
            widget = event.widget
            if key == 'Focus_Out':
                # Get new text that has been typed into widget
                text = widget.get()
                # Print to terminal
                print("From widget" , text)
                #For in the main function 


            # Destroy the entry widget
            widget.destroy()
            # Destroy all widgets
            widget.master.destroy()
            # Get the row from the table that was edited
            # table variable exists here because it was called before the callback
            values = list(table.item(row, 'values'))

            # Store new value in the appropriate row and column
            values[col] = text

            # Store in new data the new value 
            data[col] = text

            table.item(row, values=values)


            # We also store it in the data file 
    
            edit = False
           
          
        if edit or row <= 0:
            return

        edit = True
        # Get the Tkinter functionality for our window
        root = window.TKroot
        # Gets the Widget object from the PySimpleGUI table - a PySimpleGUI table is really
        # what's called a TreeView widget in TKinter
        table = window[key].Widget
        # Get the row as a dict using .item function and get individual value using [col]
        # Get currently selected value
        text = table.item(row, "values")[col]
        # Return x and y position of cell as well as width and height (in TreeView widget)
        x, y, width, height = table.bbox(row, col)

        # Create a new container that acts as container for the editable text input widget
        frame = sg.tk.Frame(root)
        # put frame in same location as selected cell
        frame.place(x=x, y=y, anchor="nw", width=width, height=height)

        # textvariable represents a text value
        textvariable = sg.tk.StringVar()
        textvariable.set(text)
        # Used to acceot single line text input from user - editable text input
        # frame is the parent window, textvariable is the initial value, justify is the position
        entry = sg.tk.Entry(frame, textvariable=textvariable, justify=justify)
        # Organizes widgets into blocks before putting them into the parent
        entry.pack()
        # selects all text in the entry input widget
        entry.select_range(0, sg.tk.END)
        # Puts cursor at end of input text
        entry.icursor(sg.tk.END)
        # Forces focus on the entry widget (actually when the user clicks because this initiates all this Tkinter stuff, e
        # ending with a focus on what has been created)
        entry.focus_force()
        # When you click outside of the selected widget, everything is returned back to normal
        # lambda e generates an empty function, which isc turned into an event function 
        # which corresponds to the "FocusOut" (clicking outside of the cell) event
        entry.bind("<FocusOut>", lambda e, r=row, c=col, t=text, k='Focus_Out':callback(e, r, c, t, k))


        return text

#Tabel headings 
# 71 values until ns71

# Auto fill 
# For lus 

# What if we wanna expand the tabel ? 

# Making tabel dimensions 

# Wanna do it only once 
def read_csv_file(): 
    # using loadtxt()
    # first colum 
    browsername = np.loadtxt("dataSS.csv",delimiter=";", dtype=str, usecols= (0))
    print(browsername)
    # 2nd colum 
    namespace = np.loadtxt("dataSS.csv",delimiter=";", dtype=str, usecols= (1))
    print(namespace)
    # 3nd colum 
    description = np.loadtxt("dataSS.csv",delimiter=";", dtype=str, usecols= (2))
    print(description)

    namespacedata = np.array(namespace)
    # Save all the resuts in an function 
    # We reasamble in an new tabel description + value, we export the tabel 


headings = ['GroupName', 'Protocol', 'endpoint', 'user', 'pass', 'csv-file-with-addresses' ]

# 4 * 6 = 24 
#Best we call it from the config file 

data = [
    ['Arburg', 'OPCUA', 'opc.tcp://10.210.40.215:4880/Arburg', 'host_computer',' ', 'dataSS.csv'],
    ['', '', '', '',' ', ''], 
    ['', '', '', '',' ', '']
]



# Data we can get out of the functions
# We can add functions like connectios successfull and expetions 
# Saving all the data in one array ??
# We load from an csv all the 
#We wanna add 71 x ns(n), we iterate the number behindn we add it into headings 

def load_config(): 
    print("loading data")
    data = [
        [ my_parser(150308794076421552), my_parser(129402203518110603), my_parser(556803059551467806) , my_parser(223225519456388549)," ", "dataSS.csv"],
        ['', '', '', '',' ', ''], 
        ['', '', '', '',' ', '']
    ]


    return data 
  

#Every time 
def save_config(row, col, value, idd):
    # Sla op de coordinaten en de waarde, bij het loaden zal de tabel oproepen met 
    # deze coordinaten
    a.updateById(idd,{"row":row})
    a.updateById(idd,{"col":col})

    if(value != None):
         a.updateById(idd,{"value":value})
 

def my_parser(id_json):
        vv = []
        test = a.getByQuery({"id":id_json})
        data1 = test[0]
        #for r in data1 ['row']: 
            #print(r)
       # for c in data1 ["col"]: 
           # print(c)
        for v in data1 ["value"]:
            vv.append(v)
        #rcv = ''.join(vv)
        print(''.join(vv))
        #row = r
        #col = c 
        value = ''.join(vv)
        #return r , c , value 
        return value 

def main():
    global edit 
    edit = False
    sg.set_options(dpi_awareness=True)

    layout = [
            [sg.Menu(menu_def)],
            [sg.Combo(values=('Mange first connection', 'Mange second connection', 'Mange third connection'), default_value='Mange first connection', readonly=False, k='-AmountConnnection-')]
    ]

    # We insert data in the tabel using data, than we update the values from the tabel
    layout_ = [[sg.Table(values=load_config(), headings=headings, max_col_width=25,
                        font=("Arial", 15),
                        auto_size_columns=True,
                        # display_row_numbers=True,
                        justification='right',
                        num_rows=20,
                        alternating_row_color=sg.theme_button_color()[1],
                        key='-TABLE-',
                        # selected_row_colors='red on yellow',
                        # enable_events=True,
                        # select_mode=sg.TABLE_SELECT_MODE_BROWSE,
                        expand_x=True,
                        expand_y=True,
                        enable_click_events=True,  # Comment out to not enable header and other clicks
                        )],

              [sg.Text('Cell clicked:'), sg.T(key='-CLICKED_CELL-')], [sg.Button('connect'), sg.Button('Cancel')],]
    
    logging_layout = [[sg.Multiline(size=(30, 30), key='-pop up-')]
    ]  # identify the multiline via key option


    layout +=[[sg.TabGroup([[      
                        sg.Tab('Connection', layout_),
                        sg.Tab('Output', logging_layout)
                    ]], key='-pop up-', expand_x=True, expand_y=True),
                    
                    ]]

    
    window = sg.Window('Clickable Table Element', layout, resizable=True, finalize=True)

    while True:
        print()
        event, values = window.read()
        path_certificate = "C:/Users/te542932/Desktop/Machines-connectie-karakteristieken/OpcuaSoftwareNodeDYS/Python_GUI_client_OPCUA/certificate.pem"
        path_key = "C:/Users/te542932/Desktop/Machines-connectie-karakteristieken/OpcuaSoftwareNodeDYS/Python_GUI_client_OPCUA/key.pem"

        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        # Checks if the event object is of tuple data type, indicating a click on a cell

        elif isinstance(event, tuple):
            if isinstance(event[2][0], int) and event[2][0] > -1:
                cell = row, col = event[2]
                # This the row or col where we are clicking to change it

            # Displays that coordinates of the cell that was clicked on
            window['-CLICKED_CELL-'].update(cell)

            # Every time we call the function we save the value 
            cell_data = edit_cell(window, '-TABLE-', row+1, col, justify='right')
            #Save the data from the specific cell 
            
            # We can save the value of every 
            # row1, col1, value1 = my_parser(150308794076421552) 

            # In functie van de row en col met de juiste id uploaden 

            # Manueel alle rows and colums 

                 # Saving the data 

            print("From widget ...", text, row, col ) 

            if row == 0 and col == 0:  
                save_config(0, 0, text, 150308794076421552)

            elif row == 0 and col == 1:  
                save_config(0, 1, text, 129402203518110603)

            elif row == 0 and col == 2:  
                save_config(0, 2, text, 556803059551467806)

            elif row == 0 and col == 3:  
                save_config(0, 3, text, 223225519456388549)

            elif row == 0 and col == 4:  
                save_config(0, 4, text, 118972688174942392)

            elif row == 0 and col == 5:  
                save_config(0, 5, text, 289290901641572105)

            print("From main", cell_data, row, col ) 
            #Every time we save an value we wanna know what is the value, what value we wanna save and where. 
            # We coud loop the row and col and in function of it we save the value in the correct coordinates

            # 4 * 9 matrix 

            # 36 slotten 
            # Aanvullen met de id om data te kunnen opslaan per venster
            # Wil ik per venster ?? 
            
            # When we want to call this function ?? 
        
  
        elif values[0] == 'certificate':
            sg.popup('Menu item chosen', values[0])
            path_certificate = sg.popup_get_file('Please enter a file name')
        
        elif values[0] == 'key':
            sg.popup('Menu item chosen', values[0])
            path_key = sg.popup_get_file('Please enter a file name')

        elif values[0] == 'About...':
            sg.popup('This app is in progress, still have bugs, contact rayan.azzi@te.com by any questions')

        elif event == "Create": 
            servername = values[1]

        elif event == "connect": 
            if __name__ == "__main__":
                logging.basicConfig(level=logging.INFO)

                asyncio.get_event_loop().run_until_complete(Connection.Get_all_data(endpoint1, username1, user_pas1, "dataSS.csv"))
                #Trying to fix an bug 
                #We want to make multiple connextions for examle 3, but everytime we press on connection 
                #We wanna decide what the hardcoded amount is ... 

                # Before we connect we check if the end point exsist (Server check we control)

                # We coud try to make an connection name and add settings and get feedback if the settings are wrong. 
                # Like Arburg -> properties -> connection , we get a table back as response

                # Make an function for multiple connections 
                #if values["-AmountConnnection-"] == "Mange first connection":
                    # Want to add the first config 
                    #a.add({"name":endpoint1, "user":username1, "pass":user_pas1, "server-name":servername, "groupname":groupname})
                       
                            # We update an exsisting saved config / load if there is none typed
                            #a.updateById("270693355111457007",{"name":values[3]})
                            #a.updateById("270693355111457007",{"user":values[4]})
                            #a.updateById("270693355111457007",{"server-name":values[1]})
                            #a.updateById("270693355111457007",{"groupname":values[2]})
                       
                   # print("wait")
                    #tabelC1 = asyncio.get_event_loop().run_until_complete(Connection.Opcua_using_async(endpoint1, username1, user_pas1))
                    #sg.popup(tabelC1)
          
            
                if values["-AmountConnnection-"] == "Mange second connections":
                    # Want to add the first config 
                    #a.add({"name":endpoint2, "user":username2, "pass":user_pas2, "server-name":servername2, "groupname":groupname2})
                   
                    print("Second")
                    #tabelC1 = asyncio.get_event_loop().run_until_complete(Connection.Opcua_using_async(endpoint1, username1, user_pas1))
                    #sg.popup(tabelC1)

        # Make this function return the new array 
      
    
        elif event == "cancel":
            window.close()

        elif event == "close":
            window.close()


        #Only run ocua function if i get the addresses first
        elif path_certificate != "" and path_key != "":
            #opcua_client(path_certificate, path_key, values[2], values[3])
            print('Trying an connextion with the next parameters : ', values[1], values[2], values[3], path_certificate, path_key)

       
    #sg.popup('Results', 'The value returned from popup_get_file', text)
    print('values 1 ', values[1])
    print('Value 2 ', values[2])
    print('value 3 ', values[3])
    print('value 4 ', values[4])
    print('Data', data)

    window.close()

main()