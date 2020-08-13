# 現在時刻
import tkinter as t
import datetime

def Update():
    dt = datetime.datetime.today()
    ans.set((dt))

win = t.Tk()
win.title('My add')
win.geometry('500x500')

ans = t.StringVar()
Update()

label = t.Label(win, textvariable=ans)
label.config(font=('Arial', 20), fg='blue')
label.pack()

addButton = t.Button(win, text='Update', command=Update)  # UPdate 為上傳最新時間
addButton.config(font=('Arial', 20), fg='orange')
addButton.pack()

win.mainloop()