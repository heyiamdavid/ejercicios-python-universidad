class Node:
    def __init__(self, elem, next_node=None):
        self.elem = elem
        self.next = next_node
        
class SLinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    def add_first(self, elem):
        nuevo_nodo = Node(elem)
        nuevo_nodo.next = self._head
        self._head = nuevo_nodo
        self._size += 1

    def remove_first(self):
        if self._head is None:
            raise Exception("Lista vacía")
        elem = self._head.elem
        self._head = self._head.next
        self._size -= 1
        return elem

    def add_last(self, elem):
        nuevo_nodo = Node(elem)
        if self._head is None:
            self._head = nuevo_nodo
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = nuevo_nodo
        self._size += 1

    def __iter__(self):
        current = self._head
        while current is not None:
            yield current.elem
            current = current.next

    def __str__(self):
        return " -> ".join([str(e) for e in self])

    def __len__(self):
        return self._size
#me quede aqui....
    def search(self, elem):
        current = self._head
        while current:
            if current.elem == elem:
                return True
            current = current.next
        return False

    def insert_at(self, index, elem):
        if not 0 <= index <= self._size:
            raise IndexError("Índice fuera de rango")
        if index == 0:
            return self.add_first(elem)
        current = self._head
        for _ in range(index - 1):
            current = current.next
        current.next = Node(elem, current.next)
        self._size += 1

    def remove_at(self, index):
        if not 0 <= index < self._size:
            raise IndexError("Indice fuera de rango")
        if index == 0:
            return self.remove_first()
        current = self._head
        for _ in range(index - 1):
            current = current.next
        eliminado = current.next.elem
        current.next = current.next.next
        self._size -= 1
        return eliminado