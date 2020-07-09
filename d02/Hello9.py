# 撰寫一個BMI系統
# 可以輸人名，身高cm，體重kg
# 系統會算出 BMI結果是否正常，過高，過低
# 資料呈現: 小明的身高170cm 體重60kg BMI計算結果為20.76 (正常)
print("BMI 系統")
n=str(input("請輸入名字:"))
h=float(input("請輸入身高:"))
w=float(input("請輸入體重:"))
BMI=w/((h/100)**2)
result = "正常" if 18 < BMI <=23 else "過高" if BMI>23 else "過低"
print('%s 的身高是 %5.1f cm 體重是 %5.1f kg BMI計算結果為 %5.2f (%s)' %(n, h ,w ,BMI, result))