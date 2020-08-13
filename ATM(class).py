class Account:
    __money = 0  # (私有)物件屬性/變數/資產
    # __anything 為私有屬性,只能在class和def中使用

    def __init__(self, m) -> None:  # 建構式
        self.__money = m  #  開戶時所存的第一筆金額

    def transfer(self, who, m):  # 轉帳(給誰, 錢)
        print("轉帳給:" + who + "  " + "金額:" + str(m))
        if m <= 0:
            print("轉帳金額必須大於0")
            return
        if m > self.__money:
            print("餘額不足")
            return
        else:
            self.__money = self.__money - m

    def save(self, m):  # 存款(m為要存款金額)
        print("存款:" + str(m))
        if m <= 0:
            print("存款金額必須大於0")
            return
        else:
            self.__money = self.__money + m

    def withdraw(self, m):  # 提款(m表示要提款的金額)
        print("提款:" + str(m))
        if m <= 0:
            print("提款金額必須大於0")
            return
        if m > self.__money:
            print("餘額不足")
            return
        else:
            self.__money = self.__money - m

    def __str__(self) -> str:
        return "帳戶餘額:" + str(self.__money)

if __name__ == '__main__':
    account1 = Account(100000)  # 建立一個物件
    print(account1)

    account1.save(20000)  # 存款
    print(account1)

    account1.withdraw(30000)  # 提款
    print(account1)

    account1.withdraw(-60000)  # 防止作弊
    print(account1)

    account1.transfer('Mary', 9999)  # 轉帳
    print(account1)
