# Read files 
# Write files
# Read structure
# Using shared folder 162.109.54.99//
# Files : 
# Machienes to test with EU 63 that work 
#M236 , m461; m582 , m607 , m614 , m615 

# https://docs.fabfile.org/en/latest/getting-started.html

# To connect to the server to retirve the data 
from contextlib     import closing
from fabric.network import connect

user = 'root' # your SSH user
host = '162.109.54.99' #IP of your server
port = '80' #SSH Port
remote_file = '/m614/cycle.txt'

with closing(connect(user, host, port)) as ssh, \
     closing(ssh.open_sftp()) as sftp, \
     closing(sftp.open(remote_file)) as file:
    for line in file:
        print(line)

import sys

class EuroMap63:

    #What is not working for the moment accessing the folder on the server 

    # We make an Session file. That calls the job file 
    # Later we can scale it for for multiple differant session names
    # We write in the correct folder 
    # We can again make an tabel where we have the address to the file 
    #162.109.54.99//
    #string_in_string = "Shepherd {} is on duty.".format(shepherd)

    machine= "/M614/"

    def sessionStart():
        server = "162.109.54.99//"
        #with open( '{}M614/SESS0000.req'.format(server), 'w') as f:
        with open( '//162.109.54.99/M614/SESS0000.req', 'w') as f:
            f.write('REQ_0000 EXECUTE "C:\EM63\M614\cycle.job";')
    
    # If it does not exist make one other wise don't, first we look for the file 
    def makeJob(): 
        with open('REPORT0001.job', 'w') as f:
            f.write('REQ_0000 EXECUTE "C:\EM63\M614\cycle.job";')

    # The dat file has the data we wanna read
    def ReadDat():
         with open('REPORT0001.dat') as f:
             lines = f.readlines()
             print(lines)
    
    #We wanna split the file .dat and read the values. Maybe a Graph or something similar. 
#EuroMap63.sessionStart()



