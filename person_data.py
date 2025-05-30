class Person:
    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object
person1 = Person("Alice", 25)
person1.greet()
