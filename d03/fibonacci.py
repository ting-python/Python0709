# 求解費式數列第30項
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(30))

# 0,1,1,2,3,5,8,13,21,34......
