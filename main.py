import asyncio
from telethon.sync import TelegramClient, events , utils
from google_trans_new import google_translator
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



msg=client.get_messages(channel_name, 1)
print(msg)
print(msg[0])
msgtext=msg[0].message
print(msgtext)
msgid=msg[0].id
print(msgid)
datetimestr=msg[0].date
print(datetimestr)


# client.send_message(-707770260,msgtext+"\n"+str(datetimestr))
client.send_message(forward_chat,msgtext+"\n\n# Translated #\n\n"+translate(msgtext)+"\n\n"+str(datetimestr))

try:
    print('(Press Ctrl+C to stop this)')
    client.run_until_disconnected()
finally:
    client.disconnect()