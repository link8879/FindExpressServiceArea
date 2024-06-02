from tkinter import *
from tkinter import font
from tkinter import ttk
import xmlReader as xml
from tkintermapview import TkinterMapView


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

    def delete_button(self):
        DeleteButton = Button(self, image=self.TrashImage, width=50, height=50, command=self.delete_bookmark)
        DeleteButton.pack()
        DeleteButton.place(x=700, y=525)

    def update_bookmark_list(self, new_restarea):
        self.BMSet.add(new_restarea)
        self.Bookmark['values'] = list(self.BMSet)

    def delete_bookmark(self):
        selected = self.Bookmark.get()
        if selected in self.BMSet:
            self.BMSet.remove(selected)
            self.Bookmark.set('')
            self.text_box.destroy()
            self.map_widget.destroy()
            print(f"Deleted bookmark: {selected}")

        self.Bookmark['values'] = list(self.BMSet)

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.HomeImage = PhotoImage(file="image/홈 아이콘.png")
        self.OilImage = PhotoImage(file="image/주유소 아이콘.png")
        self.BookmarkImage = PhotoImage(file="image/즐겨찾기(빈 별).png")
        self.TrashImage = PhotoImage(file="image/trash.png")

        self.default_font = font.Font(family="긱블말랑이", size=14)
        self.larger_font = font.Font(family="긱블말랑이", size=20)

        self.BMSet = set()

        self.TopImage()
        self.TopText()
        self.delete_button()

        self.TempFont = font.Font(self, size=20, family='긱블말랑이')
        self.Bookmark = ttk.Combobox(self, font=self.TempFont, width=30, height=10, values=list(self.BMSet))
        self.Bookmark.pack()
        self.Bookmark.place(x=210, y=120)
        self.Bookmark.bind("<<ComboboxSelected>>", self.SecondComboBoxSelected)

        self.map_widget = TkinterMapView(width=300, height=340, corner_radius=0)
        self.text_box = Text(self, width=40, height=26)

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

    def SetTextBox(self):
        self.text_box.destroy()
        self.text_box = Text(self, width=40, height=26)

        self.text_box.place(x=200, y=160)
        self.text_box.delete('1.0', END)

        self.text_box.tag_configure("default", font=self.default_font)
        self.text_box.tag_configure("large", font=self.larger_font)

        info = xml.XmlReader.serviceAreaInfoReader(self.Bookmark.get())  # adress parking up and down info
        self.text_box.insert('1.0', '1.주소' + '\n', "large")
        self.text_box.insert('end', info['address'] + '\n', "default")

        food_menu = xml.XmlReader.FoodMenuReader(self.Bookmark.get())  # food info
        self.text_box.insert('end', '2.음식 메뉴' + '\n',"large")
        for food in food_menu:
            self.text_box.insert('end', food + '\n',"default")

        self.text_box.insert('end', '3.주차 대수' + '\n',"large")
        self.text_box.insert('end', '소형차 ' + str(info['small_parking']) + '\n',"default")
        self.text_box.insert('end', '대형차 ' + str(info['big_parking']) + '\n',"default")

        self.text_box.config(state=DISABLED)
    def SetMap(self):
        self.map_widget.destroy()
        info = xml.XmlReader.serviceAreaInfoReader(self.Bookmark.get())
        self.map_widget = TkinterMapView(width=300, height=340, corner_radius=0)
        address = info['address']
        self.map_widget.set_zoom(10)

        location=xml.XmlReader.serviceAreaLocationReader(address)

        if location['y'] == 0 and location['x'] == 0:
            label = ttk.Label(self.map_widget, text="위치를 찾을 수 없습니다.", style="Error.TLabel")
            label.place(relx=0.5, rely=0.5, anchor="center")
        else:
            self.map_widget.set_position(location['y'], location['x'])
            self.map_widget.set_marker(location['y'], location['x'], text=address)
        self.map_widget.place(x=500, y=160)

    def SecondComboBoxSelected(self,event):
        # Text Box
        self.SetTextBox()
        # map
        self.SetMap()
