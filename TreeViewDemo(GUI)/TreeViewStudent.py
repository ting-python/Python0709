import tkinter
from tkinter import ttk

win = tkinter.Tk()

data1 = ['1', 'John']
data2 = ['2', 'Mary']
data3 = ['3', 'Helen']

tree = ttk.Treeview(win, columns=['1', '2'], show='headings')
tree.heading('1', text='ID')
tree.heading('2', text='Name')

tree.column('1', width=100, anchor='center')
tree.column('2', width=100, anchor='center')

tree.insert('', 'end', values=data1)
tree.insert('', 'end', values=data2)
tree.insert('', 'end', values=data3)
tree.grid()

tree.pack()

win.mainloop()