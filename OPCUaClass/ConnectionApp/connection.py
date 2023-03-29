
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
#from subhandler import subHandler
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

            
                        print("Coud not make an connection")  

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
                        done = "Succesfully connected"

                except :
                    print("Something wrong, looks like the username, password or endpoint is wrong")  
                    # If something went wrong we stop the lus
                    ReadStatus = False

            return done , DF


        async def Get_all_data_anonymous(end, file_address):
            
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

            
                        print("Coud not make an connection")  

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
                        done = "Succesfully connected"

                except :
                    print("Something wrong, looks like the username, password or endpoint is wrong")  
                    # If something went wrong we stop the lus
                    ReadStatus = False

            return done , DF
                    

                    
