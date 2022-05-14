from selenium import webdriver
import time
import math
import os 

try: 
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input0 = browser.find_element_by_name("firstname")
    input0.send_keys('Ivan')
    input1 = browser.find_element_by_name("lastname")
    input1.send_keys('Ivanov')
    input2 = browser.find_element_by_name("email")
    input2.send_keys('Ivanov@mail.ru')
    input3 = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'new.txt')           # добавляем к этому пути имя файла 
    input3.send_keys(file_path)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button")    
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

 
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
