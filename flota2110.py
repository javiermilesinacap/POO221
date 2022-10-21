class Vehiculo: 

    def __init__(self):
        __lat = 0
        __lon = 0
        __velocidad = 0
        print("Se ha creado un Vehículo")
    def getLat(self):
        return self.__lat  
    def getLon(self):
        return self.__lon  
    def setLat(self, latitud):
        self.__lat = latitud 
    def setLon(self,longitud):
        self.__lon = longitud
    def setVelocidad(self,velocidad):
        self.__velocidad = velocidad
objeto=Vehiculo()
objeto.setLat(1234)
objeto.setLon(5678)
print("Objeto",objeto.getLat())
print("Objeto",objeto.getLon())

