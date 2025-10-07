import random
def sleep(self):
    if self.energy == 0:
        print("Вы поспали, в результате вы восстановили энергию и настал новый день!")
        self.days += 1
        self.energy += 10
        self.information_food = random.randint(0, 22)
        self.food -= self.information_food
        print(f"За день у вас отнялось {self.information_food} еды")
        self._check_plant_growth()
        if 'Кот' in self.pets:
            self.money += 100
            self.food -= 10
        if self.greenhouse == 0:
            print()
        elif self.greenhouse == 1:
            fd = random.randint(0, 5)
            gd = random.randint(0, 3)
            answer = fd + gd
            self.food += answer
            print(f"Теплица принесла вам за ночь {answer} еды")
        elif self.greenhouse == 2:
            fd = random.randint(10, 20)
            gd = random.randint(10, 20)
            answer = fd + gd
            self.food += answer
            print(f"Теплица принесла вам за ночь {answer} еды")
    else:
        print("У вас еще осталась энергия. Пожалуйста, займитесь чем-то чтобы у вас не было энергии и вы смогли поспать")