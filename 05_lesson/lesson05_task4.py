from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Открыть браузер FireFox
driver = webdriver.Firefox()

# Перейти на страницу http://the-internet.herokuapp.com/login
driver.get("http://the-internet.herokuapp.com/login")

# В поле username ввести значение tomsmith
username_input = driver.find_element_by_id("username")
username_input.send_keys("tomsmith")

# В поле password ввести значение SuperSecretPassword!
password_input = driver.find_element_by_id("password")
password_input.send_keys("SuperSecretPassword!")

# Нажать кнопку Login
login_button = driver.find_element_by_css_selector("button[type='submit']")
login_button.click()

# Найти текст с зеленой плашки и вывести в консоль
success_message = driver.find_element_by_css_selector(".flash.success")
print(success_message.text)

# Закрыть браузер
driver.quit()