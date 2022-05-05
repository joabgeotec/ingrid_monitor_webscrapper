
#Login to Twitter using Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#Data needed to login
user_name = "email@email.email"
password = "notAveryGoodPW"
#Create a Chrome driver
driver = webdriver.Chrome()
# driver.get("https://www.twitter.com")
# #Use the data to login
# element = driver.find_element_by_id("email")
# element.send_keys(user_name)
# element = driver.find_element_by_id("pass")
# element.send_keys(password)
# #Login to Twitter
# element.send_keys(Keys.RETURN)
driver.close()
