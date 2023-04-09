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


class Enemy(Person):
    def __init__(self, weapon, first_name, last_name, health, status):
        super().__init__(first_name, last_name, health, status)
        self.weapon = weapon

    def introduce(self):
        print("You are my arch enemy!!!")

    def hurt(self, other):
        if self.weapon == "rock":
            other.health -= 10
        elif self.weapon == "stick":
            other.health -= 5
        print(other.health)

    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and weak".format(other.first_name))

    def steal(self, other):
        print("Ha ha ha, {}, I have your stuff!".format(other.first_name))
        if other.status == True:
            other.status == False

Alex = Enemy("rock", "Alex", "Popolinous", 75, status=False)
# Alex.introduce here uses the function from the 'Enemy' class -> we have overwritten the parent class
Alex.introduce()
# Bob and John take the function from the parent class 'Person'
Bob.introduce()
John.introduce()

