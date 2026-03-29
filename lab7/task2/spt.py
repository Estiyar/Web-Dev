class Person:
    def __init__(self , name , age , gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        return f"My name is {self.name}"
    def getinfo(self):
        return f"{self.age} , {self.name} , {self.gender}"
    def __str__(self):
        return self.getinfo()

class Student(Person):
    def __init__(self , name , age , gender , major):
        super().__init__(name , age , gender)
        self.major = major
    def getinfo(self):
        return f"{self.age} , {self.name} , {self.gender} , {self.major}"
    def study(self):
        return "I am studying"
    def __str__(self):
        return super().__str__() + f" , {self.major}"

