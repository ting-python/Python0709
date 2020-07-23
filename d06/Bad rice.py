# 安裝外掛
# 按紅燈泡第一項 install下載
import requests
import json
path = "https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx"

# data 轉字串
data = requests.get(path).text # 取得網路原始字串資料

# json字串轉python可用的物件
list = json.loads(data)

for rice in list:
    name = str(rice.get('品名'))
    if name.__contains__("壽司"):
        print(name, "    ",rice.get('不合格原因'))