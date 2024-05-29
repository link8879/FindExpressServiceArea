from tkinter import *
import tkinter.ttk as ttk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import font
import xmlReader as xml
from tkintermapview import TkinterMapView
from geopy.geocoders import Nominatim

class HomePage(Frame):
    def TopText(self):
        TempFont = font.Font(self, size=40, weight='bold', family='긱블말랑이')
        MainText = Label(self, font=TempFont, text="휴게소 정보")
        MainText.pack()
        MainText.place(x=340, y=20)

    def email_button(self):
        EmailButton = Button(self, image=self.EmailImage, width=50, height=50)
        EmailButton.pack()
        EmailButton.place(x=700, y=525)

    def telegram_button(self):
        TelegramButton = Button(self, image=self.TelegramImage, width=50, height=50)
        TelegramButton.pack()
        TelegramButton.place(x=600, y=525)

    def bookmark_button(self):
        BookmarkButton = Button(self, image=self.BMImage, width=50, height=50)
        BookmarkButton.pack()
        BookmarkButton.place(x=500, y=525)

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.default_font = font.Font(family="긱블말랑이", size=14)
        self.larger_font = font.Font(family="긱블말랑이", size=20)

        self.HomeImage = PhotoImage(file="image/홈 아이콘.png")
        self.OilImage = PhotoImage(file="image/주유소 아이콘.png")
        self.BookmarkImage = PhotoImage(file="image/즐겨찾기(빈 별).png")
        self.EmailImage = PhotoImage(file="image/gmail.png")
        self.TelegramImage = PhotoImage(file="image/텔레그램.png")
        self.BMImage = PhotoImage(file="image/즐겨찾기(빈 별)(50x50).png")

        self.Highway_Routes = xml.XmlReader.AllExReader()
        #self.Highway_Routes = [str(i) + "번 휴게소" for i in range(1, 101)]
        self.ListOfRestAreas = [str(i) + "번 휴게소" for i in range(1, 101)]

        self.TopImage()
        self.TopText()

        # highway route list
        # height = Number of times the list will display
        self.Highway_Route_List = ttk.Combobox(self, width=20, height=10, values=self.Highway_Routes,font=self.default_font)
        self.Highway_Route_List.place(x=285, y=100)
        self.Highway_Route_List.bind("<<ComboboxSelected>>", self.ComboBoxSelected)

        # RestArea list
        self.RestArea_List = ttk.Combobox(self, width=20, height=10, values=self.ListOfRestAreas,font = self.default_font)
        self.RestArea_List.place(x=285, y=130)
        self.RestArea_List.bind("<<ComboboxSelected>>",self.SecondComboBoxSelected)

        self.bookmark_button()
        self.telegram_button()
        self.email_button()

        # page button
        HomeButton = Button(self, image=self.HomeImage, width=100, height=100, command=lambda:
        controller.show_frame("HomePage"))
        HomeButton.pack()
        HomeButton.place(x=25, y=185)

        OilButton = Button(self, image=self.OilImage, width=100, height=100, command=lambda:
        controller.show_frame("OilPage"))
        OilButton.pack()
        OilButton.place(x=25, y=325)

        BookmarkPageButton = Button(self, image=self.BookmarkImage, width=100, height=100, command=lambda:
        controller.show_frame("Bookmark"))
        BookmarkPageButton.pack()
        BookmarkPageButton.place(x=25, y=465)

        self.map_widget = TkinterMapView(width=300, height=340, corner_radius=0)
        self.text_box = Text(self, width=40, height=26)


    def TopImage(self):
        MainCanvas = Canvas(self, width=150, height=150, bg='white')
        MainCanvas.pack()
        MainCanvas.place(x=0, y=0)

    def ComboBoxSelected(self,event):
        self.ListOfRestAreas = xml.XmlReader.AllServiceAreaReader(self.Highway_Route_List.get())
        if len(self.ListOfRestAreas) == 0:
            self.RestArea_List['values'] = ['휴게소가 존재하지 않습니다']
        else:
            self.RestArea_List['values'] = self.ListOfRestAreas
    def SetTextBox(self):
        self.text_box.destroy()
        self.text_box = Text(self, width=40, height=26)

        self.text_box.place(x=200, y=160)
        self.text_box.delete('1.0', END)

        self.text_box.tag_configure("default", font=self.default_font)
        self.text_box.tag_configure("large", font=self.larger_font)

        info = xml.XmlReader.serviceAreaInfoReader(self.RestArea_List.get())  # adress parking up and down info
        self.text_box.insert('1.0', '1.주소' + '\n', "large")
        self.text_box.insert('end', info['address'] + '\n', "default")

        food_menu = xml.XmlReader.FoodMenuReader(self.RestArea_List.get())  # food info
        self.text_box.insert('end', '2.음식 메뉴' + '\n',"large")
        for food in food_menu:
            self.text_box.insert('end', food + '\n',"default")

        # parking info
        # parking = xml.XmlReader.serviceAreaInfoReader(self.RestArea_List.get())
        self.text_box.insert('end', '3.주차 대수' + '\n',"large")
        self.text_box.insert('end', '소형차 ' + str(info['small_parking']) + '\n',"default")
        self.text_box.insert('end', '대형차 ' + str(info['big_parking']) + '\n',"default")

        self.text_box.config(state=DISABLED)
    def SetMap(self):
        self.map_widget.destroy()
        info = xml.XmlReader.serviceAreaInfoReader(self.RestArea_List.get())
        self.map_widget = TkinterMapView(width=300, height=340, corner_radius=0)
        address = info['address']
        self.map_widget.set_zoom(10)

        location=xml.XmlReader.serviceAreaLocationReader(address)

        if location['y'] == 0 and location['x'] == 0:
            label = ttk.Label(self.map_widget, text="위치를 찾을 수 없습니다.", style="Error.TLabel")
            label.place(relx=0.5, rely=0.5, anchor="center")
        else:
            self.map_widget.set_position(location['y'], location['x'])
            self.map_widget.set_marker(location['y'], location['x'], text=address)
        self.map_widget.place(x=500, y=160)

    def SecondComboBoxSelected(self,event):
        # Text Box
        self.SetTextBox()
        # map
        self.SetMap()











