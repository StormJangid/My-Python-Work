from selenium import webdriver

chromedriver = 'C:\\Users\\darkstorm\\Downloads\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(chromedriver)

query_string = "dada ravan"
URL = "http://www.youtube.com/results?search_query=" + query_string

driver.get(URL)

element = driver.find_element_by_id("thumbnail")

element.click()

