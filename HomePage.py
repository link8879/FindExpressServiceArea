from tkinter import *
import tkinter.ttk as ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import xmlReader as xml
from tkintermapview import TkinterMapView
class HomePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.HomeImage = PhotoImage(file="image/홈 아이콘.png")
        # self.HomeImage = self.HomeImage.subsample(6, 6)
        self.OilImage = PhotoImage(file="image/주유소 아이콘.png")
        self.BookmarkImage = PhotoImage(file="image/즐겨찾기(빈 별).png")

        self.Highway_Routes = xml.XmlReader.AllExReader()
        #self.Highway_Routes = [str(i) + "번 휴게소" for i in range(1, 101)]
        self.ListOfRestAreas = [str(i) + "번 휴게소" for i in range(1, 101)]

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
        BookmarkButton.place(x=200, y=550)

        TelegramButton = Button(self, text="텔레그램에 보내기")
        TelegramButton.place(x=450, y=550)

        EmailButton = Button(self, text="이메일로 보내기")
        EmailButton.place(x=650, y=550)

        # page button
        HomeButton = Button(self, image=self.HomeImage, width=100, height=100, command=lambda:
        controller.show_frame("HomePage"))
        HomeButton.place(x=10, y=255)

        OilButton = Button(self, image=self.OilImage, width=100, height=100, command=lambda:
        controller.show_frame("OilPage"))
        OilButton.place(x=10, y=370)

        BookmarkPageButton = Button(self, image=self.BookmarkImage, width=100, height=100, command=lambda:
        controller.show_frame("Bookmark"))
        BookmarkPageButton.place(x=10, y=485)



    def ComboBoxSelected(self,event):
        print(xml.XmlReader.AllServiceAreaReader(self.Highway_Route_List.get()))
        self.ListOfRestAreas = xml.XmlReader.AllServiceAreaReader(self.Highway_Route_List.get())
        if len(self.ListOfRestAreas) == 0:
            self.RestArea_List['values'] = ['휴게소가 존재하지 않습니다']
        else:
            self.RestArea_List['values'] = self.ListOfRestAreas

    def SecondComboBoxSelected(self,event):
        # Text Box
        self.text_box = Text(self, width=40, height=25)
        self.text_box.place(x=200, y=160)
        self.text_box.delete('1.0',END)

        info = xml.XmlReader.serviceAreaInfoReader(self.RestArea_List.get())#adress parking up and down info
        self.text_box.insert('1.0','★주소★' + '\n')
        self.text_box.insert('end',info['address']+'\n')

        food_menu = xml.XmlReader.FoodMenuReader(self.RestArea_List.get())  #food info
        self.text_box.insert('end', '★음식 메뉴★' + '\n')
        for food in food_menu:
            self.text_box.insert('end', food + '\n')

        #parking info

        # map
        self.map_widget = TkinterMapView(width=800, height=500, corner_radius=0)

        address = '대전광역시 유성구 지족로 362'
        print(address)
        marker = self.map_widget.set_address(str(address))
        print(marker)
        self.map_widget.set_zoom(15)

        self.map_widget.place(x=400, y=160)











