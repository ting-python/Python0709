# 匿名函數

def max(n, m):
    if n > m:
        return n
    else:
        return m

def max2(n, m):
    return n if n > m else m

if __name__ == '__main__':
    a = max(10, 20)
    b = max2(30, 10)
    print(a, b)
    mymax = lambda n, m: n if n > m else m  # 無名稱
    print(mymax(40, 60))
