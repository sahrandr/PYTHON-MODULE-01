#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        self._stats = Plant.Stats()

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")
        self._stats.show += 1

    def grow(self):
        self.height += 0.8
        self._stats.grow += 1

    def age_up(self):
        self.age += 1
        self._stats.age += 1

    @staticmethod
    def is_older_than_year(age):
        return age > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    class Stats:
        def __init__(self):
            self.grow = 0
            self.age = 0
            self.show = 0

        def display(self):
            print(
                f"Stats: {self.grow} grow, {self.age} age, {self.show} show")


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
        self._shade = 0

    def produce_shade(self):
        print(
            f"Tree {self.name} now produces a shade of {self.height}cm long and {self.trunk_diameter}cm wide.")
        self._shade += 1

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self):
        super().bloom()
        self.seeds = 42

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")


def display_stats(plant):
    print(f"[statistics for {plant.name}]")
    plant._stats.display()

    if isinstance(plant, Tree):
        print(f"{plant._shade} shade")


def main():
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print("Is 30 days more than a year? ->", Plant.is_older_than_year(30))
    print("Is 400 days more than a year ->", Plant.is_older_than_year(400))
    rose = Flower("Rose", 15.0, 10, "red")
    print("=== Flower")
    rose.show()
    rose.bloom()
    rose.show()
    display_stats(rose)

    oak = Tree("Oak", 200.0, 365, 5.0)
    print("=== Tree")
    oak.show()
    oak.produce_shade()
    display_stats(oak)
    oak.produce_shade()
    display_stats(oak)

    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()

    for i in range(20):
        sunflower.grow()
        sunflower.age_up()

    sunflower.bloom()
    sunflower.show()

    display_stats(sunflower)

    unknown = Plant.create_anonymous()
    unknown.show()
    display_stats(unknown)


if __name__ == "__main__":
    main()
