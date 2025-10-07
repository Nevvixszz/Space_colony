from sleep import sleep
from show import show
from teplica import teplica
from library import library
from games import igri
from buy import buy
from plants import _check_plant_growth, _check_plant_status
import os
import json
from datetime import datetime
from root import root
from rinoc import rinoc
class Space:
    def __init__(self):
        self.user = 0
        self.food = 100
        self.water = 100
        self.money = 1000
        self.pets = []
        self.energy = 10
        self.days = 0
        self.greenhouse = 0
        self.library = 0
        self.build = []
        self.apples = 0
        self.bananas = 0
        self.potatos = 0
        self.garden = {"Яблоко": self.apples, "Бананы": self.bananas, "Картошка": self.potatos}
        self.apple = 0
        self.banana = 0
        self.potato = 0
        self.planted = {
            "Яблоко":{"штук": 0, "plant_time": None, "growth_time": 140},
            "Бананы":{"штук": 0, "plant_time": None, "growth_time": 180},
            "Картошка":{"штук": 0, "plant_time": None, "growth_time": 100}
        }
        self.password_username = {"root": 12345}
    def save(self):
        if not os.path.exists("сохранения"):
            os.makedirs("сохранения")
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"сохранение_{timestamp}.json"
        filepath = os.path.join("сохранения", filename)
        planted_for_save = {}
        for plant_name, plant_data in self.planted.items():
            planted_for_save[plant_name] = {
                "штук": plant_data["штук"],
                "growth_time": plant_data["growth_time"],
                "plant_time": plant_data["plant_time"].isoformat() if plant_data["plant_time"] else None
            }      
        save_data = {
            "юзер": self.user,
            "еда": self.food,
            "вода": self.water,
            "денег": self.money,
            "питомцев": self.pets,
            "энергии": self.energy,
            "дней": self.days,
            "Теплица": self.greenhouse,
            "Лаборатория": self.library,
            "Строения": self.build,
            "Яблок": self.apples,
            "Бананы": self.bananas,
            "Картошка": self.potatos,
            "Яблок для посадки": self.apple,
            "Бананов для посадки": self.banana,
            "Картошки для посадки": self.potato,
            "Посаженных растений": planted_for_save
        }
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(save_data, f, ensure_ascii=False, indent=2)
        print("Игра сохранена в файл: ", filename)
        return filename
    def load(self, filename):
        try:
            if not os.path.dirname(filename):
                filename = os.path.join("сохранения", filename)
            with open(filename, 'r', encoding='utf-8') as f:
                save_data = json.load(f)
            self.user = save_data["юзер"]
            self.food = save_data["еда"]
            self.water = save_data["вода"]
            self.money = save_data["денег"]
            self.pets = save_data["питомцев"]
            self.energy = save_data["энергии"]
            self.days = save_data["дней"]
            self.greenhouse = save_data["Теплица"]
            self.library = save_data["Лаборатория"]
            self.build = save_data["Строения"]
            self.apples = save_data["Яблок"]
            self.bananas = save_data["Бананы"]
            self.potatos = save_data["Картошка"]
            self.apple = save_data["Яблок для посадки"]
            self.banana = save_data["Бананов для посадки"]
            self.potato = save_data["Картошки для посадки"]
            if "Посаженных растений" in save_data:
                planted_save_data = save_data["Посаженных растений"]
                for plant_name in ["Яблоко", "Бананы", "Картошка"]:
                    if plant_name in planted_save_data:
                        plant_data = planted_save_data[plant_name]
                        self.planted[plant_name]["штук"] = plant_data.get("штук", 0)
                        self.planted[plant_name]["growth_time"] = plant_data.get("growth_time", 140 if plant_name == "Яблоко" else 180 if plant_name == "Бананы" else 100)
                        if plant_data.get("plant_time"):
                            self.planted[plant_name]["plant_time"] = datetime.datetime.fromisoformat(plant_data["plant_time"])
                        else:
                            print("В сохранении нет данных о растениях!")
            print("Игра загружена из файла: ", filename)
            return True
        except Exception as error:
            print(f"Ошибка загрузки {error}")
            return False
    def list_saves(self):
        if not os.path.exists("сохранения"):
            print("Нет сохранений")
            return []
        saves = []
        print("Доступные сохранения: ")
        for i, filename in enumerate(os.listdir("сохранения")):
            if filename.endswith(".json"):
                saves.append(filename)
                filepath = os.path.join("сохранения", filename)
                file_time = os.path.getctime(filepath)
                time_str = datetime.fromtimestamp(file_time).strftime("%d.%m.%Y %H:%M")
                print(f"{i+1}, {filename} (создано {time_str})")
        return saves
    show = show
    sleep = sleep
    igri = igri
    teplica = teplica
    buy = buy
    library = library
    _check_plant_growth = _check_plant_growth
    _check_plant_status = _check_plant_status
    root = root
    rinoc = rinoc
def main():
    k = Space()
    print("Добро по жаловать в космическую игру!\nДоступные команды: buy show sleep build play save load_save рынок exit")
    while True:
        e = input("\nВведите команду: ").strip().lower()
        if e == "buy":
            k.buy()
        elif e == "show":
            k.show()
        elif e == "sleep":
            k.sleep()
        elif e == "build":
            kaka = input("Введите постройку: ")
            if kaka == "Теплица":
                k.teplica()
            elif kaka == "Лаборатория":
                k.library()
        elif e == "play":
            k.igri()
        elif e == "root":
            k.root()
        elif e == "рынок":
            k.rinoc()
        elif e == "exit":
            print("Выход из игры...")
            break
        elif e == "save":
            k.save()
        elif e == "load_save":
            saves = k.list_saves()
            if saves:
                try:
                    save_num = int(input("Введите номер сохранения: ")) - 1
                    if 0 <= save_num < len(saves):
                        save_path = os.path.join("сохранения", saves[save_num])
                        k.load(save_path)
                    else:
                        print("Неверный номер")
                except ValueError:
                    print("Введите число!")
        else:
            print("Неизвестная команда")

if __name__ == "__main__":
    main()
