"""
Escribe una función llamada texto_a_asteriscos(texto) que reciba una cadena de texto y devuelva su representación con asteriscos en mayúsculas
 en bloques de 5x4 por letra. 

Ejemplo texto_a_asteriscos("HI") ---> 

*  * ****
*  *  ** 
****  ** 
*  *  ** 
*  * ****



"""""

abecedario={
        'A': [' ** ', '*  *', '****', '*  *', '*  *'],
        'B': ['*** ', '*  *', '*** ', '*  *', '*** '],
        'C': [' ** ', '*  *', '*   ', '*  *', ' ** '],
        'D': ['*** ', '*  *', '*  *', '*  *', '*** '],
        'E': ['****', '*   ', '*** ', '*   ', '****'],
        'F': ['****', '*   ', '*** ', '*   ', '*   '],
        'G': [' ** ', '*   ', '* **', '*  *', ' ** '],
        'H': ['*  *', '*  *', '****', '*  *', '*  *'],
        'I': ['****', ' ** ', ' ** ', ' ** ', '****'],
        'J': ['  **', '   *', '   *', '*  *', ' ** '],
        'K': ['*  *', '* * ', '**  ', '* * ', '*  *'],
        'L': ['*   ', '*   ', '*   ', '*   ', '****'],
        'M': ['*  *', '** *', '* **', '*  *', '*  *'],
        'N': ['*  *', '** *', '* **', '*  *', '*  *'],
        'O': [' ** ', '*  *', '*  *', '*  *', ' ** '],
        'P': ['*** ', '*  *', '*** ', '*   ', '*   '],
        'Q': [' ** ', '*  *', '*  *', '* **', ' ***'],
        'R': ['*** ', '*  *', '*** ', '* * ', '*  *'],
        'S': [' ***', '*   ', ' ** ', '   *', '*** '],
        'T': ['****', ' ** ', ' ** ', ' ** ', ' ** '],
        'U': ['*  *', '*  *', '*  *', '*  *', ' ** '],
        'V': ['*  *', '*  *', '*  *', ' * *', '  * '],
        'W': ['*  *', '*  *', '* **', '** *', '*  *'],
        'X': ['*  *', ' * *', '  * ', ' * *', '*  *'],
        'Y': ['*  *', ' * *', '  * ', '  * ', '  * '],
        'Z': ['****', '  * ', ' *  ', '*   ', '****'],
        ' ': ['    ','    ','    ','    ','    ',]
    }

#[]  lista o array
#{}  conjunto o diccionario si pasamos llave y valor


def texto_a_asterisco(texto: str):
    texto = texto.upper() 

    for nivel in range(5): # estoy haciendo un loop por cada linea de mi lista
        for char in texto: # Hago un loop que recorre mi texto completo
            print(abecedario[char][nivel], end= " ") # imprimo solo la linea en la que voy de cada letra dejando un espacio entre print y print (en lugar de una linea)
        print() #imprimo otra linea para bajar de nivel

texto_a_asterisco("pedro hola")















