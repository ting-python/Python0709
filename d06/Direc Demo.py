# 字典資料格式
# {key:value}
fruits = {'orange':20 , 'apple':10 , 'watermelon':30}

# 利用 get(放入key值) 得到 value值
print("orange是",fruits.get('orange'),"元")

# setdefault(Key值, 預設值(若不存在)
print("banana是", fruits.setdefault('banana' ,70) , "元")
print(fruits)

# 取得所有 Key值
names = fruits.keys()
print(names, type(names))

# 取得逤有 value值
values = fruits.values()
print(values, type(values) ,sum(values))

