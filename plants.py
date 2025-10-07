import datetime
def _check_plant_growth(self):
    current_time = datetime.datetime.now()
    
    for plant_name, plant_data in self.planted.items():
        if plant_data["plant_time"] and plant_data["штук"] > 0:
            if isinstance(plant_data["plant_time"], str):
                plant_time = datetime_datetime_fromisoformatat(plant_data["plant_time"])
            else:
                plant_time = plant_data["plant_time"]
            time_passed = (current_time - plant_data["plant_time"]).total_seconds()
            
            if time_passed >= plant_data["growth_time"]:
                if plant_name == "Яблоко":
                    harvest = plant_data["штук"] * 3 
                    self.apples += harvest
                    print(f"{plant_name} выросли! Собрано {harvest} еды!")
                elif plant_name == "Бананы":
                    harvest = plant_data["штук"] * 4
                    self.bananas += harvest
                    print(f"{plant_name} выросли! Собрано {harvest} еды!")
                elif plant_name == "Картошка":
                    harvest = plant_data["штук"] * 5
                    self.potatos += harvest
                    print(f"{plant_name} выросли! Собрано {harvest} еды!")
                plant_data["штук"] = 0
                plant_data["plant_time"] = None

def _check_plant_status(self):
    current_time = datetime.datetime.now()
    has_plants = False
    
    print("Статус растений")
    for plant_name, plant_data in self.planted.items():
        if plant_data["plant_time"] and plant_data["штук"] > 0:
            has_plants = True
            if isinstance(plant_data["plant_time"], str):
                plant_time = datetime.datetime.fromisoformat(plant_data["plant_time"])
            else:
                plant_time = plant_data["plant_time"]
            time_passed = (current_time - plant_data["plant_time"]).total_seconds()
            time_left = max(0, plant_data["growth_time"] - time_passed)
            
            if time_left > 0:
                print(f"{plant_name}: {plant_data['штук']} - осталось {int(time_left)} сек.")
            else:
                print(f"{plant_name}: {plant_data['штук']} - ГОТОВО к сбору!")
    
    if not has_plants:
        print("Нет посаженных растений")   