import tkinter
from tkinter import ttk

win = tkinter.Tk()

data1 = ['1', 'John', '男']
data2 = ['2', 'Mary', '女']

tree = ttk.Treeview(win, columns=['1', '2', '3'], show='headings')  # 表格
#                             ['序號', '姓名', '性別']

# 標題
tree.heading('1', text='序號')
tree.heading('2', text='姓名')
tree.heading('3', text='性別')

# 間隔
tree.column('1', width=100, anchor='center')  # anchor = 位置
tree.column('2', width=100, anchor='center')  # anchor = 位置
tree.column('3', width=100, anchor='center')  # anchor = 位置

# 插入
tree.insert('', 'end', values=data1)
tree.insert('', 'end', values=data2)

tree.grid()
tree.pack()

win.mainloop()
