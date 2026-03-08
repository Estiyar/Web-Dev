from models import Animal, Dog, Cat

dog1 = Dog("Buddy", 3, "brown", "Labrador")
dog2 = Dog("Max", 5, "black", "German Shepherd")
cat1 = Cat("Whiskers", 2, "white", True)
cat2 = Cat("Luna", 4, "gray", False)

animals = [dog1, dog2, cat1, cat2]

for animal in animals:
    print(animal)
    print(animal.info())
    print(animal.speak())
    print()

print(dog1.fetch())
print(cat1.purr())

###
