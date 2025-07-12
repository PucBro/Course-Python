#Instrucción del ejercicio
#intToRoman(num: int) -> str
#Convierte un número entero positivo en su representación con números romanos.
#romanToInt(s: str) -> int
#Convierte una cadena con un número romano válido en su equivalente decimal.
#Restricciones
#Solo se aceptan números enteros positivos en el rango de 1 a 3999.
#Puedes asumir que las cadenas romanas de entrada siempre son válidas (siguen la notación romana estándar).
#No es necesario manejar números menores a 1 o mayores a 3999.
def decimal_a_romano():
    decimal = int(input("Ingrese un número: "))
    unidad = decena = centena = uMil = 0
    rom1 = rom2 = rom3 = rom4 = ""

    if 0 < decimal <= 3999:
        unidad = decimal % 10
        decena = (decimal % 100) // 10
        centena = (decimal % 1000) // 100
        uMil = decimal // 1000

        if unidad == 1:
            rom1 = "I"
        elif unidad == 2:
            rom1 = "II"
        elif unidad == 3:
            rom1 = "III"
        elif unidad == 4:
            rom1 = "IV"
        elif unidad == 5:
            rom1 = "V"
        elif unidad == 6:
            rom1 = "VI"
        elif unidad == 7:
            rom1 = "VII"
        elif unidad == 8:
            rom1 = "VIII"
        elif unidad == 9:
            rom1 = "IX"

        if decena == 1:
            rom2 = "X"
        elif decena == 2:
            rom2 = "XX"
        elif decena == 3:
            rom2 = "XXX"
        elif decena == 4:
            rom2 = "XL"
        elif decena == 5:
            rom2 = "L"
        elif decena == 6:
            rom2 = "LX"
        elif decena == 7:
            rom2 = "LXX"
        elif decena == 8:
            rom2 = "LXXX"
        elif decena == 9:
            rom2 = "XC"

        if centena == 1:
            rom3 = "C"
        elif centena == 2:
            rom3 = "CC"
        elif centena == 3:
            rom3 = "CCC"
        elif centena == 4:
            rom3 = "CD"
        elif centena == 5:
            rom3 = "D"
        elif centena == 6:
            rom3 = "DC"
        elif centena == 7:
            rom3 = "DCC"
        elif centena == 8:
            rom3 = "DCCC"
        elif centena == 9:
            rom3 = "CM"

        if uMil == 1:
            rom4 = "M"
        elif uMil == 2:
            rom4 = "MM"
        elif uMil == 3:
            rom4 = "MMM"

        print("El número romano es:", rom4 + rom3 + rom2 + rom1)
    else:
        print("Ingrese un número de 1 a 3999")


decimal_a_romano()
