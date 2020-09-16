from selenium import webdriver
#ChromeDriverManager это настройка на выбор google chrome как тестовой среды
from webdriver_manager.chrome import ChromeDriverManager
import time

url = "https://github.com"
#открытие браузера по ссылке(url)
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(url)
browser.set_window_size(1024, 600)
browser.maximize_window()
time.sleep(5)
#способ 1
# название_тэг - > p,h1,input,a
# свойство -> id,name,type,class,href
# find_element_by_xpath("//название_тэг[@свойство='значение']")
# a_marketplace = browser.find_element_by_xpath("//a[@href='/marketplace']")
# if a_marketplace.text == "Marketplace":
#     a_marketplace.click()

#способ 2 """(поискать по chain)"""
#find_elements_by_tag_name("название тэга")
summary_arr = browser.find_elements_by_tag_name("summary")
for summary in summary_arr:
    if summary.text == "Explore":
        summary.click()
        time.sleep(5)
        a_topics = browser.find_element_by_xpath("//a[@href='/topics']")
        a_topics.click()
        # inner_element = browser.find_element_by_xpath("//*[contains(text(), '" + "Topics" + "')]")
        # inner_element.click()
#команда для закрытия браузера
time.sleep(5)
browser.quit()
