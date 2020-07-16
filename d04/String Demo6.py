report = '台積電目前價格每股315.5元,非常適合賣出4000股,目前我的庫存有6000股 '
# 求賣出後的庫存總值 = ?
sell = int(report[22:26])
have = int(report[35:39])
price = float(report[9:14])
nowhave = (have - sell) * price
print(nowhave)