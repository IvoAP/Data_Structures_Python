from stack import Stack

stack = Stack()


stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)


print("Top element:", stack.peek())  


print("Stack size:", stack.size())  


print("Popped element:", stack.pop())  
print("Popped element:", stack.pop())  


print("Top element after pop:", stack.peek())  

print("Is stack empty?", stack.is_empty())  


print("Current stack:", stack) 


print("Popped element:", stack.pop()) 
print("Popped element:", stack.pop())  


try:
    stack.pop()
except IndexError as e:
    print("Error:", e)  # Deve retornar "pop from empty stack"
