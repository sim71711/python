from tkinter import *
from tkinter import messagebox

def keyEvent(event):
    keycode = event.keycode
    keysym = event.keysym
    shift_pressed = (event.state & 0x0001) != 0  # Shift 눌림 여부

    arrow_keys = {
        37: "왼쪽 화살표",
        38: "위쪽 화살표",
        39: "오른쪽 화살표",
        40: "아래쪽 화살표"
    }

    # Shift가 눌렸고, 키가 방향키일 때만 처리
    if shift_pressed and keycode in arrow_keys and keysym in ["Left", "Up", "Right", "Down"]:
        message = "눌린 키 : Shift + " + arrow_keys[keycode]
        messagebox.showinfo("키보드 이벤트", message)

window = Tk()
window.bind("<Key>", keyEvent)
window.mainloop()
