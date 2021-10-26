from tkinter import *

root = Tk()
root.title("Kangdy GUI")
root.geometry("640x480") #가로 * 세로
# root.geometry("640x480+100+300") #가로 * 세로 + x좌표 + y좌표

# root.resizable(False, False) # 너비 높이 값 변경 불가
label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="img/CheckBox.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")

    global photo2
    photo2 = PhotoImage(file="img/RedX.png")
    label2.config(image=photo2)
btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()