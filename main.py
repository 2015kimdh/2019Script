from tkinter import *

# window 생성
window = Tk()
window.title("패스트푸드점 검색기")
width = 480         # 화면 넓이
height = 720        # 화면 높이
window.geometry(str(width)+'x'+str(height)+"-200+200")  # 위에서 설정한 값들을 바탕으로 화면을 만듦
                                                        # width, height로 크기 조절하고 오른쪽 숫자는 생성되는 위치

def InitInputSIGUN():
    # 시·군 입력하는 라벨 & 엔트리 생성

    # 먼저 frame 만들고 위치는 place로 설정해 주었음
    SGFrmae = Frame(window, bg='white')
    SGFrmae.pack()
    SGFrmae.place(x=10, y=600)

    # Label 만들어서 frame 안에 넣었음
    SIGUN = Label(SGFrmae, text="시·군      ")
    SIGUN.pack(side=LEFT)

    # Entry 만들어서 배치
    SIGUNEntry = Entry(SGFrmae)
    SIGUNEntry.pack(side=RIGHT)

def InitInputSector():
    # 동·면·읍 입력하는 라벨 & 엔트리 생성
    # 시·군 코드와 설명은 동일함
    
    StFrame = Frame(window, bg='white')
    StFrame.pack()
    StFrame.place(x=10, y=630)

    SECTOR = Label(StFrame, text="동·면·읍  ")
    SECTOR.pack(side=LEFT)

    SECTOREntry = Entry(StFrame)
    SECTOREntry.pack(side=RIGHT)


InitInputSIGUN()
InitInputSector()

window.mainloop()