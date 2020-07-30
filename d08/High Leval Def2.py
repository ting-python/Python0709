# 函數中的函數
def plus(x):
    return x + 1

def minus(y):
    return y - 1

def main(func, n):
    if(n < 200):
        n = 200
    return func(n)

if __name__ == "__main__":
    print(main(plus, 50))
    print(main(plus, 250))
    print(main(minus, 70))
    print(main(minus, 270))
