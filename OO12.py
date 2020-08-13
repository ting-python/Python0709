class USD:  # 換美金
    def __get__(self, instance, owner):  # instance = Exchange
        money = instance.money
        return money / 30

class JPY:  # 換日幣
    def __get__(self, instance, owner):  # instance = Exchange
        money = instance.money
        return money * 3

class CNY:  # 換人民幣
    def __get__(self, instance, owner):  # instance = Exchange
        money = instance.money
        return money / 5

class Exchange:
    def __init__(self, money) -> None:
        self.money = money

    usd = USD()
    jpy = JPY()
    cny = CNY()

if __name__ == '__main__':
    ex = Exchange(10000)
    print(ex.usd)
    print(ex.jpy)
    print(ex.cny)
