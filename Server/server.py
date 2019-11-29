import socket
import sys
import threading
import pymongo
import time
import string
from servermethods import *

#host = "192.168.0.19"
host = "192.168.0.16" 
port = 9000
message = " "




####CLIENT THREAD FUNCTION####
def clientthread(conn, ip):
    print("Connected to: ", ip)
    while True:
        #Receive the data from the client
        data = conn.recv(1024)
        #Convert bytes to string
        message = data.decode("utf-8")

        #Parse the password and username from a single string
        newdata = message.split() #split string into a list

        #Get the username and password
        command = newdata[0]
        username = newdata[1]
        password = newdata[2]

        #Determine which command is sent from the Client and execute that command
        if command == "register":
            register(username, password)
        
        if command == "login":
            sendback = login(username, password)
            if sendback == False:
                break
                
            sendback_byte = sendback.encode()
            conn.sendall(sendback_byte)
        

        if command == "data":
            datavalues()

        
        
        #Close the connection
        conn.close()
        break 







#Create a Socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created")

try:
    serversocket.bind((host,port))
except socket.error:
    print("Failed to Bind to Socket")
    sys.exit()

print("Socket has been successfully binded...")

#Listen to incoming connection
serversocket.listen(10)



#Accept Clients
while True:
    conn, addr = serversocket.accept()

    #Start a new thread for each client
    threading._start_new_thread(clientthread, (conn,addr))








