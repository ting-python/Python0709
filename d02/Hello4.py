#資料轉換
x = input("請輸入X:")
y = input("請輸入Y:")
print(x,y)
sum = x + y
print(sum)
#觀察XY的資料型態
print(x,type(x),y,type(y))
#經觀察結果發現XY皆為str字串
#所以要透過int(字串變數)進行字串轉數字的程序
sum = int(x) + int(y)
print(sum)
