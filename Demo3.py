import tkinter
from firebase import firebase
firebase = firebase.FirebaseApplication('https://atom940414.firebaseio.com', None)

# 按下open時可將 firebase 上 myhouse 的門打開
def openthedoor():
    result = firebase.patch('/myhouse', {'open': 1})

# 按下close時可將 firebase 上 myhouse 的門關閉
def closethedoor():
    result = firebase.patch('/myhouse', {'open': 0})

win = tkinter.Tk()
win.title('Door Open')
win.geometry('300x100')

OpenButton = tkinter.Button(win, text='Open', command=openthedoor)  # UPdate 為上傳最新時間
OpenButton.config(font=('Arial', 20))
OpenButton.pack(side=tkinter.LEFT)

CloseButton = tkinter.Button(win, text='Close', command=closethedoor)  # UPdate 為上傳最新時間
CloseButton.config(font=('Arial', 20))
CloseButton.pack(side=tkinter.RIGHT)

win.mainloop()

