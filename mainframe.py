# 초기 화면을 담당하는 곳임
from tkinter import *
from tkinter import font
from tkinter import messagebox

class MainFrame:
    def __init__(self, window, w, h):

        #self.frame = window
        self.width = w
        self.height = h
        self.frame = Frame(window, width=self.width, height=self.height)  # window 에 초기화면 frame을 생성한다.

        self.TempFont = font.Font(size=12, family='Consolas') # 여기저기서 쓸 폰트. 맘에 안 들면 바꿔라

        # 당장은 안 쓰지만 이따가 필요한 것들
        self.mainText = None
        self.sigunText = None
        self.dongText = None

        self.sigunLabel = None
        self.dongLabel = None
        self.SearchButton = None

        self.dataList = []

        self.RenderTextScrollbar = None
        self.RenderText = None

        #self.frame.pack()

    def SearchButtonAction(self):
        # 검색 버튼 눌렸을 때 xml 파싱하는 거임
        import http.client
        import urllib

        conn = http.client.HTTPSConnection("openapi.gg.go.kr")
        hangul_utf8 = urllib.parse.quote(str(self.sigunLabel.get()))
        conn.request("GET",
                     "/Resrestrtfastfood?KEY=fead735fe2264921943cc45687420e65&pSize=1000&SIGUN_NM=" + hangul_utf8)
        req = conn.getresponse()

        self.dataList.clear()
        self.RenderText.configure(state='normal')

        if req.status == 200:
            Doc = req.read().decode('utf-8')
        if Doc is None:
            print("에러")
        else:
            from xml.etree import ElementTree
            tree = ElementTree.fromstring(Doc)

            itemElements = tree.getiterator("row")

            if self.dongLabel.get() == "":
                for row in itemElements:
                    name = row.find("BIZPLC_NM")
                    status = row.find("BSN_STATE_NM")
                    addr = row.find("REFINE_ROADNM_ADDR")
                    addr2 = row.find("REFINE_LOTNO_ADDR")
                    wido = row.find("REFINE_WGS84_LAT")
                    gyungdo = row.find("REFINE_WGS84_LOGT")

                    if status.text == "운영중":
                        self.dataList.append((name.text, addr.text, addr2.text, wido.text, gyungdo.text))
            else:
                for row in itemElements:
                    name = row.find("BIZPLC_NM")
                    status = row.find("BSN_STATE_NM")
                    addr = row.find("REFINE_ROADNM_ADDR")
                    addr2 = row.find("REFINE_LOTNO_ADDR")
                    wido = row.find("REFINE_WGS84_LAT")
                    gyungdo = row.find("REFINE_WGS84_LOGT")

                    if status.text == "운영중":
                        if addr.text is not None:
                            if self.dongLabel.get() in addr.text:
                                self.dataList.append((name.text, addr.text, addr2.text, wido.text, gyungdo.text))

            self.InitRenderText()


    def InitRenderText(self):
        # 데이터들을 출력한다
        self.RenderTextScrollbar = Scrollbar(self.frame)
        self.RenderTextScrollbar.place(x=self.width * 0.9, y=self.height / 30, height=self.height / 10 * 5.2)

        self.RenderText = Text(self.frame, width=45, height=12, borderwidth=12, relief='ridge',
                               yscrollcommand=self.RenderTextScrollbar.set)
        j = 0

        for i in self.dataList:
            self.RenderText.insert(INSERT, "[")
            self.RenderText.insert(INSERT, j + 1)
            self.RenderText.insert(INSERT, "] ")
            self.RenderText.insert(INSERT, "시설명: ")
            if i[0] is not None:
                self.RenderText.insert(INSERT, i[0])
            self.RenderText.insert(INSERT, "\n")

            if i[1] is not None:
                self.RenderText.insert(INSERT, "도로명주소: ")
                self.RenderText.insert(INSERT, i[1])
                self.RenderText.insert(INSERT, "\n\n")
            else:
                self.RenderText.insert(INSERT, "지번주소: ")
                self.RenderText.insert(INSERT, i[2])
                self.RenderText.insert(INSERT, "\n\n")
            j += 1

        self.RenderText.place(x=self.width/20, y=self.height/30)
        self.RenderTextScrollbar.config(command=self.RenderText.yview)

        self.RenderText.configure(state='disabled')

    def SetData(self, DataList):
        self.dataList = DataList

    def GetData(self):
        return self.dataList

    def InitTopText(self):
        # 상단에 앱 정보를 띄워주는 라벨
        self.mainText = Label(self.frame, font=self.TempFont, text="경기도 위치 패스트푸드점 검색기능을 제공")
        self.mainText.place(x=self.width * 0.07, y=self.height * 0.6)

        # 입력 라벨들인데 엔트리 옆에 있는 메시지 문장
        self.sigunText = Label(self.frame, font=self.TempFont, text="시ㆍ군")
        self.sigunText.place(x=self.width * 0.03, y=self.height / 10 * 7.2)

        self.dongText = Label(self.frame, font=self.TempFont, text="동 단위")
        self.dongText.place(x=self.width * 0.03, y=self.height / 10 * 8.2)

    def InitSearchEntry(self):
        # 대망의 입력 엔트리들
        self.sigunLabel = Entry(self.frame, font=self.TempFont, width=26, borderwidth=12, relief='ridge')
        self.sigunLabel.place(x=self.width * 0.2, y=self.height / 10 * 7)

        self.dongLabel = Entry(self.frame, font=self.TempFont, width=26, borderwidth=12, relief='ridge')
        self.dongLabel.place(x=self.width * 0.2, y=self.height / 10 * 8)


    def InitSearchButton(self):
        # 검색 버튼을 만듦
        self.SearchButton = Button(self.frame, font=self.TempFont, text="확 인", command=self.SearchButtonAction)
        self.SearchButton.place(x=self.width * 0.8, y=self.height / 10 * 9)

        # Search1Button = Button(g_Tk, font=TempFont, text="갱 신", command=WizetClear)
        # Search1Button.pack()
        # Search1Button.place(x=w * 0.2, y=h / 10 * 9)


