# 裝飾
def bread(func):
    print("麵包")
    return func

def hotdog():
    print("熱狗")

def egg():
    print("雞蛋")

def ham(func):
    print("火腿")
    return func

if __name__ == '__main__':
    b1 = bread(hotdog)
    b1()
    print('__________________')
    b2 = bread(ham(egg))
    b2()