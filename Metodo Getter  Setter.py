class Persona: 
    def __init__(self, nombre,edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, new_nombre):
        self._nombre = new_nombre
     
joven = Persona("Lucas",25) 

nombre = joven.get_nombre
print(joven._nombre) 

joven.set_nombre("Pepito")
print(joven._nombre)

name =input("Ingrese el nombre de su jugador")
joven.set_nombre(name)
print(joven._nombre)

