from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.datafolks.com")

Home = driver.find_element_by_class_name("tn-atom")
assert Home.text == "Home"

Portfolio = driver.find_element_by_class_name("tn-atom")
assert Portfolio.text == "Portfolio"

Services = driver.find_element_by_class_name("tn-atom")
assert Services.text == "Services"

ContactUs = driver.find_element_by_class_name("tn-atom")
assert ContactUs.text == "Contact Us"

driver.quit()