report = '台積電目前價格每股300元,非常適合買進'
amount = 1000 # 想買 1000股(1張)
price = report[9:12]
print(price)
cost = amount * int(price) # 請算出買進成本
print(cost)