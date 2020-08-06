class Account:
    __money = 0

    # 初始金額(m)
    def __init__(self, m) -> None:
        self.__money = m

    # 帳戶餘額
    def __str__(self) -> str:
        return "帳戶餘額:" + str(self.__money)

    # 存款
    def save(self, m):
        self.__money += m

    #　提款
    def takeout(self, m):
        self.__money -= m

    # 轉帳
    def transfer(self, m, target):  # 多少錢/誰
        self.takeout(m)
        target.save(m)

    def getmoney(self):
        return self.__money