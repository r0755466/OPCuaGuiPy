#One command to add all packages
# pip install -r req.txt

import sys
sys.path.insert(0, "..")

import logging
import asyncio

from asyncua import Client, ua, Node
#For file reading purposes 
from asyncua.client.ua_file import UaFile

from time import sleep

from IPython import embed

from tabulate import tabulate

_logger = logging.getLogger(__name__)


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

#Make an class that checks how many connections are they: 
# We limit the connections to 5 for example: For debugging we stay on 3. 
# We simulate ur connection 

#Make an function to get multiple conections: 


async def main():
    handler = SubHandler()

    #How much do i wanna wait before to read the data
    ReadEvery = 10
    ReadState = True

    while True:
        # We hard code max connections are for example 5 
        
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
                # ...

                while ReadState: 



                    print("Getting Machine parameters from MachineData")

                    #f80001
                    struct1 =  client.get_node("ns=2;i=117622")
                    #data = await client.load_type_definitions()  
                    # scan server for custom structures and import them. legacy code
                    data1 = await client.load_data_type_definitions() 
                    # scan server for custom structures and import them
                    f80001_value = await struct1.read_value()
                 
                    #f9000
                    struct2 =  client.get_node("ns=2;i=117672")
                    #data = await client.load_type_definitions()  
                    # scan server for custom structures and import them. legacy code
                    data2 = await client.load_data_type_definitions() 
                    # scan server for custom structures and import them
                    ff9000_value = await struct2.read_value()

                    #f9000A
                    struct3 =  client.get_node("ns=2;i=117682")
                    #data = await client.load_type_definitions()  
                    # scan server for custom structures and import them. legacy code
                    data3 = await client.load_data_type_definitions() 
                    # scan server for custom structures and import them
                    f9000A_value = await struct3.read_value()


                    # Wanna get the value of multiple nodes in one go 
                    #nodes = ['ns=2; i=117622']
                    #Value_test = client.get_values(nodes)

                   

                    alone_value = await client.load_data_type_definitions()

                    #Test get namespace 
                    namespace_index = client.get_namespace_array()

                    
                    
                    #We have ur label 
                    #Create data
                    data = [["f80001", f80001_value, " "], 
                            ["f9000", ff9000_value," "], 
                            ["f9000A", f9000A_value," "], 
                            ["f9001",   Value_test," "],
                            ["f9002", namespace_index," "],
                            ["t007", 88," "],
                            ["t007", 88," "],
                            ["t008", 88," "],
                            ["t009", 88," "],
                            ["t0010", 88," "],
                            ["t9000", 88," "],
                            ["t9001", 88," "],
                            ["t9002", 88," "],
                            ["t99128", 88," "]]

                    #define header names
                    col_names = ["f-value", "Value", "Description-level-higher"]

                    #display 
                    print("Parameters inside MachineData")
                    print(tabulate(data, headers=col_names))

                    #Getting the data every 10 seconds 
                    sleep(ReadEvery)
                    ReadState = False


                    #We disconnect when we get the data
                


               # print("BEFORE", f80001_value)
                #print("BEFORE", ff9000_value)

            #Read it making an request 
            #For the moment it is hard coded to have an structure 

            while True:
                    #Change to 10 seconds 
                    await asyncio.sleep(2)
                    await client.check_connection()  # Throws a exception if connection is lost

        except (ConnectionError, ua.UaError):
            _logger.warning("Reconnecting in 2 seconds")
            await asyncio.sleep(2)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
