from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

empleo = "Analista de pruebas"
lugar = "Bogota"

driver = webdriver.Firefox(executable_path = "/home/santiagob/Escritorio/choucair/geckodriver")
driver.get("https://www.choucairtesting.com/empleos-2/")

element = driver.find_element_by_id("search_keywords")
element.send_keys(empleo)
element = driver.find_element_by_id("search_location")
element.send_keys(lugar)
element.send_keys(Keys.RETURN)

start = time.time()
count = 0
while count == 0:
    element = driver.find_elements_by_xpath("//li[contains(@class,'job_listing')]")
    count = len(element)
    tmp_end = time.time()
    if tmp_end - start > 60:
        count = -1

end = time.time()
if count != -1:
    print("Se encontro " + str(len(element)) + " elemento(s) en " + str(end - start) + " Segundos")
else:
    print("No se encontraron elementos")

driver.close()
