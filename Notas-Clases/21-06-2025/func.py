pi=3.14

def area_circulo(radio: int) -> float:
    return pi*(radio**2) 

def vol_cilindro(radio, altura):
    area = area_circulo(radio)
    print(area)
    return area*altura



vol_cilindro(3, 5)


vol_cilindro(altura=5, radio=3)


print(f"volumen de cilindro altura=5 radio=3 {vol_cilindro(3,5)}")
print(f"volumen de cilindro altura=3 radio=5 {vol_cilindro(5,3)}")


def volumen(x, y, z):
    print(x*y*z)

volumen(3,3,3)



#Loops 

for i in range(5,100, 10):
    if i == 5:
        continue # Se salta al siguiente
    elif i == 15:
        print("este es 15")
    elif i == 25:
        print("este es 15")
    else:
        print("no es igual a 5")
    
    print(i)



counter=0
while True:
    print(counter)
    counter = counter +1
    counter += 1
    if counter >10:
        break # se romple el bucle

 # Ceros valen cero y los 1 valen 2 a la potencia de la posición donde se encuentra ese 1 el resultado es la suma 

#  0 = 0,    1 =1,     10 =2,   11=3, 1, 0, 0= 4
#                                     2**2  2**1   2**0

# 1, 0,1, 0, 1, 0 , 1  ----> 2**0 + 0+ 2**2 + 0+ 2**4 + 0+ 2**6 = 1+4+16+64 = 85

binario = 0b10
print( f"101010 en binario es {0b1010101}")

#101 -> 5 y 111 ->7      010 -> 2**1=2     11=2**1 + 2**0 = 3

#Operador bitwise

print(5 & 7)# El operador "and" me da 001 en 3 & 5. Evalúa bit a bit la operación y da 1 si son el mismo y da 0 si uno de los dos es 0

print(5|7) # Operador or me da 1 si el uno de los bits evaluados es 1 y si los dos son 0 regresa 0

print(5^2) #Operador XOR da 1 cuando los digitos son distintos y 0 cuando son iguales

print(~5) # Esto da -(x+1)

print(10 >> 2) # Recorre posiciones del bit hacia la derecha recorre los del primer número tantas veces como diga el número después de >> 2
#(dividimos con división entera el número por 2**y donde y es el número que va después de << )

print(10 << 2) # Recorre posiciones del bit hacia la izquierda (multiplicamos el número por 2**y donde y es el número que va después de << )

# 10 = 8 +2 =2**3 + 2**1 -> 1010    101000


#1 1 111 111 -> 2**8-1  = 255
      