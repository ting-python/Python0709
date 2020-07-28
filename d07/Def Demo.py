def calc(x=1, y=2) -> int :   # 此自建函式只能回傳 int
    return x + y

def calc2(x=None, y=None) -> int :
    if x == None:
        print("使用者沒帶入x值")
        return 0
    if y == None:
        print("使用者沒帶入x值")
        return 0

if __name__ == '__main__':
    sum = calc(10, 20)
    print(sum)
    sum = calc()
    print(sum)
    sum = calc(7)
    print(sum)
    sum = calc(y=7)
    print(sum)

    sum = calc2()
    print(sum)