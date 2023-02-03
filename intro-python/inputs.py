# nombre = input('Ingrese su nombre: ') #me permite ingresar valores desde teclado
#todo valor retornado del 'input' es un String
# print(nombre)

num1 = input('ingrese un valor numérico: ')

num2 = input('ingrese otro valor numérico: ')

try:
    suma = int(num1) + int(num2)
except:
    print('solo se permiten valores numéricos')
    exit()

print(suma)

