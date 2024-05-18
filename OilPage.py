from tkinter import *
import tkinter.ttk as ttk

class OilPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.HomeImage = PhotoImage(file="image/홈 아이콘.png")
        self.OilImage = PhotoImage(file="image/주유소 아이콘.png")
        self.BookmarkImage = PhotoImage(file="image/즐겨찾기(빈 별).png")

        RestAreas = [str(i) + "번 휴게소" for i in range(1, 101)]

        # Entry를 이용해서 휴게소 검색창
        RestAreas_Search_1 = Entry(self, width=33)
        RestAreas_Search_1.place(x=200, y=100)
        RestAreas_Search_2 = Entry(self, width=33)
        RestAreas_Search_2.place(x=490, y=100)

        # 휴게소 비교 콤보박스
        RestAreas_List_1 = ttk.Combobox(self, width=30, height=10, values=RestAreas)
        RestAreas_List_1.place(x=200, y=130)
        RestAreas_List_2 = ttk.Combobox(self, width=30, height=10, values=RestAreas)
        RestAreas_List_2.place(x=490, y=130)

        HomeButton = Button(self, image=self.HomeImage, width=100, height=100, command=lambda:
        controller.show_frame("HomePage"))
        HomeButton.place(x=10, y=255)

        OilButton = Button(self, image=self.OilImage, width=100, height=100, command=lambda:
        controller.show_frame("OilPage"))
        OilButton.place(x=10, y=370)

        BookmarkPageButton = Button(self, image=self.BookmarkImage, width=100, height=100, command=lambda:
        controller.show_frame("Bookmark"))
        BookmarkPageButton.place(x=10, y=485)