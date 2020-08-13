class Engine:
    power = 0

    def __init__(self, power) -> None:
        self.power = power

    def __str__(self) -> str:
        return "Engine Power:%d  " % (self.power)

class Wheel:
    count = 0

    def __init__(self, count) -> None:
        super().__init__()
        self.count = count

    def __str__(self) -> str:
        return "Wheels count:%d  " %(self.count)

class Car(Engine, Wheel):
    name = ''

    def __init__(self, name, power, count) -> None:
        Engine.__init__(self, power)
        Wheel.__init__(self, count)
        self.name = name

    def __str__(self) -> str:
        return Engine.__str__(self) + Wheel.__str__(self) + 'Name:%s' % (self.name)


if __name__ == '__main__':
    car = Car('BMW', 5000, 4)
    print(car)
