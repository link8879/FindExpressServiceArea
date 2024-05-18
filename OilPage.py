from tkinter import *

class OilPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        label = Label(self, text="Oil Page")
        label.place(x=350, y=50)  # 중앙에 배치

        HomeButton = Button(self, text="홈", width=10, height=10, command=lambda:
        controller.show_frame("HomePage"))
        HomeButton.place(x=5, y=0)

        OilButton = Button(self, text="주유소 가격 비교", width=10, height=10, command=lambda:
        controller.show_frame("OilPage"))
        OilButton.place(x=5, y=200)

        BookmarkPageButton = Button(self, text="즐겨찾기", width=10, height=10, command=lambda:
        controller.show_frame("Bookmark"))
        BookmarkPageButton.place(x=5, y=400)