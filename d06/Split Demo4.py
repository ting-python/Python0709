data = 'orange=10,apple=30,berry=20'
# 將字串轉為字典(dict)格式
fruits = dict(item.split("=") for item in data.split(","))
# 先將data用逗號分為三筆資料
# 再將3項data中資料轉為item
# 最後將item的三筆資料各自用=隔開 
print(fruits)
print(fruits.get("apple"))