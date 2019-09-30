import random


class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        name = input("Enter the name of the ability: ")
        max_damage = int(input("What is its' max damage? "))
        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("Enter the name of this weapon: ")
        max_damage = int(input("What is its' max damage? "))
        return Weapon(name, max_damage)

    def create_armor(self):
        name = input("Enter the name of this Armor: ")
        max_block = int(input("What is its' max block power? "))
        return Armor(name, max_block)

    def create_hero(self):
        hero = Hero(input("Enter Hero's name: "))

        to_add_ability = input("Enter Y/N if you want to add ability: ").lower()
        while to_add_ability == 'y':
            hero.add_ability(self.create_ability())
            to_add_ability = input("Want to add another ability? Y/N: ").lower()

        print("-----------------------------------")

        to_add_weapon = input("Enter Y/N if you want to add weapon: ").lower()
        while to_add_weapon == 'y':
            hero.add_weapon(self.create_weapon())
            to_add_weapon = input("Want to add another weapon? Y/N: ").lower()

        print("-----------------------------------")

        to_add_armor = input("Enter Y/N if you want to add armor: ").lower()
        while to_add_armor == 'y':
            hero.add_armor(self.create_armor())
            to_add_armor = input("Want to add more armor? Y/N: ").lower()

        print("-----------------------------------")

        return hero

    def build_team_one(self):
        team = Team("Team 1")
        print("You are now building {}!".format(team.name))
        num_of_heros = input("How many heroes do you want to create for {}? ".format(team.name))
        print("-----------------------------------")
        for i in num_of_heros:
            print("Creating Hero {} for team {}!".format(i, team.name))
            team.add_hero(self.create_hero())

        self.team_one = team

    def build_team_two(self):
        team = Team("Team 2")
        print("You are now building {}!".format(team.name))
        num_of_heros = input("How many heroes do you want to create for {}? ".format(team.name))
        print("-----------------------------------")
        for i in num_of_heros:
            print("Creating Hero {} for team {}!".format(i, team.name))
            team.add_hero(self.create_hero())

        self.team_two = team

    def team_battle(self):
        print("{} is attacking {}....".format(self.team_one.name, self.team_two.name))
        self.team_one.attack(self.team_two)

    def show_stats(self):
        team1_kills = 0
        team1_deaths = 0
        team2_kills = 0
        team2_deaths = 0

        print("-----------------------------------")
        print("Stats for {}!".format(self.team_one.name))
        for hero in self.team_one.heroes:
            print("Hero: {} has {} kills and {} deaths and is {}!".format(hero.name, hero.kills, hero.deaths, hero.is_alive()[1]))
            team1_kills += hero.kills
            team1_deaths += hero.deaths

        if team1_deaths != 0:
            print("Kill/Death ratio for team {} is {}!".format(self.team_two.name, team1_kills / team1_deaths))
        else:
            print("Kill/Death ratio for team {} is {}!".format(self.team_two.name, team1_kills))

        print("-----------------------------------")
        print("Stats for {}!".format(self.team_two.name))
        for hero in self.team_two.heroes:
            print("Hero: {} has {} kills and {} deaths and is {}!".format(hero.name, hero.kills, hero.deaths, hero.is_alive()[1]))
            team2_kills += hero.kills
            team2_deaths += hero.deaths

        if team2_deaths != 0:
            print("Kill/Death ratio for team {} is {}!".format(self.team_two.name, team2_kills / team2_deaths))
        else:
            print("Kill/Death ratio for team {} is {}!".format(self.team_two.name, team2_kills))

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def attack(self, other_team):
        if len(self.heroes) == 0 or len(other_team.heroes) == 0:
            print("Not enough players on a team. Its a draw!")
            return

        while True:
            team1_random_hero = self.get_random_living_hero(self)
            team2_random_hero = self.get_random_living_hero(other_team)

            if team1_random_hero is None or team2_random_hero is None:
                break

            team1_random_hero.fight(team2_random_hero)

        if team1_random_hero is None:
            print("Team {} wins! ".format(other_team.name))
        else:
            print("Team {} wins! ".format(self.name))

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = health

    def stats(self):
        print("------------")
        print("Team {} Stats!!".format(self.name))
        print("------------")
        for hero in self.heroes:
            if(hero.deaths != 0):
                print("Hero {} has this ratio of kills to deaths: {}".format(hero.name, (hero.kills / hero.deaths)))
            else:
                print("Hero {} has this ratio of kills to deaths: {}".format(hero.name, hero.kills * 1.0))

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

    # Helper functions
    def get_random_living_hero(self, team):
        living_heroes = []
        for hero in team.heroes:
            if hero.is_alive()[0]:
                living_heroes.append(hero)

        if len(living_heroes) != 0:
            return living_heroes[random.randint(0, len(living_heroes) - 1)]
        else:
            return None

    def get_num_living_heroes(self, team):
        num_of_living_heroes = 0
        for hero in team.heroes:
            if hero.is_alive()[0]:
                num_of_living_heroes += 1

        return num_of_living_heroes

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

    def add_kills(self, num_kills):
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        self.deaths += num_deaths

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
        if self.current_health > 0:
            return True, "alive"
        else:
            return False, "dead"

    def fight(self, opponent):
        game_result = 0

        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            return game_result

        while True:
            opponent.take_damage(self.attack())
            # print("{} health: {}".format(self.name, self.current_health))
            # print("{} health: {}".format(opponent.name, opponent.current_health))
            if not opponent.is_alive()[0]:
                self.add_kills(1)
                opponent.add_deaths(1)
                return -1
            self.take_damage(opponent.attack())
            # print("{} health: {}".format(self.name, self.current_health))
            # print("{} health: {}".format(opponent.name, opponent.current_health))
            if not self.is_alive()[0]:
                self.add_deaths(1)
                opponent.add_kills(1)
                return 1

    def set_current_health(self, value):
        self.current_health = value

    def get_current_health(self):
        return self.current_health

    def add_weapon(self, weapon):
        self.abilities.append(weapon)


if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()


if __name__ == "__main_":
    ability1 = Ability("Coding Attack", 40)
    ability2 = Ability("Super Debugging", 50)
    ability3 = Ability("Fast typing", 70)
    ability4 = Ability("Good program design", 20)

    hero1 = Hero("Andrey", 200)
    hero2 = Hero("Jon", 200)
    hero3 = Hero("Youseff", 200)

    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero3.add_ability(ability1)

    # game_result = hero1.fight(hero2)
    #
    # if game_result == -1:
    #     print("{} won!".format(hero1.name))
    # elif game_result == 1:
    #     print("{} won!".format(hero2.name))
    # else:
    #     print("It was a tie!")

    team1 = Team("One")
    team1.add_hero(hero1)
    team1.add_hero(hero3)

    team2 = Team("Two")
    team2.add_hero(hero2)

    team1.view_all_heroes()
    team2.view_all_heroes()

    team1.attack(team2)

    team1.stats()
    team2.stats()
