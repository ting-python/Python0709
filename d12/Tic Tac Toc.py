# 井字遊戲
ttt = [['O','O','X'], ['X','O',' '], ['X',' ','X']]
#           [0]             [1]            [2]
for row in ttt:
    print(row)

print('_______________')
# 如何讓O贏
n = int(input('請輸入位置0~8: '))
ttt[n//3][n%7] = 'O'
ttt[2][1] = 'O'  # [2]的[1]
for row in ttt:
    print(row)

