lista = []

lista2= ["hola", 2, True, 2.5] # pueden meterle todo tipo de dato

print(lista2)

lista2.append(3) # ingresamos el valor 3

print(lista2)

print(lista2[0]) #indexo el indice 0

print(lista2[1:3]) # Hacer un slice de la lista

#Slice tres parametros [start:stop:step]


print(lista2[0:4:2]) # imprime "hola" y True 

string1= "lo que sea"

print(string1[0::2])


string2 = "bob"

print(string2[::-1])


print(string2 == string2[::-1]) #checa si esto es palindromo 

lista3 = lista2.copy() #copiamos la lista y de esta manera lista2 y lista 3 son variables distintas

print(lista2.pop()) #eliminamos último elemento 

print(lista3) # lista 3 no se ve afectada
print(lista2)

tupla = ("perro", 2, True )
tupla2=("elemento",)

def func(a,b):
    return a**2, b**2

cuadrado1, cuadrado2 = func(3,5)
print(f"este es cuadrado1 {cuadrado1}")
print(f"este es cuadrado2 {cuadrado2}")
print(func(3,2))

lista2[0] = 3

print(lista2)

print(tupla[0])



for elemento in lista2:
    print(f"Este es un elemento de mi lista {elemento}")

for char in string2:
    print(f"este es un caracter {char}")

del lista2[0]

print(lista2)
print(lista3)


