class Bird:
    def move(self):
        print('我會飛')

class Penguin(Bird):  # 企鵝也是鳥哦
    def move(self):  # 複寫
        print("我不會飛, 我會走路和游泳")


if __name__ == '__main__':
    bird = Bird()
    bird.move()

    penguin = Penguin
    penguin.move()