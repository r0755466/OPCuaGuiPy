
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

#Connection class, for multiple connections 
from connection import Connection 

from pysondb import db

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

sg.theme('DarkAmber')   # Add a touch of color

#We are adding some menus 
menu_def = [['add certficates', ['certificate', 'key',]],
                ['Help', 'About...'],
                ['app', 'close'],
                
                ]

# All the stuff inside your window.
tab1_layout =  [[sg.T('feedback console')]]

layout = [
  [sg.Menu(menu_def)],
  [sg.Combo(values=('Mange first connection', 'Mange second connection', 'Mange third connection'), default_value='Mange first connection', readonly=False, k='-AmountConnnection-')]
]

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

layout2 = [

  [sg.Text('Server-name'), sg.InputText(servername2)],
  [sg.Text('Group'), sg.InputText(groupname2)],
  [sg.Text('Enter the endpoint address'), sg.InputText(endpoint2)],
  [sg.Text('Enter username'), sg.InputText(username2)],
  [sg.Text('Enter password'), sg.InputText(user_pas2)],
  [sg.Button('connect'), sg.Button('Cancel')],
]

layout3 = [
  [sg.Text('Server-name'), sg.InputText(servername3)],
  [sg.Text('Group'), sg.InputText(groupname3)],
  [sg.Text('Enter the endpoint address'), sg.InputText(endpoint3)],
  [sg.Text('Enter username'), sg.InputText(username3)],
  [sg.Text('Enter password'), sg.InputText(user_pas2)],
  [sg.Button('connect'), sg.Button('Cancel')],
]


logging_layout = [[sg.Multiline(size=(30, 5), key='-pop up-')]
]  # identify the multiline via key option


layout +=[[sg.TabGroup([[      
                    sg.Tab('Connection1', layout1),
                    sg.Tab('Output', logging_layout)

                    ]], key='-pop up-', expand_x=True, expand_y=True),
                    
                    ]]
# Maybe can use it later pysondb convert --c file.csv --d file.json

# Create the Window
window = sg.Window('Opcua client app', layout, resizable=True, finalize=True)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    # Load configuration 

    # variables 
    # Connection 1:  

    event, values = window.read()
    #Print for the log consone interface 
    # Need to remove it after the debug fase. 
    path_certificate = "C:/Users/te542932/Desktop/Machines-connectie-karakteristieken/OpcuaSoftwareNodeDYS/Python_GUI_client_OPCUA/certificate.pem"
    path_key = "C:/Users/te542932/Desktop/Machines-connectie-karakteristieken/OpcuaSoftwareNodeDYS/Python_GUI_client_OPCUA/key.pem"

    data = a.getBy({"id":"270693355111457007"})

    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    
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
        a.add({"servername":values[1], "groupname": values[2]})


    
    elif event == "connect": 
        if __name__ == "__main__":
            logging.basicConfig(level=logging.INFO)
            #Trying to fix an bug 
            #We want to make multiple connextions for examle 3, but everytime we press on connection 
            #We wanna decide what the hardcoded amount is ... 

            # Before we connect we check if the end point exsist (Server check we control)

            # We coud try to make an connection name and add settings and get feedback if the settings are wrong. 
            # Like Arburg -> properties -> connection , we get a table back as response

            # Make an function for multiple connections 
            if values["-AmountConnnection-"] == "Mange first connection":
                # Want to add the first config 
                #a.add({"name":endpoint1, "user":username1, "pass":user_pas1, "server-name":servername, "groupname":groupname})

                # We update an exsisting saved config / load if there is none typed
                a.updateById("270693355111457007",{"name":values[3]})
                a.updateById("270693355111457007",{"user":values[4]})
                a.updateById("270693355111457007",{"server-name":values[1]})
                a.updateById("270693355111457007",{"groupname":values[2]})

                tabelC1 = asyncio.get_event_loop().run_until_complete(Connection.Opcua_using_async(endpoint1, username1, user_pas1))
                sg.popup(tabelC1)
            
            elif values["-AmountConnnection-"] == "Mange second connections":
                 # Want to add the first config 
                #a.add({"name":endpoint2, "user":username2, "pass":user_pas2, "server-name":servername2, "groupname":groupname2})
                tabelC1 = asyncio.get_event_loop().run_until_complete(Connection.Opcua_using_async(endpoint1, username1, user_pas1))
                sg.popup(tabelC1)


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


# We try to connect, making an class connection 
window.close()