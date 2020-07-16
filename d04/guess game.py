import random
ans = random.randint(1,99)
min, max = 0,100
count = 10  # 最多猜 5 次
while count > 0:
    guess = int(input('請在%d ~ %d之間猜一數字: ' % (min,max)))
    count = count - 1
    if guess >= max or guess <= min:
        print("輸入範圍錯誤")
        count = count + 1
        continue
    elif guess > ans:
        max = guess
    elif guess < ans:
        min = guess
    else:
        print("恭喜答對!!!!!! \'-' ")
        break

    if count == 0:
        print("GAME OVER #-# ")
        print("Answer is %d" % (ans))

