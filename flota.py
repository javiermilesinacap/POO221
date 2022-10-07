import math
#Funcionalidades
velocidad = 0
encendido = False
distancia =0.0
latD=0.0
latO=0.0
lonD=0.0
lonO=0.0
def acelerar():
    global velocidad
    velocidad += 10
    print("-"*5+">acelerando\n\n"+str(velocidad) + " Km/h")
    pass
def frenar():
    global velocidad
    velocidad -= 10
    print("-"*5+">frenando\n\n")
    pass
def encender():
    global encendido
    encendido = not(encendido)
    print("-"*5+">encendiendo\n\n")
    pass
def calculadistancia():
    global distancia,latD,latO,lonD,lonO
    print("-"*5+">La distancia es\n\n")
    distancia = math.sqrt(pow(latD - latO,2)+pow(lonD-lonO,2))
    print("la distancia recorrida es: "+str(distancia))
    pass
def virarI():
    print("-"*5+">Girando a la izquierda\n\n")
    pass
def virarD():
    print("-"*5+">Virando derecha\n\n")
    pass

print('''
        Este programa, muestra la distancia recorrida por un vehículo, entre dos puntos geográficos
        indicando el total a pagar por un pasajero, dado el valor por Km.
    ''')
while(True):
    print(''' 
        1.- Para acelerar
        2.- Para frenar
        3.- Iniciar Carrera
        4.- Finalizar Carrera
        0.- Salir
    ''')
    opcion = int(input("Ingrese su opcion"))
    if(opcion==1):
        acelerar()
    if(opcion==2):
        frenar()
    if(opcion==3):
        latO = float(input("Ingrese latitud de Origen"))
        lonO = float(input("Ingrese longitud de Origen"))
        pass
    if(opcion==4):
        latD = float(input("Ingrese latitud de Destino"))
        lonD = float(input("Ingrese longitud de Destino"))
        calculadistancia()
        pass
    if(opcion==0):
        print("|"*10+"Gracias 0por su preferencia"+"|"*10)