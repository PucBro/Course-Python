from variables_globales import misiones

'''
def crear_mision():
    nombre = input("Nombre de la mision: ").strip()
    if nombre.upper() not in misiones:
        misiones.append(nombre.upper())
        print(f"Se ha creado la mision {nombre}.")
        print(f"\n La nueva lista de misiones es:\n")
        for i,nombre in enumerate(misiones,1):
            print(f"{i}.{nombre}")
    else:
        print(f"\n\u26A0\uFE0F La mision {nombre} ya existe.")
'''

def crear_mision():
    nombre = input("Nombre de la misión: ").strip().upper()

    # Verificar si ya existe una misión con ese nombre
    nombres_existentes = {m["nombre"] for m in misiones} # es un set, trabaja como si fuera un for reducido como resultado varoles no duplicados
    if nombre in nombres_existentes:
        print(f"\nLa misión '{nombre}' ya existe.")
        return

    # Pedir eventos
    eventos = []
    print("Ingresa los eventos de la misión uno por uno. Escribe 'fin' para terminar.")
    while True:
        evento = input("> ").strip()
        if evento.lower() == "fin":
            break
        if evento:
            eventos.append(evento.upper())

    nueva_mision = {
        "nombre": nombre,
        "eventos": eventos
    }

    misiones.append(nueva_mision)

    print(f"\nMisión '{nombre}' creada con {len(eventos)} evento(s).")
    print("\nLista actual de misiones:")
    for i, m in enumerate(misiones, 1):
        print(f"{i}. {m['nombre']}")

 
 
def ver_misiones_completas():
    if not misiones:
        print("No hay misiones registradas.")
        return

    print("\nLista de misiones con sus eventos:\n")

    for i, mision in enumerate(misiones, 1):
        print(f"{i}. Misión: {mision['nombre']}")
        if mision['eventos']:
            for j, evento in enumerate(mision['eventos'], 1):
                print(f"   {j}.{evento}")
        else:
            print("Esta misión no tiene eventos.")
        print("-" * 40) #Separador de misiones


def modificar_misiones():
    if not misiones:
        print("No hay misiones registradas")
        return
        
    print("\n Misiones disponibles: \n")
    for i,mision in enumerate(misiones,1):
        print(f"{i}.{mision['nombre']}")
        
    idx=int(input("\n Selecciona el número de una mision: "))-1
    mision_selec=misiones[idx_mision]
    
    print(f"\n Misión seleccionada: {mision_selec['nombre']}\n")
    print("1. Modificar misión")
    print("2. Eliminar misión")
    print("3. Cancelar")
    
    opcion=input("\nElige una opción: ").strip() #.strip elimina espacios en blanco quita caracteres especiales al inicio y al final de un string
    
    match opcion:
       case "1":
            nuevo_nombre = input("Nuevo nombre de la misión (Enter para no cambiar): ").strip().upper()
            if nuevo_nombre:
                # Cambiar en misiones globales el nuevo nombre de la mision
                mision_sel['nombre'] = nuevo_nombre
                # Cambiar también en las misiones asignadas a aventureros si es que ya se las había asignado
                for misiones_aven in aventurero_misiones.values():
                    for m in misiones_aven:
                        if m['nombre'] == mision_sel['nombre']:
                            m['nombre'] = nuevo_nombre
                print("✅ Nombre modificado.")

            # Modificar eventos
            print("\nEventos actuales:")
            for i, e in enumerate(mision_sel['eventos'], 1):
                print(f"{i}. {e}")
                
            if input("¿Quieres agregar un nuevo evento? (s/n): ").lower() == "s": #si ingresa n se sale del if
                nuevo_evento = input("Nombre del nuevo evento: ").strip()
                mision_sel['eventos'].append(nuevo_evento)
                # También agregarlo a los aventureros que tengan esta misión
                for misiones_av in aventurero_misiones.values():
                    for m in misiones_av:
                        if m['nombre'] == mision_sel['nombre']:
                            m['eventos'].append(nuevo_evento)
                print("✅ Evento agregado.")

       case "2":
            # Eliminar mision de variable global de misiones, para que ya no aparezca
            misiones.remove(mision_sel)
            # Eliminar de todos los aventureros que hasta el momento tengan esa mision
            for misiones_av in aventurero_misiones.values():
                misiones_av[:] = [m for m in misiones_av if m['nombre'] != mision_sel['nombre']]
            print(f"✅ Misión '{mision_sel['nombre']}' eliminada de la lista y de todos los aventureros.")

       case "3":
            print("Cancelado.")

       case _:
            print("Opción no válida.")