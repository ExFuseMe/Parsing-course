import random


class NPC():
    def Attack(self):
        if self.id == 1:
            unit_2.hp -= self.dmg
            print('Первый атакует, у противника осталось', unit_2.hp, 'hp')
        else:
            if self.accuracy >= random.randint(0, 100):
                unit_1.hp -= self.dmg
                print('Второй атакует, у противника осталось', unit_1.hp, 'hp')
            else:
                print("Второй промахнулся")
# different classes of npc's
class SimpleUnit(NPC):
    def __init__(self, id, power):
        self.id = id
        dmg_rating = 0.5
        self.armor = 100
        self.health = 100
        self.hp = self.health + self.armor
        self.dmg = power*dmg_rating

class Archer(NPC):
    def __init__(self,id, power):
        self.id = id
        self.health = 100
        self.armor = 75
        dmg_rating = 0.75
        self.accuracy = 90
        self.hp = self.health + self.armor
        self.dmg = power*dmg_rating


unit_1 = SimpleUnit(1, 100)
unit_2 = Archer(2, 100)

while True:
    if unit_1.hp <= 0:
        print('Выиграл юнит 2')
        break
    unit_1.Attack()
    if unit_2.hp <= 0:
        print('Выиграл юнит 1')
        break
    unit_2.Attack()