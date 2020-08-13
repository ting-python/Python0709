import tkinter
from tkinter import messagebox

def Hello():  # 按下 OK 後叫出視窗
    messagebox.showinfo('Hello', 'Python')

def cancel():  # 按下Exit後離開視窗
    win.quit()

win = tkinter.Tk()

win.title('我的小視窗')  # 標題名稱
win.geometry('500x300')  # 視窗大小

label = tkinter.Label(win, text='Hello')  # label=字串
label.pack()
label.config(font=('Arial', 40), bg='Red', fg='Yellow')  # config=其他屬性

button1 = tkinter.Button(win, text='OK', command=Hello)  # button=按鈕
button1.config(font=('Arial', 30))                       # command=指令(呼叫def)
button1.pack(side=tkinter.LEFT)

button2 = tkinter.Button(win, text='Exit', command=cancel)
button2.config(font=('Arial', 30))
button2.pack(side=tkinter.RIGHT)

win.mainloop()