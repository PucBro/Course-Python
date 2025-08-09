from variables_globales import aventureros,misiones,aventurero_misiones

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
            
            
def asignar_mision_a_aventurero():
     if not aventureros: #Revisa si el diccionario de aventureros está vacío.
         print("No hay aventureros")
         return # return como buena práctica para que salga de la función si la condición se cumple
        
     if not misiones:# Revisa si el diccionario de misiones está vacío
         print("No hay misiones")
         return
         
     print("\n Los aventureros son") #imprimir todos los aventureros
     for i,aventurero in enumerate(aventureros,1):
         print(f"{i}.{aventurero}")
     idx_aventurero=int(input("Selecciona un aventurero: "))-1
     nombre_aven=aventureros[idx_aventurero]
     
     print("\n Misiones: ") #imprimir todos los aventureros
     for i,mision in enumerate(misiones,1):
         print(f"{i}.{mision}")
     idx_mision=int(input("Selecciona una misión: "))-1
     mision_select=misiones[idx_mision]
     
     if nombre_aven not in aventurero_misiones: #Inicialización lista de misiones para el aventurero si no existe
         aventurero_misiones[nombre_aven]=[]
         
     
     nombres_misiones_aven={m['nombre'] for m in aventurero_misiones[nombre_aven]}
     if mision_select["nombre"] in nombres_misiones_aven:
         print(f"{"nombre_aven"} ya cuenta con la misión '{mision_select['nombre']}'")
         return
         
         
     copiar_mision={
     "nombre":mision_select["nombre"],
     "eventos":list(mision_select["eventos"])
     }
     
     aventurero_misiones[nombre_aven].append(copiar_mision)
     
     print(f" Misión '{mision_select['nombre']}' asignada a {nombre_aven}")
          
         
    