def inputNumber():
    try:
        x = int(input('請輸入數字'))
        print('您輸入的是', x)
    except Exception as e:  # 若輸入發生錯誤
        print('輸入錯誤, 錯誤原因', e)

if __name__ == '__main__':
    inputNumber()