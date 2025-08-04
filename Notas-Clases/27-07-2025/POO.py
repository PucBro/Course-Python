#Abstracción 

from abc import ABC, abstractmethod

class Abstracta(ABC):

    
    def metodo_1(self):
        print("No soy un método abstracto")
    def metodo_2(self):
        pass
    
    @abstractmethod
    def metodo_abstracto(self):
        pass
    
    



class NoAbstracta(Abstracta):
    
    def __init__(self, var):
        self.__var = var
    
    @property
    def var(self):
        return self.__var
    
    @var.setter
    def var(self,name):
        self.__var = name

    def metodo_abstracto(self):
        print("definí mi método")


obj_1= NoAbstracta("hola")

obj_1.var = "Alejandro"

print(obj_1.var)


NoAbstracta("nombre").metodo_abstracto()






