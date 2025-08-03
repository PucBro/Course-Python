from variables_globales import aventureros

def crear_aventurero():
    nombre = input("Nombre del aventurero: ").strip()
    if nombre.upper() not in aventureros:
        aventureros.append(nombre.upper())
        print(f"Se ha creado el aventurero {nombre}.")
        print(f"\n La nueva lista de aventureros es:\n")
        for i,nombre in enumerate(aventureros,1):
            print(f"{i}.{nombre}")
    else:
        print(f"\n\u26A0\uFE0F Aventurero {nombre} ya existe.")

def listar_aventureros():
    if not aventureros:
        print("No existen aventureros")
    else:
        print(f"\n La lista de aventureros es:\n")
        for i,nombre in enumerate(aventureros,1):
            print(f"{i}.{nombre}")
            
            
 