# 自動將所有分數+10分
def add10(scores):
    for i in range(0,len(scores)):
        scores[i] += 10

# 針對單一分數+10
def add10_singleValue(s):
    global score     # 將score脫離區域變數
    score = s + 10

if  __name__ == '__main__':
    scores = [50,60,70]
    add10(scores)
    print(scores)

    score = 90       # main score
    add10_singleValue(score)
    print(score)