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

    def set_height(self, value):
        if value < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height uptade rejected")
        else:
            self._height = value
            print(f"Height uptaded: {int(value)}cm")

    def set_age(self, value):
        if value < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age uptade rejected")
        else:
            self._age = value
            print(f"Age uptaded: {value}cm")

    def get_height(self):
        return (self._height)

    def get_age(self):
        return (self._age)

    def show(self):
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")


def main():
    print("=== Garden Security System ===")
    plant = Plant("Rose", 5.0, 10)
    print(f"Plant created:", end=" ")
    plant.show()

    plant.set_height(25)
    plant.set_age(30)

    plant.set_height(-15)
    plant.set_age(-20)

    print("Current state:", end=" ")
    plant.show()

if __name__ == "__main__":
    main()
