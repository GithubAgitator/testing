import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# browser = webdriver.Chrome()
# browser.implicitly_wait(5)
# browser.get("http://suninjuly.github.io/cats.html")
#
#
# but = browser.find_element(By.ID, "button")
# but.click()
#
#************************


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
#
# browser = webdriver.Chrome()
# # говорим WebDriver ждать все элементы в течение 5 секунд
#
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text

#********************************************
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"

browser.get(link)

WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))
btn2 = browser.find_element(By.ID, 'book')
btn2.click()


def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")

x1 = x_element.text
x = int(x1)

y = calc(x)
y_el = browser.find_element(By.CSS_SELECTOR, "[id = 'answer']")
y_el.send_keys(y)

button3 = browser.find_element(By.XPATH, "//button[@type='submit']")
button3.click()
