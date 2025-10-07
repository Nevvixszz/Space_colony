def library(self):
    if p == "Лаборатория":
        if self.energy == 0:
            print("У вас 0 энергии, пора спать")
        if self.money <= 0:
            print("У вас 0 рублей, сходите пофармиться в угадай число или задание на логику")
        if self.library == 0:
            print('У вас нет лаборатории!')
        elif self.library == 2:
            self.cat = 2000
            self.robopes = 8000
            self.library_upgrade_money = 25000
        elif self.library == 3:
            self.cat = 1000
            self.robopes = 5000
        elif self.library == 1:
            self.cat = 3000
            self.robopes = 10000
            self.library_upgrade_money = 17000

        print("Добро пожаловать в лабораторию! Чем вы хотите заняться на сегодня?")
        print("Создать питомца, Улучшить строение, Повысить энергию")
        y = input("")
        if y == "Создать питомца":
            print("Cписок питомцев (чем больше цифра - тем лучше питомец):\n [1] Кот\n + добавляет деньги каждый день (100)\n - к затрате еды")
            print("[2] РобоПёс\n + х2 деньги от игр\n + к защите от мелких угроз\n - 1 энергии каждый день")
            i = int(input("Введите питомца: "))
            if i == 1:
                if self.money <= self.cat:
                    print(f"Недостаточно денег! Нужно {self.cat}")
                else:    
                    self.money -= self.cat
                    self.energy -= 3
                    self.pets.append("Кот")
            elif i == 2:
                if self.money <= self.robopes:
                    print(f"Недостаточно денег! Нужно {self.robopes}")
                else:
                    self.money -= self.robopes
                    self.energy -= 5
                    self.pets.append("РобоПёс")        
        elif y == "Повысить энергию":
            print("Улучшение энергии стоит 10000р. Да нет?")
            w = input("")
            if w == "Да":
                self.energy_upgrade += 10
                self.money -= 30000
            elif w == "Нет":
                print("OK")
        elif y == "Улучшить строение":
            if self.library == 3:
                print("Лаборатория на макс. уровне!")
            elif self.library == 1 or 2:
                hoi = input(f"Улучшение будет стоить {self.library_upgrade}. Да нет?")
                if hoi == "Да":
                    if self.money <= self.library_upgrade_money:
                        print("У вас недостаточно денег!")
                    else:
                        self.money -= self.library_upgrade_money
                        self.energy -= 1
                        self.library += 1
                        print("Лаборатория успешно улучшена!")