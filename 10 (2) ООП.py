# import random
#
# class Tank:
#     '''Template of tanks'''
#
#     def __init__(self, model, armor, min_damage, max_damage, health):
#         self.model = model
#         self.armor = armor
#         self.damage = random.randint(min_damage, max_damage)
#         self.health = health
#
#     def print_info(self):
#         print(f'Командир, по экипажу {self.model} попали, у нас осталось {self.health} очков здоровья')
#
#     def health_down(self, enemy_damage):
#         self.health -= enemy_damage
#         print(f'\n{self.model}:')
#         print(f'Командир, по экипажу {self.model} попали, у нас осталось {self.health} очков здоровья')
#
#     def shot(self, enemy):
#         if enemy.health <= 0 or self.damage >= self.health:
#             self.health = 0
#             print(f'Экипаж танка {enemy.model} уничтожен')
#         else:
#             enemy.health_down(enemy.damage)
#             print(f'\n{self.model}:')
#             print(f'Точно в цель, у противника {enemy.model} осталось {enemy.health} едениц здоровья')
#
#
# class SuperTank(Tank):
#     '''Template of SuperTanks'''
#
#     def __init__(self, model, armor, min_damage, max_damage, health):
#         super().__init__(model, armor, min_damage, max_damage, health)
#         self.forceArmor = True
#
#     def health_down(self, enemy_damage):
#         super().health_down(enemy_damage / 2)
#
#
#
# tank1 = Tank('T-34', 90, 20, 30 ,100)
# tank2 = Tank('Tiger', 120, 10, 50, 120)
# tank3 = SuperTank('Rhino', 200, 50, 580, 300)
#
#
# tank1.print_info()
# tank2.print_info()
#
# tank3.shot(tank2)
# tank1.shot(tank2)
# tank1.shot(tank3)
# tank1.shot(tank2)
# tank2.shot(tank3)
# tank1.shot(tank2)
# tank1.shot(tank2)


# class A:
#     def one(self):
#         print(1)
#
#     def two(self):
#         print(2)
#
# class B(A):
#     def two(self):
#         print('two')
#
#     def three(self):
#         print(3)
#
# print('B')
# b = B()
# b.one()
# b.two()
# b.three()
#
# print('A')
# a = A()
# a.three()



import random

class user:
    def __init__(self, health ):
        self.health = health
    def attack(self, target):
        pass
    def take_damage(self, damage):
        self.health -= damage


class Magician(user):
    def __init__(self, health, mana):
        super().__init__(health)
        self.mana = mana

    def cast_spell(self, spell_name, target):
        if self.mana >= spell_name.mana_cost:
            spell_name.cast(target)
            self.mana -= spell_name.mana_cost
        else:
            print('Нет маны для атаки')


class Warrior(user):
    def __init__(self, health, strength):
        super().__init__(health)
        self.strength = strength
    def attack(self, target):
        damage = self.strength
        target.take_damage(damage)

class Archer(user):
    def __init__(self, health, dexterity):
        super().__init__(health)
        self.dexterity = dexterity

    def attack(self, target):
        damage = self.dexterity
        target.take_damage(damage)

hero_magician = Magician(350, 500)
hero_warrior = Warrior(450, 350)
hero_archer = Archer(400, 400)

