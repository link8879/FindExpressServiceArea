from tkinter import *
import tkinter.ttk as ttk
from tkinter import font
import xmlReader as xml


class OilPage(Frame):
    def TopText(self):
        TempFont = font.Font(self, size=40, weight='bold', family='긱블말랑이')
        MainText = Label(self, font=TempFont, text="휴게소 별 주유소 가격 비교")
        MainText.pack()
        MainText.place(x=190, y=20)

    def SearchButton_1st(self):
        TempFont = font.Font(self, size=10, family='긱블말랑이')
        SearchButton = Button(self, font=TempFont, command=self.SearchButton_1stAction, text="검색")
        SearchButton.pack()
        SearchButton.place(x=427, y=106)

    def SearchButton_2nd(self):
        TempFont = font.Font(self, size=10, family='긱블말랑이')
        SearchButton = Button(self, font=TempFont, text="검색")
        SearchButton.pack()
        SearchButton.place(x=717, y=106)

    def ShowOilPrice(self):
        self.FOil_canvas = Canvas(self, width=550, height=300, bg='white')
        self.FOil_canvas.pack()
        self.FOil_canvas.place(x=200, y=185)

    def TopImage(self):
        MainCanvas = Canvas(self, width=150, height=150, bg='white')
        MainCanvas.pack()
        MainCanvas.place(x=0, y=0)

    def FirstRestAreaList(self):
        TempFont = font.Font(self, size=10, family='긱블말랑이')
        RestAreas_List_1 = ttk.Combobox(self, font=TempFont, width=30, height=10, values=self.RestAreas)
        RestAreas_List_1.pack()
        RestAreas_List_1.place(x=200, y=140)

    def SecondRestAreaList(self):
        TempFont = font.Font(self, size=10, family='긱블말랑이')
        RestAreas_List_2 = ttk.Combobox(self, font=TempFont, width=30, height=10, values=self.RestAreas)
        RestAreas_List_2.pack()
        RestAreas_List_2.place(x=490, y=140)

    def SearchFirstRestArea(self):
        TempFont = font.Font(self, size=10, family='긱블말랑이')
        RestAreas_Search_1 = Entry(self, textvariable=self.first_RA, width=26, font=TempFont)
        RestAreas_Search_1.pack()
        RestAreas_Search_1.place(x=200, y=110)

    def SearchSecondRestArea(self):
        TempFont = font.Font(self, size=10, family='긱블말랑이')
        RestAreas_Search_2 = Entry(self, textvariable=self.second_RA, width=26, font=TempFont)
        RestAreas_Search_2.pack()
        RestAreas_Search_2.place(x=490, y=110)

    def SearchButton_1stAction(self):
        # xml.XmlReader.GasstationReader(self.first_RA)
        service_area_name = self.first_RA.get()
        prices = xml.XmlReader.GasstationReader(service_area_name)
        for company, price in prices.items():
            text = f"{company}: 경유 - {price['disel']}원, 휘발유 - {price['gasoline']}원"
            print(text)


    def display_oil_prices(self, prices):
        self.FOil_canvas.delete("all")
        y = 10
        for company, price in prices.items():
            text = f"{company}: 경유 - {price['disel']}원, 휘발유 - {price['gasoline']}원"
            self.FOil_canvas.create_text(10, y, anchor="nw", text=text)
            y += 20

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.HomeImage = PhotoImage(file="image/홈 아이콘.png")
        self.OilImage = PhotoImage(file="image/주유소 아이콘.png")
        self.BookmarkImage = PhotoImage(file="image/즐겨찾기(빈 별).png")

        self.RestAreas = xml.XmlReader.AllServiceAreaReader('경부선')

        self.first_RA = StringVar()
        self.second_RA = StringVar()

        self.TopText()
        self.TopImage()

        self.SearchFirstRestArea()
        self.SearchSecondRestArea()

        self.FirstRestAreaList()
        self.SecondRestAreaList()

        self.SearchButton_1st()
        self.SearchButton_2nd()

        self.ShowOilPrice()

        # 버튼
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