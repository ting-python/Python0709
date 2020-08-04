# 裝飾
def onion(func):
    print("洋蔥")
    return func

def hotdog(func):
    print("熱狗")
    return func

@hotdog
@onion
def bread():
    print("麵包")
    return

if __name__ == '__main__':
    bread()
