print('Hola mundo')
print('UNAH')

# Tipos de datos

# tipos de datos inferidos
suma = 2 + 2  # int
numero = 6  # int
nombre = 'Juan'  # string

# nombre = 6

# print(  type( nombre ) , nombre )
# print( nombre + " Alvarenga" )

flotante = 4.0
# print(type(flotante), flotante)

# Listas

lista = [1, 2, 3, 4, 5, 3]

# print(len(lista))
lista.append(56)

# print(type(lista), lista)

# print(len(lista))

# liminar un elemento de la lista
# lista.pop() # elimina el ultimo elemento de la lista

# lista.remove(3) # elimina el primer elemento que encuentra y que es
# enviado como argumento

# lista.remove(5)


del lista[5]  # delete

lista_nombres = ['Juan', 'Fabiola', 'Paola', 'Mario', 'Juan']

# print("posicion de juan",lista_nombres.index("Mario"))

# nueva_variable = lista_nombres[3]

# lista_nombres.remove('Juan')
# del lista_nombres[3]

# lista_nombres.sort() # ordena la lista de forma ascendente
# lista_nombres.reverse() # ordena la lista de forma descendente

lista_nombres[0] = 'Pedro'

lista_nombres2 = lista_nombres.copy()  # hace una copia integrea de la lista

# print('refenrecia posicion 3:', lista_nombres[3])

lista_nombres2[0] = lista_nombres[3]  # 'Juan'

# Desestructuracion
# nombre1 = lista_nombres[0]
# nombre2 = lista_nombres[1]

nombre1, nombre2, nombre3, nombre4, nombre5 = lista_nombres

primero, *_, ultimo = lista_nombres

print(primero)
print(ultimo)
# print(nombre3)
# print(nombre4)
# print(nombre5)

# print(lista_nombres)
# print(lista_nombres2)


# tuplas
tupla = (21, 1, 3, 4, 2, 2, 5) # equivalente al const en JAVA

# tupla = (12) #no es valido
# tupla[0] = 7 #tampoco es valido

print(tupla[0])

print(tupla.count(2)) # cuenta cuantas veces aparece en la tupla el valor enviado

# Diccionarios
diccionario = {
    'nombre': 'Juan',
    'apellido': 'Alvarenga',
    'edad': 28,
    'mayor_de_edad': True,
    # 'nombre':'Pedro'
}



# ref = 'nombre'

diccionario_copia = diccionario.copy() # hace una copia integra del diccionario

diccionario['nombre'] = 'Pedro'
diccionario['color_favorito'] = 'Azul'
# del diccionario['mayor_de_edad'] # Elimina la llave a la que se hace referencia
# diccionario.pop("mayor_de_edad") # Elimina la llave que es enviada como parametro
diccionario.popitem() #elimina la ultima llave agregada

print('original', diccionario)
print('copia',diccionario_copia)

# print(diccionario['nombre'])
# print(diccionario['apellido'])
# print(diccionario['edad'])