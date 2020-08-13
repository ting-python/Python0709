class BMI:
    h = 0
    w = 0
    __bmi = 0

    def __init__(self, h ,w) -> None:
        self.h = h
        self.w = w
        self.__bmi = w/(h/100)**2

    def getBMI(self):
        return self.__bmi

    def __str__(self) -> str:
        return "h: %d w: %d bmi: %.2f" % (self.h, self.w, self.__bmi)

if __name__ == '__main__':
    b = BMI(170, 60)
    print(b.getBMI())
    print(b)
