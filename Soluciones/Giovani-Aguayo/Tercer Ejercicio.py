def convertirDecimalARomano():
    numero = int(input("Introduce un numero decimal"))

    valores = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    resultado = ""

    for valor, simbolo in valores:
        while numero >= valor:
            resultado += simbolo
            numero -= valor
    return resultado


def convertirRomanoADecimal():
    numero = input("Introduce un numero romano")

    valores = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    total = 0
    i = 0

    while i < len(numero):
        valor1 = valores[numero[i]]

        if i + 1 < len(numero):
            valor2 = valores[numero[i + 1]]

            if valor1 < valor2:
                total += valor2 - valor1
                i += 2

            else:
                total += valor1
                i += 1
        else:
            total += valor1
            i += 1

    return total


print(convertirRomanoADecimal())

print(convertirDecimalARomano())
