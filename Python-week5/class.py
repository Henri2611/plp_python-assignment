# Base Class
class Character:
    def __init__(self, name, power_level):
        self.name = name
        self.power_level = power_level

    def introduce(self):
        return f"I am {self.name} with power level {self.power_level}!"

    def attack(self):
        return f"{self.name} attacks with basic strength!"


# Subclass: Demon Slayer
class DemonSlayer(Character):
    def __init__(self, name, power_level, breathing_style):
        super().__init__(name, power_level)
        self.breathing_style = breathing_style

    def attack(self):
        return f"{self.name} uses {self.breathing_style} Breathing! "


# Subclass: Demon
class Demon(Character):
    def __init__(self, name, power_level, blood_art):
        super().__init__(name, power_level)
        self.blood_art = blood_art

    def attack(self):
        return f"{self.name} unleashes Blood Demon Art: {self.blood_art}! "


# Example usage
tanjiro = DemonSlayer("Tanjiro", 95, "Water")
nezuko = Demon("Nezuko", 90, "Exploding Blood")

print(tanjiro.introduce())
print(tanjiro.attack())
print(nezuko.introduce())
print(nezuko.attack())
