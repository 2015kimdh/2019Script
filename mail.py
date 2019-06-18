def sendMail():
    global wnd, mailEntry

    tkinter.messagebox.showinfo("정보", "지도에 표시된 지역의 정보를 메일로 전송합니다.\n 만약, 가게를 선택하지 않았다면 먼저 선택해주세요.")
    wnd = Tk()
    TempFont = font.Font(wnd, size=15, weight='bold', family='Consolas')

    Label(wnd, font=TempFont, width=10, borderwidth=12, text="받는 사람").grid(row=0, column=0)
    mailEntry = Entry(wnd, font=TempFont, width=40, borderwidth=10, relief='sunken')
    mailEntry.grid(row=0, column=1)

    send = Button(wnd, font=TempFont, text="보내기", command=Send_To_user)
    send.grid(row=1, column=1, sticky='e')

def Send_To_user():
    global wnd, mailEntry, MapEntry

    import smtplib
    from email.mime.text import MIMEText  # 본문내용을 전송할 때 사용되는 모듈
    from email.mime.multipart import MIMEMultipart  # 메시지를 보낼 때 메시지에 대한 모듈


    if not MapEntry.get().isdecimal():
        tkinter.messagebox.showerror("에러", "가게를 선택해주세요.")
        wnd.destroy()
        return

    msg = MIMEMultipart('alternative')

    host = "smtp.gmail.com"
    port = "587"
    title = "패스트푸드점 검색 결과"
    num = int(MapEntry.get())

    senderAddr = "moss2223@gmail.com"
    password = "gmltmd29"
    recipientAddr = mailEntry.get()

    if DataList[num][1] is None:
        dataAddr = DataList[num][2]
    else:
        dataAddr =DataList[num][1]

    msgtext = "시설명: " + DataList[num][0] + "\n" + "주소: " + dataAddr \
              + "\n"

    msg['Subject'] = title
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    msgPart = MIMEText(msgtext, 'plain')
    msg.attach(msgPart)

    s = smtplib.SMTP(host, port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, password)
    s.sendmail(senderAddr, [recipientAddr], msg.as_string(()))
    s.close()
    wnd.destroy()

    tkinter.messagebox.showinfo("메일 보내기", "메일 전송을 완료하였습니다.")

def Init_Mail():
    global mailButton
    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')

    mailButton = Button(g_Tk, font=TempFont, text="Gmail", command=sendMail)
    mailButton.place(x=w/2- 50,  y=h/10*9)