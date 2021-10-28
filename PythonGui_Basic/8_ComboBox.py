import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Kangdy GUI")
root.geometry("640x480") #가로 * 세로

value = [str(i) + "일" for i in range(1, 32)]
combobox =ttk.Combobox(root, height=5, values=value)
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정

readonly_combobox =ttk.Combobox(root, height=10, values=value, state="readonly")
readonly_combobox.current(0) # 0번째 인덱스 값 선택
readonly_combobox.pack()

def btncmd():
    print(combobox.get()) # 선택 값 설정
    print(readonly_combobox.get())
btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()