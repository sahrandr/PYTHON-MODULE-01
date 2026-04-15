#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

    def grow(self):
        self.height = self.height + 0.8

    def age_up(self):
        self.age = self.age + 1

rose = Plant("Rose", 25.0, 30)
oak = Plant("Oak", 200.0, 365)
cactus = Plant("Cactus", 5.0, 90)
sunflower = Plant("Sunflower", 80.0, 45)
fern = Plant("Fern", 15.0, 120)

plants = [rose, oak, cactus, sunflower, fern]

def main():
    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end=" ")
        plant.show()

if __name__ == "__main__":
    main()
