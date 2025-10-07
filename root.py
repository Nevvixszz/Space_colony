def root(self):
    try:
        if self.user == 1:
            print("Вы в режиме администратора!")
        else:
            password = int(input("Введите пароль: "))
            if password == self.password_username["root"]:
                self.user += 1
                print("Вы вошли в режим root. helproot для просмотра команд")
            else:
                print("Неверный пароль!")
    except ValueError:
        print("Пароль должен быть из чисел")
    if self.user == 1:
        vail = input("Введите команду root: ")
        if vail == "helproot":
            print("Команды: money, builds")
        elif vail == "money":
            print("Деньги зачислены")
            self.money += 100000