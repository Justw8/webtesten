from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('enter the location of the Chromedriver here')
driver.get("http://www.python.org") 
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("selenium")
elem.send_keys(Keys.RETURN)
assert "Google" in driver.title # this will throw an assert error
driver.close()
