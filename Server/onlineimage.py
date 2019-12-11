#This page is used to upload the image from the twitter analytics to imgur
from imgurpython import ImgurClient
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime


album = None
image_path = "graph.jpg"
#The imgur api is used and the keys are obtained.
client_id =
client_secret = 
imgur_username = ""
imgur_password = ""

#ingur client initializes the api keys
client = ImgurClient(client_id, client_secret)

#authorization pin is initialized 
authorization_url = client.get_auth_url('pin')

#using selenium we can open a firefox browser automatically logging into the account specified and get the pin
driver = webdriver.Firefox()
driver.get(authorization_url)

#find the username and password elements on the html page and inputting the ones we have specified
username = driver.find_element_by_xpath('//*[@id="username"]')
password = driver.find_element_by_xpath('//*[@id="password"]')
username.clear()
username.send_keys(imgur_username)
password.send_keys(imgur_password)

driver.find_element_by_name("allow").click()

#if we can log in in 5 seconds abort 
timeout = 5 
try:
    element_present = EC.presence_of_element_located((By.ID,'pin'))
    WebDriverWait(driver, timeout).until(element_present)
    pin_element = driver.find_element_by_id('pin')
    pin = pin_element.get_attribute("value")
except TimeoutException:
    print("Timed out waiting for page to load")
driver.close()

credentials = pin

#initialize the image
config = {
    'album': album,
    'name': "Nodes",
    'title': "Node Graph",
    'description': 'Node Graph for twitter followers: {0}'.format(datetime.now())
}
#upload the image to imgur and return the url to save in database
print("Uploading Image...")
image = client.upload_from_path(image_path, config=config, anon=False)
print("DONE")
print("{0}".format(image['link']))
