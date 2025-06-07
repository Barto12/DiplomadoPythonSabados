#Crear un  un diccionario, agregar, eliminar y modificar claves.

contactos = {
    "Maria": "5555777788",
    "Pedro": "6655877768"
}

# Agregamos un contacto

contactos["Sofia"] = "6667887767"

#modificamos
contactos["Pedro"] = "6667884567"

#eliminar
del contactos["Maria"]
print(contactos)

