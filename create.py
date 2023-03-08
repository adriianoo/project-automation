from selenium import webdriver

# Pfad der Brave Browser-Exe
brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

# ChromeOptions-Objekt
option = webdriver.ChromeOptions()
option.binary_location = brave_path

# Webdriver-Objekt unter Verwendung des ChromeOptions-Objekt
browser = webdriver.Chrome(options=option)

# Opens login url
browser.get('https://github.com/login')




#python_button = browser.find_element_by_xpath("//input[@name='login']")[0]
#python_button.send_keys('adriianoo')