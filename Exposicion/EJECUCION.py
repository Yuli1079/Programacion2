import os
os.system("cls")
print()
#-------------------------------------------

animales_terrestres = set(["Tortuga", "Lobo", "Perro", "Cangrejo"])
print("Terrestres: ", animales_terrestres)
animales_acuaticos = set(["Tortuga","Tiburón", "Pulpo", "Cangrejo"])
print("Acuáticos: ", animales_acuaticos)
# Con el metodo o funcion interna 
animales_terrestres_y_acuaticos = animales_terrestres.intersection(animales_acuaticos)
print("Intersección de acuaticos y terrestres con el metodo: ", animales_terrestres_y_acuaticos)
# También usando el operador &
animales_terrestres_y_acuaticos = animales_terrestres & animales_acuaticos
print("Intersección de acuaticos y terrestres usando &: ", animales_terrestres_y_acuaticos)

#-------------------------------------------
print()
os.system('pause')
os.system('cls')