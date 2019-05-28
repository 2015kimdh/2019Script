from tkinter import *
from tkinter import font
import tkinter.messagebox
g_Tk = Tk()
w = 400
h = 600
g_Tk.geometry(str(w)+"x"+str(h)+"+750+200")
DataList = []
def InitTopText():
    TempFont = font.Font(g_Tk, size=12, family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text="경기도 위치 패스트푸드점 검색기능을 제공")
    MainText.pack()
    MainText.place(x=w*0.07, y = h*0.6)
    SigunText = Label(g_Tk, font = TempFont, text="시ㆍ군")
    SigunText.pack()
    SigunText.place(x=w * 0.03, y=h / 10 * 7.2)
    DongText = Label(g_Tk, font=TempFont, text="동 단위")
    DongText.pack()
    DongText.place(x=w * 0.03, y=h / 10 * 8.2)

#def InitSearchListBox():
#
#    global SearchListBox
#    ListBoxScrollbar = Scrollbar(g_Tk)
#    ListBoxScrollbar.pack()
#    ListBoxScrollbar.place(x=150, y=50)
#    TempFont = font.Font(g_Tk, size=15, weight='bold',family='Consolas')
#    SearchListBox = Listbox(g_Tk, font=TempFont,
#                            activestyle='none',
#                            width = 10, height = 1, borderwidth = 12, relief = 'ridge',
#                            yscrollcommand = ListBoxScrollbar.set)
#    SearchListBox.insert(1, "도서관")
#    SearchListBox.insert(2, "모범음식점")
#    SearchListBox.insert(3,"마트")
#    SearchListBox.insert(4, "문화시설")
#    SearchListBox.pack()
#    SearchListBox.place(x=10, y=50)
#    ListBoxScrollbar.config(command=SearchListBox.yview)

def InitInputLabel():
    global InputLabel
    global InputLabel1
    TempFont = font.Font(g_Tk, size=15, weight='bold', family ='Consolas')
    InputLabel = Entry(g_Tk, font =TempFont, width =26, borderwidth =12, relief ='ridge')
    InputLabel.pack()
    InputLabel.place(x=w*0.2, y=h/10*7)

    InputLabel1 = Entry(g_Tk, font=TempFont, width=26, borderwidth=12, relief='ridge')
    InputLabel1.pack()
    InputLabel1.place(x=w * 0.2, y=h / 10 * 8)

    # InputLabel[1] = Entry(g_Tk, font=TempFont, width=26, borderwidth=12, relief='ridge')
    # InputLabel[1].pack()
    # InputLabel[1].place(x=w * 0.2, y=h / 10 * 7)

def InitSearchButton():

    TempFont = font.Font(g_Tk, size=15, weight='bold', family ='Consolas')
    SearchButton = Button(g_Tk, font =TempFont, text="확 인", command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=w*0.8, y=h/10*9)

def SearchButtonAction():

    #global SearchListBox
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    iSearchIndex =0#SearchListBox.curselection()[0]

    if iSearchIndex == 0:
        SearchLibrary()
    elif iSearchIndex == 1:
            pass#   SearchGoodFoodService()
    elif iSearchIndex == 2:
        pass#SearchMarket()
    elif iSearchIndex == 3:
        pass#SearchCultural()

    RenderText.configure(state='disabled')


def SearchLibrary():
    import http.client
    import urllib
    from xml.dom.minidom import parse, parseString
    conn = http.client.HTTPSConnection("openapi.gg.go.kr")
    hangul_utf8 = urllib.parse.quote(str(InputLabel.get()))
    conn.request("GET", "/Resrestrtfastfood?KEY=fead735fe2264921943cc45687420e65&pSize=1000&SIGUN_NM=" + hangul_utf8)
    req = conn.getresponse()
    i = 0

    global DataList
    DataList.clear()

    if req.status == 200:
        BooksDoc = req.read().decode('utf-8')
    if BooksDoc == None:
        print("에러")
    else:
        from xml.etree import ElementTree
        tree = ElementTree.fromstring(BooksDoc)
        print(BooksDoc)

        itemElements = tree.getiterator("row")

        if InputLabel1.get() == "":
            for row in itemElements:
                name = row.find("BIZPLC_NM")
                status = row.find("BSN_STATE_NM")
                addr = row.find("REFINE_ROADNM_ADDR")
                addr2 = row.find("REFINE_LOTNO_ADDR")
                wido = row.find("REFINE_WGS84_LAT")
                gyungdo = row.find("REFINE_WGS84_LOGT")
                # if len(addr.text) > 0:
                #     return {"NM":name.text, "addr":addr.text}\
                if status.text == "운영중":
                    DataList.append((name.text, addr.text, addr2.text, wido.text, gyungdo.text))
                    RenderText.insert(INSERT, "[")
                    RenderText.insert(INSERT, i + 1)
                    RenderText.insert(INSERT, "] ")
                    RenderText.insert(INSERT, "시설명: ")
                    if name.text != None:
                        # RenderText.insert(INSERT, name.text)
                        RenderText.insert(INSERT, DataList[i][0])
                    RenderText.insert(INSERT, "\n")

                    if addr.text != None:
                        RenderText.insert(INSERT, "도로명주소: ")
                        # RenderText.insert(INSERT, addr.text)
                        RenderText.insert(INSERT, DataList[i][1])
                    else:
                        RenderText.insert(INSERT, "지번주소: ")
                        # RenderText.insert(INSERT, addr2.text)
                        RenderText.insert(INSERT, DataList[i][2])
                    RenderText.insert(INSERT, "\n\n")
                    i += 1
        else:
            for row in itemElements:
                name = row.find("BIZPLC_NM")
                status = row.find("BSN_STATE_NM")
                addr = row.find("REFINE_ROADNM_ADDR")
                addr2 = row.find("REFINE_LOTNO_ADDR")
                wido = row.find("REFINE_WGS84_LAT")
                gyungdo = row.find("REFINE_WGS84_LOGT")
                # if len(addr.text) > 0:
                #     return {"NM":name.text, "addr":addr.text}\
                if status.text == "운영중":
                    if addr.text != None:
                        if InputLabel1.get() in addr.text:
                            DataList.append((name.text, addr.text, addr2.text, wido.text, gyungdo.text))
                            RenderText.insert(INSERT, "[")
                            RenderText.insert(INSERT, i + 1)
                            RenderText.insert(INSERT, "] ")
                            RenderText.insert(INSERT, "시설명: ")
                            if name.text != None:
                                # RenderText.insert(INSERT, name.text)
                                RenderText.insert(INSERT, DataList[i][0])
                            RenderText.insert(INSERT, "\n")
                            RenderText.insert(INSERT, "도로명주소: ")
                            # RenderText.insert(INSERT, addr.text)
                            RenderText.insert(INSERT, DataList[i][1])
                            RenderText.insert(INSERT, "\n\n")
                            i += 1
                    else:
                        if InputLabel1.get() in addr2.text:
                            DataList.append((name.text, addr.text, addr2.text, wido.text, gyungdo.text))
                            RenderText.insert(INSERT, "[")
                            RenderText.insert(INSERT, i + 1)
                            RenderText.insert(INSERT, "] ")
                            RenderText.insert(INSERT, "시설명: ")
                            if name.text != None:
                                # RenderText.insert(INSERT, name.text)
                                RenderText.insert(INSERT, DataList[i][0])
                            RenderText.insert(INSERT, "\n")
                            RenderText.insert(INSERT, "지번주소: ")
                            # RenderText.insert(INSERT, addr2.text)
                            RenderText.insert(INSERT, DataList[i][2])
                            RenderText.insert(INSERT, "\n\n")
                            i += 1


def InitRenderText():
   global RenderText
   RenderTextScrollbar = Scrollbar(g_Tk)
   RenderTextScrollbar.place(x=w*0.9, y=h/30, height = h/10*5.2)
   RenderTextScrollbar#.place(x=375, y=200)

   TempFont = font.Font(g_Tk, size=10, family='Consolas')
   RenderText = Text(g_Tk, width=45, height=22,borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
   RenderText.pack()
   RenderText.place(x=w/20, y=h/30)
   RenderTextScrollbar.config(command=RenderText.yview)
   # RenderTextScrollbar.pack(side=RIGHT, fill=Y)

   RenderText.configure(state='disabled')

    #…
InitTopText()
#InitSearchListBox()
InitInputLabel()
InitSearchButton()
InitRenderText()
#InitSendEmailButton()
#InitSortListBox()
#InitSortButton()
g_Tk.mainloop()
