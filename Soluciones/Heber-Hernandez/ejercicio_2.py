"""
EJERCICIO 2

HEBER HERNANDEZ

21/Jun/25

Crea una función que, dado un número entero positivo, retorne la fecha correspondiente según el calendario gregoriano, asumiendo que el conteo inicia el 1 de enero del año 0001.

Importante: Toma en cuenta la regla de los años bisiestos:

    Un año es bisiesto si es divisible por 4, excepto cuando es divisible por 100, a menos que también sea divisible por 400.

Ejemplo:
Si la función recibe 370, debe retornar: 05/01/0002.

"""


def format_date(days: int, month: int, year: int) -> str:
    return f"{days:02d}/{month:02d}/{year:04d}"


def leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def get_year(days: int):
    days_year = 365

    years_count = 1

    while days > days_year:
        if leap_year(years_count):
            days_year = 366
        else:
            days_year = 365

        days -= days_year
        years_count += 1

    return years_count , days


def get_month(days: int, year: int):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if leap_year(year):
        days_in_month[1] = 29
    month = 1
    for days_in_current_month in days_in_month:
        if days <= days_in_current_month:
            break
        days -= days_in_current_month
        month += 1

    return month, days


def get_date(days:int) :
    try:
        if days < 1:
            return "El número de días debe ser un entero positivo"

        year, remaining_days = get_year(days)
        month, day = get_month(remaining_days, year)
        return format_date(day, month, year)

    except Exception as e:
        return f"Error: {str(e)}"




if __name__ == "__main__":
    days_input = 370
    date_result = get_date(days_input)
    print(f"Fecha correspondiente a {days_input} días: {date_result}")







