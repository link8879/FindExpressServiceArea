from tkinter import *
import tkinter.ttk as ttk
from tkinter import font
from xmlReader import *

class OilPage(Frame):
    def SearchButton_1st(self):
        TempFont = font.Font(self, size=10, weight='bold', family='긱블말랑이')
        SearchButton = Button(self, font=TempFont, text="검색")
        SearchButton.pack()
        SearchButton.place(x=440, y=100)

    def SearchButton_2nd(self):
        TempFont = font.Font(self, size=10, weight='bold', family='긱블말랑이')
        SearchButton = Button(self, font=TempFont, text="검색")
        SearchButton.pack()
        SearchButton.place(x=740, y=100)

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.HomeImage = PhotoImage(file="image/홈 아이콘.png")
        self.OilImage = PhotoImage(file="image/주유소 아이콘.png")
        self.BookmarkImage = PhotoImage(file="image/즐겨찾기(빈 별).png")

        RestAreas = [str(i) + "번 휴게소" for i in range(1, 101)]

        # Entry를 이용해서 휴게소 검색창
        RestAreas_Search_1 = Entry(self, width=33, )
        RestAreas_Search_1.place(x=200, y=100)
        RestAreas_Search_2 = Entry(self, width=33)
        RestAreas_Search_2.place(x=490, y=100)

        self.SearchButton_1st()
        self.SearchButton_2nd()

        # 휴게소 비교 콤보박스
        RestAreas_List_1 = ttk.Combobox(self, width=30, height=10, values=RestAreas)
        RestAreas_List_1.place(x=200, y=130)
        RestAreas_List_2 = ttk.Combobox(self, width=30, height=10, values=RestAreas)
        RestAreas_List_2.place(x=490, y=130)

        # 그림 넣을 캔버스
        self.MainCanvas = Canvas(self, width=150, height=150, bg='white')
        self.MainCanvas.place(x=0, y=0)

        # 버튼
        HomeButton = Button(self, image=self.HomeImage, width=100, height=100, command=lambda:
        controller.show_frame("HomePage"))
        HomeButton.place(x=25, y=185)

        OilButton = Button(self, image=self.OilImage, width=100, height=100, command=lambda:
        controller.show_frame("OilPage"))
        OilButton.place(x=25, y=325)

        BookmarkPageButton = Button(self, image=self.BookmarkImage, width=100, height=100, command=lambda:
        controller.show_frame("Bookmark"))
        BookmarkPageButton.place(x=25, y=465)