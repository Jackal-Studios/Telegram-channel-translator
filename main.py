import asyncio
from telethon.sync import TelegramClient, events , utils
from google_trans_new import google_translator
import time
translator = google_translator()
api_id = int(open('./secrets/api_id.txt','r+').readline().strip().replace("\n",""))
api_hash = open('./secrets/api_hash.txt','r+').readline().strip().replace("\n","")
phone=open('./secrets/phonenumber.txt','r+').readline().strip().replace("\n","")
password=open('./secrets/password.txt','r+').readline().strip().replace("\n","")
channel_name="ukrpravda_news"
forward_chat=-707770260
last_id_processed=0

client = TelegramClient('./secrets/session_name', api_id, api_hash)
client.start(phone=phone, password=password)

def translate(text,lang='en'):
    return translator.translate(text, lang_tgt=lang)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html
from selenium.webdriver.firefox.options import Options
option=Options()
option.headless=True
def translate2(text):
    driver = webdriver.Firefox(firefox_options=option)
    driver.get("https://translate.google.com/")

    try:
        wait = WebDriverWait(driver, 3)
        wait.until(EC.element_to_be_clickable((By.XPATH,
                                               "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qfvgSe']"))).click()
    except:
        print("i guess no cookie")
    driver.find_element_by_xpath("//textarea[@class='er8xn']").send_keys(text)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH,
                                           "//button[@class='VfPpkd-Bz112c-LgbsSe VfPpkd-Bz112c-LgbsSe-OWXEXe-e5LLRc-SxQuSe yHy1rc eT1oJ qiN4Vb itOtF IK3GNd']"))).click()
    # print(driver.find_element_by_xpath("//span[@jsname='W297wb']").text)
    # print(driver.save_screenshot("123.png"))
    txt = driver.find_element_by_xpath("//span[@jsname='W297wb']").text
    driver.close()
    return txt


# msg=client.get_messages(channel_name, 1)
# print(msg)
# print(msg[0])
# msgtext=msg[0].message
# print(msgtext)
# msgid=msg[0].id
# print(msgid)
# datetimestr=msg[0].date
# print(datetimestr)
#
#
# # client.send_message(-707770260,msgtext+"\n"+str(datetimestr))
# if(msg[0].media):
#     client.send_file(forward_chat,msg[0].media, caption = msgtext+"\n\n# Translated #\n\n"+translate(msgtext)+"\n\n"+str(datetimestr))
#     #msg[0].media, caption = "hello"
# else:
#     client.send_message(forward_chat,msgtext+"\n\n# Translated #\n\n"+translate(msgtext)+"\n\n"+str(datetimestr))

while(True):
    try:
        msg = client.get_messages(channel_name, 1)
        msgtext = msg[0].message
        msgid = msg[0].id
        datetimestr = msg[0].date
        if(msgid!=last_id_processed):
            last_id_processed=msgid

            if (msg[0].media):
                client.send_file(forward_chat, msg[0].media,
                                 caption=msgtext + "\n\n# Translated #\n\n" + translate(msgtext) + "\n\n" + str(
                                     datetimestr))
            else:
                client.send_message(forward_chat,
                                    msgtext + "\n\n# Translated #\n\n" + translate(msgtext) + "\n\n" + str(datetimestr))
    except Exception:
        print("an error occured")
        print(Exception)
        try:
            client.send_message(forward_chat,"*Failed to load media*\n\n"+msgtext+"\n\n# Translated #\n\n"+translate(msgtext)+"\n\n"+str(datetimestr))
        except:
            print("another error occured")
    time.sleep(0.01)
# try:
#     print('(Press Ctrl+C to stop this)')
#     client.run_until_disconnected()
# finally:
#     client.disconnect()