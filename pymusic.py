import json
import time
import os

DATA_FILE = "pymusic_data.json"

# Cargar datos desde archivo JSON o iniciar estructura vacía
def cargar_datos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"catalogo": [], "playlists": {}}

# Guardar datos en archivo JSON
def guardar_datos(datos):
    with open(DATA_FILE, "w") as f:
        json.dump(datos, f, indent=4)

# Agregar una nueva canción
def agregar_cancion(catalogo, generos_set):
    titulo = input("🎵 Título: ")
    artista = input("🎤 Artista: ")
    genero = input("🎶 Género: ")
    duracion = input("⏱ Duración (mm:ss): ")
    cancion = {
        "titulo": titulo,
        "artista": artista,
        "genero": genero,
        "duracion": duracion,
        "reproducciones": 0
    }
    catalogo.append(cancion)
    generos_set.add(genero)
    print("✅ Canción agregada.")

# Buscar canciones por título o artista
def buscar(catalogo):
    texto = input("🔍 Buscar por título o artista: ").lower()
    resultados = [c for c in catalogo if texto in c["titulo"].lower() or texto in c["artista"].lower()]
    for c in resultados:
        print(f"{c['titulo']} - {c['artista']} [{c['genero']}] {c['duracion']}")

# Filtrar canciones por género
def filtrar_por_genero(catalogo, generos_set):
    print("🎧 Géneros disponibles:", ", ".join(sorted(generos_set)))
    g = input("🎚 Género a filtrar: ").lower()
    filtrados = [c for c in catalogo if c["genero"].lower() == g]
    for c in filtrados:
        print(f"{c['titulo']} - {c['artista']} ({c['duracion']})")

# Crear playlist
def crear_playlist(catalogo, playlists):
    nombre = input("📁 Nombre de la playlist: ")
    playlists[nombre] = []
    while True:
        titulo = input("➕ Agrega canción (o escribe 'salir'): ").lower()
        if titulo == 'salir':
            break
        encontrada = next((c for c in catalogo if c["titulo"].lower() == titulo), None)
        if encontrada:
            playlists[nombre].append(encontrada)
            print(f"✅ '{titulo}' agregada a '{nombre}'")
        else:
            print("❌ Canción no encontrada")

# Simular reproducción de una canción
def reproducir(catalogo):
    titulo = input("▶️ Reproducir canción: ").lower()
    cancion = next((c for c in catalogo if c["titulo"].lower() == titulo), None)
    if cancion:
        print(f"🎶 Reproduciendo: {cancion['titulo']} - {cancion['artista']}...")
        time.sleep(2)
        cancion["reproducciones"] += 1
        print("✅ Reproducción finalizada.")
    else:
        print("❌ Canción no encontrada")

# Mostrar top 3 canciones más reproducidas
def top_3(catalogo):
    top = sorted(catalogo, key=lambda c: c["reproducciones"], reverse=True)[:3]
    print("🏆 Top 3 más reproducidas:")
    for i, c in enumerate(top, 1):
        print(f"{i}. {c['titulo']} - {c['artista']} ({c['reproducciones']} reproducciones)")

# Menú principal
def menu():
    datos = cargar_datos()
    catalogo = datos["catalogo"]
    playlists = datos["playlists"]
    generos_set = set([c["genero"] for c in catalogo])  # Usar set para evitar géneros duplicados

    while True:
        print("\n🎼 PyMusic – Tu Biblioteca Musical 🎵")
        print("1. Agregar canción")
        print("2. Buscar canción")
        print("3. Filtrar por género")
        print("4. Crear playlist")
        print("5. Reproducir canción")
        print("6. Ver top 3")
        print("7. Guardar y salir")

        op = input("Seleccione una opción: ")

        if op == "1":
            agregar_cancion(catalogo, generos_set)
        elif op == "2":
            buscar(catalogo)
        elif op == "3":
            filtrar_por_genero(catalogo, generos_set)
        elif op == "4":
            crear_playlist(catalogo, playlists)
        elif op == "5":
            reproducir(catalogo)
        elif op == "6":
            top_3(catalogo)
        elif op == "7":
            guardar_datos({"catalogo": catalogo, "playlists": playlists})
            print("💾 Datos guardados. ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida.")

# Ejecutar programa
menu()
