# 換錢
def usd(money):  # 美金
    return money / 30

def jpy(money):  # 日幣
    return money * 4

def exchange(func, money):
    money -= 100  # 手續費
    return func(money)

if __name__ == '__main__':
    print(exchange(jpy, 500))  # 日幣換台幣
    print(exchange(usd, 400))  # 美金換台幣
