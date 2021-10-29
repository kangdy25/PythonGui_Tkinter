from tkinter import *
from typing import List

root = Tk()
root.title("Kangdy GUI")
root.geometry("640x480") #가로 * 세로
# root.geometry("640x480+100+300") #가로 * 세로 + x좌표 + y좌표

chkvar = IntVar() # chkvar에 int 형으로 값을 저장한다
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# chkbox.select()
# chkbox.deselect()
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일 동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0 : 체크 해제, 1 : 체크 표시
    print(chkvar2.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()