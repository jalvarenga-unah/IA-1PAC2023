print('ciclos for y while')

lista_nombres = ["Juan", "Pedro", "Enrique"]
numeros = [1, 2, 3, 4, 5, 5, 6, 4, 3, 5, 63, 2, 4]

diccionario = {
    "nombre":"Juan",
    "apellido":"Alvarenga",
    "edad": 28
}

# for value in diccionario:
#     print( diccionario[value])

for value in diccionario.values():
    print(value)

for key, value in diccionario.items():
    print("key: "+key+ ", value: "+ str(value) )
    print(f"Key: {key}, value: {value}")

# ciclo FOR mediante uso de "range"
# for index in range(0, 10):
#     print(index)

for value in lista_nombres:
    print(value)

# contador = 0
#
# while contador < len(numeros):
#     print(numeros[contador])
#     contador = contador + 1

