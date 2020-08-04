from util import *    # 若有其他import則寫在__init__中即可

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def bmi(h, w):
    return w/(h/100)**2

def getRandomNum():
    return random.randint(1, 10)