import telepot
from telepot.loop import MessageLoop
import xmlReader as xml
import time

TELEGRAM_BOT_TOKEN = '7487840630:AAESYT6x9QOzLPV3GVB_omE89qjazEFSKAI'

def read_xml_data(rest_area_name):
    try:
        data = xml.XmlReader.GasstationReader(rest_area_name)
        if data:
            response = ""
            for company, price in data.items():
                response += "{}: 휘발유 - {}, 경유 - {}\n".format(
                    company, price['disel'], price['gasoline']
                )
            return response if response else "해당 휴게소 정보를 찾을 수 없습니다."
        else:
            return "해당 휴게소 정보를 찾을 수 없습니다."
    except Exception as e:
        return str(e)

def handle_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        rest_area_name = msg['text']
        response = read_xml_data(rest_area_name)
        bot.sendMessage(chat_id, response)

bot = telepot.Bot(TELEGRAM_BOT_TOKEN)

MessageLoop(bot, handle_message).run_as_thread()

print('Listening for incoming messages...')

while True:
    time.sleep(10)