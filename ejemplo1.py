class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            # Primer nodo: apunta a sí mismo
            self.cabeza = nuevo
            nuevo.siguiente = self.cabeza
        else:
            temp = self.cabeza
            # Recorremos hasta el último nodo
            while temp.siguiente != self.cabeza:
                temp = temp.siguiente
            temp.siguiente = nuevo
            nuevo.siguiente = self.cabeza

    def recorrer(self):
        if self.cabeza is None:
            return
        temp = self.cabeza
        while True:
            print(temp.dato, end=" -> ")
            temp = temp.siguiente
            if temp == self.cabeza:
                break
        print("(ciclo cerrado)")

# Ejemplo de uso
lista = ListaCircular()
lista.insertar(5)
lista.insertar(10)
lista.insertar(15)
lista.insertar(20)

print("Recorrido seguro de la lista circular:")
lista.recorrer()
