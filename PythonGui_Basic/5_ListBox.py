from tkinter import *
from typing import List

root = Tk()
root.title("Kangdy GUI")
root.geometry("640x480") #가로 * 세로
# root.geometry("640x480+100+300") #가로 * 세로 + x좌표 + y좌표

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # 리스트 삭제
    # listbox.delete(0)

    # 개수 확인
    # print("리스트에는", listbox.size(), "개가 있어요")

    # 항목 확인
    # print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))

    # 선택된 항목 확인 (위치로 반환)
    print("선택된 항목 : ", listbox.curselection())


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()