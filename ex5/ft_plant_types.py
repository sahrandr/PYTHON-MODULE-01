#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        if height < 0:
            print(f"{name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = height

        if age < 0:
            print(f"{name}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age

    def grow(self):
        self._height += 0.8

    def age_up(self):
        self._age += 1

    def show(self):
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(
            f"Tree {self.name} now produces a shade of {self._height}cm long and {self.trunk_diameter}cm wide.")

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritionnal_value = 0

    def grow(self):
        super().grow()

    def age_up(self):
        super().age_up()
        self.nutritionnal_value += 1

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritionnal_value}")


def main():
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 15.0, 10, "red")
    print("=== Flower")
    rose.show()
    rose.bloom()
    rose.show()

    oak = Tree("Oak", 200.0, 365, 5.0)
    print("=== Tree")
    oak.show()
    oak.produce_shade()

    tomato = Vegetable("Tomato", 5.0, 10, "April")
    print("=== Vegetable")
    tomato.show()

    for i in range(20):
        tomato.grow()
        tomato.age_up()


if __name__ == "__main__":
    main()
