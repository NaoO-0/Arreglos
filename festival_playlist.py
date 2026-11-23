nombres = []
artistas = []
duraciones = []
popularidades = []


def leer_entero(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            print(f"Ingresa un número entre {minimo} y {maximo}.")
        except ValueError:
            print("Entrada no válida. Ingresa un número entero.")


def leer_decimal(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            print("La duración debe ser mayor que 0.")
        except ValueError:
            print("Entrada no válida. Ingresa un número.")


def agregar_canciones():
    cantidad = leer_entero("¿Cuántas canciones deseas agregar? ", 1, 1000)
    for i in range(cantidad):
        print(f"\nCanción {i + 1}")
        nombre = input("Nombre: ").strip()
        artista = input("Artista: ").strip()
        duracion = leer_decimal("Duración en minutos: ")
        popularidad = leer_entero("Popularidad (1-100): ", 1, 100)

        nombres.append(nombre)
        artistas.append(artista)
        duraciones.append(duracion)
        popularidades.append(popularidad)
    print("\nCanciones agregadas correctamente.")


def ver_reportes():
    if not nombres:
        print("\nNo hay canciones registradas.")
        return

    total = len(nombres)
    duracion_total = sum(duraciones)
    promedio = sum(popularidades) / total

    indice_max = popularidades.index(max(popularidades))
    indice_min = popularidades.index(min(popularidades))

    print("\n--- REPORTES ---")
    print(f"Número total de canciones: {total}")
    print(f"Duración total de la playlist: {duracion_total:.2f} minutos")
    print(f"Canción más popular: {nombres[indice_max]} - {artistas[indice_max]} "
          f"({popularidades[indice_max]})")
    print(f"Canción menos popular: {nombres[indice_min]} - {artistas[indice_min]} "
          f"({popularidades[indice_min]})")
    print(f"Promedio de popularidad: {promedio:.2f}")


def mostrar_cancion(i):
    print(f"- {nombres[i]} | {artistas[i]} | {duraciones[i]:.2f} min | "
          f"Popularidad: {popularidades[i]}")


def buscar_canciones():
    if not nombres:
        print("\nNo hay canciones registradas.")
        return

    print("\n--- BUSCAR CANCIONES ---")
    print("1. Por artista")
    print("2. Por rango de popularidad")
    opcion = leer_entero("Elige una opción: ", 1, 2)

    encontrados = []

    if opcion == 1:
        artista = input("Nombre del artista: ").strip().lower()
        for i in range(len(nombres)):
            if artista in artistas[i].lower():
                encontrados.append(i)
    else:
        minimo = leer_entero("Popularidad mínima (1-100): ", 1, 100)
        maximo = leer_entero("Popularidad máxima (1-100): ", 1, 100)
        if minimo > maximo:
            minimo, maximo = maximo, minimo
        for i in range(len(nombres)):
            if minimo <= popularidades[i] <= maximo:
                encontrados.append(i)

    if encontrados:
        print("\nResultados:")
        for i in encontrados:
            mostrar_cancion(i)
    else:
        print("\nNo se encontraron canciones.")


def playlist_recomendada():
    if not nombres:
        print("\nNo hay canciones registradas.")
        return

    promedio = sum(popularidades) / len(popularidades)
    print(f"\n--- PLAYLIST RECOMENDADA (popularidad mayor a {promedio:.2f}) ---")

    hay_recomendadas = False
    for i in range(len(nombres)):
        if popularidades[i] > promedio:
            mostrar_cancion(i)
            hay_recomendadas = True

    if not hay_recomendadas:
        print("Ninguna canción supera el promedio de popularidad.")


def menu():
    while True:
        print("\n===== FESTIVAL PLAYLIST =====")
        print("1. Agregar canciones")
        print("2. Ver reportes")
        print("3. Buscar canciones")
        print("4. Playlist recomendada")
        print("5. Salir")

        opcion = leer_entero("Elige una opción: ", 1, 5)

        if opcion == 1:
            agregar_canciones()
        elif opcion == 2:
            ver_reportes()
        elif opcion == 3:
            buscar_canciones()
        elif opcion == 4:
            playlist_recomendada()
        else:
            print("¡Adios!")
            break


menu()