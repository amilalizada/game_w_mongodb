import copy
import numpy as np

class Player:
    def __init__(self, name, max_health, max_energy, items=[]):
        self.name = name
        self.health = max_health
        self.max_health = max_health,
        self.energy = max_energy
        self.max_energy = max_energy
        self.items = copy.deepcopy(items)


    def attack(self, player):
        energy_cost = 5

        if self.energy >= energy_cost:
            attack_strength = np.random.randint(1, 6)
            player.health -= attack_strength
            self.energy -= energy_cost
            print(f"{self.name} attacked {player.name} for {attack_strength} damage")
        else:
            print(f"{self.name} does not have enough energy to attack {self.player}")


    def heal(self, amount):
        self.health += amount

        if self.health > self.max_health:
            self.health = self.max_health


    def stats(self):
        return vars(self)


    def use_items(self, item_name):
        try:
            item = next(item for item in self.items if item.name == item_name)
            item.quantity -= 1

            for effect in items.effects:
                for method, value in effect.items():
                    class_method = getattr(self, method)
                    class_method(value)
            if item.quantity == 0:
                self.items.remove(item)
        except:
            print(f"{self.name} does not have any {item_name}")


class Item:
    def __init__(self, name, quantity, effects=[]):
        self.name = name
        self.quantity = quantity
        self.effects = effects


    def __repr__(self):
        return f"Item(name={self.name}, quantity={self.quantity}, effects={self.effects})"


potion = Item("health", 2, [{"heal": 10}])

player1 = Player("player1", 50, 25, [potion])

player2_items = [Item("greater_healing_position", 2, [{"heal": 25}])]

player2 = Player("player2", 60, 35, player2_items)

player1.attack(player2)
