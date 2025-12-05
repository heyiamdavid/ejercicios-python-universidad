from collections import deque

print(" PlayList Rotativa --- Round-Robin \n")

playlist = deque()
n = int(input("¿Cuántas canciones deseas agregar? "))

for i in range(n):
    nombre = input(f"Nombre de la canción {i+1}: ")
    duracion = int(input(f"Duración de '{nombre}' (en segundos): "))
    playlist.append((nombre, duracion))
    print()

quantum = int(input("\nIngresa el quantum (tiempo por turno): "))
print("\n--- Iniciando Reproduccion---\n")

turno = 1
while playlist:
    nombre, duracion = playlist.popleft()

    print(f"Turno {turno}:")
    print(f"  Canción actual: {nombre}")
    print(f"  Duración restante: {duracion} segundos")

    reproducir = min(duracion, quantum)
    print(f"  Reproduciendo {reproducir} segundos...")

    duracion -= reproducir

    if duracion > 0:
        print(f" {nombre} vuelve al final de la cola con {duracion} segundos restantes.\n")
        playlist.append((nombre, duracion))
    else:
        print(f"  ✔ {nombre} FINALIZADA.\n")
    turno += 1

print(" Todas las canciones han terminado.")