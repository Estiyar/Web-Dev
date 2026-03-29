class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def speak(self):
        return "..."

    def info(self):
        return f"{self.name} is {self.age} years old and is {self.color}"

    def __str__(self):
        return f"Animal: {self.name}"


class Dog(Animal):
    def __init__(self, name, age, color, breed):
        super().__init__(name, age, color)
        self.breed = breed

    def speak(self):
        return "Gav!"

    def bite(self):
        return f"{self.name} bite me!"

    def __str__(self):
        return f"Dog: {self.name} ({self.breed})"


class Cat(Animal):
    def __init__(self, name, age, color, indoor):
        super().__init__(name, age, color)
        self.indoor = indoor

    def speak(self):
        return "Meow!"

    def sleep(self):
        return f"{self.name} is sleeping"

    def __str__(self):
        return f"Cat: {self.name}"


##