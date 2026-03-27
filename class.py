# # def fun():
# #     pass
# # fun()

# # fun1()
# # def fun1():
# #     pass

# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart

# x = Complex(3.0, -4.5)
# print(x.r, x.i)

# class MyClass:
#     """A simple example class"""
#     i = 12345

#     def f(self):
#         return 'hello world'
    
# x = MyClass()
# x.counter = 1
# while x.counter < 10:
#     x.counter = x.counter * 2
# print(x.counter)
# del x.counter

# print(x.f())
# xf = x.f
# print(xf())

# class MyClass:
#     """A simple example class"""
#     i = 12345

#     def f(self,a):
#         return 'hello world'+ str(a)
# x = MyClass()
# # print(MyClass.f(1)) # MyClass.f(1) give error because f is instance method and need instance to call it
# print(x.f("1")) # x.f(1)

# class Dog:

#     kind = 'canine'         # class variable shared by all instances

#     def __init__(self, name):
#         self.name = name    # instance variable unique to each instance


# # for immutable objects like strings, integers, tuples
# d = Dog('Fido')
# e = Dog('Buddy')
# print(d.kind)                  # shared by all dogs
# print(e.kind)                  # shared by all dogs
# print(d.name)                  # unique to d
# print(e.name)                  # unique to e

# # for mutable objects like lists, dictionaries
# class Dog:

#     tricks = []             # mistaken use of a class variable

#     def __init__(self, name):
#         self.name = name

#     def add_trick(self, trick):
#         self.tricks.append(trick)

# d = Dog('Fido')
# e = Dog('Buddy')
# print(d.add_trick('roll over'))
# print(e.add_trick('play dead'))
# print(d.tricks)                # unexpectedly shared by all dogs


# # Function defined outside the class
# def f1(self, x, y):
#     return min(x, x+y)

# class C:
#     f = f1

#     def g(self):
#         return 'hello world'

#     h = g
# obj = C()
# print(obj.f(3, 4))
# print(obj.g())
# print(obj.h())

# class Bag:
#     def __init__(self):
#         self.data = []

#     def add(self, x):
#         self.data.append(x)

#     def addtwice(self, x):
#         self.add(x)
#         self.add(x)
# b = Bag()
# b.add(3)
# b.addtwice(4)
# print(b.data)
# c=Bag()
# print(c.data)

# class Mammal:
#     def __init__(self, name):
#         print(name, "is a mammal")

# class CanFly(Mammal):
#     def __init__(self, name):
#         print(name, "cannot fly")
#         super().__init__(name)

# class CanSwim(CanFly):
#     def __init__(self, name):
#         print(name, "cannot swim")
#         super().__init__(name)

# class Animal(CanSwim):
#     def __init__(self, name):
#         super().__init__(name)

# dog = Animal("Dog")

# class Mapping:
#     def __init__(self, iterable):
#         self.items_list = []
#         self.__update(iterable)

#     def update(self, iterable):
#         for item in iterable:
#             self.items_list.append(item)

#     __update = update   # private copy of original update() method

# class MappingSubclass(Mapping):
#     def __init__(self, keys, values):
#         super().__init__(zip(keys, values))

#     def update(self, keys, values):
#         # provides new signature for update()
#         # but does not break __init__()
#         for item in zip(keys, values):
#             self.items_list.append(item)
# Mapping2=Mapping(['a', 'b', 'c'])
# print(Mapping2.items_list)
# mapping1 = MappingSubclass(['a', 'b', 'c'], [1, 2, 3])
# print(mapping1.items_list)

# class Mapping:
#     def __init__(self, iterable):
#         self.items_list = []
#         self.__update(iterable)

#     def update(self, iterable):
#         for item in iterable:
#             self.items_list.append(item)
#     __data=34

#     __update = update   # private copy of original update() method

# class MappingSubclass(Mapping):

#     def update(self, keys, values):
#         # provides new signature for update()
#         # but does not break __init__()
#         for item in zip(keys, values):
#             self.items_list.append(item)
            
            
# mapping1 = MappingSubclass([1,2])
# mapping1.update(['a', 'b', 'c'], [1, 2, 3])
# print(mapping1.items_list)
# # print(mapping1.__data) # will give error because __data is private variable
# print(mapping1._Mapping__data) # will work because name mangling is done by adding                                                                                                                      

# class myclass:
#     __data=45
# obj=myclass()
# # print(obj.__data) # will give error because __data is private variable
# print(obj._myclass__data) # will work because name mangling is done by adding


# from abc import ABC, abstractmethod

# class Dog(ABC):  # Abstract Class
#     def __init__(self, name):
#         self.name = name

#     @abstractmethod
#     def sound(self):  # Abstract Method
#         pass

#     def display_name(self):  # Concrete Method
#         print(f"Dog's Name: {self.name}")

# class Labrador(Dog):  # Partial Abstraction
#     def sound(self):
#         print("Labrador Woof!")

# class Beagle(Dog):  # Partial Abstraction
#     def sound(self):
#         print("Beagle Bark!")

# # Example Usage
# dogs = [Labrador("Buddy"), Beagle("Charlie")]
# for dog in dogs:
#     dog.display_name()  # Calls concrete method
#     dog.sound()  # Calls implemented abstract method
    
class car_site:
    def __init__(self,no):
        self.no=no
    def display(self):
        print(self.no)
class engine:
    def __init__(self,power):
        self.power=power
    def display(self):
        print(f"Power of engine {self.power}cc")
class car(car_site,engine):
    def __init__(self, no,power,model):
        car_site.__init__(self,no)
        engine.__init__(self,power)
        self.model=model
    def display(self):
        return engine.display(self)
obj=car(200,21,"arc")
obj.display()

class Duck:
    def make_sound(self):
        return "Quack, quack!"

class Dog:
    def make_sound(self):
        return "Woof, woof!"
    
class Plane:
    def fly(self):
        return "The plane is flying."

def cause_to_make_sound(entity):
    # Python doesn't check the type, it just assumes the method exists
    print(entity.make_sound())

# Both work because they have a make_sound() method
cause_to_make_sound(Duck()) # Output: Quack, quack!
cause_to_make_sound(Dog())  # Output: Woof, woof!

# This would cause an AttributeError at runtime because a Plane has no make_sound()
# cause_to_make_sound(Plane())
