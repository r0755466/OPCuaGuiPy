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



async def main():
    handler = SubHandler()

    #How much do i wanna wait before to read the data
    ReadEvery = 10

    while True:

        # We hard code max connections are for example 5 
        
    
        client = Client(url="opc.tcp://0.0.0.0:4841/Arburg")

        #client = Client(url="opc.tcp://10.210.40.215:4880/Arburg")

        # client = Client(url="opc.tcp://localhost:53530/OPCUA/SimulationServer/")

        # We need to set the user and password for verification
        client.set_user('host_computer')
        client.set_password(' ')

        #Can connect and get the datum
        try:
            async with client:
                _logger.warning("Connected")
                subscription = await client.create_subscription(500, handler)
                #Scan the server for structures: 
                # ...

                while True: 
                    time(2)
                    print("Connected with server with Endpoint ", url)


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
