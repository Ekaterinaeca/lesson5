from selenium import webdriver

# Пример для Google Chrome
driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/classattr")

# находим и кликаем на синюю кнопку
blue_button = driver.find_element_by_class_name("btn-primary")
blue_button.click()

# закрываем браузер
driver.quit()