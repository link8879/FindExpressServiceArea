from tkinter import *
from HomePage import HomePage
from OilPage import OilPage
from Bookmark import Bookmark
import telepot
from telepot.loop import MessageLoop
import xmlReader as xml
import threading
import time

TELEGRAM_BOT_TOKEN = '7487840630:AAESYT6x9QOzLPV3GVB_omE89qjazEFSKAI'

class MainGUI(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("쉼표")

        # window size
        self.geometry("800x600")
        self.resizable(False, False)

        self.telegram_bot_running = False

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        for F in (HomePage, OilPage, Bookmark):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.place(relwidth=1, relheight=1) # Place the frame in the entire area

        self.show_frame("HomePage")
        self.telegram_thread = None

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

        for frames in self.frames.values():
            if hasattr(frames, 'map_widget'):
                frames.map_widget.destroy()

        if hasattr(frame, 'Highway_Route_List'):
            frame.map_widget.destroy()
            frame.text_box.destroy()
            frame.Highway_Route_List.set('')
            frame.RestArea_List.set('')

        if hasattr(frame, 'Bookmark'):
            frame.map_widget.destroy()
            frame.text_box.destroy()
            frame.Bookmark.set('')

    def get_page(self, page_name):
        return self.frames[page_name]

    def start_telegram_bot(self):
        if not self.telegram_bot_running:
            self.telegram_bot_running = True
            self.telegram_thread = threading.Thread(target=self.run_telegram_bot)
            self.telegram_thread.start()

    def stop_telegram_bot(self):
        if self.telegram_bot_running:
            self.telegram_bot_running = False
            if self.telegram_thread:
                self.telegram_thread.join()

    def run_telegram_bot(self):
        self.bot = telepot.Bot(TELEGRAM_BOT_TOKEN)
        MessageLoop(self.bot, self.handle_message).run_as_thread()
        while self.telegram_bot_running:
            time.sleep(10)

    def handle_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            text = msg['text']
            if text == '/start':
                response = ("안녕하세요\n"
                            "휴게소와 관련된 정보를 알려주는 봇 쉼표입니다.\n"
                            "휴게소에 있는 음식 메뉴를 알고싶다면 - [음식, 휴게소이름]을 입력해주세요\n"
                            "휴게소에 있는 주유소 정보를 알고싶다면 - [주유소, 휴게소이름]을 입력해주세요\n"
                            "휴게소의 주차 가능 대수(소형차, 대형차) 정보를 알고싶다면 - [주차장, 휴게소이름]을 입력해주세요")
            elif text.startswith('주유소, '):
                rest_area_name = text.replace('주유소, ', '').strip()
                response = self.read_gas_station_data(rest_area_name)
            elif text.startswith('음식, '):
                rest_area_name = text.replace('음식, ', '').strip()
                response = self.read_foodMenu_data(rest_area_name)
            elif text.startswith('주차장, '):
                rest_area_name = text.replace('주차장, ', '').strip()
                response = self.read_parking_info_data(rest_area_name)
            else:
                response = "알 수 없는 명령어입니다.\n" \
                           "사용 가능한 명령어:\n" \
                           "- [음식, 휴게소이름]\n" \
                           "- [주유소, 휴게소이름]\n" \
                           "- [주차장, 휴게소이름]\n" \
                           "명령어 예시 - 음식, 건천(부산)휴게소"
            self.bot.sendMessage(chat_id, response)

    def read_gas_station_data(self, rest_area_name):
        rest_area_name = rest_area_name.replace('휴게소', '')
        try:
            data = xml.XmlReader.GasstationReader(rest_area_name)
            if data:
                response = ""
                for company, price in data.items():
                    if company == 'AD':
                        company = '알뜰 주유소'
                        response += "{}: 휘발유 - {}, 경유 - {}\n".format(company, price['disel'], price['gasoline'])
                    elif company == 'SK':
                        company = 'SK 주유소'
                        response += "{}: 휘발유 - {}, 경유 - {}\n".format(company, price['disel'], price['gasoline'])
                    elif company == 'HD':
                        company = '현대오일뱅크 주유소'
                        response += "{}: 휘발유 - {}, 경유 - {}\n".format(company, price['disel'], price['gasoline'])
                    elif company == 'S':
                        company = 'S-OIL 주유소'
                        response += "{}: 휘발유 - {}, 경유 - {}\n".format(company, price['disel'], price['gasoline'])
                return response if response else "해당 휴게소 정보를 찾을 수 없습니다."
            else:
                return "해당 휴게소 정보를 찾을 수 없습니다."
        except Exception as e:
            return str(e)

    def read_foodMenu_data(self, rest_area_name):
        try:
            data = xml.XmlReader.FoodMenuReader(rest_area_name)
            if data:
                response = "해당 주유소에 있는 음식메뉴\n"
                for food in data:
                    response += food + '\n'
                return response if response else "해당 휴게소의 음식 정보를 찾을 수 없습니다."
            else:
                return "해당 휴게소의 음식 정보를 찾을 수 없습니다."
        except Exception as e:
            return str(e)

    def read_parking_info_data(self, rest_area_name):
        try:
            data = xml.XmlReader.serviceAreaInfoReader(rest_area_name)
            if data:
                response = "주차 가능 대수\n"
                for key, value in data.items():
                    if key == 'small_parking':
                        response += "소형차: " + str(value) + "대\n"
                    elif key == 'big_parking':
                        response += "대형차: " + str(value) + "대\n"
                return response if response else "해당 휴게소의 주차장 정보를 찾을 수 없습니다."
            else:
                return "해당 휴게소의 주차장 정보를 찾을 수 없습니다."
        except Exception as e:
            return str(e)

if __name__ == "__main__":
    app = MainGUI()
    app.mainloop()