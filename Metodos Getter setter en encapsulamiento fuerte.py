
class Personaje: 
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
       
    def get_nombre(self):
        return self.__nombre
  
    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre

dalto = Personaje("kiki", 11)


nombre = dalto.get_nombre()
print(nombre)


caracter = input("Ingrese el nombre del Personaje: ")

dalto.set_nombre(caracter)

nombre = dalto.get_nombre()
print("El nombre de tu personaje es ", nombre)

        