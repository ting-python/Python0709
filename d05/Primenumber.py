# 如何判斷質數

def isprime(n):
    bool = True # 假設是質數
    for i in range(2, n//2+1):  # range = begin(含begin) ~ end(不含end)
        if n % i == 0:
            bool = False
            print('因數是' , i)
    return bool
if '__main__' == __name__:  # Python 的主程式
    for n in range(2,101):
        if isprime(n):
            print(n)
print(n , '是質數' if bool else '不是質數')