import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Kangdy GUI")
root.geometry("640x480") #가로 * 세로

# 기차 예매 시스템이라 가정
def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료 되었습니다.")

def warn():
    msgbox.showwarning("경고", "이미 선택된 좌석입니다.")

def error():
    msgbox.showerror("에러", "결제에 실패했습니다.")

def okcancel():
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 퍼스트 클래스 좌석입니다. 예매하시겠습니까?")

def retrycancel():
    msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")

def yesorno():
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?")

def yesornoorcancel():
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다. \n저장 후 프로그램을 종료하시겠습니까?")
    print("응답:", response) # True, False, None 
    
    if response == 1:
        print("예")
    elif response == 0:
        print("아니오")
    else:
        print("취소")
        
Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()

Button(root, command=okcancel, text="확인 / 취소").pack()
Button(root, command=retrycancel, text="재시도 / 취소").pack()
Button(root, command=yesorno, text="예 / 아니오").pack()
Button(root, command=yesornoorcancel, text="예 / 아니오 / 취소").pack()

root.mainloop()