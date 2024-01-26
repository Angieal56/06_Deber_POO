num1 = 3
num2 = 4.25

resultado = num1 + num2 

print(resultado)
print(type(num1))


def recorrer(elemento):
    for item in elemento:
        print(f"El elemento actual es: {item}")
        
lista1 = [1,2,3,4]
lista2 = "maquina"

recorrer(lista1)
recorrer(lista2)