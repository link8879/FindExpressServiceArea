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
        SearchButton = Button(self, font=self.TempFont, command=self.SearchButton_1stAction, text="검색")
        SearchButton.pack()
        SearchButton.place(x=427, y=106)

    def SearchButton_1stAction(self):
        selected_area = self.first_RA.get().replace('휴게소', '')
        print(selected_area)
        Oilprice = xml.XmlReader.GasstationReader(selected_area)

        self.FRA = selected_area + "휴게소"
        self.FCompany = "주유소가 없습니다."
        self.FGasoline = 0
        self.FDisel = 0

        for company, price in Oilprice.items():
            prices = "{}: 휘발유 - {}, 경유 - {}".format(company, price['gasoline'], price['disel'])
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

    def SearchButton_2nd(self):
        SearchButton = Button(self, font=self.TempFont, command=self.SearchButton_2ndAction, text="검색")
        SearchButton.pack()
        SearchButton.place(x=717, y=106)

    def SearchButton_2ndAction(self):
        selected_area = self.second_RA.get().replace('휴게소', '')
        print(selected_area)
        Oilprice = xml.XmlReader.GasstationReader(selected_area)

        self.SRA = selected_area + "휴게소"
        self.SCompany = "주유소가 없습니다."
        self.SGasoline = 0
        self.SDisel = 0

        for company, price in Oilprice.items():
            prices = "{}: 휘발유 - {}, 경유 - {}".format(company, price['gasoline'], price['disel'])
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

    def TopImage(self):
        MainCanvas = Canvas(self, width=150, height=150, bg='white')
        MainCanvas.pack()
        MainCanvas.place(x=0, y=0)

        MainCanvas.create_image(0, 0, anchor=NW, image=self.MainImage)


    def extract_price(self, price_str):
        clean_str = price_str.replace(',', '').replace('원', '')
        return float(clean_str)

    def FirstRouteSelected(self, event):
        print(xml.XmlReader.AllServiceAreaReader(self.Highway_List.get()))
        self.First_restareas = xml.XmlReader.AllServiceAreaReader(self.Highway_List.get())
        if len(self.First_restareas) == 0:
            self.RestAreas_List_1['values'] = ['휴게소가 존재하지 않습니다']
        else:
            self.RestAreas_List_1['values'] = self.First_restareas

    def SecondRouteSelected(self, event):
        print(xml.XmlReader.AllServiceAreaReader(self.Highway_List_2.get()))
        self.Second_restareas = xml.XmlReader.AllServiceAreaReader(self.Highway_List_2.get())
        if len(self.Second_restareas) == 0:
            self.RestAreas_List_2['values'] = ['휴게소가 존재하지 않습니다']
        else:
            self.RestAreas_List_2['values'] = self.Second_restareas

    def FirstAreaSelected(self, event):
        selected_area = self.RestAreas_List_1.get().replace('휴게소', '')
        Oilprice = xml.XmlReader.GasstationReader(selected_area)

        self.FRA = selected_area + "휴게소"
        self.FCompany = "주유소가 없습니다."
        self.FGasoline = 0
        self.FDisel = 0

        for company, price in Oilprice.items():
            prices = "{}: 휘발유 - {}, 경유 - {}".format(company, price['gasoline'], price['disel'])
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

        self.SRA = selected_area + "휴게소"
        self.SCompany = "주유소가 없습니다."
        self.SGasoline = 0
        self.SDisel = 0

        for company, price in Oilprice.items():
            prices = "{}: 휘발유 - {}, 경유 - {}".format(company, price['gasoline'], price['disel'])
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
        y_base = 250
        scale = 0.1
        self.Oil_canvas.delete('price')


        self.Oil_canvas.create_rectangle(250, 25, 270, 45, fill="tomato")
        self.Oil_canvas.create_rectangle(400, 25, 420, 45, fill="deepskyblue")

        self.Oil_canvas.create_text(330, 35, text=self.FRA, font=self.TempFont, tags='price')
        self.Oil_canvas.create_text(480, 35, text=self.SRA, font=self.TempFont, tags='price')

        # 가격 그래프
        self.Oil_canvas.create_rectangle(250, 250 - self.FGasoline * 0.1, 300, 250, fill="tomato", tags='price')
        self.Oil_canvas.create_rectangle(400, 250 - self.FDisel * 0.1, 450, 250, fill="tomato", tags='price')
        self.Oil_canvas.create_rectangle(300, 250 - self.SGasoline * 0.1, 350, 250, fill="deepskyblue", tags='price')
        self.Oil_canvas.create_rectangle(450, 250 - self.SDisel * 0.1, 500, 250, fill="deepskyblue", tags='price')

        # 주유소 회사 로고
        if self.FCompany == '알뜰 주유소':
            self.Oil_canvas.create_image(25, 25, anchor=NW, image=self.AD_oil_company, tags='price')
        elif self.FCompany == 'SK 주유소':
            self.Oil_canvas.create_image(25, 25, anchor=NW, image=self.SK_oil_company, tags='price')
        elif self.FCompany == 'HD현대오일뱅크':
            self.Oil_canvas.create_image(25, 25, anchor=NW, image=self.HD_oil_company, tags='price')
        elif self.SCompany == 'S':
            self.Oil_canvas.create_image(25, 25, anchor=NW, image=self.S_oil_company, tags='price')

        if self.SCompany == '알뜰 주유소':
            self.Oil_canvas.create_image(25, 175, anchor=NW, image=self.AD_oil_company, tags='price')
        elif self.SCompany == 'SK 주유소':
            self.Oil_canvas.create_image(25, 175, anchor=NW, image=self.SK_oil_company, tags='price')
        elif self.SCompany == 'HD현대오일뱅크':
            self.Oil_canvas.create_image(25, 175, anchor=NW, image=self.HD_oil_company, tags='price')
        elif self.SCompany == 'S':
            self.Oil_canvas.create_image(25, 175, anchor=NW, image=self.S_oil_company, tags='price')

        # 휴게소 이름, 주유소 이름
        self.Oil_canvas.create_text(85, 135, text=self.FRA + " " + self.FCompany, font=self.TempFont, tags='price')
        self.Oil_canvas.create_text(85, 285, text=self.SRA + " " + self.SCompany, font=self.TempFont, tags='price')

        # 가격 표시
        self.Oil_canvas.create_text(275, y_base - self.FGasoline * scale - 15, text=int(self.FGasoline), font=self.TempFont, tags='price')
        self.Oil_canvas.create_text(325, y_base - self.SGasoline * scale - 15, text=int(self.SGasoline), font=self.TempFont, tags='price')
        self.Oil_canvas.create_text(425, y_base - self.FDisel * scale - 15, text=int(self.FDisel), font=self.TempFont, tags='price')
        self.Oil_canvas.create_text(475, y_base - self.SDisel * scale - 15, text=int(self.SDisel), font=self.TempFont, tags='price')

        # 경유, 휘발유 표시
        TempFont = font.Font(self, size=20, weight='bold', family='긱블말랑이')
        self.Oil_canvas.create_text(300, 270, text="휘발유", font=TempFont)
        self.Oil_canvas.create_text(450, 270, text="경유", font=TempFont)

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        # 이미지
        self.HomeImage = PhotoImage(file="image/홈 아이콘.png")
        self.OilImage = PhotoImage(file="image/주유소 아이콘.png")
        self.BookmarkImage = PhotoImage(file="image/즐겨찾기(빈 별).png")
        self.AD_oil_company = PhotoImage(file="image/알뜰 주유소(98x100).png")
        self.SK_oil_company = PhotoImage(file="image/SK(128x100).png")
        self.HD_oil_company = PhotoImage(file="image/현대오일뱅크(200x68).png")
        self.S_oil_company = PhotoImage(file="image/S-OIL(200x68).png")
        self.MainImage = PhotoImage(file="image/쉼표 로고.png")

        # 폰트
        self.TempFont = font.Font(self, size=10, family='긱블말랑이')

        self.FRA = ""
        self.SRA = ""

        # 1번 주유소
        self.FCompany = ""
        self.FGasoline = 0
        self.FDisel = 0
        # 2번 주유소
        self.SCompany = ""
        self.SGasoline = 0
        self.SDisel = 0

        self.highway_routes = xml.XmlReader.AllExReader()
        self.First_restareas = []
        self.Second_restareas = []

        self.Oil_canvas = Canvas(self, width=550, height=300, bg='white')
        self.Oil_canvas.pack()
        self.Oil_canvas.place(x=200, y=185)

        self.TopText()
        self.TopImage()

        # self.SearchFirstRestArea()
        self.first_RA = StringVar()
        RestAreas_Search_1 = Entry(self, textvariable=self.first_RA, width=26, font=self.TempFont)
        RestAreas_Search_1.pack()
        RestAreas_Search_1.place(x=200, y=110)

        self.second_RA = StringVar()
        RestAreas_Search_2 = Entry(self, textvariable=self.second_RA, width=26, font=self.TempFont)
        RestAreas_Search_2.pack()
        RestAreas_Search_2.place(x=490, y=110)

        self.Highway_List = ttk.Combobox(self, font=self.TempFont, width=12, height=10, values=self.highway_routes)
        self.Highway_List.place(x=200, y=140)
        self.Highway_List.bind("<<ComboboxSelected>>", self.FirstRouteSelected)

        self.Highway_List_2 = ttk.Combobox(self, font=self.TempFont, width=12, height=10, values=self.highway_routes)
        self.Highway_List_2.place(x=490, y=140)
        self.Highway_List_2.bind("<<ComboboxSelected>>", self.SecondRouteSelected)

        self.RestAreas_List_1 = ttk.Combobox(self, font=self.TempFont, width=15, height=10, values=self.First_restareas)
        self.RestAreas_List_1.pack()
        self.RestAreas_List_1.place(x=320, y=140)
        self.RestAreas_List_1.bind("<<ComboboxSelected>>", self.FirstAreaSelected)

        self.RestAreas_List_2 = ttk.Combobox(self, font=self.TempFont, width=15, height=10, values=self.Second_restareas)
        self.RestAreas_List_2.pack()
        self.RestAreas_List_2.place(x=610, y=140)
        self.RestAreas_List_2.bind("<<ComboboxSelected>>", self.SecondAreaSelected)

        self.SearchButton_1st()
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