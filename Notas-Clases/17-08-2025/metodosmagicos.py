class Humano():

    def __init__(self, name, age:int, children):
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
    
        
    def __getattr__(self, attr):
        if attr == "atributo":
            self.atributo = "atributo"
            return "Hola"
        else:
            raise AttributeError("Este no me gusta")
    
    def __setattr__(self, name, value):
        if name == "age":
            if isinstance(value, int):
                super().__setattr__(name,value)
            else:
                raise ValueError("Esto no es un entero estás bien wey")
        else:
            super().__setattr__(name,value)
        
    
    def __bool__(self):
       return len(self.name)>0 and self.age > 0
    
    def __len__(self):
        return len(self.children)
    
    
    def __add__(self, humano):
       return self.age + humano.age
    
    def __mul__(self, humano):
        return self.age*humano.age
    
    def __eq__(self, humano):
        return self.name == humano.name


#assert Humano("Diego", 20, [])
pedro = Humano("Pedro", 20, ["Maria"])
pedro.atributo = "este es mi nuevo atributo"
pedro.age = "veinte años"
print(pedro.atributo)
print(pedro.atributo)
print(pedro.age)

#False, 0 y None son los valores falsos por defecto de python 
#Cuando el método __bool__ de un objeto retorna falso y cuando un objeto no tiene método __bool__ pero el método __len__ retorna alguno
#de los valores falsos por defecto 