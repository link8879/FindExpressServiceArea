from tkinter import *
from HomePage import HomePage
from OilPage import OilPage
from Bookmark import Bookmark

class MainGUI(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("쉼표")

        # window size
        self.geometry("800x600")
        self.resizable(False, False)

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

        for frames in self.frames.values():
            if hasattr(frames,'map_widget'):
                frames.map_widget.destroy()

        if hasattr(frame, 'text_box'):
            frame.map_widget.destroy()
            frame.text_box.destroy()
            frame.Highway_Route_List.set('')
            frame.RestArea_List.set('')


if __name__ == "__main__":
    app = MainGUI()
    app.mainloop()