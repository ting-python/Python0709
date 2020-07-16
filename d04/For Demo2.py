scores = [100,90,80,70,60] # 數組
for i in range(0, len(scores)):
    print(scores[i])

#求總分
sum = 0
for i in range(0, len(scores)):
    sum = scores[i] + sum
print("總分 = %d" % sum )

#求平均
avg = sum/len(scores)
print("平均 = %.1f" % avg)