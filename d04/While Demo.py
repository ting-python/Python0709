import random
while True:
    n = random.randint(1,100)
    # 3的倍數才要印出
    if n % 3 == 0:
        print(n)
    # 若 n = 11的倍數就停止
    if n % 11 == 0:
        break