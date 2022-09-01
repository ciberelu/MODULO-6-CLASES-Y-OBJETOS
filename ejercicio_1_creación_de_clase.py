from turtle import color


class Vehiculo:
    color = ""
    ruedas = 0
    puertas = 0

class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 0

    def hola ():
        print ("hola")

carro = Coche
carro.hola()
print (type(carro()))