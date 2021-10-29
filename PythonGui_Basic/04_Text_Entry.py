from tkinter import *

root = Tk()
root.title("Kangdy GUI")
root.geometry("640x480") #가로 * 세로
# root.geometry("640x480+100+300") #가로 * 세로 + x좌표 + y좌표

# root.resizable(False, False) # 너비 높이 값 변경 불가

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요") 

e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력해요")

def btncmd():
    print(txt.get("1.0", END))
    print(e.get())
    # 1 : 첫 번째 raw d위치, 0 : 0번째 column 위치
    txt.delete("1.0",END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()
root.mainloop()