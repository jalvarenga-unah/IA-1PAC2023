#definicion de una clase
class Cuadrado:
    # base = 2
    # altura = 3

    #constructor
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

#  fin de la clase


# var1 es de tripo "Cuadrado"
var1 = Cuadrado(2,4) #la instancia de la clase "Cuadrado# "

print(var1.base)
print(var1.altura)
print(f"el area del cuadrado es: {var1.area()}") #llamado del metodo

# var2 = Cuadrado(3,3)
# print(var2.base)
# print(var2.altura)