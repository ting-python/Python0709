import tkinter
import tkinter.ttk as ttk

win = tkinter.Tk()
win.title('計算機')

s = ttk.Style()
s.configure('My.TButton', font=('Arial', 15))

var = tkinter.StringVar()
var.set("")

def C():
    var.set(0)
def back():
    s = var.get()
    var.set(s[:len(s)-1])
def b3():
    pass
def b4():
    pass
def b5():
    pass
def b6():
    pass
def b7():
    pass
def b8():
    pass
def b9():
    pass
def b10():
    pass
def b11():
    pass
def b12():
    pass
def b13():
    pass
def b14():
    pass
def b15():
    pass
def b16():
    pass
def b17():
    pass
def b18():
    pass

my_lable = ttk.Label(win, textvariable=var, anchor=tkinter.E)
my_lable.config(font=('Arial', 30))

btn1 = ttk.Button(win, text='C', style='My.TButton', command=C)
back = ttk.Button(win, text='<-', style='My.TButton', command=back)
btn3 = ttk.Button(win, text='/', style='My.TButton', command=b3)
btn4 = ttk.Button(win, text='7', style='My.TButton', command=b4)
btn5 = ttk.Button(win, text='8', style='My.TButton', command=b5)
btn6 = ttk.Button(win, text='9', style='My.TButton', command=b6)
btn7 = ttk.Button(win, text='*', style='My.TButton', command=b7)
btn8 = ttk.Button(win, text='4', style='My.TButton', command=b8)
btn9 = ttk.Button(win, text='5', style='My.TButton', command=b9)
btn10 = ttk.Button(win, text='6', style='My.TButton', command=b10)
btn11 = ttk.Button(win, text='-', style='My.TButton', command=b11)
btn12 = ttk.Button(win, text='1', style='My.TButton', command=b12)
btn13 = ttk.Button(win, text='2', style='My.TButton', command=b13)
btn14 = ttk.Button(win, text='3', style='My.TButton', command=b14)
btn15 = ttk.Button(win, text='+', style='My.TButton', command=b15)
btn16 = ttk.Button(win, text='0', style='My.TButton', command=b16)
btn17 = ttk.Button(win, text='.', style='My.TButton', command=b17)
btn18 = ttk.Button(win, text='=', style='My.TButton', command=b18)

win.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
win.columnconfigure((0, 1, 2, 3), weight=1)

lable.grid(row=0, column=0, rowspan=1, columnspan=4, sticky='EWNS')

btn1.grid(row=1, column=0, rowspan=1, columnspan=2, sticky='EWNS')
btn2.grid(row=1, column=2, rowspan=1, columnspan=1, sticky='EWNS')
btn3.grid(row=1, column=3, rowspan=1, columnspan=1, sticky='EWNS')

btn4.grid(row=2, column=0, rowspan=1, columnspan=1, sticky='EWNS')
btn5.grid(row=2, column=1, rowspan=1, columnspan=1, sticky='EWNS')
btn6.grid(row=2, column=2, rowspan=1, columnspan=1, sticky='EWNS')
btn7.grid(row=2, column=3, rowspan=1, columnspan=1, sticky='EWNS')

btn8.grid(row=3, column=0, rowspan=1, columnspan=1, sticky='EWNS')
btn9.grid(row=3, column=1, rowspan=1, columnspan=1, sticky='EWNS')
btn10.grid(row=3, column=2, rowspan=1, columnspan=1, sticky='EWNS')
btn11.grid(row=3, column=3, rowspan=1, columnspan=1, sticky='EWNS')

btn12.grid(row=4, column=0, rowspan=1, columnspan=1, sticky='EWNS')
btn13.grid(row=4, column=1, rowspan=1, columnspan=1, sticky='EWNS')
btn14.grid(row=4, column=2, rowspan=1, columnspan=1, sticky='EWNS')
btn15.grid(row=4, column=3, rowspan=2, columnspan=1, sticky='EWNS')

btn16.grid(row=5, column=0, rowspan=1, columnspan=1, sticky='EWNS')
btn17.grid(row=5, column=1, rowspan=1, columnspan=1, sticky='EWNS')
btn18.grid(row=5, column=2, rowspan=1, columnspan=1, sticky='EWNS')

win.mainloop()
