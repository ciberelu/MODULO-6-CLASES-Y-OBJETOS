from turtle import color


class Vehiculo:
    puertas = 4
    def __init__(self, color, ruedas, puertas) -> None:
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas


class Coche(Vehiculo):

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada, ) -> None:
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada 
    
    def retorno (self):
        return color


    
nuevoCarro = Coche( "rojo", 4, 4, 150, 200)

print ("el color del carro es ", nuevoCarro.color, " tiene ", nuevoCarro.ruedas, " ruedas", "tiene  puertas ", nuevoCarro.puertas, " va a una velocidad de ", nuevoCarro.velocidad, " y tiene una cilindrada de ", nuevoCarro.cilindrada)

