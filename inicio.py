#Salida de datos
print("Escribe tu nombre")
#Entrada de datos
miVariable = input()
#Salida de datos
print("Su nombre es: "+miVariable)
#Entrada
edad = int(input("Escribe tu edad"))
#Salida
print("Tu edad es:"+edad+" Años")
#Proceso
edad = int(edad)+1
edad += 1 #Equivalente al anterior
print("En 2 años más, tendrás "+str(edad))
#Se puede realizar muchos IF, pero es ineficiente
if(edad>18):
    print("Es mayor de edad")
if(edad==18):
    print("Cumpli+ó la mayoría de edad")
if(edad<18):
    print("Es menor de edad")
#Otra alternativa
if(edad>18):
    print("Es mayor de edad")
    if(edad>65):
        print("Es adulto mayor")
else:
    if(edad<5):
        print("Es infante")
    print("Es menor de edad")
print("Fin del programa")
i=0
while(i<10):
    print("ciclo")
    i=i+1  #  i +=1 es equivalente