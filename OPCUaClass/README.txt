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



