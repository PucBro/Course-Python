class MiPrimeraClase(): #Nombre de clase Pascal Case
    var = "perro" # variable de clase afecta a todos los objetos a la vez
    #counter = 0

    
    
    def __init__(self,name):
        self.humano = name #Variable de instancia solo afecta al objeto creado 
        self.counter = 1

    def saludar(self):
        self.counter += 1
        #MiPrimeraClase.counter =  MiPrimeraClase.counter + 1 
        print(self.humano)
        print("hola")
    

var = MiPrimeraClase("Jonathan")
var.saludar()
var2 = MiPrimeraClase("Edgar")
var2.saludar()

MiPrimeraClase.saludar(var)
print(MiPrimeraClase.var)

print(var.humano)
print(var2.humano)


print(var.counter)
print(var2.counter)

var.perro = 2 #Declaro variable de instancia fuera de mi clase 

print(var.perro)
#print(var2.perro) Esto da error porque no he declarado perro para var2


