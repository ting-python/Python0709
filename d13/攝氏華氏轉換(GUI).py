import tkinter
import tkinter.ttk as ttk

win = tkinter.Tk()
win.title('溫度轉換')
win.geometry("500x500")

def CtoF():
    c = int(my_Entryc.get())
    f = c * 9 / 5 + 32
    f_value.set(f)
    print("華氏溫度: ", f)

def FtoC():
    f = int(my_Entryf.get())
    c = (f-32) * 5 / 9
    c_value.set(c)
    print("攝氏溫度: ", c)

# Frame(攝氏)
framec = ttk.Frame(win)
framec.pack()

# Frame(華氏)
framef = ttk.Frame(win)
framef.pack()

# Label
my_Labelc = ttk.Label(framec, text='攝氏')
my_Labelf = ttk.Label(framef, text='華氏')

# Entry
c_value = tkinter.DoubleVar()
c_value.set(0)
f_value = tkinter.DoubleVar()
f_value.set(0)
my_Entryc = ttk.Entry(framec, textvariable=c_value)
my_Entryf = ttk.Entry(framef, textvariable=f_value)

# Button
my_Buttonc = ttk.Button(framec, text='轉換', command=CtoF)
my_Buttonf = ttk.Button(framef, text='轉換', command=FtoC)

my_Labelc.pack(side=tkinter.LEFT)
my_Entryc.pack(side=tkinter.LEFT)
my_Buttonc.pack(side=tkinter.LEFT)

my_Labelf.pack(side=tkinter.LEFT)
my_Entryf.pack(side=tkinter.LEFT)
my_Buttonf.pack(side=tkinter.LEFT)

My_label = ttk.Label(win, text="我好棒", font=("Arial", 50))
My_label.pack()

win.mainloop()