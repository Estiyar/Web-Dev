from animals import Animal, Dog, Cat

dog1 = Dog("B", 3, "brown", "Labrador")
dog2 = Dog("M", 5, "black", "German Shepherd")
cat1 = Cat("W", 2, "white", True)
cat2 = Cat("L", 4, "gray", False)

animals = [dog1, dog2, cat1, cat2]

for animal in animals:
    print(animal)
    print(animal.info())
    print(animal.speak())
    print()

print(dog1.bite())
print(cat1.sleep())

###
