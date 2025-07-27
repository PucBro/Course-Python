class Hierba:
    atributo = "hojas"
    __debilidad = "Fuego"
    _var ="ihadfesgbiua"

    def __init__(self, ataque_hierba, ataque_otro_tipo = ""):    
        self.__var = "hola"   
        self.ataque_hierba = ataque_hierba
        try:
            super().__init__(ataque_otro_tipo)
        except:
            pass

    @classmethod  
    def get_debilidad(cls):
        return cls.__debilidad 
    
    def get____var(self):
        return self.__var

    def atacar(self):
        try:
            self.ataque = super().atacar() 
            return f"{self.ataque} ataca con hojas"
        except:
            return "ataca con hojas"
        


class Fuego: 
    atributo = "llamas"
    def __init__(self, ataque_fuego, ataque_otro_tipo = ""):
        
        self.ataque_fuego = ataque_fuego
        try:
            super().__init__(ataque_otro_tipo)
        except:
            pass
    
    def atacar(self):
        try:
            self.ataque = super().atacar() 
            return f"{self.ataque} y ataca con llamas"
        except:
            return "ataca con llamas"
        

class HierbaFuego(Hierba, Fuego):   
    def __init__(self, name, ataque_hierba, ataque_fuego):
        super().__init__(ataque_hierba, ataque_fuego)
        print(self.ataque_hierba, self.ataque_fuego)
        self.name = name
    
    def atacar(self):
        self.ataque = super().atacar()
        print(f"HierbaFuego:  {self.name} {self.ataque}")

class FuegoHierba(Fuego, Hierba):
    def __init__(self, name, ataque_fuego, ataque_hierba):
        super().__init__(ataque_fuego, ataque_hierba)
        print(self.ataque_fuego, self.ataque_hierba)
        self.name = name
    
    def atacar(self):
        self.ataque = super().atacar()
        print(f"FuegoHierba:  {self.name} {self.ataque}")

        

print(HierbaFuego.__mro__)
print(FuegoHierba.__mro__)

print(HierbaFuego.atributo)

print(HierbaFuego.atributo)

hierbaFuego = HierbaFuego("charizard",  "hojas navaja", "lanzallamas")

fuegohierba = FuegoHierba("venasaur", "lanzallamas", "hojas navaja")

print(hierbaFuego.name)

hierbaFuego.atacar()

fuegohierba.atacar()

print(Hierba.get_debilidad())

print(Hierba._var)

print(fuegohierba.get____var())

print(fuegohierba.__var)


