from selenium import webdriver
import time

# Открыть браузер Google Chrome
driver = webdriver.Chrome()

# Перейти на страницу
driver.get("http://uitestingplayground.com/dynamicid")

# Найти и кликнуть на синюю кнопку
blue_button = driver.find_element_by_xpath("//button[contains(text(),'Blue Button')]")
blue_button.click()

time.sleep(5)

# Закрыть браузер
driver.quit()