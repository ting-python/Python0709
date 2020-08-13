class Human:
    name = ''
    age = 0
    sex = ''

    def __str__(self) -> str:  # 物件中的方法(需含self)
        return self.name + ', ' + str(self.age) + ', ' + self.sex


if __name__ == '__main__':
    h1 = Human()
    h1.name = 'Atom'
    h1.age = 16
    h1.sex = '男'

    h2 = Human()
    h2.name = 'Anita'
    h2.age = 15
    h2.sex = '女'

    print(h1, h2)