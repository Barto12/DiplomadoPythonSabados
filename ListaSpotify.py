# Aplicacion de lista de canciones de Spotify

# definir arreglo de canciones

canciones = ["Coldplay- Yellow", "Imagine Dragons- Believer",
             "Adele - Hello", "Dua Lipa - Levitating"]

while True:
    print("-- Menu de  reproduccion---")
    print("1. Ver canciones")
    print("2. Reproducir cancion")
    print("3. Buscar cancion")
    print("4. Salir del menu")

    opcion = input("Elige una opcion (1-4):")

    if opcion == "1":
        print("Lista de canciones:")
        for i in range (len(canciones)):
            print(f"{i + 1}).{canciones[i]}")

    elif opcion == "2":
        num = int(input("¿Que numero de cancion quieres reproducir?:"))
    if ! <= num <= len(canciones): # Ver porque sucede este error y arrreglarlo
            print(f"Reproduciendo")# Ver porque sucede este error y arrreglarlo
    {canciones[num - 1]""})# Ver porque sucede este error y arrreglarlo

    elif opcion == "3": # Ver porque sucede este error y arrreglarlo
     buscar = input("Escribe una palabra para buscar: ").lower() # Ver porque sucede este error y arrreglarlo
     encontrado = False # Ver porque sucede este error y arrreglarlo
     for cancion in canciones: # Ver porque sucede este error y arrreglarlo
         if buscar in cancion.lower(): # Ver porque sucede este error y arrreglarlo
    print("Encontrada:", cancion) # Ver porque sucede este error y arrreglarlo

    encontrado = True
    break
    if not encontrado:  # Ver porque sucede este error y arrreglarlo
        print("No se encontro ninguna cancion con ese termino.") # Ver porque sucede este error y arrreglarlo

    elif opcion == "4": # Ver porque sucede este error y arrreglarlo
        print ("Saliendo del reprodcutor...") # Ver porque sucede este error y arrreglarlo
        break # Ver porque sucede este error y arrreglarlo

    else:  # Ver porque sucede este error y arrreglarlo
        print("Opcion invalida. Intenta de nuevo.") # Ver porque sucede este error y arrreglarlo

