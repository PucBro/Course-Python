counter = 3

lista= ["agua", "platanos", "manzanas"]

"""
def suma(a, b):
    try:
        global counter
        print(lista[counter])
        counter = counter -1
        print("hola")
        print(f"este es el contador {counter}")
        return (a+b)/counter
    except (IndexError, ZeroDivisionError) as e:
        counter -= 1
        return e       
    except Exception:
        return f"esto es muy general"
"""
def func():
    global counter
    counter-=1
    if counter < 0:
        raise IndexError()






while counter > -2:
    lista1= ["manzana"]

    if lista1: #No me evalúa el if si lista 1 es  vacía
        print("hola")
    else:
        print("adios")
        break
    print(func())


#Python considera como falso, el False, valores iguales cero, variables que son None, listas, conjuntos, 
# diccionarios, tupla vacías 