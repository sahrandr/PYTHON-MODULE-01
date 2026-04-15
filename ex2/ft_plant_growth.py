#!/usr/bin/env python3

class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age_up = age

	def show(self):
		print(f"{self.name}: {self.height:.1f}cm, {self.age_up} days old")

	def grow(self):
		self.height = self.height + 0.8

	def age(self):
		self.age_up = self.age_up + 1

def main():
    print("=== Garden Plant Growth ===")

    plant = Plant("Rose", 25.0, 30)

    initial_height = plant.height

    plant.show()

    for i in range(1, 8):
        print(f"===Day {i}===")
        plant.grow()
        plant.age()
        plant.show()
    growth = plant.height - initial_height
    print(f"Growth this week: {round(growth, 1)}cm")

if __name__ == "__main__":
	main()
