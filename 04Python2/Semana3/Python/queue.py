class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Elemento '{item}' añadido a la cola. Cola actual: {self.queue}")

    def dequeue(self):
        if self.is_empty():
            print("No se puede hacer dequeue. La cola está vacía.")
            return None
        else:
            item = self.queue.pop(0)
            print(f"Elemento '{item}' eliminado de la cola. Cola actual: {self.queue}")
            return item

    def size(self):
        return len(self.queue)

# Ejemplo de uso
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.dequeue()
queue.enqueue(3)
queue.dequeue()
queue.dequeue()
queue.dequeue()

