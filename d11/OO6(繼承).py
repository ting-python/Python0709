# class - 繼承

class Human:  # father
    def __init__(self, name, age, sex) -> None:
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self) -> str:
        return 'name:%s, age:%d, sex:%s' % (self.name, self.age, self.sex)


class Student(Human):  # son
    def __init__(self, name, age, sex, number, grade) -> None:
        super().__init__(name, age, sex)  # 將 3項資料傳給father
        self.number = number  # 將 2項資料傳給son
        self.grade = grade

    def __str__(self) -> str:
        return super().__str__() + 'number:%d, grade:%s' % (self.number, self.grade)
        # return father(Human)的資料 + son(Student)的資料

if __name__ == '__main__':
    st = Student('John', 18, '男', 1, '一年級')
    print(st)
    print(st.name)  # 繼承了 father的 name

