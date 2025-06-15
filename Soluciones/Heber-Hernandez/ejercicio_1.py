# HEBER HERNANDEZ

# 14/Jun/25


# Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
#  * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#  *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#  *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#  *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#  *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.


def count_numbers(texto1:str, texto2:str) -> int:
    """
    Imprime los números del 1 al 100, reemplazando múltiplos de 3 y/o 5 por textos
    Retorna la cantidad de veces que se imprime un número.
    """
    count = 0

    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(f"{texto1} y {texto2}")

        elif number % 3 == 0:
            print(texto1)

        elif number % 5 == 0:
            print(texto2)

        else:
            print(number)
            count += 1
    return count

funcion = count_numbers(texto1="multiplo de 3", texto2="multiplo de 5")

print(f"El número de veces que se ha impreso un número: {funcion}")


