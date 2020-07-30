# 泡沫排序法(由小到大)
rows = [{"age":10, "score":70},
        {"age":40, "score":100},
        {"age":30, "score":80}
        ]

for i in range(0, len(rows)-1):  # i為第一位數
    for j in range(i+1, len(rows)):  # j為i的下一位數
        x = rows[i]
        if rows[i].get("age")>rows[j].get("age"):
            rows[i] = rows[j]
            rows[j] = x


print(rows)