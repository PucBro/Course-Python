
# Imports de diferentes módulos metodos en especifico
from aventureros import crear_aventurero,listar_aventureros,asignar_mision_a_aventurero
from misiones import crear_mision,ver_misiones_completas



# web iconos https://emojigraph.org/es/mage/

def menu():
    
    while True:
        print("\n\U0001F9D9 Libro de Aventura")
        print("\n1.Crear nuevo aventurero\u2795")
        print("2.Mostrar aventureros") #Me falta ícono
        print("3.Crear nueva mision\u2795")
        print("4.Mostrar misiones\U0001f440")
        print("5.Modificar Misiones\u270F\uFE0F me falta")
        print("6.Asignar Misiones a Aventureros") #Me falta ícono
        print("7.Copiar Misiones\U0001f4dd me falta")
        print("8.Salir\U0001f3c3\u200D\u2642\uFE0F")
        opcion=input() #input regresa un string
        match opcion:
             case "1":
                 #metodo del modulo para crear nuevo aventurero
                 print("\nCreando aventurero")
                 crear_aventurero()
             case "2":
                 #metodo del modulo aventureros para listar aventureros
                 listar_aventureros()
             case "3": 
                 #métdo del módulo para crear una nueva mision.
                 print("\nCreando mision")
                 crear_mision()
             case "4":
                 #método del módulo para ver misiones
                 print("\nViendo misiones")
                 ver_misiones_completas()
             case "5":
                 #método del modulo para modificar misiones
                 print("\nModificando misiones")
             case "6":
                 #metodo para asignar misiones a aventureros
                 print("\nAsignando misiones")
                 asignar_mision_a_aventurero()
             case "7":    
                 # Metodo del modulo para copiar misiones
                 print("\nCopiando misiones")
             case "8":
                 print("\nSaliendo")
                 break #para romper el while, y salir del programa
             case _:
                 print("\nOpción no válida, intenta de nuevo")
                 
if __name__ == "__main__":
    menu()

