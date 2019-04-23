from selenium import webdriver



def login():
    driver = webdriver.Chrome()
    driver.get('https://www.gmail.com')
    driver.find_element_by_id("identifierId").send_keys("bhojaknamrata@gmail.com")
    driver.find_element_by_id("identifierNext").click()

    driver.find_element_by_name("password").send_keys("naam@123")
    driver.find_element_by_id("submit").send_keys.click()
    driver.close()

login()



