# 加法的方法
def add(x, y):
    print("執行到add()方法")
    result = x+y
    return result

# 訊息說明方法
def info():
    print("執行到 info() 方法")
    print("本程式是由 Python 所撰寫")
    return # 可加可不加

# 判斷性別
# A155556666
def checksex(id):
    sex = id[1]  #sex = 第一個字(A = 0)
    if sex == '1':
        print("男性")
    if sex == '2':
        print("女性")
    return

# 主程式
sum = add(10,20)
print(sum)
info()
checksex('A233334444')
