import random as r
import time as t
ttt = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
def play():
    # 空棋盤
    for row in ttt:
        print(row)

    # 使用者先下
    n = int(input('請輸入位置(0~8):　'))
    ttt[n//3][n%3] = 'O'
    for row in ttt:
        print(row)

    print('電腦計算中...')
    t.sleep(2)

    # 換電腦下
    while True:
        n = r.randint(0, 8)
        if ttt[n//3][n%3] == ' ':
            ttt[n//3][n%3] = 'X'
            break
    play()

if __name__ == '__main__':
    play()