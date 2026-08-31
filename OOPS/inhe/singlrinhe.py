
# main class
class Animal :
    def eat(self):
        print("Animal is Eating...")
        
# sub class
class Dog(Animal):
    def bark(self):
        print("Dog is Barking...")
        
        
d = Dog()

d.eat()
d.bark()