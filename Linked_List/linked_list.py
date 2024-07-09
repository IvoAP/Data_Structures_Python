class List_Node:
    def __init__(self, value = 0, next= None):
        self.value = value
        self.next = next
    

class Linked_List:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = List_Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = List_Node(value)

    def is_empty_list(self) -> bool :
        if not  self.head:
            return True
        else:
            return False
        
    def size_list(self) -> int : 
        if not self.head :
            return 0
        else:
            counter = 1
            current = self.head
            while current.next:
                counter += 1
                current = current.next
        
        return counter
    
    def remove(self, val):
        current = self.head
        prev_node = None

        if current and current.value == val:
            self.head = current.next
            return
        
        while current and current.value != val:
            prev_node = current
            current = current.next
        
        if current:
            prev_node.next = current.next

    def display(self) :
        current = self.head
        while current :
            print(current.value, end=" -> ")
            current = current.next
        print("None")
            
                


        
    