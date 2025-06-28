dictionary = {

    "llave1": 3,

    "llave2": 4,

    "llave3": ("hola", 2,3),
    
    "llave 4": { "hola": { "otro": 30, "diccionario": {} }}

}

print(dictionary["llave1"])
print(dictionary["llave 4"]["hola"])
print(dictionary["llave3"][1]) # esto da 2

for key in dictionary:
    print(f"este es un valor de una llave en mi diccionario {dictionary[key]}")

print(list(dictionary.keys())) # Esto da una lista de las llaves

print(dictionary.values())

conjunto = set("bob")
conjunto1 = {1,2,3}
print(conjunto)
conjunto ={"hola", 2, True, False}
print(conjunto)
conjunto.add("otro elemento")
print(conjunto)
conjunto.remove("otro elemento")
print(conjunto)
element= conjunto.pop()
print(element)
