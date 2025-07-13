#import math  (Primer método de importar)

'''
pi = 3.14

pi2=math.pi

print(math.sin(pi))
print(math.sin(pi2) )
'''

#Segundo método Importa todos las funciones, variables y objetos del módulo directo a nuestro script
""" 
from math import *

pi = "hola"

print(pi)
"""

#tercera manera Importa solo lo que pedimos
""" 
from math import pi, sin, cos

print(cos(pi))
print(sin(pi))

"""

#Alias

""" 
import math as m 

print(m.pi)

from math import pi as p
# pi  No reconoce pi como pi solo como p
print(p)
"""


#varios módulos en una sola línea 

""" 

import math as m, sys as s, random as r

print(m.sqrt(5))
print(s.platform)
print(r.randint(1,20))

from math import pi as p, sin as s

print(p)
print(s(p))

"""

"""
Pa el examen de certificación:
sin(),
cos(),
tan(),

asin(),  -> inverso de sin i.e asin(sin(x))=x
acos(),
atan()

sinh()
cosh()
tanh()

asinh()
acosh()
atanh()

Más importantes:
    pow() -> potencía 
    sqrt() -> raíz cuadrada
    floor() -> redondea al número entero más cercano menor o igual al número que le damos
    log() -> con base e si lo ocupan con un solo argumento, si lo ocupan con 2 uno es la base y otro es a lo que le quieren sacar logaritmo
    exp() -> con base e
    log10() -> con base 10
    log2() -> con base 2
    e -> constante de euler
    ceil() -> redondea hacía arriba un entero
    trunc() -> elimina el . decimal del número 
    hypot() -> saca la hipotenusa
    factorial() -> saca el factorial de un número





"""


from math import *

print(log(8))

print(log(8,2))

print(trunc(-3.99))
print(floor(-3.99))

print(factorial(5))