# ¿Que es una tupla?
# es una coleccion ordenada e inmutable de elementos
# Se define con paretesis ()

#Caracteristicas
# Ordenadas
# Inmutables (no se pueden modificar)
#Pueden contener elementos de distintos tipos
# Se pueden repetir valores

#Ejemplo basico

mi_tupla =("Python", 3.10, True)
print(mi_tupla[0]) # Python
print(len(mi_tupla)) # 3

# acceder a elementos de una tupla
lenguaje, version , activo = mi_tupla
print(version) # 3.10

# Que no podemos hacer?

# mi_tupla[0] = "Java"  x error: las tuplas son inmutables