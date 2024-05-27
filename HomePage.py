from tkinter import *
import tkinter.ttk as ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import font
import xmlReader as xml
from tkintermapview import TkinterMapView
from geopy.geocoders import Nominatim

class HomePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.HomeImage = PhotoImage(file="image/홈 아이콘.png")
        self.OilImage = PhotoImage(file="image/주유소 아이콘.png")
        self.BookmarkImage = PhotoImage(file="image/즐겨찾기(빈 별).png")

        self.Highway_Routes = xml.XmlReader.AllExReader()
        #self.Highway_Routes = [str(i) + "번 휴게소" for i in range(1, 101)]
        self.ListOfRestAreas = [str(i) + "번 휴게소" for i in range(1, 101)]

        self.TopImage()

        # highway route list
        # height = Number of times the list will display
        self.Highway_Route_List = ttk.Combobox(self, width=50, height=10, values=self.Highway_Routes)
        self.Highway_Route_List.place(x=285, y=100)
        self.Highway_Route_List.bind("<<ComboboxSelected>>", self.ComboBoxSelected)

        # RestArea list
        self.RestArea_List = ttk.Combobox(self, width=50, height=10, values=self.ListOfRestAreas)
        self.RestArea_List.place(x=285, y=130)
        self.RestArea_List.bind("<<ComboboxSelected>>",self.SecondComboBoxSelected)


        # button
        BookmarkButton = Button(self, text="즐겨찾기에 추가")
        BookmarkButton.pack()
        BookmarkButton.place(x=200, y=550)

        TelegramButton = Button(self, text="텔레그램에 보내기")
        TelegramButton.pack()
        TelegramButton.place(x=450, y=550)

        EmailButton = Button(self, text="이메일로 보내기")
        EmailButton.pack()
        EmailButton.place(x=650, y=550)

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
    def TopImage(self):
        MainCanvas = Canvas(self, width=150, height=150, bg='white')
        MainCanvas.pack()
        MainCanvas.place(x=0, y=0)

    def ComboBoxSelected(self,event):
        print(xml.XmlReader.AllServiceAreaReader(self.Highway_Route_List.get()))
        self.ListOfRestAreas = xml.XmlReader.AllServiceAreaReader(self.Highway_Route_List.get())
        if len(self.ListOfRestAreas) == 0:
            self.RestArea_List['values'] = ['휴게소가 존재하지 않습니다']
        else:
            self.RestArea_List['values'] = self.ListOfRestAreas
    def SetTextBox(self):
        default_font = font.Font(family="긱블말랑이", size=10)
        larger_font = font.Font(family="긱블말랑이", size=15)
        self.text_box = Text(self, width=40, height=26)
        self.text_box.place(x=200, y=160)
        self.text_box.delete('1.0', END)

        self.text_box.tag_configure("default", font=default_font)
        self.text_box.tag_configure("large", font=larger_font)

        info = xml.XmlReader.serviceAreaInfoReader(self.RestArea_List.get())  # adress parking up and down info
        self.text_box.insert('1.0', '★주소★' + '\n', "large")
        self.text_box.insert('end', info['address'] + '\n', "default")

        food_menu = xml.XmlReader.FoodMenuReader(self.RestArea_List.get())  # food info
        self.text_box.insert('end', '★음식 메뉴★' + '\n')
        for food in food_menu:
            self.text_box.insert('end', food + '\n')

        # parking info
        # parking = xml.XmlReader.serviceAreaInfoReader(self.RestArea_List.get())
        self.text_box.insert('end', '★주차 대수★' + '\n')
        self.text_box.insert('end', '소형차 ' + str(info['small_parking']) + '\n')
        self.text_box.insert('end', '대형차 ' + str(info['big_parking']) + '\n')

    def SetMap(self):
        info = xml.XmlReader.serviceAreaInfoReader(self.RestArea_List.get())
        self.map_widget = TkinterMapView(width=300, height=340, corner_radius=0)
        address = info['address']
        self.map_widget.set_zoom(10)
        location = xml.XmlReader.serviceAreaLocationReader(address)

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











