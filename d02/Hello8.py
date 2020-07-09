pen = 15
amount = 200
total = pen * amount
print(pen,amount,total)
print(pen,amount,total,sep="&")
print(pen,amount,total,sep=",")
#print('筆一支15元，200支總共是3000元')
print('筆一支'+str(pen)+'元，'+str(amount)+'支總共是'+str(total)+'元')
print('筆一支%d元，%d支總共是%d元' % (pen, amount,total))