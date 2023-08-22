

print("DIFERENCIA")

Conjunto_1 = {1, 2, 3}
Conjunto_2 = {3, 4, 5}
diferencia = Conjunto_1.difference(Conjunto_2)
print(diferencia)
# Resultado: {1, 2}

print("-------------------------------------------------------------------------------")

print("DIFERENCIA SIMETRICA")

Conjunto_1 = {1, 2, 3}
Conjunto_2 = {3, 4, 5}

Diferencia_Simetrica = Conjunto_1.symmetric_difference(Conjunto_2)
print(Diferencia_Simetrica)
# Resulatdo:  {1, 2, 4, 5}

print("-------------------------------------------------------------------------------")

print("COMPROBACION DE PERTENECIA")

Conjunto = {1, 2, 3}
print(2 in Conjunto)  # True
print(4 in Conjunto)  # False

print("-------------------------------------------------------------------------------")

print("SUBCONJUNTO Y SUPERCONJUNTO")

conjunto_1 = {1, 2}
conjunto_2 = {1, 2, 3, 4}
print(conjunto_1.issubset(conjunto_2))  # True
print(conjunto_2.issuperset(conjunto_1))  # True

print("-------------------------------------------------------------------------------")

print("OPERACIONES DE MODIFICACION")

conjunto = {1, 2, 3}
conjunto.add(4)
conjunto.remove(2)
print(conjunto)
# Resultado: {1, 3, 4}




