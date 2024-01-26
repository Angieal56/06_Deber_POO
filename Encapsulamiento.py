class MiClase:
    def __init__(self):

        self._atributo_privado = "valor"

    def _hablar(self):
        print("Hola estoy hablando")
      
objeto = MiClase()

print(objeto._atributo_privado)      
print(objeto._hablar())
