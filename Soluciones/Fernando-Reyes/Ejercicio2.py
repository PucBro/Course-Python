#Reto semanal 2:

#Crea una función que, dado un número entero positivo, retorne la fecha correspondiente según el calendario gregoriano, asumiendo que el conteo inicia el 1 de enero del año 0001.

#Importante: Toma en cuenta la regla de los años bisiestos:

#Un año es bisiesto si es divisible por 4, excepto cuando es divisible por 100, a menos que también sea divisible por 400.

#Ejemplo:
#Si la función recibe 370, debe retornar: 05/01/0002.

#Hint: 
#Primero realicen una función para calcular el año en el que están 
from datetime import date, timedelta

def calcularFecha(dias):
    fechaInicio = date(1,1,1)
    nuevaFecha = fechaInicio + timedelta(dias - 1)
    print(nuevaFecha)

calcularFecha(12345)    
  
        