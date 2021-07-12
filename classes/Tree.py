
class tree():

    def __init__(self, name, life, atack, defense, heal):

        self.nome    = name
        self.vida    = life
        self.atack   = atack
        self.defense = defense
        self.heal    = heal
    

    def prt(self):
        print(self.nome,self.level)
    
    def arena(self):
        print("Log")