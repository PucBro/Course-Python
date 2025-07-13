'''Instrucción del ejercicio

Implementa dos funciones en Python que conviertan números entre el sistema decimal y el sistema de numeración romana.

    intToRoman(num: int) -> str
    Convierte un número entero positivo en su representación con números romanos.

    romanToInt(s: str) -> int
    Convierte una cadena con un número romano válido en su equivalente decimal.

Restricciones

    Solo se aceptan números enteros positivos en el rango de 1 a 3999.

    Puedes asumir que las cadenas romanas de entrada siempre son válidas (siguen la notación romana estándar).

    No es necesario manejar números menores a 1 o mayores a 3999.'''

#intToRoman (Decimal a Romano)

def intToRoman(num: int) -> str:
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    resultado = ""
    i = 0
    while num > 0:
        while num >= valores[i]:
            resultado += simbolos[i]
            num -= valores[i]
        i += 1
    return resultado

# romanToInt (Romano a Decimal)

def romanToInt(s: str) -> int:
    romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    anterior = 0
    for letra in reversed(s):
        valor = romanos[letra]
        if valor < anterior:
            total -= valor
        else:
            total += valor
        anterior = valor
    return total

# Pruebas para ver los resultados
print("Decimal a Romano:")
print(f"58 -> {intToRoman(58)}")          # Se debera imprimir "LVIII"
print(f"1994 -> {intToRoman(1994)}")      # Se debera imprimir "MCMXCIV"

print("\nRomano a Decimal:")
print(f"LVIII -> {romanToInt('LVIII')}")  # Se debera imprimir 58
print(f"MCMXCIV -> {romanToInt('MCMXCIV')}")  #Se debera imprimir 1994

