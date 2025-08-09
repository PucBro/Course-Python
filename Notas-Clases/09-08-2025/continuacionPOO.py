class Humano():

    def __init__(self, name, age, children):
        self.name  = name
        self.age = age
        self.children = children
        self.position = 0
    def __repr__(self):
        return f"Humano(name: Diego, age: 28, children: [])"
    def __str__(self):
        return f"Humano"
    
    def __iter__(self):
        self.position = 0
        return self
    
    def __next__(self):
        if self.position < len(self.children) :
            child = self.children[self.position]
            # child2 = self.children[self.position + 1]
            self.position += 2
            return child
        else: 
            raise StopIteration
    
    def __len__(self):
        return len(self.children)
    
    def __add__(self, humano):
       return self.age + humano.age
    
    def __mul__(self, humano):
        return self.age*humano.age
    
    def __eq__(self, humano):
        return self.name == humano.name
    
    


        
    

diego = Humano("Pedro", 28, [])
pedro2= Humano("Pedro", 40, ["Juanito", "Roberto", "mengano"])
pedro = Humano("Pedro", 40, ["Juanito", "Roberto", "mengano"])

print(diego != pedro )

print(repr(diego))
print(pedro)

#child, child2 = next(pedro)
#child, child2 = next(pedro)
# child, child2 = next(pedro) Este falla por la excepción 

print(next(iter(["manzana", "pera"])))

print(f" Pedro tiene {len(pedro)} hijos")
print(f" Diego tiene {len(diego)} hijos")

print(diego + pedro)
print(diego*pedro)


for child in pedro:
    #Primer paso hace iter(pedro) y obtiene un iterador o un error en caso de que la clase de pedro no sea iterable
    #va a llamar a child, child2 = next(pedro) en cada paso 
    print(f"Este es el hijo 1 {child}") 