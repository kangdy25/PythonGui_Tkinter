from tkinter import *

root = Tk()
root.title("Kangdy GUI")
root.geometry("640x480") #가로 * 세로

def create_new_file():
    print("새 파일을 만듭니다.")

menu = Menu(root)

# File Menu
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)

menu.add_cascade(label="File", menu=menu_file)


# Edit 메뉴 (빈 값)
menu.add_cascade(label="Edit")


# Language 메뉴 추가 (Radio 버튼을 통해 택 1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu_lang.add_radiobutton(label="React Native")
menu_lang.add_radiobutton(label="Flutter")
menu.add_cascade(label="Language", menu=menu_lang)


# CheckBox 메뉴 추가
menu_check = Menu(menu, tearoff=0)
menu_check.add_checkbutton(label="Show Minimap")
menu_check.add_checkbutton(label="Show Breadcrumbs")
menu_check.add_checkbutton(label="Render Whitespace")
menu.add_cascade(label="View", menu=menu_check)

root.config(menu=menu)
root.mainloop()