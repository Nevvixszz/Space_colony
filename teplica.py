import time
import datetime
from plants import _check_plant_growth, _check_plant_status
def teplica(self):
    if self.greenhouse == 0:
        print("У вас нет теплицы!")
    elif self.greenhouse == 1 or 2:
        self._check_plant_status()
        print("Добро пожаловать в теплицу! Что вы хотите сделать?")
        teplic = input("Введите команду для теплицы: (Улучшить, посадить растения, проверить растения)")
        if teplic == "Улучшить":
            if self.money <= 15000:
                print("У вас недостаточно денег, надо минимум 15000")
            else:
                if self.greenhouse == 1:
                    self.teplica = 15000
                    yay = input(f"Стоимость будет стоить {self.teplica}. Вы точно хотите улучшить теплицу?: ")
                    if yay == "да":
                        self.greenhouse += 1
                        print(f"Теплица успешно улучшена до уровня {self.greenhouse}!")
                        self.money -= self.teplica
                    else:
                        print("Ок")
                elif self.greenhouse == 2:
                    self.teplica = 25000
                    yay = input(f"Стоимость будет стоить {self.teplica}. Вы точно хотите улучшить теплицу?: ")
                    if yay == "да":
                        if self.money <= 25000:
                            print("У вас недостаточно денег. Сходите пофармиться в играх")
                        else:
                            self.greenhouse += 1
                            print(f"Теплица успешно улучшена до уровня {self.greenhouse}!")
                            self.money -= self.teplica
                    else:
                        print("Ок")
        elif teplic == "посадить растения":
            if self.energy <= 0:
                print("У вас недостаточно энергии, идите спать")
            if self.apple and self.potato and self.banana == 0:
                print("У вас еще нет ни одного растения! Вы можете купить растения в магазине")
            else:
                print(f"Список растений:\nКартошка: {self.potato}, Бананы: {self.banana}, Яблок: {self.apple}")
                lol = input("Введите что вы хотите посадить (Яблоко, бананы, картошка) или собрать/проверить растения: ")
                if lol == "яблоко":
                    if self.apple == 0:
                        print("У вас нет яблок!")
                    else:
                        self.planted["Яблоко"]["штук"] += 1
                        self.planted["Яблоко"]["plant_time"] = datetime.datetime.now()
                        self.apples += 1
                        self.apple -= 1
                        self.energy -= 1
                        print("Яблоко успешно посажено!")
                        print("Ждите примерно 140 секунд...")
                elif lol == "бананы":
                    if self.banana == 0:
                        print("У вас нет бананов!")
                    else:
                        self.planted["Бананы"]["штук"] += 1
                        self.planted["Бананы"]["plant_time"] = datetime.datetime.now()
                        self.bananas += 1
                        self.energy -= 1
                        self.banana -= 1
                        print("Банан успешно посажен!")
                        print("Ждите примерно 180 секунд...")
                elif lol == "картошка":
                    if self.potato == 0:
                        print("У вас нет картошки!")
                    else:
                        self.planted["Картошка"]["штук"] += 1
                        self.planted["Картошка"]["plant_time"] = datetime.datetime.now()
                        self.potatos += 1
                        self.energy -= 1
                        self.potato -= 1
                        print("Картошка успешно посажена!")
                        print("Ждите примерно 100 секунд...")
                else:
                    print("Неверное название растения!")
        elif teplic == "проверить растения":
            self._check_plant_status()
        elif teplic == "собрать растения":
            self._check_plant_growth()