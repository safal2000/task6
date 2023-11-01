class Adult:
    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour

    def can_drive(self):
        if self.age >= 18:
            print(self.name, ", You are old enough to drive!")
        else:
            print(self.name, ", You are not old enough to drive")

# Create a subclass Child that inherits from Adult
class Child(Adult):
    def __init__(self, name, age, eye_colour, hair_colour):
        super().__init__(name, age, eye_colour, hair_colour)  # Call the constructor of the parent class

# Ask the user for input and create a Person or Child object based on age
name = input("What is your name? ")
age = int(input("How old are you? "))
eye_colour = input("What is your eye colour? ")
hair_colour = input("What is your hair colour? ")

if age >= 18:
    adult = Adult(name, age, eye_colour, hair_colour)
    adult.can_drive()
else:
    child = Child(name, age, eye_colour, hair_colour)
    child.can_drive()




