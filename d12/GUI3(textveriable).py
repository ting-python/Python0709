# 更改變數
import tkinter as t

def add():
    n = int(ans.get())  # 抓取ans值
    n = n + 1  # ans值+1
    ans.set(n)  # 回傳ans值

win = t.Tk()
win.title('My add')
win.geometry('300x300')

ans = t.IntVar()
ans.set(0)

label = t.Label(win, textvariable=ans)  # label的值不可改動 / textvariable可改動
label.config(font=('Arial', 30), fg='blue')
label.pack()

addButton = t.Button(win, text='Add', command=add)
addButton.config(font=('Arial', 30), fg='orange')
addButton.pack()

win.mainloop()