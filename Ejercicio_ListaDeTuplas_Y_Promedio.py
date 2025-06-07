# Manejar tuplas dentro de una lista y calcular el promedio


# lista de alumnos con tupla (nombre , calificacion)

alumnos =[("Ana", 8.5), ("Luis", 7.8),("Eva",9.2)]

#Calcular el promedio

promedio = sum([nota for _, nota in alumnos]) / len(alumnos)
print(f"Promedio general: {promedio:2f}")