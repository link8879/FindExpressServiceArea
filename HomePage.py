from tkinter import *
import tkinter.ttk as ttk
from tkinter import PhotoImage

class HomePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.HomeImage = PhotoImage(file="홈 아이콘.png")
        self.HomeImage = self.HomeImage.subsample(6, 6)

        Highway_Routes = [str(i) + "번 노선" for i in range(1, 101)]
        ListOfRestAreas = [str(i) + "번 휴게소" for i in range(1, 101)]

        # highway route list
        # height = Number of times the list will display
        Highway_Route_List = ttk.Combobox(self, width=50, height=10, values=Highway_Routes)
        Highway_Route_List.place(x=285, y=100)

        # RestArea list
        RestArea_List = ttk.Combobox(self, width=50, height=10, values=ListOfRestAreas)
        RestArea_List.place(x=285, y=130)

        label = Label(self, text="Home Page")
        label.place(x=350, y=50)    # 중앙에 배치

        HomeButton = Button(self, text="홈", image=self.HomeImage, command=lambda:
        controller.show_frame("HomePage"))
        HomeButton.place(x=5, y=0)

        OilButton = Button(self, text="주유소 가격 비교", padx=10, pady=10, command=lambda:
        controller.show_frame("OilPage"))
        OilButton.place(x=5, y=200)

        BookmarkButton = Button(self, text="즐겨찾기", padx=10, pady=10, command=lambda:
        controller.show_frame("Bookmark"))
        BookmarkButton.place(x=5, y=400)