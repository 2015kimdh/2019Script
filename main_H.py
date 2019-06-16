# 내가 테스트로 분리해본 메인임
# 쓸지 말지는 다음에 만나서 결정하자
# 무언가를 추가 하고싶으면 해당 프레임 파일로 가서 수정할 것

from tkinter import *
from tkinter import font
import maps
import mainframe_H

g_Tk = Tk()
w = 400
h = 600
g_Tk.geometry(str(w)+"x"+str(h)+"-100-100")
g_Tk.title("패스트푸드점 검색기")
DataList = []

mainFrame = mainframe_H.MainFrame(g_Tk, w, h)
secondFrame = Frame(g_Tk, width=w, height=h)
a = Label(secondFrame, width=40, height=40, text="두번째 프레임이다!")
a.pack()
secondFrame.pack()


secondFrame.tkraise()

g_Tk.mainloop()
