import socket
import sys
import threading
import pymongo
import time
import string
from servermethods import *
import pickle
#from onlineimage import *


#change addess and port depending on where the server is being run from 
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
        
        #Determine which command is sent from the Client and execute that command

        #Register command from client
        if command == "register":
            #Save values received into array and to split them up
            username = newdata[1]
            password = newdata[2]
            handle = newdata[3]
            print(handle)
            #call te database function in servermethods to add entries to database
            sendback = register(username, password, handle)

            #return to the client whether the query failed or went through
            if sendback == False:
                errormessage = "Denied2"
                sendback_byte = errormessage.encode()
                conn.sendall(sendback_byte)
                conn.close()
            if sendback == True:
                errormessage = "Verified"
                sendback_byte = errormessage.encode()
                conn.sendall(sendback_byte)
                conn.close()
                
                
        #Login command received from client
        if command == "login":
            username = newdata[1]
            password = newdata[2]
            #Call the database function in server methods to check if the password mataches the username registered
            sendback = login(username, password)

            #If it doesnt match return denied to client
            if sendback == False:
                errormessage = "Denied2"
                sendback_byte = errormessage.encode()
                conn.sendall(sendback_byte)
                conn.close()
                

            sendback_byte = sendback.encode()
            conn.sendall(sendback_byte)
        
        #Growth command for the average likes in 6 months
        if command == "growth":
            #Get the username from the client and initialize a list for the values we want to send back
            username = newdata[1]
            likes = []
            months = []
            

            #Get the handle with the given username and parse the data
            handle = getHandle(username)
            handlestr = str(handle)
            data = getLikesSixMonths(handlestr)

            #Convert the data into a string
            for i in range(len(data)):
                months.append(data[i][0])

            for i in range(len(data)):
                likes.append(data[i][1])


            #Reverse the Lists to the correct order
            months.reverse()
            likes.reverse()

            #Convert lists to String
            months_str = ""
            likes_str = ""
          

            months_str = ' '.join(map(str, months)) 
            likes_str = ' '.join(map(str, likes)) 

            #Send strings over connection
            sendback_months = months_str.encode()
            conn.sendall(sendback_months)

            #Must send a space in order for the client to parse the information
            space = " "
            send_space = space.encode()
            conn.sendall(send_space)

            sendback_likes = likes_str.encode()
            conn.sendall(sendback_likes)

       
            conn.close()


        #Command for getting the average likes for 4 weeks
        if command == "growth2":
            username = newdata[1]
            likes = []
            weeks = []
            
            #Using the username sent from the client, call a database function to return the users handle
            handle = getHandle(username)
            handlestr = str(handle)
            #perform the twitter parsing on that handle. Function located in server methods
            data = getLikesforWeeks(handlestr)

            #Convert the data into a string
            for i in range(len(data)):
                weeks.append(data[i][0])

            for i in range(len(data)):
                likes.append(data[i][1])


            #Reverse the Lists to the correct order
            weeks.reverse()
            likes.reverse()

            #Convert lists to String
            weeks_str = ""
            likes_str = ""
            

            weeks_str = ' '.join(map(str, weeks)) 
            likes_str = ' '.join(map(str, likes)) 

            #Send strings over connection
            sendback_weeks = weeks_str.encode()
            conn.sendall(sendback_weeks)

            #Must send a space in order for the client to parse the information
            space = " "
            send_space = space.encode()
            conn.sendall(send_space)

            sendback_likes = likes_str.encode()
            conn.sendall(sendback_likes)

       
            conn.close()




        #Function that is used to get average retweets for 4 weeks
        if command == "growth3":
            username = newdata[1]
            tweets = []
            months = []

            #Using the username sent from the client, call a database function to return the users handle
            handle = getHandle(username)
            handlestr = str(handle)
            data = getTweetsforWeeks(handlestr)

            #Convert the data into a string
            for i in range(len(data)):
                months.append(data[i][0])

            for i in range(len(data)):
                tweets.append(data[i][1])


            #Reverse the Lists to the correct order
            months.reverse()
            tweets.reverse()

            #Convert lists to String
            months_str = ""
            tweets_str = ""
            

            months_str = ' '.join(map(str, months)) 
            tweets_str = ' '.join(map(str, tweets)) 

            #Send strings over connection
            sendback_months = months_str.encode()
            conn.sendall(sendback_months)

            space = " "
            send_space = space.encode()
            conn.sendall(send_space)

            sendback_tweets = tweets_str.encode()
            conn.sendall(sendback_tweets)

       
            conn.close()


        #Function that is used to get average retweets per 6 months
        if command == "growth4":

            username = newdata[1]
            tweets = []
            weeks = []

            #Using the username sent from the client, call a database function to return the users handle
            handle = getHandle(username)
            handlestr = str(handle)
            data = getTweetsforMonths(handlestr)

            #Convert the data into a string
            for i in range(len(data)):
                weeks.append(data[i][0])

            for i in range(len(data)):
                tweets.append(data[i][1])


            #Reverse the Lists to the correct order
            weeks.reverse()
            tweets.reverse()

            #Convert lists to String
            weeks_str = ""
            tweets_str = ""
            

            weeks_str = ' '.join(map(str, weeks)) 
            likes_str = ' '.join(map(str, tweets)) 

            #Send strings over connection
            sendback_weeks = weeks_str.encode()
            conn.sendall(sendback_weeks)

            #Must send a space in order for the client to parse the information
            space = " "
            send_space = space.encode()
            conn.sendall(send_space)

            sendback_tweets = tweets_str.encode()
            conn.sendall(sendback_tweets)

       
            conn.close()


        #Followers method used to get the node map for analysis
        if command == "followers":
            username = newdata[1]
            #image = postImage()
            #print(image)
            image = getURL(username)
            top = getTopFollower(username)
            top_str = str(top)
            
            #Encode the image url into bytes
            sendback_url = image.encode()
            conn.sendall(sendback_url)

            #Must send a space in order for the client to parse the information
            space = " "
            send_space = space.encode()
            conn.sendall(send_space)

            #encode the string into bytes to send back to client
            sendback_top = top_str.encode()
            conn.sendall(sendback_top)
            conn.close()

        if command == "prediction":
            username = newdata[1]

            #Using the username sent from the client, call a database function to return the users handle
            handle = getHandle(username)
            handlestr = str(handle)

            #With the handle call the prediction function from server methods file
            data = makePrediction(handlestr)

            #put the return value in a string
            prediction_str = ""
            prediction_str = ' '.join(map(str, data)) 
            print(prediction_str)

            #encode the string into bytes to send back to client
            sendback_prediction = prediction_str.encode()
            conn.sendall(sendback_prediction)
            conn.close()



        
        
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








