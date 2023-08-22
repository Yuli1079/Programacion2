#Operaciones de Subconjunto y Superconjunto. 

# Definir conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_c = {2, 3, 6}

# Verificar si un conjunto es subconjunto de otro .issubset
subconjunto = conjunto_a.issubset(conjunto_b)  # True, porque todos los elementos de A están en B
print("\n",subconjunto)

# Verificar si un conjunto es superconjunto de otro .issuperset
superconjunto = conjunto_b.issuperset(conjunto_a)  # True, porque todos los elementos de A están en B
print("\n",superconjunto)

# Verificar si dos conjuntos son iguales
son_iguales = conjunto_a == conjunto_c  # False, porque los conjuntos tienen elementos diferentes
print("\n",son_iguales)

""" """ """
Ejemplo: Una empresa de ropa necesita saber si sus 3 sucursales venden productos solamente correspondientes a la 
empresa en general. Los datos son: 

Productos de empresa: blusas, jean, shorts, pantalones, sudaderas, jogger, vestidos, camisas, correas y carteras. 

sucursal 1: blusas, jean, pantalones, sudaderas. 
sucursal 2: camisas, zapatos, correas, jean y jogger. 
sucursal 3: short, vestidos, carteras. 

"""


C_empresa = {"blusas", "jean", "shorts", "pantalones", "sudaderas", "jogger", "vestidos", "camisas", "correas", "carteras"}
sucursal_1 = {"blusas", "jean", "pantalones", "sudaderas"}
sucursal_2 = {"camisas", "zapatos", "correas", "jean", "jogger"}
sucursal_3 = {"short", "vestidos", "carteras"}

Datos_conjunto = [sucursal_1, sucursal_2, sucursal_3]

for Conjunto in Datos_conjunto:
    verificacion = Conjunto.issubset(C_empresa)
    print("\n El conjunto", Conjunto, "es subconjunto de C_empresa:", verificacion)

