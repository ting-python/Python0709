
users = [
            {'name':'John', 'h':170, 'w':60},
            {'name':'Mary', 'h':160, 'w':48}
        ]
# 計算每一筆 bmi
for user in users: # 依序將 users中的每一筆資料轉為 user
    h = user.get('h')
    w = user.get('w')
    bmi = "%.2f" % (w/((h/100)**2))
    print(user, type(user), bmi)






