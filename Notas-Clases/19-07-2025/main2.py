import sys
import os 
""" 
for p in sys.path:
    print(p)

print(__file__) ## __file__ nos da el absolute path del archivo donde ejecutamos

current_path = os.path.dirname(__file__) ## path absoluto del directorio donde nos encontramos
perro_path =os.path.join(current_path, '../13-07-2025')

print(perro_path)


sys.path.append(perro_path)


"""

import platform


import random



print(random.randrange(1,10,3)) # entero entre 1 y 9

print(random.randint(1,2)) #entero entre 1 y 2

print(random.random()) # float entre 0 y 1

print(random.choice([1,2,10,20,15])) #Escoge uno de la lista aleatoriamente

print(random.uniform(5, 10))# float entre 5 y 10


#random.choice(range(1,10,3))  Lo mismo que randrange

print(random.sample([1,2,10,20,15], 3)) # saca una sublista aleatoria de 3 elementos de nuestra lista original



