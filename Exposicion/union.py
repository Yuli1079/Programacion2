#Union de conjuntos 
#Se crea conjunto mediante llaves o funcion set 
multiplos3= set(range(3,32,3))
multiplos4= set(range(4,41,4))
multiplos5= set(range(5,51,5))

print(multiplos5)

#Permite la union de dos conjuntos tomando los  valores sin repetir. 
union1 = multiplos3.union(multiplos4)
union2 = multiplos3 | multiplos4 | multiplos5

print(union1)
print(union2)

#Ejercicios 

""" """ """
Una empresa de electrodomesticos y aparatos electronicos tiene diferen puntos de ventas en la ciudad y desea saber cuales 
productos en general se venden por todos los puntos.


Se presenta el listado de los productos vendidos en cada sucursal.

Punto 1: Computadores, Celulares, audifonos, televisores

Punto 2: Neveras, lavadoras, computadores, celulares

Punto 3: Celulares, lavadoras, aireacondicionado,  microondas

"""
Punto1 = {"computadores", "celulares", "audifonos", "televisores"}
Punto2 = {"Neveras", "lavadoras", "computadores", "celulares"}
Punto3 = {"celulares", "lavadoras", "aireacondicionado", "microondas"}

Ventas_de_empresa = Punto1|Punto2|Punto3 

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

print(Ventas_de_empresa)


