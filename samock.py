from tkinter import *
import tkinter.messagebox

class TickTacToe:
    def pressed(self, Row, Col):
        for r in range(5, -1, -1): # r = 5 , 4, 3 , 2 , 1
            if self.buttonList[r * 7 + Col]['text'] == ' ':
                if self.turn:   # o 차례
                    self.buttonList[r * 7 + Col].configure(text="O", image=self.imageList[0])
                    self.board[r * 7 + Col] = "O"
                else:           # x 차례
                    self.buttonList[r * 7 + Col].configure(text="X", image=self.imageList[1])
                    self.board[r * 7 + Col] = "X"
                self.turn = not self.turn
                break

        for r in range(6):
            for c in range(7):
                print(self.board[r * 7 + c], end=' ')
            print()
        print()
        self.endGame()

    def SetendGame(self, Row, Col):
        self.buttonList[Row * 7 + Col].configure(relief="solid")

    def endGame(self):
        count = 0
        temp = ' '
        # 가로 체크
        for r in range(5, -1, -1):
            for c in range(7):
                if self.board[r * 7 + c] != ' ':
                    if self.board[r * 7 + c] == temp:
                        count += 1
                    else:
                        temp = self.board[r * 7 + c]
                        count = 0
                else:
                    temp = ' '
                    count = 0
                if 3 <= count:
                    self.MBox(temp)
                    count = 0
                    break

        count = 0
        temp = ' '
        # 세로 체크
        for c in range(7):
            for r in range(5, -1, -1):
                if self.board[r * 7 + c] != ' ':
                    if self.board[r * 7 + c] == temp:
                        count += 1
                    else:
                        temp = self.board[r * 7 + c]
                        count = 0
                else:
                    temp = ' '
                    count = 0
                if 3 <= count:
                    self.MBox(temp)
                    count = 0
                    break

        count = 0
        temp = ' '
        # 오른쪽 위 대각선 체크
        # 왼쪽 위부터 밑으로 내려오면서 오른쪽 위 대각선 체크
        for r in range(3, 6):
            for i in range(r + 1):
                if self.board[r * 7 - i * 6] != ' ':
                    if self.board[r * 7 - i * 6] == temp:
                        count += 1
                    else:
                        temp = self.board[r * 7 - i * 6]
                        count = 0
                else:
                    temp = ' '
                    count = 0
                if 3 <= count:
                    self.MBox(temp)
                    count = 0
                    break
        # 왼쪽 아래 부터 오른쪽으로 가면서 오른쪽 위 대각선 체크
        count = 0
        temp = ' '
        for c in range(3):
            for i in range(6 - c):
                if self.board[36 + c - i * 6] != ' ':
                    if self.board[36 + c - i * 6] == temp:
                        count += 1
                    else:
                        temp = self.board[36 + c - i * 6]
                        count = 0
                else:
                    temp = ' '
                    count = 0
                if 3 <= count:
                    self.MBox(temp)
                    count = 0
                    break


        count = 0
        temp = ' '
        # 왼쪽 위 대각선 체크
        # 오른쪽 위부터 밑으로 내려오면서 왼쪽 위 대각선 체크
        for r in range(4, 7):
            for i in range(r):
                if self.board[r * 7 - 1 - i * 8] != ' ':
                    if self.board[r * 7 - 1 - i * 8] == temp:
                        count += 1
                    else:
                        temp = self.board[r * 7 - 1 - i * 8]
                        count = 0
                else:
                    temp = ' '
                    count = 0
                if 3 <= count:
                    self.MBox(temp)
                    count = 0
                    break
        # 오른쪽 아래 부터 왼쪽으로 가면서 왼쪽 위 대각선 체크
        count = 0
        temp = ' '
        for c in range(3):
            for i in range(6 - c):
                if self.board[40 - c - i * 8] != ' ':
                    if self.board[40 - c - i * 8] == temp:
                        count += 1
                    else:
                        temp = self.board[40 - c - i * 8]
                        count = 0
                else:
                    temp = ' '
                    count = 0
                if 3 <= count:
                    self.MBox(temp)
                    count = 0
                    break

        if not ' ' in self.board:
            self.MBox(' ')





    def MBox(self, txt):
        if txt == 'O':
            tkinter.messagebox.showinfo("승리", "O 승리!")
        elif txt == 'X':
            tkinter.messagebox.showinfo("승리", "X 승리!")
        else:
            tkinter.messagebox.showinfo("비김", "비겼습니다!")
        self.again()


    def again(self):
        for r in range(6):
            for c in range(7):
                self.buttonList[r*7+c].configure(text=' ', image=self.imageList[2], relief="flat")
                self.board[r*7+c] = ' '
                self.turn = True


    def __init__(self):
        window = Tk()
        window.title("사목게임")
        self.imageList = []
        self.turn = True
        self.imageList.append(PhotoImage(file="C:/Users/정희승/Downloads/book/pybook/image/o.gif"))
        self.imageList.append(PhotoImage(file="C:/Users/정희승/Downloads/book/pybook/image/x.gif"))
        self.imageList.append(PhotoImage(file="C:/Users/정희승/Downloads/book/pybook/image/empty.gif"))
        self.buttonList = []
        self.board = []
        frame1 = Frame(window)
        frame1.pack()
        for r in range(6):
            for c in range(7):
                self.board.append(' ')
                self.buttonList.append(Button(frame1, text=" ", image=self.imageList[2],
                                              command=lambda Row = r, Col = c:self.pressed(Row, Col)))
                self.buttonList[r*7+c].grid(row=r, column=c)
        frame2 = Frame(window)
        frame2.pack()
        Button(frame2, text="다시하기", command=self.again).pack()

        window.mainloop()

TickTacToe()
