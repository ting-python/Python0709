def calc(score):
    if score >=90:
        print("A")
    if 90>=score>=80:
        print("B")
    if 80>=score>=70:
        print("C")
    if 70>=score>=60:
        print("D")
    if 60>=score>=50:
        print("E")
    if score<50:
        print("E")

dict = {'level':lambda cin: calc(cin)}

if __name__ == '__main__':
    dict.get('level')(95)  # 得到A
    dict.get('level')(85)  # 得到B
    dict.get('level')(75)  # 得到B
    dict.get('level')(65)  # 得到D
    dict.get('level')(55)  # 得到E
    dict.get('level')(25)  # 得到E

