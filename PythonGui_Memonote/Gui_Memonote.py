from tkinter import *

root = Tk()
root.title("제목 없음-메모장")
root.geometry("640x480")

topmenu = Menu(root)

# 파일 메뉴
menu_file = Menu(topmenu, tearoff=0)
menu_file.add_command(label="   새로 만들기")
topmenu.add_cascade(label="파일(F)", menu=menu_file)

# 편집 메뉴
menu_file = Menu(topmenu, tearoff=0)
menu_file.add_command(label="   새로 만들기")
topmenu.add_cascade(label="편집(E)", menu=menu_file)

# 편집 메뉴
menu_file = Menu(topmenu, tearoff=0)
menu_file.add_command(label="   새로 만들기")
topmenu.add_cascade(label="포맷(o)", menu=menu_file)

# 편집 메뉴
menu_file = Menu(topmenu, tearoff=0)
menu_file.add_command(label="   새로 만들기")
topmenu.add_cascade(label="보기(v)", menu=menu_file)

# 편집 메뉴
menu_file = Menu(topmenu, tearoff=0)
menu_file.add_command(label="   새로 만들기")
topmenu.add_cascade(label="도움말(H)", menu=menu_file)

root.config(menu=topmenu)
root.mainloop()