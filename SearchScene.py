from tkinter import *
from tkinter import font
import pypy

window = Tk()
window.title("패스트푸드점 검색기")
width = 400         # 화면 넓이
height = 600        # 화면 높이
window.geometry(str(width)+'x'+str(height)+"-100+100")


def FilterAction():
    pass


def InitFilterLabel():
    tempfont = font.Font(window, family='Consolas', size=12, weight='bold')

    FilterText = Label(window, font=tempfont, text="필터링")
    FilterText.place(x=width / 12, y=height / 20)


def InitFilterEntry():
    global FilterEntry

    tempfont = font.Font(window, family='Consolas', size=12, weight='bold')
    FilterEntry = Entry(window, font=tempfont)
    FilterEntry.place(x=width / 4, y=height / 20)


def InitFilterButton():
    tempfont = font.Font(window, family='Consolas', size=12, weight='bold')

    FilterButton = Button(window, font=tempfont, text="검색", command=FilterAction)
    FilterButton.place(x=width * 3 / 4, y=height / 25)


class ShowBox:
    def __init__(self, frame, s):
        self.dat = s
        self.L = Label(frame, text=self.dat)
        self.L.pack()
        self.L.bind("<Button-1>", self.Click)

    def Click(self, event):
        print("나는", self.dat, "입니다")


def Click(event):
    print(event)

def InitShowBox():
    pass
    # Showframe = LabelFrame(window, width=width/2, height=height/2, bg='white', text="나 여깄어요")
    # Showframe.place(x=width / 12, y=height/10)


    #
    # TempFont = font.Font(window, size=10, family='Consolas')
    # RenderText = Text(window, font=TempFont, width=45, height=22, borderwidth=12, relief='ridge')
    # RenderText.pack()
    #
    # first = ShowBox(RenderText, "1st")
    # second = ShowBox(RenderText, "2nd")
    # third = ShowBox(RenderText, "3rd")

    # firstF = Frame(Showframe)
    # firstF.pack()
    # firstL = Label(firstF, text="1st")
    # firstL.pack()
    # firstL.bind("<Button-1>", Click)
    #
    # secondF = Frame(Showframe)
    # secondF.pack()
    # secondL = Label(firstF, text="2st")
    # secondL.pack()
    # secondL.bind("<Button-1>", Click)
    #
    # thirdF = Frame(Showframe)
    # thirdF.pack()
    # thirdL = Label(firstF, text="3st")
    # thirdL.pack()
    # thirdL.bind("<Button-1>", Click)



pypy.InitInputLabel()
pypy.InitSearchButton()

window.mainloop()
