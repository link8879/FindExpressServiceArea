from tkinter import *

class MainGUI(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("쉼표")

        # window size
        self.geometry("800x600")

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        for F in (HomePage, OilPage, Bookmark):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.place(relwidth=1, relheight=1) # Place the frame in the entire area

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class HomePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        label = Label(self, text="Home Page")
        label.place(x=350, y=50)    # 중앙에 배치

        HomeButton = Button(self, text="홈", command=lambda:
                            controller.show_frame("HomePage"))
        HomeButton.place(x=5, y=0)

        OilButton = Button(self, text="주유소 가격 비교", command=lambda:
                            controller.show_frame("OilPage"))
        OilButton.place(x=5, y=200)

        BookmarkButton = Button(self, text="즐겨찾기", command=lambda:
                            controller.show_frame("Bookmark"))
        BookmarkButton.place(x=5, y=400)

class OilPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        label = Label(self, text="Oil Page")
        label.place(x=350, y=50)  # 중앙에 배치

        HomeButton = Button(self, text="홈", command=lambda:
                        controller.show_frame("HomePage"))
        HomeButton.place(x=5, y=0)

        OilButton = Button(self, text="주유소 가격 비교", command=lambda:
                        controller.show_frame("OilPage"))
        OilButton.place(x=5, y=200)

        BookmarkButton = Button(self, text="즐겨찾기", command=lambda:
                        controller.show_frame("Bookmark"))
        BookmarkButton.place(x=5, y=400)

class Bookmark(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        label = Label(self, text="즐겨찾기")
        label.place(x=350, y=50)  # 중앙에 배치

        HomeButton = Button(self, text="홈", command=lambda:
                        controller.show_frame("HomePage"))
        HomeButton.place(x=5, y=0)

        OilButton = Button(self, text="주유소 가격 비교", command=lambda:
                        controller.show_frame("OilPage"))
        OilButton.place(x=5, y=200)

        BookmarkButton = Button(self, text="즐겨찾기", command=lambda:
                        controller.show_frame("Bookmark"))
        BookmarkButton.place(x=5, y=400)

if __name__ == "__main__":
    app = MainGUI()
    app.mainloop()