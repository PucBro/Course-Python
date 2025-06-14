

fernando = "string" # esto es un string
brayan = 1   # esto es un int
Paloma = 1.5 # esto es un float
Jesus = True # esto es un bool
Zaid = 's' # esto es un string

esto_es_un_bool = False 

print(type(fernando))
print(type(brayan))
print(type(Paloma))
print(type(Jesus))
print(type(Zaid))

fernando = False

print(type(fernando))

print(brayan + Paloma)
print(type(brayan + Paloma))

print(Jesus + brayan)
print(type(Jesus + brayan))

#print(brayan + fernando)  no falla 

print(1+2) #operador suma
print(2*3) #operador multiplicación
print(1-3) #operador resta
print(21 % 4 ) #módulo residuo de dividir 21 entre 4
print(3/3) # división regresa float 
print( 7// 3) # división entera regresa entero redondeando hacia abajo
print( 2**2) #potenciación 

#Crea un programa que imprima por consola todos los números comprendidos
 #* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
print("Separador")
print("-----------")

for i in range(10, 56):
    if i % 2 == 0 and (i != 16 and i % 3!= 0):
        print(i)





