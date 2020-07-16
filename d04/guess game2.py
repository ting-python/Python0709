import random
import sys
ans = random.randint(1,100)
min, max = 0,100
while True:
    guess = int(input('請在%d ~ %d之間猜一數字: ' % (min,max)))
    if guess >= max or guess <= min:
        print("輸入範圍錯誤")
        continue
    elif guess > ans:
        max = guess
    elif guess < ans:
        min = guess
    else:
        print("恭喜答對!!!!!! (˙_˙) ")
        break

    print('在%d~%d之間猜一數字,按下ENTER讓電腦猜...... '% (min,max))
    sys.stdin.read(1)

    #電腦猜
    cpug = random.randint(min+1, max-1)
    if cpug > ans:
        max = cpug
        print("電腦猜%d"%(cpug))
    elif cpug < ans:
        min = cpug
        print("電腦猜%d"%(cpug))
    else:
        print("電腦勝利!!! ˇ-ˇ ")
        print("Answer is %d"%(ans))
        break
