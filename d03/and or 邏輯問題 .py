a = True
b = False
c = True
print(a and b) #a,b之中只要其一為False則結果為False
print(a and c) #a,c兩者皆為True則結果為True
print(a or b) #a,b兩者其一為True則結果為True
print(b or c) #b,c兩者其一為True則結果為True

print("----------")

score = 70
print(score >= 60 and score % 2 == 0)
print(score >= 60 and score % 2 == 1)
print(score >= 60 or score % 2 == 1 and score % 2 == 0)
print(score >= 60 and score % 2 == 1 or score % 2 == 0)