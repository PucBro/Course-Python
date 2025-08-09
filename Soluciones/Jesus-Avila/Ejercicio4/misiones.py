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
        print(f"\n⚠️ La misión '{nombre}' ya existe.")
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

    print(f"\n✅ Misión '{nombre}' creada con {len(eventos)} evento(s).")
    print("\n📋 Lista actual de misiones:")
    for i, m in enumerate(misiones, 1):
        print(f"{i}. {m['nombre']}")

 
 
def ver_misiones_completas():
    if not misiones:
        print("⚠️ No hay misiones registradas.")
        return

    print("\n📘 Lista de misiones con sus eventos:\n")

    for i, mision in enumerate(misiones, 1):
        print(f"{i}. 🗺️ Misión: {mision['nombre']}")
        if mision['eventos']:
            for j, evento in enumerate(mision['eventos'], 1):
                print(f"   {j}.{evento}")
        else:
            print("⚠️ Esta misión no tiene eventos.")
        print("-" * 40) #Separador de misiones

