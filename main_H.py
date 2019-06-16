# 내가 테스트로 분리해본 메인임
# 쓸지 말지는 다음에 만나서 결정하자

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

g_Tk.mainloop()
