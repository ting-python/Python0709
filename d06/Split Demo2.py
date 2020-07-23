data = '170,60&160,48'
# 試算出這兩筆 bmi 各是多少

for row in data.split("&"):
    print(row, type(row))
    r = row.split(",")
    bmi = '%.2f' % (float(r[1])/(float(r[0])/100)**2)
    print(bmi)
