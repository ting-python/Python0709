# 骰子比大小
# 決定比大(1) OR 比小(0)
import random as r
flag = int(input('比大(1) OR 比小(0): '))
user = r.randint(1,6) + r.randint(1,6) + r.randint(1,6)
pc = r.randint(1,6) + r.randint(1,6) + r.randint(1,6)
if flag == 1:
    winner = "玩家" if user>pc else "電腦"
    flag = "大"
else:
    winner = "玩家" if user<pc else "電腦"
    flag = "小"
result = " 比{0}, 玩家的點數:{1} 電腦的點數:{2} 贏家: {3}"\
    .format(flag, user, pc, winner)
print(result)