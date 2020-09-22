from selenium import webdriver
# ChromeDriverManager это настройка на выбор google chrome как тестовой среды
from webdriver_manager.chrome import ChromeDriverManager
import time
import datetime
import random
from utils import doScreen

# variables
github_username = "kirigaikabuto"
github_password = "Aigerim73211"
folder = "./images/"

url = "https://github.com"
# открытие браузера по ссылке(url)
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(url)
browser.set_window_size(1024, 600)
browser.maximize_window()
time.sleep(5)
# способ 1
# название_тэг - > p,h1,input,a
# свойство -> id,name,type,class,href
# find_element_by_xpath("//название_тэг[@свойство='значение']")
a_marketplace = browser.find_element_by_xpath("//a[@href='/login']")
if a_marketplace.text == "Sign in":
    a_marketplace.click()
time.sleep(5)

# login
username_input = browser.find_element_by_xpath("//input[@name='login']")
username_input.send_keys(github_username)

password_input = browser.find_element_by_xpath("//input[@name='password']")
password_input.send_keys(github_password)

div_error = browser.find_element_by_xpath("//div[@id='js-flash-container']")
if len(div_error.text) > 0:
    print("before click btn there are error")
    nameFile = str(random.randint(0, 100))
    screenType = "login"
    doScreen(browser, folder, nameFile, screenType)
else:
    print("before click btn no error")
input_submit = browser.find_element_by_xpath("//input[@name='commit']")
input_submit.click()

div_error = browser.find_element_by_xpath("//div[@id='js-flash-container']")
if len(div_error.text) > 0:
    print("After click btn there are error")
    nameFile = str(random.randint(0, 100))
    screenType = "login"
    doScreen(browser, folder, nameFile, screenType)
else:
    print("After click btn no error")

# time.sleep(5)
# main page

# summary_profile = browser.find_element_by_xpath("//summary[@aria-label='View profile and more']")
# summary_profile.click()
#
# time.sleep(3)
#
# inner_element = browser.find_element_by_xpath("//*[contains(text(), '" + "Sign out" + "')]")
# inner_element.click()

# способ 2 """(поискать по chain)"""
# find_elements_by_tag_name("название тэга")
# summary_arr = browser.find_elements_by_tag_name("summary")
# for summary in summary_arr:
#     if summary.text == "Explore":
#         summary.click()
#         time.sleep(5)
#         a_topics = browser.find_element_by_xpath("//a[@href='/topics']")
#         a_topics.click()
#         # inner_element = browser.find_element_by_xpath("//*[contains(text(), '" + "Topics" + "')]")
#         # inner_element.click()
# команда для закрытия браузера
time.sleep(5)
browser.quit()
