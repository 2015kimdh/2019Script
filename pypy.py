from tkinter import *
from tkinter import font
import maps
import tkinter.messagebox


g_Tk = Tk()
w = 400
h = 600
g_Tk.geometry(str(w)+"x"+str(h)+"-100-100")
DataList = []
FrameNum = 0

def InitTopText():
    global MainText
    global SigunText
    global DongText

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

    Search1Button = Button(g_Tk, font=TempFont, text="갱 신", command=WizetClear)
    Search1Button.pack()
    Search1Button.place(x=w * 0.2, y=h / 10 * 9)

def SearchButtonAction():

    if FrameNum == 0:
        SearchLibrary()
    elif FrameNum == 1:
        SearchMap()



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

#def SearchLibrary():
#    import http.client
#    import urllib
#    from xml.dom.minidom import parse, parseString
#    conn = http.client.HTTPSConnection("openapi.gg.go.kr")
#    hangul_utf8 = urllib.parse.quote(str(InputLabel.get()))
#    conn.request("GET", "/Resrestrtfastfood?KEY=fead735fe2264921943cc45687420e65&pSize=1000&SIGUN_NM=" + hangul_utf8)
#    req = conn.getresponse()
#    i = 0
#
#    global DataList
#    DataList.clear()
#
#    if req.status == 200:
#        BooksDoc = req.read().decode('utf-8')
#    if BooksDoc == None:
#        print("에러")
#    else:
#        from xml.etree import ElementTree
#        tree = ElementTree.fromstring(BooksDoc)
#
#        itemElements = tree.getiterator("row")
#
#        if InputLabel1.get() == "":
#            for row in itemElements:
#                name = row.find("BIZPLC_NM")
#                status = row.find("BSN_STATE_NM")
#                addr = row.find("REFINE_ROADNM_ADDR")
#                addr2 = row.find("REFINE_LOTNO_ADDR")
#                wido = row.find("REFINE_WGS84_LAT")
#                gyungdo = row.find("REFINE_WGS84_LOGT")
#                # if len(addr.text) > 0:
#                #     return {"NM":name.text, "addr":addr.text}\
#                if status.text == "운영중":
#                    DataList.append((name.text, addr.text, addr2.text, wido.text, gyungdo.text))
#                    RenderText_1.insert(INSERT, "[")
#                    RenderText_1.insert(INSERT, i + 1)
#                    RenderText_1.insert(INSERT, "] ")
#                    RenderText_1.insert(INSERT, "시설명: ")
#                    if name.text != None:
#                        # RenderText.ins#ert(INSERT, name.text)
#                        RenderText_1.insert(INSERT, DataList[i][0])
#                    RenderText_1.insert(INSERT, "\n")
#
#                    if addr.text != None:
#                        RenderText_1.insert(INSERT, "도로명주소: ")
#                        # RenderText.insert(INSERT, addr.text)
#                        RenderText_1.insert(INSERT, DataList[i][1])
#                    else:
#                        RenderText_1.insert(INSERT, "지번주소: ")
#                        # RenderText.insert(INSERT, addr2.text)
#                        RenderText_1.insert(INSERT, DataList[i][2])
#                        RenderText_1.insert(INSERT, "\n\n")
#                    i += 1
#        else:
#            for row in itemElements:
#                name = row.find("BIZPLC_NM")
#                status = row.find("BSN_STATE_NM")
#                addr = row.find("REFINE_ROADNM_ADDR")
#                addr2 = row.find("REFINE_LOTNO_ADDR")
#                wido = row.find("REFINE_WGS84_LAT")
#                gyungdo = row.find("REFINE_WGS84_LOGT")
#                # if len(addr.text) > 0:
#                #     return {"NM":name.text, "addr":addr.text}\
#                if status.text == "운영중":
#                    if addr.text != None:
#                        if InputLabel1.get() in addr.text:
#                            DataList.append((name.text, addr.text, addr2.text, wido.text, gyungdo.text))
#                            RenderText_1.insert(INSERT, "[")
#                            RenderText_1.insert(INSERT, i + 1)
#                            RenderText_1.insert(INSERT, "] ")
#                            RenderText_1.insert(INSERT, "시설명: ")
#                            if name.text != None:
#                                # RenderText.insert(INSERT, name.text)
#                                RenderText_1.insert(INSERT, DataList[i][0])
#                            RenderText_1.insert(INSERT, "\n")
#                            RenderText_1.insert(INSERT, "도로명주소: ")
#                            # RenderText.insert(INSERT, addr.text)
#                            RenderText_1.insert(INSERT, DataList[i][1])
#                            RenderText_1.insert(INSERT, "\n\n")
#                            i += 1
#                    else:
#                        if InputLabel1.get() in addr2.text:
#                            DataList.append((name.text, addr.text, addr2.text, wido.text, gyungdo.text))
#                            RenderText_1.insert(INSERT, "[")
#                            RenderText_1.insert(INSERT, i + 1)
#                            RenderText_1.insert(INSERT, "] ")
#                            RenderText_1.insert(INSERT, "시설명: ")
#                            if name.text != None:
#                                # RenderText.insert(INSERT, name.text)
#                                RenderText_1.insert(INSERT, DataList[i][0])
#                            RenderText_1.insert(INSERT, "\n")
#                            RenderText_1.insert(INSERT, "지번주소: ")
#                            # RenderText.insert(INSERT, addr2.text)
#                            RenderText_1.insert(INSERT, DataList[i][2])
#                            RenderText_1.insert(INSERT, "\n\n")
#                            i += 1


def InitRenderText():
   global RenderText
   RenderTextScrollbar = Scrollbar(g_Tk)
   RenderTextScrollbar.place(x=w * 0.9, y=h / 30, height=h / 10 * 5.2)

   TempFont = font.Font(g_Tk, size=10, family='Consolas')
   RenderText = Text(g_Tk, width=45, height=12, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
   j = 0

   for i in DataList:
       RenderText.insert(INSERT, "[")
       RenderText.insert(INSERT, j + 1)
       RenderText.insert(INSERT, "] ")
       RenderText.insert(INSERT, "시설명: ")
       if i[0] != None:
           # RenderText.ins#ert(INSERT, name.text)
           RenderText.insert(INSERT, i[0])
       RenderText.insert(INSERT, "\n")

       if i[1] != None:
           RenderText.insert(INSERT, "도로명주소: ")
           # RenderText.insert(INSERT, addr.text)
           RenderText.insert(INSERT, i[1])
           RenderText.insert(INSERT, "\n\n")
       else:
           RenderText.insert(INSERT, "지번주소: ")
           # RenderText.insert(INSERT, addr2.text)
           RenderText.insert(INSERT, i[2])
           RenderText.insert(INSERT, "\n\n")
       j += 1



   RenderText.pack()
   RenderText.place(x=w/20, y=h / 30)
   RenderTextScrollbar.config(command=RenderText.yview)
   # RenderTextScrollbar.pack(side=RIGHT, fill=Y)

   RenderText.configure(state='disabled')


def InitRenderText_1():
    global RenderText_1
    global RenderText_1Scrollbar
    RenderText_1Scrollbar = Scrollbar(g_Tk)
    RenderText_1Scrollbar.place(x=w * 0.9, y=h / 30, height=h / 10 * 5.2)
    RenderText_1Scrollbar  # .place(x=375, y=200)

    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText_1 = Text(g_Tk, width=45, height=22, borderwidth=12, relief='ridge',
                      yscrollcommand=RenderText_1Scrollbar.set)
    RenderText_1.pack()
    RenderText_1.place(x=w / 20, y=h / 30)
    RenderText_1Scrollbar.config(command=RenderText_1.yview)
    # RenderTextScrollbar.pack(side=RIGHT, fill=Y)

    RenderText_1.configure(state='disabled')

    #…


def SearchMap():
    global m_frame

    if MapEntry.get() is not '':
        s = int(MapEntry.get())

        map_image = maps.show_map(float(DataList[s][4]), float(DataList[s][3]))

        m_frame = Frame(g_Tk)
        m_frame.place(x=w / 10, y=h / 2)
        Label(m_frame, image=map_image, height=h/3, width=w * 2 / 3, background="white").pack()


def InitMapInput():

    global MapEntry

    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    MapEntry = Entry(g_Tk, font=TempFont, width=20, borderwidth=10, relief='sunken')
    MapEntry.place(x=w / 10 * 2.5, y=h / 10 * 3.5)

    Label(g_Tk, font=TempFont, text="번호").place(x=w/20, y=h / 10 * 3.7)


def WizetClear():

    global  FrameNum
    FrameNum += 1
    FrameNum = FrameNum % 2

    if FrameNum == 0:
        RenderText.destroy()
        MapEntry.destroy()
        m_frame.destroy()
        InitTopText()
        # InitSearchListBox()
        InitInputLabel()
        InitRenderText_1()
        InitSearchButton()
        # InitSendEmailButton()
        # InitSortListBox()
        # InitSortButton()
    elif FrameNum == 1:
        RenderText_1.destroy()
        RenderText_1Scrollbar.destroy()
        InputLabel.destroy()
        InputLabel1.destroy()
        SigunText.destroy()
        MainText.destroy()
        DongText.destroy()
        InitRenderText()
        InitMapInput()





InitTopText()
# InitSearchListBox()
InitInputLabel()
InitRenderText_1()
InitSearchButton()
g_Tk.update()
g_Tk.after_cancel(g_Tk)
g_Tk.mainloop()