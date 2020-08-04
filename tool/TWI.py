def getTWIIList():
    file = open('../tool/BWIBBU_d_ALL_20200804.csv')  # 從tool中抓取資料
    data = file.readlines()

    list = []  # 用來存放已整理好的資料
    # 證券代號,證券名稱,殖利率(%),股利年度,本益比,股價淨值比,財報年/季,
    for row in data:
        row = row.replace("\n", "")  # 將\n拿掉
        row = row.replace("\"", "")  # 將雙引號拿掉
        array = row.split(",")
        if len(array) == 8 and array[0] != "證券代號" :   # 抓取只有8筆資料者
            dict = {}   # 存放每一筆紀錄
            dict.setdefault("證券代號",array[0])  # {"證券代號":1101}
            dict.setdefault("證券名稱", array[1])
            dict.setdefault("殖利率", float(array[2]) if array[4] != "-" else -1)
            dict.setdefault("股利年度", array[3])
            dict.setdefault("本益比", float(array[4]) if array[4] != "-" else -1)
            dict.setdefault("股價淨值比", float(array[5]))
            dict.setdefault("財報年季", array[6])
            list.append(dict)  # 加入到 list
    return list

# pb=股價淨值比 pe=本益比 dy=殖利率
def analysys(pe, dy, pb):
    rows = getTWIIList()
    '''
    本益比 : 股價多久可還本
    殖利率 : 每股股息（現金股利）除以每股股價 -> 有定存概念股的含意
    股價淨值比 : "<1" -> 股價低估(適合買進) / ">1" -> 股價高估(適合賣出)
                [股價 ÷ 每股淨值]
    '''
    list = []
    for row in rows:
        if row.get('本益比') < pe and \
                row.get('殖利率') > dy and \
                row.get('股價淨值比') < pb:
            list.append(row)
    return list

# 根據證券名稱放取的該筆資料
def GetProductByName(name):
    rows = getTWIIList()
    for row in rows:  # 不斷執行直到證券名稱=name
        if row.get('證券名稱') == name:
            return row
    return None