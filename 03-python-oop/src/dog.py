"""
Write a class that represents a dog. We should be able to:
- Access the dog's name, breed, and age
- Make the dog bark
- Print the dog as a string
"""


#variable = attribute/property

#self is a reference to the object you are currently building. It only has to be the first parameter in your constructor function

# class Dog:
#    def __init__(self, name, age): # constructor function
#         print('calling constructor')
#         self.name = name
#         # creates a variable name and attach it to the Dog object so you can access it by my_dog.name
#         self.age = age # creates a variable name and attach it to the Dog object so you can access it by my_dog.age
#     def bark(self, sound):
#         return f"{self.name} says {sound}"

# # my_dog is the object
# # my_dog = Dog()
# my_dog = Dog('rex', 4)
# print(my_dog.bark('woof'))

# print(my_dog.name, my_dog.age)

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self, sound):
        return f"{self.name} who is {self.age} years old says {sound}"


my_dog = Dog('rex', 4)

print(my_dog.bark('woof'))

print(my_dog.name, my_dog.age)


