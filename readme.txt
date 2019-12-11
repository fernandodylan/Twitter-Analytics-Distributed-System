In order to use this application you will need python 3 with pip installed. After that you can proceed to install the following libraries with pip
pip install networkx
pip install tweepy
pip install flask
pip install bcrypt
pip install pymongo
pip install matplotlib
pip install selenium 
pip install gecko

In order to run the database you must install a mongodb database on the same machine as the server
On windows this can be done with an exe file from the mongodb website on linux the command is:
 sudo apt-get install -y mongodb-org

To view the database you will need a graphical interface 
The commands to install compass which is a mongo db GUI is as follows on Linux 
wget https://downloads.mongodb.com/compass/mongodb-compass_1.15.1_amd64.deb
sudo dpkg -i mongodb-compass_1.15.1_amd64.deb

Once these two commands are executed you can open your local mongo database and create a database named "influencecalculator" as well as a collection named "USERS"


The client requires the installation of android studio. Once android studio is install the client can be run on the built in emulator. 
Android studio can be installed on the android studio website.

Before installation the client and server must be configured with the ip address and port that the server will run on. 
This will need to be changed in the server.py file on line 13.
This will also need to be changed in the android client java code located in the runnable thread function. This function is located in every file of the client.
Once all the installations are complete open the server folder with a terminal and run "python3 server.py"

Subsequently the client can be opened with the android studio emulator.

Everything is now set to use the twitter influence application.
