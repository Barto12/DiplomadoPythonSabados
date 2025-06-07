# Ejercicio comparacion de dos tuplas y encontrar las diferencias


t1 = (1,2,3,4)
t2 = (3,4,5,6)

# Mostrar los elementos comunes

comunes = tuple(set(t1) & set(t2))
print("Elementos comunes:",comunes)