
# Agregar elementos a una lista

nombres = ["Ana", "Luis"]
nombres.append("Carlos")
#Agrega al final
nombres.insert(1, "Maria")
#Insertamos en la posicion 1

print(nombres) # ["Ana", "Maria, "Luis", "Carlos"]

# Eliminamos elementos de una lista

colores = ["rojo", "verde", "azul", "verde"]
colores.remove("verde") # elimina la primera ocurrencia "verde"
eliminado = colores.pop() # elimina el ultimo elemento

print("Lista actual:", colores)
print("Elemento eliminado:", eliminado)

# Explicacion

# remove (valor) elimina la primera aparicion de ese valor
# pop() elimine y devuelve el ultimo elemento

