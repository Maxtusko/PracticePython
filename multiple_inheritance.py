# Parent class 1

class Item():
    def __init__(self, sku):
        self.sku = sku

    def print_sku(self):
        print("The sku is {}.".format(self.sku))

# Parent class 2
class Garment():
    def __init__(self, section, type):
        self.section = section
        self.type = type

    def print_garment(self):
        print("The garment is in a section {} {}.".format(self.section, self.type))


# Child class
class Shirts(Item, Garment):
    def __init__(self, sku, section, type, name, color):
        self.name = name
        self.color = color
        Item.__init__(self, sku)
        Garment.__init__(self, section, type)

    def print_shirt(self):
        print("{} {} on sale!".format(self.color, self.type))

Tshirt = Shirts("00123", "summer", "Shirts", "Polo", "White")
Tshirt.print_sku()
Tshirt.print_garment()
Tshirt.print_shirt()
