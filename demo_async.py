import sys
from time import sleep
sys.path.insert(0, "..")
import logging

from opcua import Client


if __name__ == "__main__":
    #logging.basicConfig(level=logging.DEBUG)
    client = Client("opc.tcp://10.210.40.215:4880/Arburg")
    # client = Client("opc.tcp://admin@localhost:4840/freeopcua/server/") #connect using a user
    try:
        print("wait")
        sleep(0.5)
        print("go")
        client.connect()
        print("annndddd")
        sleep(0.5)
        print("done")
        root = client.get_root_node()
        print("Objects node is: ", root)
        # Node objects have methods to read and write node attributes as well as browse or populate address space
        print("Children of root are: ", root.get_children())
        print("name of root is", root.get_browse_name())
        objects = client.get_objects_node()
        #print("childs og objects are: ", objects.get_children())
        print("noted")
        var = client.get_node("ns=2;i=140842")
        var = var.get_value()
        print("node value: ",var)
    finally:
        sleep(2)
        client.disconnect()
