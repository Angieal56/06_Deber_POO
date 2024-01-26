class Clase:
    def _init__(self):

        self.__atributo_privado = "Valor"
 
      
    def __hablar(self):
        print("Hola estoy hablando")
     
objeto2 = Clase()

print(objeto2.__hablar())