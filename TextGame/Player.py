
# Player class for making the player object
class Player:
    # Initializes the player character
    def __init__(self, name, health, print_class, character_class, stre, defe, speed, inte, conc, cha, mana, cash):
        self.name = name
        self.health = health
        self.print_class = print_class
        self.character_class = character_class
        self.stre = stre
        self.defe = defe
        self.speed = speed
        self.inte = inte
        self.conc = conc
        self.cha = cha
        self.mana = mana
        self.cash = cash

    def take_damage(self, i):
        self.health = - i