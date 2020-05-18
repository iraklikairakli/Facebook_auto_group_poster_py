from time import sleep
import selenium as se
                                                                                  #Now this code working as background Pl
options = se.webdriver.ChromeOptions()
options.add_argument('headless')
driver = se.webdriver.Chrome(chrome_options=options)



                                                                         #if do not want background session please uncomment this line and Comment Line 6,7,8
"""                                                      

# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.default_content_setting_values.notifications": 2}
# chrome_options.add_experimental_option("prefs", prefs)
# driver = webdriver.Chrome(chrome_options=chrome_options)

"""




group_list = ['https://www.facebook.com/groups/100486223809712/?ref=bookmarks',
         'https://www.facebook.com/groups/1816476555286543/?ref=bookmarks',
         'https://www.facebook.com/groups/405180892976133/?ref=bookmarks',
              'https://www.facebook.com/groups/813174648730720/?ref=bookmarks',
              'https://www.facebook.com/groups/954760024587211/?ref=bookmarks',
              'https://www.facebook.com/groups/2404565156526895/?ref=bookmarks',
              'https://www.facebook.com/groups/1221957911239504/?ref=bookmarks',
             'https://www.facebook.com/groups/297316660750219/?ref=bookmarks',
              'https://www.facebook.com/groups/1412330928881236/?ref=bookmarks',
              'https://www.facebook.com/groups/474891299356835/?ref=bookmarks',
              'https://www.facebook.com/groups/CANCERZODIACTALK/?ref=bookmarks',
              'https://www.facebook.com/groups/1519581644801371/?ref=bookmarks',
              'https://www.facebook.com/groups/1519581644801371/?ref=bookmarks',
              'https://www.facebook.com/groups/703597519797673/?ref=bookmarks']

message = "Checkout an amazing selenium script for posting in Facebook Groups!\nhttps://github.com/lalongooo/selenium-fb-group-poster"



def Facebook():
    usr = ''
    pwd = ''

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
        print('ტექსტი გაიგზავნა')
        sleep(4)
        post_element = driver.find_element_by_xpath('./html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/div/div[2]/div/div[2]/button')
        post_element.click()
        print('Sucsesfully posted')
        sleep(5)

Facebook()