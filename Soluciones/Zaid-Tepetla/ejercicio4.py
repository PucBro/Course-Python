'''
La función debe:

Aceptar tres argumentos:

Un mensaje para pedir el dato (prompt).

Un límite mínimo aceptable.

Un límite máximo aceptable.

Si el usuario ingresa una cadena que no es un valor entero, la función debe mostrar el mensaje 
[Error: entrada incorrecta] y pedir al usuario que ingrese el valor nuevamente.

Si el usuario ingresa un número que está fuera del rango especificado, la función debe mostrar el mensaje 
[Error: el valor no está dentro del rango permitido (min..max)] y pedir al usuario que ingrese el valor nuevamente.

Si el valor ingresado es válido, la función debe retornarlo como resultado.
'''

def input_int_in_range(prompt, min_val, max_val):
    while True:
        entrada = input(prompt)  # Paso 1: Pedir el dato
        
        if entrada.lstrip('-').isdigit():  # Paso 2: Verificar si es número
            num = int(entrada)
            
            if num >= min_val and num <= max_val:  # Paso 3: Verificar rango
                return num
            else:
                print("[Error: el valor debe estar entre " + str(min_val) + " y " + str(max_val) + "]")
        else:
            print("[Error: ingresa un número entero]")

# Ejemplo de uso:
numero = input_int_in_range("Ingresa un número entre -10 y 10: ", -10, 10)

print("El número ingresado es: " + str(numero))