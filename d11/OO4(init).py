class BMI:
    name = ''
    h = 0
    w = 0
    __bmi = 0

    def __init__(self, name, h ,w) -> None:
        self.name = name
        self.h = h
        self.w = w
        self.__bmi = w/(h/100)**2

    def getBMI(self):
        return self.__bmi

    def __str__(self) -> str:
        return "%s h: %d w: %d bmi: %.2f" % (self.name, self.h, self.w, self.__bmi)

if __name__ == '__main__':
    file = open('student.txt', 'r')
    list = []
    for student in file.readlines():
        rows = student.split(",")
        name = rows[0].strip()
        h = float(rows[1].strip())  # strip() 去除空白
        w = float(rows[2].strip())
        b = BMI(name, h, w)
        list.append(b)
    for bmi in list:
        print(bmi)
