from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re

lat=19.0713236
long=73.076675

link = 'https://stevemorse.org/jcal/latlon.php'
driver = webdriver.Chrome(r"C:\Users\mborra\chromedriver.exe")
driver.get(link)
seq = driver.find_elements_by_tag_name('iframe')
#print("No of frames present in the web page are: ", len(seq))
iframe = driver.find_elements_by_tag_name('iframe')[0]
driver.switch_to.frame(iframe)
time.sleep(2)
#print(driver.page_source)
inputElement = driver.find_element_by_name("latitude")
inputElement.send_keys(str(lat))
inputElement = driver.find_element_by_name("longitude")
inputElement.send_keys(str(long))
driver.find_element_by_xpath("//input[@type='button' and @value='Determine Address']").click()
time.sleep(1)
#print(driver.page_source)
s = driver.page_source
result = re.search('<br><i>LocationIQ</i><br>(.*)<br><br><i>MapQuest', s)
location=result.group(1)
driver.close()