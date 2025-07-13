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
    print(func())