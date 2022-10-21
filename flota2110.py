import pygame
class Vehiculo: 
    def __init__(self):
        __lat = 0
        __lon = 0
        __velocidad = 0
        print("Se ha creado un Vehículo")
    def __str__(self):
        return (f'Velocidad {self.__velocidad}, Latitud: {self.__lat}')
    def getLat(self):
        return self.__lat  
    def getLon(self):
        return self.__lon  
    def getVelocidad(self):
        return self.__velocidad
    def setLat(self, latitud):
        self.__lat = latitud
    def setLon(self,longitud):
        self.__lon = longitud
    def setVelocidad(self,velocidad):
        self.__velocidad = velocidad
objeto=Vehiculo()
pygame.init()
screen = pygame.display.set_mode((800, 600))
EJECUTA = True
while EJECUTA:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            EJECUTA = False
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_d):
            print("Avanzando")
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_a):
            print("Retrocediendo")
pygame.quit()
