# Valor fijo (cambia este número para probar)
dias_totales = 370

# Calcular el Año
ano = 1  # Empezamos en el año 1

while dias_totales > 365:
    if ano % 4 == 0:  # ¿Es bisiesto?
        dias_en_un_ano = 366
    else:
        dias_en_un_ano = 365
    
    if dias_totales >= dias_en_un_ano:
        dias_totales -= dias_en_un_ano
        ano += 1
    else:
        break

# Calcular mes y día
dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if ano % 4 == 0:  # Ajustar febrero si es bisiesto
    dias_por_mes[1] = 29

mes = 1
for dias in dias_por_mes:
    if dias_totales > dias:
        dias_totales -= dias
        mes += 1
    else:
        break

# Preparar para mostrar
# Día con 2 dígitos (ejemplo: 5 → "05")
if dias_totales < 10:
    dia_mostrar = "0" + str(dias_totales)
else:
    dia_mostrar = str(dias_totales)

# Mes con 2 dígitos (ejemplo: 1 → "01")
if mes < 10:
    mes_mostrar = "0" + str(mes)
else:
    mes_mostrar = str(mes)

# Año con 4 dígitos (ejemplo: 2 → "0002")
ano_mostrar = str(ano)
while len(ano_mostrar) < 4:
    ano_mostrar = "0" + ano_mostrar

# Por ultimo mostrar resultado
print("La fecha es:", dia_mostrar + "/" + mes_mostrar + "/" + ano_mostrar)