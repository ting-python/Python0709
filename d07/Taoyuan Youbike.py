# 桃園市民權路6號經緯度(121.311989,24.940042)

import requests
import json
from math import radians, cos, sin, asin, sqrt

def printYoubikeBySbiAmount(amount, youbikes):
    rows = []
    for youbike in youbikes:
        if int(youbikes.get('sbi')) >= amount:
            rows.append(youbike)

        print(rows)

def getYoubikes() -> list:
    limit = 500
    path = 'https://data.tycg.gov.tw/api/v1/rest/datastore/a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f?format=json&limit=%d'
    path = path % limit
    data = requests.get(path).text  # 取得網路原始字串資料(data為str型態)
    dict = json.loads(data)  # 將json字串轉成python可用的物件(dict為dict型態)
    youbikes = dict.get('result').get('records') # youbikes為list型態
    return youbikes

def getYoubikeByName(sna, youbikes=None) -> dict:  # sna=站名
    if youbikes is None:
        youbikes = getYoubikes()

    for youbike in youbikes:
        if str(youbike.get('sna')).__contains__(sna): # 此sna為桃園火車站(前站)
            return youbike                            # 以桃園火車站(前站)尋找所需要的資料格

# 透過經緯度計算距離的方法
def haversine(lon1, lat1, lon2, lat2) -> int: # 經度1，緯度1，經度2，緯度2）
    # 轉弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # 半正矢 haversine 公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # 地球平均半徑(公里)
    return c * r * 1000 # 單位公尺


def printYoubikesByDistance(m, youbikes):
    for youbike in youbikes:
        if youbike.get('distance') <= m:
            print(youbike.get("sna"), youbike.get('distance'))

def appendDistance(lat, lng, youbikes):
    for youboke in youbikes:
        d = haversine(24.990042, 121.311989, float(youboke.get("lat")), float(youboke.get("lng")))
        youboke.setdefault("distance", d)



# 求桃園火車站(前站)資料格
if __name__ == '__main__':
    youbikes = getYoubikes()
    youboke = getYoubikeByName('桃園火車站(前站)')
    d = haversine(24.990042,121.311989, float(youboke.get("lat")),float(youboke.get("lng")))
    print(d, "公尺")
    print(youboke)
    # 加入距離資訊
    appendDistance(24.990042, 121.311989,youbikes)
    print(youbikes)

    printYoubikesByDistance(500, youbikes)
    # 一次可借35台youbike的站
    printYoubikeBySbiAmount(35, youbikes)