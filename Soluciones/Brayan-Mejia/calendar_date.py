# Reto semanal 2 (Sábado 14/Jun/25):

"""
Crea una función que, dado un número entero positivo, retorne la fecha correspondiente 
según el calendario gregoriano, asumiendo que el conteo inicia el 1 de enero del año 0001.

Importante: Toma en cuenta la regla de los años bisiestos:

    Un año es bisiesto si es divisible por 4, excepto cuando es divisible por 100, 
    a menos que también sea divisible por 400.

Ejemplo: Si la función recibe 370, debe retornar: 05/01/0002.
Hint: Primero realicen una función para calcular el año en el que están 
"""

def is_leap_year(year: int) -> bool:
    return year%4 == 0 and year%100 != 0 or year%400 == 0

def calculate_year_and_remaining_days(days: int) -> tuple[int, int]:
    days_common_year = 365
    days_leap_year = 366

    year_days = 0
    year = 1

    while days > (year_days := days_leap_year if is_leap_year(year) else days_common_year):
        days -= year_days
        year += 1

    return year, days

def calculate_days_per_month(year: int) -> tuple[int]:
    february_common = 28
    february_leap = 29

    february_days = february_leap if is_leap_year(year) else february_common

    return (
        31, # January
        february_days, # February 
        31, # March
        30, # April
        31, # May
        30, # June
        31, # July
        31, # August
        30, # September
        31, # October
        30, # November
        31, # December
    )

def calculate_month_and_remaining_days(year: int, remaining_days: int) -> tuple[int, int]:
    days_per_month = calculate_days_per_month(year)
    month = 1

    while remaining_days > days_per_month[month-1]:
        remaining_days -= days_per_month[month-1]
        month += 1

    return month, remaining_days

def calendar_date(days: int) -> str:
    if days == 0: return "00/00/0000"

    year, remaining_days = calculate_year_and_remaining_days(days)
    month, day = calculate_month_and_remaining_days(year, remaining_days)

    return f"{day:02}/{month:02}/{year:04}"


assert calendar_date(0) == "00/00/0000", "Error: Zeroth (0th) day test"
assert calendar_date(1) == "01/01/0001", "Error: First (1st) day test"

assert calendar_date((n := 0 + 31)) == "31/01/0001", "Error: First (1st) month (January) test"
assert calendar_date((n := n + 28)) == "28/02/0001", "Error: Second (2nd) month (February) test"
assert calendar_date((n := n + 31)) == "31/03/0001", "Error: Third (3rd) month (March) test"
assert calendar_date((n := n + 30)) == "30/04/0001", "Error: Fourth (4st) month (April) test"
assert calendar_date((n := n + 31)) == "31/05/0001", "Error: Fifth (5st) month (May) test"
assert calendar_date((n := n + 30)) == "30/06/0001", "Error: Sixth (6st) month (June) test"
assert calendar_date((n := n + 31)) == "31/07/0001", "Error: Seventh (7st) month (July) test"
assert calendar_date((n := n + 31)) == "31/08/0001", "Error: Eighth (8st) month (August) test"
assert calendar_date((n := n + 30)) == "30/09/0001", "Error: Ninth (09st) month (September) test"
assert calendar_date((n := n + 31)) == "31/10/0001", "Error: Tenth (10st) month (October) test"
assert calendar_date((n := n + 30)) == "30/11/0001", "Error: Eleventh (11st) month (November) test"
assert calendar_date((n := n + 31)) == "31/12/0001", "Error: Twelfth (12st) month (December) test"

assert calendar_date(365 + 365 + 31 + 28) == "28/02/0003", "Error: A common year"
assert calendar_date(365 + 365 + 365 + 31 + 29) == "29/02/0004", "Error: A leap year"

assert calendar_date(370) == "05/01/0002", "Error: Task"

