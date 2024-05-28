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

    def TopImage(self):
        MainCanvas = Canvas(self, width=150, height=150, bg='white')
        MainCanvas.pack()
        MainCanvas.place(x=0, y=0)

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

    def extract_price(self, price_str):
        clean_str = price_str.replace(',', '').replace('원', '')
        return float(clean_str)

    def FirstAreaSelected(self, event):
        selected_area = self.RestAreas_List_1.get().replace('휴게소', '')
        Oilprice = xml.XmlReader.GasstationReader(selected_area)
        for company, price in Oilprice.items():
            prices = "{}: 디젤 - {}, 가솔린 - {}".format(company, price['disel'], price['gasoline'])
            if company == 'AD':
                self.FCompany = '알뜰 주유소'
            elif company == 'SK':
                self.FCompany = 'SK 주유소'
            elif company == 'HD':
                self.FCompany = 'HD현대오일뱅크'
            else:
                self.FCompany = company
            self.FGasoline = self.extract_price(price['gasoline'])
            self.FDisel = self.extract_price(price['disel'])
            print(prices)
        self.update_graph()

    def SecondAreaSelected(self, event):
        selected_area = self.RestAreas_List_2.get().replace('휴게소', '')
        Oilprice = xml.XmlReader.GasstationReader(selected_area)
        for company, price in Oilprice.items():
            prices = "{}: 디젤 - {}, 가솔린 - {}".format(company, price['disel'], price['gasoline'])
            if company == 'AD':
                self.SCompany = '알뜰 주유소'
            elif company == 'SK':
                self.SCompany = 'SK 주유소'
            elif company == 'HD':
                self.SCompany = 'HD현대오일뱅크'
            else:
                self.SCompany = company
            self.SGasoline = self.extract_price(price['gasoline'])
            self.SDisel = self.extract_price(price['disel'])
            print(prices)
        self.update_graph()

    def update_graph(self):
        self.Oil_canvas.delete('price')
        self.Oil_canvas.create_rectangle(250, 250 - self.FGasoline * 0.1, 300, 250, fill="red", tags='price')
        self.Oil_canvas.create_rectangle(400, 250 - self.FDisel * 0.1, 450, 250, fill="tomato", tags='price')
        self.Oil_canvas.create_rectangle(300, 250 - self.SGasoline * 0.1, 350, 250, fill="deepskyblue", tags='price')
        self.Oil_canvas.create_rectangle(450, 250 - self.SDisel * 0.1, 500, 250, fill="cyan", tags='price')

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.HomeImage = PhotoImage(file="image/홈 아이콘.png")
        self.OilImage = PhotoImage(file="image/주유소 아이콘.png")
        self.BookmarkImage = PhotoImage(file="image/즐겨찾기(빈 별).png")
        self.TempFont = font.Font(self, size=10, family='긱블말랑이')

        # 1번 주유소
        self.FCompany = ""
        self.FGasoline = 0
        self.FDisel = 0
        # 2번 주유소
        self.SCompany = ""
        self.SGasoline = 0
        self.SDisel = 0

        # self.RouteList = ['경부선', '고창담양선', '광주대구선', '광주대구선,무안광주선', '남해선', '남해선(영암순천)',
        #                   '남해제1지선', '남해제2지선', '논산천안선,호남선', '대구포항선', '대전남부순환선', '동해선',
        #                   '무안광주선', '부산외곽순환선', ]
        self.highway_routes = xml.XmlReader.AllExReader()
        self.all_restarea = []

        for route in self.highway_routes:
            self.all_restarea.extend(xml.XmlReader.AllServiceAreaReader(route))

        self.Oil_canvas = Canvas(self, width=550, height=300, bg='white')
        self.Oil_canvas.pack()
        self.Oil_canvas.place(x=200, y=185)

        self.first_RA = StringVar()
        self.second_RA = StringVar()

        self.TopText()
        self.TopImage()

        self.SearchFirstRestArea()
        self.SearchSecondRestArea()

        self.RestAreas_List_1 = ttk.Combobox(self, font=self.TempFont, width=30, height=10, values=self.all_restarea)
        self.RestAreas_List_1.pack()
        self.RestAreas_List_1.place(x=200, y=140)
        self.RestAreas_List_1.bind("<<ComboboxSelected>>", self.FirstAreaSelected)

        self.RestAreas_List_2 = ttk.Combobox(self, font=self.TempFont, width=30, height=10, values=self.all_restarea)
        self.RestAreas_List_2.pack()
        self.RestAreas_List_2.place(x=490, y=140)
        self.RestAreas_List_2.bind("<<ComboboxSelected>>", self.SecondAreaSelected)

        # self.SearchButton_1st()
        self.SearchButton_2nd()

        self.update_graph()

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