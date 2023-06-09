# OPCUA app 


Before we start make sure you have the latest Python version up and running: 

# We install all the dependencies
pip install -r req.txt


You can mange the .xlsx file change add the data you want. 
Than using Exel you can export and csv file. Must look like 
result.csv 
Caution: Compare the files result.xlsx and result.csv , 
if you set up an other file it looks the same the structure , delimiter ";"


#EuroMap 63 , how does it work? 
We make first an request for example: 

We have an sessionpath specifiek for machine: \EM63\M223\ 

REQ_0000 EXECUTE "\EM63\M223\cycle.job"; 

Than we create an job file where we can declare what we wanna do,
when we trigger the request. For example it makes an getid folfer witj and 
get id file soo we get an 

JOB getid RESPONSE "\EM63\M614\getid\getid.log";
GETID "\EM63\M614\getid\getid.dat";

The question now is what do we effective get? How to read value data.


When we analyse an job file from Kapware ... 

We can see like an REPORT0000 file. Where we see an cyclic time of 10 seconds: 
a lot of paramters

Soo it works, when we can all the paramters with the
correct session we get an file wirh all the data. 

We gone need to filter 701 values write an Report file, soo we can get the data. 

This was an early file DATE,TIME,ActStrCsh[1],ActTimFill[1],ActTimPlst[1],ActPrsMachSpecMax,ActPrsXfrSpec[1],ActTimCyc,@ActExtStartPos,ActTmpBrlZn[1,1],ActTmpBrlZn[1,2],ActTmpBrlZn[1,3],ActTmpBrlZn[1,4],ActTmpBrlZn[1,5],ActTmpBrlZn[1,6],ActTmpBrlZn[1,7],ActTmpBrlZn[1,8],ActStrXfr[1],ActStsMach,ActCntCycRej,ActCntCyc,ActStrPlst[1],@ActExtTorque6,@ActInjPeakTime,@ActInjPeakPos,@ActEjeDevTrq
20220729,14:33:23,4.73,0.475,1.92,1028,1026,10.22,4.80,527.1,0.0,518.0,509.1,491.1,0.0,0.0,148.2,10.00,"0A000",162,49174,48.50,31.86,0.478,9.78,-3.2



To convert the app to an exe needs to be all in one file, that is why the Allone.py is soo long. 

We gone have 2 seperated apps one with EuroMap63 and one with OPCUA GUI. 

All send data via SQL.


# FEATURES that need to be added 
Reverse main table soo we can see the data in chronogy 
add and remove element feature 
monitoring data, individual buttons to see every machine we connected with, data, status an graph 



#Features to add: 15/05 
Need to fix some bugs about when does the graphs appear. 
Show them in a picture ?

#Sending the data to the cloud ?We send it like the Spark ? 
Where do we send the data, we send it using MQTT ? like a broker? 
One by one to the broker?











