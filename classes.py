import random


class Person:
    def __init__(self, first_name, last_name, health, status):
        """ initialize attributes to be used in/available for all class
        method in this class, and for class objects created by this class"""

        self.first_name = first_name
        self.last_name = last_name
        self.health = health
        self.status = status

    def introduce(self):
        "All people introduce themselves"
        print("Hello, my name is {} {}.".format(self.first_name, self.last_name))

    def emote(self):
        emotion = random.randrange(1,3)
        if emotion == 1:
            print("{} is happy today".format(self.first_name))
        elif emotion == 2:
            print("{} is sad right now".format(self.first_name))

    def health_status(self):
        if self.health >= 76:
            print("{} is totally healthy!".format(self.first_name))
        elif self.health <=75:
            print("{} feels unwell.".format(self.first_name))
        elif self.health <= 50:
            print("{} goes to the doctor.".format(self.first_name))
        else:
            print("{} is unconscious.".format(self.first_name))

#Create a new class object:
Maria = Person("Maria", "Gomez", 95, status=True)
John = Person("John", "Smith", 85, status=False)
Bob = Person("Bob", "Novak", 65, status=True)

print("{} is my friend? {}".format(Maria.first_name, Maria.status))
print("{} is my friend? {}".format(John.first_name, John.status))

#Use a class method:
Maria.introduce()
John.emote()
Bob.health_status()
Maria.health_status()