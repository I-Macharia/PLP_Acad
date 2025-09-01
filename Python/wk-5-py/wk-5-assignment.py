# This is my submission for my OOP assignment.
"""
Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
Add attributes and methods to bring the class to life!
Use constructors to initialize each object with unique values.
Add an inheritance layer to explore polymorphism or encapsulation.

Activity 2: Polymorphism Challenge! 🎭

Create a program that includes animals or vehicles with the same action (like move()).
However, make each class define move() differently 
(for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

"""
# Create a class called "Batman"
class Heroes:
    catchphrase = "For Justice!"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.gadgets = ["Batarang", "Grapple Gun", "Smoke Bomb"]
        self.vehicle = "Batmobile"

    def drive(self):
        return(f"{self.name} is driving the Batmobile!")

    def use_gadgets(self, gadget):
        print(f"{self.name} is using the {gadget}!")
        if gadget in self.gadgets:
            return(f"{gadget} used successfully!")
        else:
            return(f"{gadget} is not available!")
        

# Create a subclass called "Superman" that inherits from "Heroes"
class Superman(Heroes):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.powers = ["X-ray Vision", "Super Strength", "Heat Vision"]

    def use_powers(self, power):
        print(f"{self.name} is using powers!")
        if power in self.powers:
            return(f"{power} used successfully!")
        else:
            return(f"{power} is not available!")

    def fly(self):
        return(f"{self.name} is flying!")


heroes = Heroes("Bruce Wayne", 30)
print(heroes.catchphrase)
print(heroes.drive())
print(heroes.use_gadgets("Grapple Gun"))

superman = Superman("Clark Kent", 35)
print(superman.catchphrase)
print(superman.fly())
print(superman.use_powers("X-ray Vision"))
