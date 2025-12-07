import random

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None

class ListaCircular:
    def __init__(self):
        self.head = self.tail = None

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if not self.head:
            self.head = self.tail = nuevo
            nuevo.next = nuevo
        else:
            self.tail.next = nuevo
            self.tail = nuevo
            self.tail.next = self.head

    def eliminar(self, nodo):
        actual = self.head
        anterior = None
        while True:
            if actual == nodo:
                if anterior: anterior.next = actual.next
                if actual == self.head: self.head = actual.next
                if actual == self.tail: self.tail = anterior
                return
            anterior, actual = actual, actual.next

jugadores = ["Ana", "Luis", "Carlos", "Sofía"]
cola = ListaCircular()
for j in jugadores: cola.agregar(j)

n = cola.head
for _ in range(random.randint(1,5)):
    n = n.next
print(" Papa Caliente ")

while cola.head != cola.tail:
    pasos = random.randint(3,10)  
    for _ in range(pasos):
        n = n.next

    print("Los eliminado son :", n.dato)
    elim = n
    n = n.next
    cola.eliminar(elim)
print("\n El Ganador es :", cola.head.dato, )