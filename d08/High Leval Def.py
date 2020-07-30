def plus(x):
    return x + 1
def minus(y):
    return y - 1
def calc(func, n):
    result = func(n)  # Ex: result = plus(5)
    return result     # return 5 + 1

if __name__ == "__main__":
    print(calc(plus, 5))
    print(calc(minus, 7))
