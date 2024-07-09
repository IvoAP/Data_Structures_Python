class Stack :
    def __init__(self) :
        self.items = []

    def push(self, item) -> None:
        self.items.append(item)


    def is_empty(self) -> bool:
        return len(self.items) == 0
    
    def pop(self) -> int:
        if  not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")
        
    def size(self) -> int:
        return len(self.items)
    
    def peek (self) -> int:
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def __str__(self) -> str:
        return str(self.items)

