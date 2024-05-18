from tkinter import *
import tkinter.ttk as ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk

class HomePage(Frame):
    def Rest_Area_Info(self):
        # Rest_Area_Information
        pass

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.HomeImage = PhotoImage(file="image/홈 아이콘.png")
        # self.HomeImage = self.HomeImage.subsample(6, 6)
        self.OilImage = PhotoImage(file="image/주유소 아이콘.png")
        self.BookmarkImage = PhotoImage(file="image/즐겨찾기(빈 별).png")

        Highway_Routes = [str(i) + "번 노선" for i in range(1, 101)]
        ListOfRestAreas = [str(i) + "번 휴게소" for i in range(1, 101)]

        # highway route list
        # height = Number of times the list will display
        Highway_Route_List = ttk.Combobox(self, width=50, height=10, values=Highway_Routes)
        Highway_Route_List.place(x=285, y=100)

        # RestArea list
        RestArea_List = ttk.Combobox(self, width=50, height=10, values=ListOfRestAreas)
        RestArea_List.place(x=285, y=130)

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

