import sys
import ATM.Account as act
# 主程式
act1 = act.Account(10000)  # 初始金額(m)
act2 = act.Account(10000)
act3 = act.Account(10000)
list = [{"John": act1}, {"Mary": act2}, {"Atom": act3}]

# 列出所有人的帳戶餘額(1.)
def displayLeft():
    for act in list:  # act = {"John": act1}, {"Mary": act2}, {"Tom": act3}
        for key in act.keys():  # 抓act中的keys(ex:"John", "Mary"...)
            print(key, act.get(key))  # print(keys中的 key(ex:"John"), act.get("John"))

# 存款(2.)
def save():
    actName = input('請輸入存款人')
    money = int(input("請輸入存款金額"))
    # 得到存款人的act1/2/3
    account = None
    for act in list:
        for key in act.keys():
            if key == actName:
                account = act.get(key)
    if account == None:
        print('查無此人')
    else:
        account.save(money)  # 此處money為另一頁的"m"

# 提款(3.)
def takeout():
    actName = input('請輸入提款人')
    money = int(input("請輸入提款金額"))
    # 得到提款人的act1/2/3
    account = None
    for act in list:
        for key in act.keys():
            if key == actName:
                account = act.get(key)
    if account == None:
        print('查無此人')
    else:
        account.takeout(money)  # 此處money為另一頁的"m"

# 轉帳(4.)
def transfer():
    fromname = input('請輸入轉帳人:')  # fromname = 轉帳人
    target = input('請輸入被轉帳人:')  # target = 被轉帳人
    m = int(input('請輸入轉帳金額'))
    fromAccount = None
    targetAccount = None
    for act in list:
        for key in act.keys():
            if key == fromname:
                fromAccount = act.get(key)
            if key == target:
                targetAccount = act.get(key)
    if fromAccount == None or targetAccount == None:
        print('查無此人')
    else:
        fromAccount.transfer(m, targetAccount)

# 開戶(5.)
def createAccount():
    accountName = input('請輸入開戶人名稱')
    m = int(input('請輸入開戶金額'))
    account = act.Account(m)
    dict = {accountName: account}
    list.append(dict)  # 將dict加入list列表

# 解約(6.)
def cancleAccount():
    cancleDict = None
    cancleName = input("請輸入解約人")
    for dict in list:
        for key in dict.keys():
            if key == cancleName:
                cancleDict = dict
    if cancleDict == None:
        print("查無此人")
    else:
        list.remove(cancleDict)  # 將被解約人從list中去除
        cancleAccount = cancleDict.get(cancleName)
        print('解約人資料:' + cancleName + ",解約金額:" + str(cancleAccount.getmoney()))
# 系統選單
while True:
    print('系統選單')
    print('__________')
    print('1. 列出所有帳戶餘額')
    print('2. 存款')
    print('3. 提款')
    print('4. 轉帳')
    print('5. 開戶')
    print('6. 解約')
    print('9. 離開')
    print('__________')
    no = int(input('請選擇(1~5): '))
    if no == 1:
        displayLeft()
        print("按下Enter繼續...")
        sys.stdin.read(1)
    elif no == 2:
        save()
        print("按下Enter繼續...")
        sys.stdin.read(1)
    elif no == 3:
        takeout()
        pass
    elif no == 4:
        transfer()
        print("按下Enter繼續...")
        sys.stdin.read(1)
    elif no == 5:
        createAccount()
        print("按下Enter繼續...")
        sys.stdin.read(1)
    elif no == 6:
        cancleAccount()
        print("按下Enter繼續...")
        sys.stdin.read(1)
    elif no == 9:
        break

print("謝謝您的使用")