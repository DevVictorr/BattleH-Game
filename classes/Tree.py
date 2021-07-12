
class tree():

    def __init__(self, nome, level):

        self.nome    = nome
        self.level   = level
    

    def prt(self):
        print(self.nome,self.level)
    
    def arena(self):
        print("Log")