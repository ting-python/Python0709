def inputNumber():
    try:  # 若錯誤 -> expect / 若正確 -> 忽略 expect
        x = int(input('請輸入分子'))
        y = int(input('請輸入分母'))
        z = x / y

    except ValueError as e:
        print('錯誤類型:', e.__class__.__name__)
        print('您輸入的不是數字, 請重新輸入')
        inputNumber()

    except ZeroDivisionError as e:
        print('錯誤類型:', e.__class__.__name__)
        print('分母不可為0, 程式結束...')
        return

    except Exception as e:
        print('錯誤類型:', e.__class__.__name__)
        print('其他錯誤, 程式結束...')
        return

    else: # 若無錯誤才執行
        print(x, '/', y, '=', z)

    finally:  # 此行必定被執行(無視return&continue&break)
        print('我一定要執行')

if __name__ == '__main__':
    inputNumber()
