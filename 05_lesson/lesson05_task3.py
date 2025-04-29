from selenium import webdriver

# Открытие браузера FireFox
browser = webdriver.Firefox()

# Переход на страницу http://the-internet.herokuapp.com/inputs
browser.get('http://the-internet.herokuapp.com/inputs')

# Находим поле ввода и вводим текст Sky
input_field = browser.find_element_by_tag_name('input')
input_field.send_keys('Sky')

# Ждем 2 секунды
browser.implicitly_wait(2)

# Очищаем поле ввода
input_field.clear()

# Ждем 2 секунды
browser.implicitly_wait(2)

# Вводим текст Pro
input_field.send_keys('Pro')

# Ждем 2 секунды
browser.implicitly_wait(2)

# Закрываем браузер
browser.quit()