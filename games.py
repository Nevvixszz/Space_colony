import random

def igri(self):
    if self.energy == 0:
        print("У вас 0 энергии, пора спать")
    else:
        t = int(input("Введите название игры (1 - угадай число, 2 - задание на логику): "))
        if t == 1:
            c = int(input("Выбери сложность 1 или 2: "))
            if c == 1:
                one = random.randint(0,9)
                k = 1
                while True:
                    for i in range(1):
                        print("["+str(k)+"] Счетчик попыток")
                        k += 1
                    b = int(input("Введите число: "))
                    if b == one:
                        print("Вы победили!")
                        self.energy -= 1
                        self.money += 50
                        break
                    elif b <= one:
                        print("Число больше, введите число побольше")
                    else:
                        print("ЧИсло меньше, введите число поменьше")

            elif c == 2:
                two = random.randint(0, 9)
                three = random.randint(0, 9)
                char = two + three
                k = 1
                while True:
                    for i in range(1):
                        print("["+str(k)+"] Счетчик попыток")
                        k += 1
                    b = int(input("Введите число: "))
                    if b == char:
                        print("Вы победили!")
                        self.energy -= 1
                        self.money += 100
                        break
                    elif b <= char:
                        print("Число больше, введите число побольше")
                    else:
                        print("Число меньше, введите число поменьше")
        if t == 2:
            parted = ['неправильно', 'месяцы',
            'сны', 'спичка']
            ran = random.choice(parted)
            if ran == "неправильно":
                io = input("Какое слово пишется неправильно?: ")
                if io == "неправильно":
                    print("Да!")
                    self.energy -= 1
                    self.money += 70
                else:
                    print("Не верно! Попробуйте в следующий раз")
            elif ran == "месяцы":
                io = input("В каком месяце есть 28 дней?: ")
                if io == "Все":
                    print("Верно!")
                    self.energy -= 1
                    self.money += 65
                else:
                    print("Не верно!")
            elif ran == "сны":
                io = input("Что можно видеть с закрытыми гразами?: ")
                if io == "сны":
                    print("Верно!")
                    self.energy -= 1
                    self.money += 70
                else:
                    print("Не верно!")
            elif ran == "спичка":
                io = input("Можно ли зажечь обычную спичку под водой, чтобы она догорела до конца?: ")
                if io == "Да":
                    print("Верно! В подводной лодке!")
                    self.energy -= 1
                    self.money += 80
                else:
                    print("Не верно!")