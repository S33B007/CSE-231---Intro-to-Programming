#class RockGuitars() goes here
class RockGuitars():
    def __init__(self, guitarist = '', guitar = ''): # giving the parameter default values
        # however if parameters were given calling the class, we give the value a member variable 
        # i.e. self.variable = variable
        self.guitarist = guitarist
        self.guitar = guitar

    def __str__(self):
        return "{:<20s} {:<20s}".format(self.guitarist, self.guitar)

    def add_entry(self, guitarist = '', guitar = ''):
        self.guitarist = guitarist
        self.guitar = guitar
        print("\n")
        return "{:<20s} {:<20s}".format(self.guitarist, self.guitar)


g_obj = RockGuitars()

g_obj.add_entry("Jimmy Page", "Gibson Les Paul Standard")

f_obj = RockGuitars()

f_obj.add_entry("Angus Young", "Jaydee SG")

print(g_obj)

print(f_obj)