class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def repeat (self, msg):
        print(f"I'm {self.name} {msg}, {msg}, {msg}")
    


# instantiate the Parrot class
blu = Parrot("Blu", 10, 'blue')
woo = Parrot("Woo", 15, 'yellow')

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))

print("{} is {} ".format( blu.name, blu.color))
print("{} is {} ".format( woo.name, woo.color))

blu.repeat("Wake up!")
