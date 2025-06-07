# Aplicación de lista de canciones de Spotify

canciones = ["Coldplay - Yellow", "Imagine Dragons - Believer",
             "Adele - Hello", "Dua Lipa - Levitating"]

while True:
    print("\n--- Menú de reproducción ---")
    print("1. Ver canciones")
    print("2. Reproducir canción")
    print("3. Buscar canción")
    print("4. Salir del menú")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        print("Lista de canciones:")
        for i in range(len(canciones)):
            print(f"{i + 1}). {canciones[i]}")

    elif opcion == "2":
        num = int(input("¿Qué número de canción quieres reproducir?: "))
        if 1 <= num <= len(canciones):
            print(f"Reproduciendo: {canciones[num - 1]}")
        else:
            print("Número inválido.")

    elif opcion == "3":
        buscar = input("Escribe una palabra para buscar: ").lower()
        encontrado = False
        for cancion in canciones:
            if buscar in cancion.lower():
                print("Encontrada:", cancion)
                encontrado = True
        if not encontrado:
            print("No se encontró ninguna canción con ese término.")

    elif opcion == "4":
        print("Saliendo del reproductor...")
        break

    else:
        print("Opción inválida. Intenta de nuevo.")
