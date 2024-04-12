from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
import os



try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter first name']")
    input1.send_keys("Роман")

    input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter last name']")
    input1.send_keys("Гусар")

    input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter email']")
    input1.send_keys("roma@mail.ru")

    upload_file = browser.find_element(By.ID, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')
    upload_file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()