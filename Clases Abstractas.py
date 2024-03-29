from abc import ABC, abstractclassmethod


class Persona(ABC):

    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad 
        
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola mi nombre es {self.nombre} y tengo {self.edad} años de edad, soy del sexo {self.sexo}")


class Estudiante(Persona):
    def __init__ (self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")
        

class Trabajador(Persona):
    def __init__ (self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    def hacer_actividad(self):
        print(f"Estoy trabajaando de {self.actividad}")
        
dalto = Estudiante("Luca", 25, "masculino", "programacion")
carlos = Trabajador("Carlos", 30, "masculino", "programador")

dalto.presentarse()
dalto.hacer_actividad()
carlos.presentarse()
carlos.hacer_actividad()
        
         
        
    
    
            
    
    
        

        
        