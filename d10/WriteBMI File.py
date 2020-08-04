file = open('bmi.csv', 'w')
data = 'Bob, 168, 78'
file.writelines(data)  # 將資料寫入 bmi.csv