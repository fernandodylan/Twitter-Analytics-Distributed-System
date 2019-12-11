import pymongo
import time
import string
from flask import Flask
from flask_bcrypt import Bcrypt
import base64
import tweepy
from datetime import datetime, timedelta
from ParsingData import ParsingData

#Functions to Hash the Passwords in the Database
app = Flask(__name__)
bcrypt = Bcrypt(app)

#Function to return the analysis
def getLikesSixMonths(handle):
    #Print for debugging purposes
    print(handle)
    user = ParsingData(handle)

    # Get the average number of likes
    data = user.avgLikesForSixMonths()
    print(data)

    return data


def getLikesforWeeks(handle):
    user = ParsingData(handle)

    # Get the average number of likes
    data = user.avgLikesForWeek()
    print(data)

    return data

def getTweetsforMonths(handle):
    user = ParsingData(handle)

    # Get the average number of likes
    data = user.avgRetweetForSixMonths()
    print(data)
    return data

    #Call the prediction function from Parsing Data
def makePrediction(handle):
        user = ParsingData(handle)

        # Get the average number of likes
        data = user.monthlyPrediction()
        print(data)
        return data

def getTweetsforWeeks(handle):
    user = ParsingData(handle)

    # Get the average number of likes
    data = user.avgRetweetForWeek()
    print(data)
    return data

def getURL(username):
    url = [] # create an empty list for URL

    #Make a Connection with the Database
    connection = pymongo.MongoClient("localhost",27017)

    #Connect to the Database
    database = connection["influencecalculator"]
    collection = database["USERS"]

    # iterate pymongo documents with a for loop
    query = {"username": username}

    for doc in collection.find(query):
    # append each document's ID to the list
        url += [doc["url"]]

        # print out the Handle
        print ("Url:", url)
    
    return url[0]


    



def getFollowers(handle):
    user = ParsingData(handle)
    data = user.getFollowersCount()
    print("\n\n")
    print(data)

def drawnetwork(handle):
    user = ParsingData(handle)
    data = user.drawNetwork()

def getTopFollower(username):
    top = [] # create an empty list for URL

    #Make a Connection with the Database
    connection = pymongo.MongoClient("localhost",27017)

    #Connect to the Database
    database = connection["influencecalculator"]
    collection = database["USERS"]

    # iterate pymongo documents with a for loop
    query = {"username": username}

    for doc in collection.find(query):
    # append each document's ID to the list
        top += [doc["topfollower"]]

        # print out the Handle
        print ("Top Follower:", top)
    
    return top[0]





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
def register(username, password, handle): 

    document = []
 
    #print("Message: ", message, message2, message3)
    print("Username: " + username)

    #Make a Connection with the Database
    connection = pymongo.MongoClient("localhost",27017)

    #Connect to the Database
    database = connection["influencecalculator"]
    collection = database["USERS"]

    #Check is user already exists in the database
    if database.collection.find({"username": username}):
        query = {"username": username}
        result = collection.find(query)
        for x in result:
            document = [x["password"]]
    
    if not document:   
        
        #Hash Password
        hashed_password = bcrypt.generate_password_hash(password)
        print(handle)
        #Create insertion items
        users = {"username": username, "password": hashed_password, "handle": handle,"followers": "placeholder", "sixmonthsdates": "placeholder", "sixmonthslikes": "placeholder", "weekspermonthdates": "placeholder","weekspermonthlikes": "placeholder" }


        collection.insert_one(users)
        return True
    else:
        return False


def getHandle(username):
    handles = [] # create an empty list for IDs

     #Make a Connection with the Database
    connection = pymongo.MongoClient("localhost",27017)

    #Connect to the Database
    database = connection["influencecalculator"]
    collection = database["USERS"]

    # iterate pymongo documents with a for loop
    query = {"username": username}
    
    for doc in collection.find(query):
    # append each document's ID to the list
        handles += [doc["handle"]]

        # print out the Handle
        print ("Handle:", handles)
    
    return handles[0]
    



