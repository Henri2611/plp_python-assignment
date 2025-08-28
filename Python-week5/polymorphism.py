class Animal:
    def move(self):
        return "This animal moves in some way."


class Dog(Animal):
    def move(self):
        return "The dog runs "


class Bird(Animal):
    def move(self):
        return "The bird flies "


class Fish(Animal):
    def move(self):
        return "The fish swims "


# Example usage (Polymorphism in action!)
animals = [Dog(), Bird(), Fish()]

for a in animals:
    print(a.move())
