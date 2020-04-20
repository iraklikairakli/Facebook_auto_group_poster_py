from time import sleep
from selenium import webdriver
EC

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)



group_list = ['https://www.facebook.com/groups/100486223809712/?ref=group_browse',
         'https://www.facebook.com/groups/100486223809712/?ref=group_browse',
         'https://www.facebook.com/groups/100486223809712/?ref=group_browse',]

message = "Checkout an amazing selenium script for posting in Facebook Groups!\nhttps://github.com/lalongooo/selenium-fb-group-poster"



def Facebook():
    usr = 'libralibra123321'
    pwd = 'abara123321'

    driver.get('https://www.facebook.com/')

    username_box = driver.find_element_by_id('email')
    username_box.send_keys(usr)

    password_box = driver.find_element_by_id('pass')
    password_box.send_keys(pwd)

    login = driver.find_element_by_id('loginbutton')
    login.click()
    sleep(2)

    for i in group_list:
        driver.get(i)
        sleep(2)
        post_box = driver.find_element_by_xpath("//*[@name='xhpc_message_text']")
        sleep(5)
        post_box.send_keys(message)
        sleep(4)
        post_element = driver.find_element_by_xpath('./html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/div/div[2]/div/div[2]/button')
        post_element.click()
        sleep(5)

Facebook()