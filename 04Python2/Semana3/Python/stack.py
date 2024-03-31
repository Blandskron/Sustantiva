class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
        print(f"Elemento '{item}' añadido a la pila. Pila actual: {self.stack}")

    def pop(self):
        if self.is_empty():
            print("No se puede hacer pop. La pila está vacía.")
            return None
        else:
            item = self.stack.pop()
            print(f"Elemento '{item}' eliminado de la pila. Pila actual: {self.stack}")
            return item

    def peek(self):
        if self.is_empty():
            print("La pila está vacía.")
            return None
        else:
            print(f"Elemento en la cima de la pila: {self.stack[-1]}")
            return self.stack[-1]

    def size(self):
        return len(self.stack)

# Ejemplo de uso
stack = Stack()
stack.push(1)
stack.push(2)
stack.peek()
stack.push(3)
stack.pop()
stack.pop()
stack.pop()
stack.pop()

