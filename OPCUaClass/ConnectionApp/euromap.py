# Read files 
# Write files
# Read structure
# Using shared folder 162.109.54.99//
# Files : 
# Machienes to test with EU 63 that work 
#M236 , m461; m582 , m607 , m614 , m615 
# To connect to the server to retirve the data 
# In folder all values Fanuc we can decide all the values we wanna store.
#MAXSESSIONS=12

from time import sleep
import numpy as np 
import pandas as pd
from tabulate import tabulate
import os

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
                #print(description_[i],"Values:", values_[i])
                return description , values
        
        # get all the ids just reading the MachineInit file. 
        # We give an feedback in function of it and we generate an tabel. 
        # Tabel

        # We save locally ur structures for ur files: 
        # We need to specify wich machine
        # If we get an response we have an connection ? 
        #Data not equal to 0 ? Just the Data is readble? 

        def sessionStart(machine):
            try: 
                #server = "////162.109.54.99"
               # with open( '{}M614/SESS0000.req'.format(server), 'w') as f:
                with open( 'C:\EM63\{}\SESS0000.req'.format(machine), 'w') as f:
                    f.write('REQ_0000 EXECUTE "C:\EM63\{}\REPORT0001.job";'.format(machine))
            except: 
                print(' We coud not get to C:\EM63\{}\SESS0000.req'.format(machine))
        
        # If it does not exist make one other wise don't, first we look for the file 
        def makeJob(machine): 
            try: 
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
            except: 
                print(' We coud not get to C:\EM63\{}\REPORT0001.job'.format(machine), 'w')   
                    # The dat file has the data we wanna read
                     # Using the next commands we overwrite it. 

        def ReadDat(machine):
        
            try:
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
            except: 
                print("We coud not get the data from 'C:\EM63\{}\REPORT0001.dat'.format(machine) ")

        def machine_init():
             with open('C:\EM63\MACHINE_inc.ini') as f:
                lines = f.readlines()
               
                data = []
                data.append(lines)

                data_np = np.array(data[0])

                test = data[0]
                values_ =  test.split(',')

                #print(values_)
          
    
        def makingconnection(machine):
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















