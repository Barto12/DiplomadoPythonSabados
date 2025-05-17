# Diplomado en Python – Sesión 2: Tipos de Datos Fundamentales y Operadores

# 1. Tipos de datos básicos
edad = 30
print("Edad:", edad, "| Tipo:", type(edad))

precio = 19.99
print("Precio:", precio, "| Tipo:", type(precio))

activo = True
print("Activo:", activo, "| Tipo:", type(activo))

nombre = "Alicia"
print("Nombre:", nombre, "| Tipo:", type(nombre))

# Explicación: Cada tipo de dato tiene un tipo específico en Python que se puede verificar con type()

print("\n--- Variables y nombres válidos ---")
nombre_usuario = "Carlos"
edad_usuario = 25
_valido = 123
nombre_completo = "Ana Pérez"
numero1 = 10

print("Usuario:", nombre_usuario, "| Edad:", edad_usuario)

# Explicación: Los nombres válidos pueden incluir letras, números y guiones bajos, pero no pueden iniciar con número ni contener espacios

print("\n--- Operadores aritméticos ---")
a = 10
b = 3
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("División Entera:", a // b)
print("Módulo:", a % b)
print("Potencia:", a ** b)

# Explicación: Python soporta operaciones matemáticas comunes. La división entera descarta decimales.

print("\n--- Operadores de comparación ---")
x = 7
y = 5
print("Igual a:", x == y)
print("Diferente de:", x != y)
print("Mayor que:", x > y)
print("Menor que:", x < y)
print("Mayor o igual que:", x >= y)
print("Menor o igual que:", x <= y)

# Explicación: Estas comparaciones devuelven True o False. Son útiles en condiciones y filtros.

print("\n--- Operadores de asignación abreviada ---")
contador = 5
contador += 2
print("+= :", contador)
contador *= 3
print("*= :", contador)
contador -= 4
print("-= :", contador)
contador /= 2
print("/= :", contador)

# Explicación: Los operadores abreviados modifican una variable y reasignan su nuevo valor.

print("\n--- Mini Reto Final ---")
nombre = input("Ingresa el nombre del producto: ")
precio = float(input("Ingresa el precio del producto: "))
print(f"Producto: {nombre}")
print("Precio mayor a $100:", precio > 100)
precio *= 1.10
print("Nuevo precio con 10% de aumento:", precio)

# Explicación: Integra todo lo aprendido en un mini programa que interactúa con el usuario.