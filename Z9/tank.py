# all data were took from https://wiki.warthunder.ru/
import os
class Tank():
    def __init__(self,id, name, level, country, year, crew, gears, weight, speed):
        self.id = id
        self.name = name
        self.level = level
        self.country = country
        self.year = year
        self.crew = crew
        self.gears = gears
        self.weight = weight
        self.speed = speed
    def GetStats(self):
        return {"Tank's name":self.name,
        "Battle rating in game":self.level, 
        "Country producer": self.country, 
        "start of production": self.year, 
        "Tank's crew": self.crew, 
        "Tank's number of gears": self.gears, 
        "Weight": self.weight, 
        "Max speed": self.speed}
    def Shoot(self):
        # with random tanks
        if self.level > int(input("What is enemy's LEVEL?\n")):
            return 'Enemy was destroyed'
        else:
            return 'Ricoshet'
    def Protection(self):
        # with random tanks
        if self.level > int(input("What is enemy's LEVEL?\n")):
            return 'Ricoshet'
        else:
            return 'We were destroyed'
    def Battle(self, level1, level2):
        # with tanks from data
        if level1 > level2:
            return 0
        elif level1 == level2:
            return 1
        else:
            return 2
if os.name == 'nt':
    os.system('cls')
T34 = Tank(1, 'T34', 3.3,'Soviet Union', 1940, 4, 4, 25.6, 55)
Pz3 = Tank(2, 'Pz.IV E', 2.3, 'German', 1941, 5, 6, 21.0, 48)
M4 = Tank(3, 'M4', 3.7, 'USA', 1942, 5, 5, 30.6, 43)
data = [T34, Pz3, M4]

class Country(Tank):
    global data
    def __init__(self, name):
        self.name = name
        self.tanks = []
        for el in data:
            if el.country == self.name:
                self.tanks.append(el.name)
    def GetTanks(self):
        return self.tanks
choice = int(input("1.Battle with tanks from data\n2.Get info by id\n3.Shoot to enemy\n4.Enemy shoots to our tank\n"))
os.system('cls')
if choice == 1:
    print(' T34 - 1\n Pz3 - 2\n M4 - 3')
    id1 = int(input('Write 1st tank id'))
    id2 = int(input('write 2nd tank id'))
    for el in data:
        if el.id == id1:
            for k in data:
                if k.id == id2:
                    if el.Battle(el.level, k.level) == 0:
                        print(el.name,'wins')
                    elif el.Battle(el.level, k.level) == 2:
                        print(k.name,'wins')
                    else:
                        print('Draw')
elif choice == 2:
    id = int(input('Write id 1-3'))
    for el in data:
        if el.id == id:
            print(el.GetStats())
elif choice == 3:
    id = int(input('Write id 1-3'))
    for el in data:
        if el.id == id:
            print(el.Shoot())
elif choice == 4:
    id = int(input('Write id 1-3'))
    for el in data:
        if el.id == id:
            print(el.Protection())
