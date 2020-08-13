# add(+) sub(-) mul(*) div(/) mod(%) pow(**)

class Number:
    __n = 0

    def __init__(self, n) -> None:
        self.__n = n

    def __str__(self) -> str:
        return str(self.__n)

    def __add__(self, x):
        self.__n = self.__n + x

    def __pow__(self, power, modulo=None):
        self.__n = self.__n ** power

if __name__ == '__main__':
    n = Number(4)
    n + 10  # n = 10 + 4 = 14
    n ** 2  # n = 14 ** 2 = 196
    print(n)

