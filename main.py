from tkinter import *

# window 생성
window = Tk()
window.title("패스트푸드점 검색기")
width = 480         # 화면 넓이
height = 600        # 화면 높이
window.geometry(str(width)+'x'+str(height)+"-100+100")  # 위에서 설정한 값들을 바탕으로 화면을 만듦
                                                        # width, height로 크기 조절하고 오른쪽 숫자는 생성되는 위치

def InitInputSIGUN():
    # 시·군 입력하는 라벨 & 엔트리 생성
    # 엔트리 값은 나중에 쓸테니 global로 설정

    global SIGUNEntry
    interval = 10

    # Label 만들어서 배치하자
    SIGUN = Label(window, text="시·군      ")
    SIGUN.place(x=10, y=height * 3 / 4 - interval)

    # Entry 만들어서 배치
    SIGUNEntry = Entry(window)
    SIGUNEntry.place(x=60, y=height * 3 / 4 - interval)

def InitInputSector():
    # 동·면·읍 입력하는 라벨 & 엔트리 생성
    # 시·군 코드와 설명은 동일함

    global SECTOREntry
    interval = 10
    gap = 20    # gap은 위의 시 군 코드 와의 간격을 위해서 설정함

    SECTOR = Label(window, text="동·면·읍  ")
    SECTOR.place(x=10, y=height * 3 / 4 - interval - gap)

    SECTOREntry = Entry(window)
    SECTOREntry.place(x=60, y=height * 3 / 4 - interval - gap)

InitInputSIGUN()
InitInputSector()

window.mainloop()