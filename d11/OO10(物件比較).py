class Drink:
    def __init__(self, name, amount, price) -> None:
        self.name = name
        self.amount = amount
        self.price = price

    def __lt__(self, other):  # 小於
        return self.price / self.amount < other.price / other.amount

    def __gt__(self, other):  # 大於
        return self.price / self.amount > other.price / other.amount
if __name__ == '__main__':
    milk = Drink('牛奶', 2, 80)
    coffee = Drink('咖啡', 3, 110)
    print(coffee < milk)  # 咖啡比牛奶便宜嗎?

    cheapName = coffee.name if coffee < milk else milk.name  # 取得較便宜的飲料名稱
    print('便宜的是' + cheapName)

    expensiveName = coffee.name if coffee > milk else milk.name
    print('貴的是' + expensiveName)