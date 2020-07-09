#隨機亂數
import random

a = random.randint(1,100)
print(a)

#樂透電腦選號
#四星彩 4個 0~9的組合，且數字可重複
n1 = random.randint(0,9)
n2 = random.randint(0,9)
n3 = random.randint(0,9)
n4 = random.randint(0,9)
print("四星彩電腦選號:",n1,n2,n3,n4)
