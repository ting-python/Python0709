class Order:
    #  地區，國家，項目，銷售渠道，順序優先，訂購日期，訂單ID，發貨日期，已售出，單價，單位成本，總收入，總費用，總利潤
    def __init__(self, region, country,item,saleschannel,
                 orderpriority,orderdate,orderID,shipDate
                 ,unitsSold,unitPrice,unitCost,totalRevenue
                 ,totalCost,totalProfit) -> None:
        self.region	= region
        self.country = country
        self.itemType = item
        self.salesChannel = saleschannel
        self.orderpriority = orderpriority
        self.orderdate = orderdate
        self.orderID = orderID
        self.shipDate = shipDate
        self.unitsSold = unitsSold
        self.unitPrice = unitPrice
        self.unitCost = unitCost
        self.totalRevenue = totalRevenue
        self.totalCost = totalCost
        self.totalprofit = totalProfit

if __name__ == '__main__':
    # 匯入資料
    file = open('10000 Sales Records.csv', 'r')
    list = []
    for data in file.readlines():
        rows = data.split(",")
        if data.__contains__('Region'):
             continue
        ord = Order(rows[0],rows[1],rows[2],rows[3],rows[4],rows[5],rows[6],rows[7],rows[8],rows[9],rows[10],rows[11],rows[12],rows[13],)
        list.append(ord)

    # 列出物品種類
    for ord in list:
        if float(ord.totalRevenue) > 6000000:
            print(ord.itemType, ord.totalRevenue)
    print("__________________________________________________")

    # 將有台灣的資料印出來
    for ord in list:
        if ord.country == 'Taiwan':
            print(ord.country, ord.itemType, ord.totalRevenue )