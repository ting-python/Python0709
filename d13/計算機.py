import tkinter
import tkinter.ttk as ttk

win = tkinter.Tk()
win.title('計算機')

# 按鈕功能設定
# C  <-  .  =
def C():
    var.set(0)
def back():
    s = var.get()
    var.set(s[:len(s)-1])
def dot():
    var.set(var.get() + ".")
def equal():
    var.set("%.2f" % eval(var.get()))

# +  -  *  /
def plus():
    var.set(var.get() + "+")
def minus():
    var.set(var.get() + "-")
def multiply():
    var.set(var.get() + "x")
def devide():
    var.set(var.get() + "/")

# 0 ~ 9
def b0():
    var.set(var.get() + 0)
def b1():
    var.set(var.get() + 1)
def b2():
    var.set(var.get() + 2)
def b3():
    var.set(var.get() + 3)
def b4():
    var.set(var.get() + 4)
def b5():
    var.set(var.get() + 5)
def b6():
    var.set(var.get() + 6)
def b7():
    var.set(var.get() + 7)
def b8():
    var.set(var.get() + 8)
def b9():
    var.set(var.get() + 9)


# 按鈕設定
# Style
ori = ttk.Style()
ori.configure('My.TButton', font=('Arial', 15))

# Lable值設定
var = tkinter.StringVar()
var.set(int(0))
my_lable = ttk.Label(win, textvariable=var,font=('Arial', 30), anchor=tkinter.E)

# C  <-  .  =
C = ttk.Button(win, text='C', style='My.TButton', command=C)
back = ttk.Button(win, text='<-', style='My.TButton', command=back)
dot = ttk.Button(win, text='.', style='My.TButton', command=dot)
equal = ttk.Button(win, text='=', style='My.TButton', command=equal)

# +  -  *  /
plus = ttk.Button(win, text='+', style='My.TButton', command=plus)
minus = ttk.Button(win, text='-', style='My.TButton', command=minus)
mutiply = ttk.Button(win, text='*', style='My.TButton', command=multiply)
devide = ttk.Button(win, text='/', style='My.TButton', command=devide)

# 0 ~ 9
btn1 = ttk.Button(win, text='1', style='My.TButton', command=b1)
btn2 = ttk.Button(win, text='2', style='My.TButton', command=b2)
btn3 = ttk.Button(win, text='3', style='My.TButton', command=b3)
btn4 = ttk.Button(win, text='4', style='My.TButton', command=b4)
btn5 = ttk.Button(win, text='5', style='My.TButton', command=b5)
btn6 = ttk.Button(win, text='6', style='My.TButton', command=b6)
btn7 = ttk.Button(win, text='7', style='My.TButton', command=b7)
btn8 = ttk.Button(win, text='8', style='My.TButton', command=b8)
btn9 = ttk.Button(win, text='9', style='My.TButton', command=b9)
btn0 = ttk.Button(win, text='0', style='My.TButton', command=b0)

win.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
win.columnconfigure((0, 1, 2, 3), weight=1)

# 無縫接合
my_lable.grid(row=0, column=0, rowspan=1, columnspan=4, sticky='EWNS', padx=(20))

C.grid(row=1, column=0, rowspan=1, columnspan=2, sticky='EWNS')
back.grid(row=1, column=2, rowspan=1, columnspan=1, sticky='EWNS')
dot.grid(row=5, column=1, rowspan=1, columnspan=1, sticky='EWNS')
equal.grid(row=5, column=2, rowspan=1, columnspan=1, sticky='EWNS')

plus.grid(row=4, column=3, rowspan=2, columnspan=1, sticky='EWNS')
minus.grid(row=3, column=3, rowspan=1, columnspan=1, sticky='EWNS')
mutiply.grid(row=2, column=3, rowspan=1, columnspan=1, sticky='EWNS')
devide.grid(row=1, column=3, rowspan=1, columnspan=1, sticky='EWNS')

btn1.grid(row=4, column=0, rowspan=1, columnspan=1, sticky='EWNS')
btn2.grid(row=4, column=1, rowspan=1, columnspan=1, sticky='EWNS')
btn3.grid(row=4, column=2, rowspan=1, columnspan=1, sticky='EWNS')
btn4.grid(row=3, column=0, rowspan=1, columnspan=1, sticky='EWNS')
btn5.grid(row=3, column=1, rowspan=1, columnspan=1, sticky='EWNS')
btn6.grid(row=3, column=2, rowspan=1, columnspan=1, sticky='EWNS')
btn7.grid(row=2, column=0, rowspan=1, columnspan=1, sticky='EWNS')
btn8.grid(row=2, column=1, rowspan=1, columnspan=1, sticky='EWNS')
btn9.grid(row=2, column=2, rowspan=1, columnspan=1, sticky='EWNS')
btn0.grid(row=5, column=0, rowspan=1, columnspan=1, sticky='EWNS')

win.mainloop()
