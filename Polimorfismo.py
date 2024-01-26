class Gato ():
    def sonido (self):
        return "Miau"
    
class Perro ():
    def sonido(self):
        return "guau" 

 
gato = Gato()
perro = Perro()
    
print(gato.sonido())
print(perro.sonido())
 

def hacer_sonido(animal):
    print(animal.sonido())    
    
hacer_sonido(gato)

print("Como hace el perro ?", perro.sonido)
    