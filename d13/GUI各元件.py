import tkinter
import tkinter.ttk as ttk
win = tkinter.Tk()


# GUI 視窗
win.title('GUI元件視窗')  # 視窗標題
win.geometry("300x300")  # 視窗大小

s = ttk.Style()
s.configure('MY.TButton', font=('Arial', 20))

# GUI 元件配置
# 標籤 label
my_label = ttk.Label(win, text="我是標籤", font=("Arial", 20))
my_label.pack()  # pack() = 放置元件

# 按鈕 Button
my_Button = ttk.Button(win, text="我是按鈕", style='My.TButton')
my_Button.pack()

# 按鈕 CheckButton(複選)
my_CheckButton = ttk.Checkbutton(win, text="我同意上述條款")
my_CheckButton.pack()

# 窗框 Frame
my_Frame = ttk.Frame(win)
my_Frame.pack()
# 按鈕 RadioButton(多選一) / 按鈕組合 Frame
m_RadioButton = ttk.Radiobutton(my_Frame, text="男", value=1)
w_RadioButton = ttk.Radiobutton(my_Frame, text="女", value=2)
m_RadioButton.pack(side=tkinter.LEFT)  # 男左女右
w_RadioButton.pack(side=tkinter.RIGHT)

# 輸入框 Entry
my_entry = ttk.Entry(win)
my_entry.pack()

# 下拉選單 Combobox
values = ['Python', 'Java', 'C']
my_combobox = ttk.Combobox(win, value=values)
my_combobox.pack()

win.mainloop()  # 視窗運行
