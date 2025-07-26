class Hierba:
    atributo = "hojas"
    def __init__(self, ataque_hierba):
        self.ataque_hierba = ataque_hierba
        pass
        


class Fuego: 
    atributo = "llamas"
    def __init__(self, ataque_fuego, ataque_hierba):
        self.ataque_fuego = ataque_fuego
        super().__init__(ataque_hierba)
        pass
        

class Pokemon(Fuego, Hierba):   
    def __init__(self, name, ataque_fuego, ataque_hierba):
        super().__init__(ataque_fuego, ataque_hierba)
        print(self.ataque_fuego, self.ataque_hierba)
        self.name = name

print(Pokemon.__mro__)

print(Pokemon.atributo)

print(Pokemon.atributo)

pokemon = Pokemon("charizard", "lanzallamas", "hojas navaja")

print(pokemon.name)


