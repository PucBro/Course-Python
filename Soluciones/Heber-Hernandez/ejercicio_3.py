"""
EJERCICIO 3: Conversión entre números decimales y romanos

 -- HEBER HERNANDEZ --


> Implementa dos funciones en Python que conviertan números entre el sistema decimal y el sistema de numeración romana.

    intToRoman(num: int) -> str
    Convierte un número entero positivo en su representación con números romanos.

    romanToInt(s: str) -> int
    Convierte una cadena con un número romano válido en su equivalente decimal.

Restricciones

    Solo se aceptan números enteros positivos en el rango de 1 a 3999.

    Puedes asumir que las cadenas romanas de entrada siempre son válidas (siguen la notación romana estándar).

    No es necesario manejar números menores a 1 o mayores a 3999.

"""



roman_to_int_map = {
    "I": 1, "V": 5, "X": 10, "L": 50,
    "C": 100, "D": 500, "M": 1000
}

int_to_roman_map = {
    1000: "M", 900: "CM", 500: "D", 400: "CD",
    100: "C", 90: "XC", 50: "L", 40: "XL",
    10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
}

def roman_symbol_map(value):
    """
    Traduce un simbolo romano a entero o un numero entero a síimbolo romano.
    """
    if isinstance(value, int):
        return int_to_roman_map.get(value)
    elif isinstance(value, str):
        return roman_to_int_map.get(value)
    else:
        return None


def int_to_roman(num: int) -> str:
    """
    Convierte un nmero entero positivo (1-3999) a numeros romanos.
    """
    if not (1 <= num <= 3999):
        raise ValueError("El numero debe estar entre 1 y 3999")

    result = ""
    for value in int_to_roman_map:
        while num >= value:
            result += int_to_roman_map[value]
            num -= value

    return result


def roman_to_int(string: str) -> int:
    """
    Convierte un numero romano valido a su aqivalente en entero
    """

    total = 0
    prev_value = 0

    for char in reversed(string):
        value = roman_symbol_map(char)
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total


if __name__ == '__main__':
    print(int_to_roman(1994))       # MCMXCIV
    print(roman_to_int("IV"))  # 1994
    print(roman_symbol_map("X"))    # 10
    print(roman_symbol_map(1000))   # M
