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

_logger = logging.getLogger(__name__)


#Class SubHandler 

class SubHandler:
    """
    Subscription Handler. To receive events from server for a subscription
    This class is just a sample class. Whatever class having these methods can be used
    """

    def datachange_notification(self, node: Node, val, data):
        """
        called for every datachange notification from server
        """
        _logger.info("datachange_notification %r %s", node, val)

    def event_notification(self, event: ua.EventNotificationList):
        """
        called for every event notification from server
        """
        pass

    def status_change_notification(self, status: ua.StatusChangeNotification):
        """
        called for every status change notification from server
        """
        _logger.info("status_notification %s", status)


def opcua_client(path_certificate, path_key, username, password): 
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

            """
                Set SecureConnection mode. String format:
                Policy,Mode,certificate,private_key[,server_private_key]
                where Policy is Basic128Rsa15, Basic256 or Basic256Sha256,
                Mode is Sign or SignAndEncrypt
                certificate, private_key and server_private_key are
                paths to .pem or .der files
                Call this before connect()

            """
            #set_security(policy, certificate_path, private_key_path,server_certificate_path=None,mode=ua.MessageSecurityMode.SignAndEncrypt):
            client.set_security(None, path_certificate, path_key, server_certificate_path=None, mode=None)
            print("Start connecting ")
            sleep(0.5)
            client.connect()
            print("Done connecting")
            sleep(0.5)


        finally:
           client.disconnect()



async def Opcua_using_async():  
    handler = SubHandler()

    #How much do i wanna wait before to read the data
    ReadEvery = 10
    ReadStatus = True

    while ReadStatus:
        client = Client(url="opc.tcp://10.210.40.215:4880/Arburg")
        # client = Client(url="opc.tcp://localhost:53530/OPCUA/SimulationServer/")

        # We need to set the user and password for verification
        client.set_user('host_computer')
        client.set_password(' ')

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

                #define header names
                col_names = ["f-value", "Value", "Description-level-higher"]
                #tabelValue = tabulate(data, headers=col_names)
                #display 
                print("Parameters inside MachineData")
                #print(tabulate(data, headers=col_names))

                #Getting the data every 10 seconds 
                sleep(0.5)

                sg.popup(tabulate(data, headers=col_names))
                #client.disconnect()


               # print("BEFORE", f80001_value)
                #print("BEFORE", ff9000_value)

            #Read it making an request 
            #For the moment it is hard coded to have an structure 
                

            """while True:
                    #Change to 10 seconds 
                    #sleep(1)

                    #We just wanna disconnect 
                    #client.disconnect()  # Throws a exception if connection is lost"""

                #To get out of the while    
            
            ReadStatus = False

        
        except (ConnectionError, ua.UaError):
            _logger.warning("Reconnecting in 2 seconds")
            sleep(1)
             #display 
            print("Parameters inside MachineData")
           
    

sg.theme('DarkAmber')   # Add a touch of color

#We are adding some menus 
menu_def = [['add certficates', ['certificate', 'key',]],
                ['Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],
                ['Help', 'About...'],]

# All the stuff inside your window.
tab1_layout =  [[sg.T('feedback console')]]

layout = [
  [sg.Menu(menu_def)],
  [sg.Text('Enter the endpoint address'), sg.InputText('opc.tcp://10.210.40.215:4880/Arburg')],
  [sg.Text('Enter username'), sg.InputText('host_computer')],
  [sg.Text('Enter password'), sg.InputText('')],
  [sg.Multiline(size=(30, 5), key='textbox')],  # identify the multiline via key option
  [sg.Button('connect'), sg.Button('Cancel')],
  #[sg.Tab('Console', tab1_layout)]
]

# Create the Window
window = sg.Window('Opcua client app', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    
    event, values = window.read()
    #Print for the log consone interface 
    # Need to remove it after the debug fase. 
    path_certificate = "C:/Users/te542932/Desktop/Machines-connectie-karakteristieken/OpcuaSoftwareNodeDYS/Python_GUI_client_OPCUA/certificate.pem"
    path_key = "C:/Users/te542932/Desktop/Machines-connectie-karakteristieken/OpcuaSoftwareNodeDYS/Python_GUI_client_OPCUA/key.pem"

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

    elif event == "connect": 
        if __name__ == "__main__":
            logging.basicConfig(level=logging.INFO)
            #Trying to fix an bug 
            asyncio.get_event_loop().run_until_complete(Opcua_using_async())
            print("Connect test")
            

    
    #Only run ocua function if i get the addresses first
    elif path_certificate != "" and path_key != "":
         #opcua_client(path_certificate, path_key, values[2], values[3])
         Opcua_using_async()
         print('Trying an connextion with the next parameters : ', values[1], values[2], values[3], path_certificate, path_key)


    #sg.popup('Results', 'The value returned from popup_get_file', text)
    print('The endpointaddress ', values[1])
    print('The username', values[2])
    print('The password', values[3])

   
         
# We try to connect, making an class connection 
window.close()