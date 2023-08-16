#Python is object oriented.
#Classes is like a constructor of objects.

class my_class:
    x = 9
  
p1 = my_class()
print(p1.x) 

class Person:
    def __init__(self, name, age ):
        self.name = name
        self.age = age


p2 = Person('Yukio', 20)
print(p2.name) #Outputs Yukio
print(p2.age) #Outputs 18
del p2 #Deletes everything

class Test:
    pass 