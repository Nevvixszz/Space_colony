def buy(self):
    self.lib = 3000
    self.wat = 100
    self.fod = 150
    self.pep = 500
    self.lib = 3000
    self.tep = 1500
    if self.energy == 0:
        print("У вас 0 энергии, пора спать")
    if self.money <= 0:
        print("У вас 0 рублей, сходите пофармиться в угадай число или задание на логику")
    else:
        while True:
            print("Магазин:\n вода 1ШТ 100р\n еда 1ШТ 150р\n человек 1ШТ 500р")
            print("Магазин строений:\n Лаборатория (3000р):\n + к созданию питомцев\n + к разработке улучшений\n - 5 воды каждый день ")
            print("Теплица (1500р):\n + к еде\n - к затрате энергии")
            print("Еда: Яблоко, Картошка, Бананы")
            a = input("Что желаете купить?")
            if a == "вода":
                self.money -= 100
                self.water += 50
                self.energy -= 1
            elif a == "еда":
                self.money -= 150
                self.food += 50
                self.energy -= 1
            elif a == "лаборатория":
                if self.money <= 3000:
                    print("Недостаточно денег")
                else:
                    if self.library == 1:
                        print("Лаборатория уже куплена!")
                    elif self.library == 2:
                        print("Лаборатория уже куплена!")
                    else:
                        self.library += 1
                        self.money -= 3000
                        self.build.append("Лаборатория")
                        self.energy -= 1
            elif a == "теплица":
                if self.money <= 1500:
                    print("Недостаточно денег")
                else:
                    if self.greenhouse == 1 or 2:
                        print("Теплица уже куплена!")
                    else:
                        self.greenhouse += 1
                        self.money -= 1500
                        self.build.append("Теплица")
                        self.energy -= 1
            elif a == "яблоко":
                if self.money <= 100:
                    print("Недостаточно денег! Нужно 100")
                else:
                    self.apple_touc = 100
                    touc = int(input("Введите колво штук яблок: "))
                    if self.money <= touc * self.apple_touc:
                        print("Недостаточно денег!")
                    else:
                        self.money -= touc * self.apple_touc
                        self.apple += touc
                        self.energy -= 1
                        print("Яблоки куплены!")
            elif a == "банан":
                if self.money <= 200:
                    print("Недостаточно денег! Нужно 200")
                else:
                    self.banana_touc = 200
                    touc = int(input("Введите колво штук бананов: "))
                    if self.money <= touc * self.banana_touc:
                        print("Недостаточно денег!")
                    else:
                        self.money -= touc * self.banana_touc
                        self.banana -= touc
                        self.energy -= 1
                        print("Бананы куплены!")
            elif a == "картошка":
                if self.money <= 70:
                    print("Недостаточно денег! Нужно 70")
                else:
                    self.potato_touc = 70
                    touc = int(input("Введите колво штук бананов: "))
                    if self.money <= touc * self.potato_touc:
                        print("Недостаточно денег!")
                    else:
                        self.money -= touc * self.potato_touc
                        self.potato += touc
                        self.energy -= 1
                        print("Картошка куплена!")
            break               
