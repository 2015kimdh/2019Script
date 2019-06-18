from tkinter import *
from tkinter import font
import maps
import tkinter.messagebox


g_Tk = Tk()
w = 600
h = 800
g_Tk.geometry(str(w)+"x"+str(h)+"-100+200")
DataList = []
DataListTemp = []
FrameNum = 0
m_frame = None

def InitTopText():
    global MainText
    global SigunText
    global DongText

    TempFont = font.Font(g_Tk, size=15, family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text="경기도 위치 패스트푸드점 검색기능을 제공")
    MainText.pack()
    MainText.place(x=w*0.15, y = h*0.6)
    SigunText = Label(g_Tk, font = TempFont, text="시ㆍ군")
    SigunText.pack()
    SigunText.place(x=w * 0.03, y=h / 10 * 7.2)
    DongText = Label(g_Tk, font=TempFont, text="동 단위")
    DongText.pack()
    DongText.place(x=w * 0.03, y=h / 10 * 8.2)

def InitInputLabel():
    global InputLabel
    global InputLabel1
    TempFont = font.Font(g_Tk, size=15, weight='bold', family ='Consolas')
    InputLabel = Entry(g_Tk, font =TempFont, width =35, borderwidth =12, relief ='ridge')
    InputLabel.pack()
    InputLabel.place(x=w*0.2, y=h/10*7)

    InputLabel1 = Entry(g_Tk, font=TempFont, width=35, borderwidth=12, relief='ridge')
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
        Frame_2_InitRenderText()
    elif FrameNum == 2:
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


def InitRenderText():
   global RenderText
   RenderTextScrollbar = Scrollbar(g_Tk)
   RenderTextScrollbar.place(x=w * 0.91, y=h / 30, height=h / 10 * 2.8)

   TempFont = font.Font(g_Tk, size=10, family='Consolas')
   RenderText = Text(g_Tk, width=70, height=15, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
   j = 0

   for i in DataListTemp:
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
    RenderText_1 = Text(g_Tk, width=69, height=30, borderwidth=12, relief='ridge',
                      yscrollcommand=RenderText_1Scrollbar.set)
    RenderText_1.pack()
    RenderText_1.place(x=w / 20, y=h / 30)
    RenderText_1Scrollbar.config(command=RenderText_1.yview)
    # RenderTextScrollbar.pack(side=RIGHT, fill=Y)

    RenderText_1.configure(state='disabled')

    #…

def Frame_2_InitRenderText():
   global Frame2RenderText
   global Frame2RenderTextScrollbar
   Frame2RenderTextScrollbar = Scrollbar(g_Tk)
   Frame2RenderTextScrollbar.place(x=w * 0.91, y=h / 30, height=h / 10 * 2.8)

   TempFont = font.Font(g_Tk, size=10, family='Consolas')
   Frame2RenderText = Text(g_Tk, width=70, height=15, borderwidth=12, relief='ridge', yscrollcommand=Frame2RenderTextScrollbar.set)
   j = 0

   global DataList
   global DataListTemp
   DataListTemp.clear()

   if NameLabel.get() is '':
        for i in DataList:
            DataListTemp.append(i)
            Frame2RenderText.insert(INSERT, "[")
            Frame2RenderText.insert(INSERT, j + 1)
            Frame2RenderText.insert(INSERT, "] ")
            Frame2RenderText.insert(INSERT, "시설명: ")
            if i[0] != None:
                # RenderText.ins#ert(INSERT, name.text)
                Frame2RenderText.insert(INSERT, i[0])
                Frame2RenderText.insert(INSERT, "\n")

            if i[1] != None:
                Frame2RenderText.insert(INSERT, "도로명주소: ")
                # RenderText.insert(INSERT, addr.text)
                Frame2RenderText.insert(INSERT, i[1])
                Frame2RenderText.insert(INSERT, "\n\n")
            else:
                Frame2RenderText.insert(INSERT, "지번주소: ")
                # RenderText.insert(INSERT, addr2.text)
                Frame2RenderText.insert(INSERT, i[2])
                Frame2RenderText.insert(INSERT, "\n\n")
            j += 1
   else:
       for i in DataList:
           if NameLabel.get() in i[0]:
               DataListTemp.append(i)
               Frame2RenderText.insert(INSERT, "[")
               Frame2RenderText.insert(INSERT, j + 1)
               Frame2RenderText.insert(INSERT, "] ")
               Frame2RenderText.insert(INSERT, "시설명: ")

               if i[0] != None:
                   # RenderText.ins#ert(INSERT, name.text)
                   Frame2RenderText.insert(INSERT, i[0])
                   Frame2RenderText.insert(INSERT, "\n")

               if i[1] != None:
                   Frame2RenderText.insert(INSERT, "도로명주소: ")
                   # RenderText.insert(INSERT, addr.text)
                   Frame2RenderText.insert(INSERT, i[1])
                   Frame2RenderText.insert(INSERT, "\n\n")
               else:
                   Frame2RenderText.insert(INSERT, "지번주소: ")
                   # RenderText.insert(INSERT, addr2.text)
                   Frame2RenderText.insert(INSERT, i[2])
                   Frame2RenderText.insert(INSERT, "\n\n")
               j += 1


   Frame2RenderText.pack()
   Frame2RenderText.place(x=w/20, y=h / 30)
   Frame2RenderTextScrollbar.config(command=Frame2RenderText.yview)
   # RenderTextScrollbar.pack(side=RIGHT, fill=Y)

   Frame2RenderText.configure(state='disabled')

def InitNameLabel():
    global NameLabel
    TempFont = font.Font(g_Tk, size=15, weight='bold', family ='Consolas')
    NameLabel = Entry(g_Tk, font =TempFont, width =35, borderwidth =12, relief ='ridge')
    NameLabel.pack()
    NameLabel.place(x=w*0.2, y=h/10*7)

def SearchMap():
    global m_frame

    if MapEntry.get() is not '':
        s = int(MapEntry.get())
        m_frame = Frame()
        map_image = maps.show_map(float(DataListTemp[s][4]), float(DataListTemp[s][3]))
        m_frame.place(x=w / 10, y=h / 2)
        Label(m_frame, image=map_image, height=h/3, width=w * 2 / 2.5, background="white", relief ='ridge', borderwidth =10).pack()


def InitMapInput():

    global MapEntry

    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    MapEntry = Entry(g_Tk, font=TempFont, width=20, borderwidth=10, relief='sunken')
    MapEntry.place(x=w / 10 * 2.5, y=h / 10 * 3.5)

    Label(g_Tk, font=TempFont, text="번호").place(x=w/20, y=h / 10 * 3.7)


def WizetClear():

    global m_frame
    global  FrameNum
    FrameNum += 1
    FrameNum = FrameNum % 3

    if FrameNum == 0:
        RenderText.destroy()
        MapEntry.destroy()
        if m_frame is not None:
            m_frame.destroy()
            m_frame = None
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

        InitNameLabel()     #필터링할 조건 이름 주기 / 데이터리스트를 초기화하거나 하지는 않음
        Frame_2_InitRenderText()    #위에서 필터링 해준거 담아오는 텍스트

    elif FrameNum == 2:
        NameLabel.destroy()
        Frame2RenderText.destroy()
        Frame2RenderTextScrollbar.destroy()

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