
# Instrucción del ejercicio


# Implementa dos funciones en Python que conviertan números entre el sistema decimal y el sistema de numeración romana.

#    intToRoman(num: int) -> str
#    Convierte un número entero positivo en su representación con números romanos.

#    romanToInt(s: str) -> int
#    Convierte una cadena con un número romano válido en su equivalente decimal.


#Restricciones


#   1.Solo se aceptan números enteros positivos en el rango de 1 a 3999.
#       ¿Cual es la mínima cantidad de símbolos romanos que se requieren para hacer cualquier número del 1 al 3999?
#   2.Puedes asumir que las cadenas romanas de entrada siempre son válidas (siguen la notación romana estándar).
#       Acotar a  que el parámetro de la función sea String, no se valido más sobre  el argumento que se pase a la  función
#   3.No es necesario manejar números menores a 1 o mayores a 3999. 
#       Acotado al rango dado, cuando se pasa el valor 3999, empiezan a  haber simbolos testados para multiplicar por 1000 en romano 


import tkinter.messagebox as messagebox
import sys
import os

os.system("cls")# Para limpiar la consola

def roman_to_numeric(): # Función para convertir romano a decimal

    dicRomanValue={'I':1, 'V':5,'X':10, 'L':50, 'C':100, 'D':500, 'M':1000} # Diccionario de letras Romanas con sus valores numéricos
    romanNumber=input("Enter a roman number: ").upper() # Con el input hacemos una entrada por  teclado y con .UPPER pasamos todo a mayúsculas
    lenghtRomanNum= len(romanNumber)-1 #Obtener la longitud del número  romano para obtener indices
    decimalNumber=0 # Variable para ir  guardando  el  valor de la suma o resta  de los  valores según el diccionario
    for index,letter in enumerate(romanNumber): # Cuando usamos dos valores  en el for, el primero  regresa el indice y el segundo el valor
        letterValue=dicRomanValue[letter] # Obtenemos el valor de la letra del diccionario con el valor del enumerate
        
        if(index<lenghtRomanNum): # si indice  menor a longitud del  numero romano para no pasarnos del largo del numero romano
            next=romanNumber[index+1] #Obtenemos el  indice de  la siguiente  letra
            nextValue=dicRomanValue[next] #Ontebemos el valor de la siguiente letra

            if(letterValue>=nextValue):
                decimalNumber+=letterValue # Si  el valor de la letra actual el  mayor a la  siguiente sumamos al resultado
            else:decimalNumber-=letterValue # si es menor restamos al resultado

        else:decimalNumber+=letterValue # Si estamos en el último valor, siempre lo sumamos
    print("Result= ", decimalNumber)




def numeric_to_Roman():
    romanSymbols=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I'] #Lista para definir simbolos romanos
    decimalValues=[1000,900,500,400,100,90,50,40,10,9,5,4,1] #Lista para definir valores numericos

    decimalUser=int(input("Entry a decimal number: "))
    romanValueDic=dict(zip(decimalValues,romanSymbols)) #función Zip crea un diccionario a partir de dos listas, deben tener la misma longitud, dict lo castea a diccionario para asegurarse.

    if(decimalUser<=0 or decimalUser>=4000):# revisa si el numero dado es menor a cero o mayor o igual a 4000
       print("Number out of range, it must be between 1 to 3999")
       sys.exit()

    romanResult=''
    for decimalDic, romSymbol in romanValueDic.items(): #Metodolo items regresará llave valor del diccionario romanValueDic
        while decimalUser >= decimalDic: #Revisa si el número ingresado es mayor a la llave decimal
            decimalUser-=decimalDic #Resta la llave al valor ingresado por el usuario
            romanResult+= romSymbol #Guarda la letra de la llave del diccionario y concateta, cuando son strings += concatena

    print("Roman number: ", romanResult)



# Dentro de un While me faltó




# Match para hacer la función de un switch en java, en python no existe switch
print("Select one option")
print("1. Convert roman number to decimal")
print("2. Convert number y roman number")
option=input() # Regresa una cadena Str
match option: # Sustitución de un switch
    case "1":
        roman_to_numeric()
    case "2":
        numeric_to_Roman()

