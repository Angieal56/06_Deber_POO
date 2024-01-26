class Persona: 
    def __init__(self, nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
  
    @property
    def nombre(self):
        return self.__nombre
 

    @nombre.setter
    def nombre(self,new_nombre):
        self.__nombre = new_nombre
      

    @nombre.deleter
    def nombre(self):
        del self.__nombre

muchacho = Persona("Kiki", 25)
nombre = muchacho.nombre
print(nombre)

muchacho.nombre = "Iri"
nombre = muchacho.nombre
print(nombre)

del muchacho.nombre
print("Holaa mundo")