from tkinter import *
from tkinter import font
from tkinter import ttk


class Bookmark(Frame):
    def TopImage(self):
        MainCanvas = Canvas(self, width=150, height=150, bg='white')
        MainCanvas.pack()
        MainCanvas.place(x=0, y=0)

    def TopText(self):
        TempFont = font.Font(self, size=40, weight='bold', family='긱블말랑이')
        MainText = Label(self, font=TempFont, text="즐겨찾기")
        MainText.pack()
        MainText.place(x=370, y=20)

    def BookMarkList(self):
        TempFont = font.Font(self, size=20, family='긱블말랑이')
        Bookmark = ttk.Combobox(self, font=TempFont, width=30, height=10, values=self.BMList)
        Bookmark.pack()
        Bookmark.place(x=210, y=120)

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.HomeImage = PhotoImage(file="image/홈 아이콘.png")
        self.OilImage = PhotoImage(file="image/주유소 아이콘.png")
        self.BookmarkImage = PhotoImage(file="image/즐겨찾기(빈 별).png")

        self.BMList = [str(i) + "번 노선" for i in range(1, 101)]

        self.TopImage()
        self.TopText()

        self.BookMarkList()

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
