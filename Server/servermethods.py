import pymongo
import time
import string
from flask import Flask
from flask_bcrypt import Bcrypt

#Functions to Hash the Passwords in the Database
app = Flask(__name__)
bcrypt = Bcrypt(app)

#Function to return the analysis
def datavalues():
    return "Send this message over to the Client"







#Login function to check whether user exists in the Database
def login(username, password):

    #Create list to hold parsed values
    document = []

    #Make a Connection with the Database
    connection = pymongo.MongoClient("localhost",27017)

    #Connect to the Database
    database = connection["influencecalculator"]
    collection = database["USERS"]

    #Check is user exists and get thier hashed password
    if database.collection.find({"username": username}):

        query = {"username": username}
        result = collection.find(query)
        for x in result:
            document = [x["password"]]
    
    
    if not document:
        return False



    result = document[0]
    hashed_password = bcrypt.check_password_hash(result, password)
    
    if hashed_password == True:
        print("Verified")
        return "Verified"
   
    else:
        print("Denied")
        return "Denied"
    

    

    



#Register function to add user to database
def register(username, password): 
 
    #print("Message: ", message, message2, message3)
    print("Username: " + username)

    #Make a Connection with the Database
    connection = pymongo.MongoClient("localhost",27017)

    #Connect to the Database
    database = connection["influencecalculator"]
    collection = database["USERS"]

    #Hash Password
    hashed_password = bcrypt.generate_password_hash(password)

    #Create insertion items
    users = {"username": username, "password": hashed_password}


    collection.insert_one(users)

    #Return Test Value
    return "yes"


