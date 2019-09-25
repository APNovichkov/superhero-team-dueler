import random

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name_of_hero_to_remove):
        is_hero_found = False
        for hero in self.heroes:
            if name_of_hero_to_remove == hero.name:
                self.heroes.remove(hero)
                is_hero_found = True
                return
        return is_hero_found

    def view_all_heroes(self):
        print("All heroes on team: {}".format(self.name))
        index = 1
        for hero in self.heroes:
            print("Hero {}: {}".format(index, hero.name))

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        return random.randint(0, self.max_damage)

class Weapon(Ability):
    def attack(self):
        return random.randint(0, 1) * self.max_damage / 2 + self.max_damage / 2


class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)


class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.abilities = []
        self.armors = []
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    def add_kill():
        self.kills += 1


    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_attack_strength = 0
        for ability in self.abilities:
            total_attack_strength += ability.attack()

        return total_attack_strength

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, damage):
        total_defending_strength = 0
        for armor in self.armors:
            total_defending_strength += armor.block()
        return damage - total_defending_strength

    def take_damage(self, damage):
        damage_taken = self.defend(damage)
        if damage_taken > 0:
            self.current_health = self.current_health - damage_taken

    def is_alive(self):
        return (self.current_health > 0)

    def fight(self, opponent):
        game_result = 0

        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            return game_result

        while True:
            opponent.take_damage(self.attack())
            # print("{} health: {}".format(self.name, self.current_health))
            # print("{} health: {}".format(opponent.name, opponent.current_health))
            if not opponent.is_alive():
                return -1
            self.take_damage(opponent.attack())
            # print("{} health: {}".format(self.name, self.current_health))
            # print("{} health: {}".format(opponent.name, opponent.current_health))
            if not self.is_alive():
                return 1

    def set_current_health(self, value):
        self.current_health = value

    def get_current_health(self):
        return self.current_health


if __name__ == "__main__":
    ability1 = Ability("Coding Attack", 40)
    ability2 = Ability("Super Debugging", 50)
    ability3 = Ability("Fast typing", 70)
    ability4 = Ability("Good program design", 20)

    hero1 = Hero("Andrey", 200)
    hero2 = Hero("Jon", 200)

    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)

    game_result = hero1.fight(hero2)

    if game_result == -1:
        print("{} won!".format(hero1.name))
    elif game_result == 1:
        print("{} won!".format(hero2.name))
    else:
        print("It was a tie!")

    team = Team("One")
    team.add_hero(hero1)
    team.add_hero(hero2)

    team.view_all_heroes()
