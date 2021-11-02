from tkinter import *
import os

root = Tk()
root.title("제목 없음-메모장")
root.geometry("640x480")

topmenu = Menu(root)

# 열기, 저장, 파일 이름
filename = "mynote.txt"

def openfile():
    if os.path.isfile(filename): # 파일이 있으면 True, 없으면 False
        with open(filename, "r", encoding="utf8") as file:
            textedit.delete("1.0", END) # 텍스트 위젯 본문 삭제
            textedit.insert(END, file.read())
    
def savefile():
    with open(filename, "w", encoding="utf8") as file: # with문을 통해서 자동으로 .close 실행
        file.write(textedit.get("1.0", END)) # 모든 내용을 가져와서 저장

# 스크롤바
memoscrollbar = Scrollbar(root)
memoscrollbar.pack(side="right", fill="y")

# 메모 적기
textedit = Text(root, yscrollcommand=memoscrollbar.set)
textedit.pack(side="left", fill="both", expand=True)

memoscrollbar.config(command=textedit.yview)


# 파일 메뉴
menu_file = Menu(topmenu, tearoff=0)
menu_file.add_command(label="   새로 만들기(N)")
menu_file.add_command(label="   새 창(W)")
menu_file.add_command(label="   열기(O)", command=openfile)
menu_file.add_command(label="   저장(S)", command=savefile)
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

# 메뉴창 설정
root.config(menu=topmenu)

root.mainloop()