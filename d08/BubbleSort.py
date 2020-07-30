# 泡沫排序法(由小到大)
rows = [8, 3, 5, 7, 2]
#      [0, 1, 2, 3, 4]

for i in range(0, len(rows)): # i為第一位數
    for j in range(i+1, len(rows)): # j為i的下一位數
        x = rows[i]
        if rows[i]>rows[j]:
            rows[i] = rows[j]
            rows[j] = x


print(rows)