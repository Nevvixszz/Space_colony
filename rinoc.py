def rinoc(self):
    if self.energy <= 0:
        print("У вас недостаточно энергии, идите спать")
    else:
        print("Здесь вы можете продать растения")
        idk = input("Введите название растения (яблоко, банан, картошка): ")
        if idk == "яблоко":
            if self.apples <= 0:
                print("У вас нет яблок!")
            else:
                self.price_apple = 300
                tata = int(input("Введите колво штук для продажи: "))
                if self.apples <= tata:
                    print("Недостаточно яблок!")
                else:
                    self.money += self.price_apple * tata
                    print("Вы успешно продали все яблоки")
                    self.apples -= tata
                    self.energy -= 1
        elif idk == "банан":
            if self.bananas <= 0:
                print("У вас нет бананов!")
            else:
                self.price_banana = 350
                tata = int(input("Введите колво штук для продажи: "))
                if self.bananas <= tata:
                    print("Недостаточно бананов!")
                else:
                    self.money += self.price_bananas * tata
                    print("Вы успешно продали все бананы!")
                    self.bananas -= tata
                    self.energy -= 1
        elif idk == "картошка":
            if self.potatos <= 0:
                print("У вас нет картошки!")
            else:
                self.price_potato = 200
                tata = int(input("Введите колво штук для продажи: "))
                if self.potatos <= tata:
                    print("Недостаточно картошки!")
                else:
                    self.money += self.price_potato * tata
                    print("Вы успешно продали всю картошку!")
                    self.potatos -= tata
                    self.energy -= 1
        else:
            print("Неверный ввод!")