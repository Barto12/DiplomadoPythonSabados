# Anidamiento

# Ejercicio de control de contraseñas

usuario = "usuario1"
contraseña= "1234"

if usuario == "admin":
    if contraseña == "1234":
        print("Acceso concedido")
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario no encontrado")
