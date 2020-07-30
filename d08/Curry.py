# 內嵌函式
def calc(x):
    def add(y):
        return x + y
    return add

if __name__ == '__main__':
    print(calc(10)(20))
    #         (x) (y)

    ten = calc(10)  # x=10,得到 add函式,但還未呼叫 add
    print(ten(20))  # y=10,呼叫 add函式
