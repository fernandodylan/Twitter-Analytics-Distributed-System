import socket

#Socket Object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind socket to ip and port

serversocket.bind(("localhost", 9000))
#192.197.54.35 school
print("Binding Successful ")



serversocket.listen(10)

#Listen for connections forever
while True:
    #Accept Connections
    clientsocket, address = serversocket.accept()
    print("Connected to ", address)

    #Listen for Messages and Print them to the Console
    data = clientsocket.recv(1024) 
    print("Received: ", repr(data))

    
    

