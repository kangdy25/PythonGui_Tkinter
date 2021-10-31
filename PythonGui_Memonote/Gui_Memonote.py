from tkinter import *

root = Tk()
root.title("제목 없음-메모장")
root.geometry("640x480")

topmenu = Menu(root)

# 파일 메뉴
menu_file = Menu(topmenu, tearoff=0)
menu_file.add_command(label="   새로 만들기(N)")
menu_file.add_command(label="   새 창(W)")
menu_file.add_command(label="   열기(O)")
menu_file.add_command(label="   저장(S)")
menu_file.add_command(label="   다른 이름으로 저장(A)")
menu_file.add_separator()
menu_file.add_command(label="   페이지 설정(U)")
menu_file.add_command(label="   인쇄(P)")
menu_file.add_separator()
menu_file.add_command(label="   끝내기(X)", command=root.quit)

topmenu.add_cascade(label="파일(F)", menu=menu_file)

# 편집 메뉴
menu_file = Menu(topmenu, tearoff=0)
menu_file.add_command(label="   새로 만들기")
topmenu.add_cascade(label="편집(E)", menu=menu_file)

# 포맷 메뉴
menu_file = Menu(topmenu, tearoff=0)
menu_file.add_command(label="   새로 만들기")
topmenu.add_cascade(label="포맷(O)", menu=menu_file)

# 보기 메뉴
menu_file = Menu(topmenu, tearoff=0)
menu_file.add_command(label="   새로 만들기")
topmenu.add_cascade(label="보기(V)", menu=menu_file)

# 도움말 메뉴
menu_file = Menu(topmenu, tearoff=0)
menu_file.add_command(label="   새로 만들기")
topmenu.add_cascade(label="도움말(H)", menu=menu_file)

# 메모 적기
textedit = Text(root)
textedit.pack()

root.config(menu=topmenu)
root.mainloop()