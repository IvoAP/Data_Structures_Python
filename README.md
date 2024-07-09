# Data Structures implementation in python3

![Badge](https://img.shields.io/badge/Status-_Desenvolvimento-yellow)
![Badge](https://img.shields.io/badge/Criado_em-_19/06/2024-gree)
![Badge](https://img.shields.io/badge/Lingugem_-Python-blue)

### Linked List 

#### Complexity 
![image](https://github.com/IvoAP/Lists_Python3/assets/35453347/84ceef4f-d2fe-4540-84aa-dabac25c0b52)

#### Explanation of the complexity 

1. append: The append function must traverse the entire list to find the last node where the new node will be added. Hence, its complexity is O(n), where n is the number of nodes in the list.

2. is_empty_list: The is_empty_list function checks if self.head is None, which is a constant-time operation, O(1).

3. size_list: The size_list function traverses all nodes in the list to count the total number of nodes. Therefore, its complexity is O(n).

4. remove: The remove function might need to traverse the entire list to find the node with the value to be removed. Hence, the complexity is O(n).

5. display: The display function traverses all nodes in the list to print their values, resulting in a complexity of O(n).

### Stack 

#### Complexity

![image](https://github.com/IvoAP/Data_Structures_Python/assets/35453347/96e054d2-9477-4621-892c-6747b4aa43d1)

#### Explanation of the complexity 
1. push: The push function adds an item to the top of the stack. This operation does not depend on the number of items in the stack, making its complexity O(1).

2. pop: The pop function removes the item from the top of the stack. Like push, this operation also does not depend on the number of items in the stack, so its complexity is O(1).

3. peek: The peek function retrieves the item from the top of the stack without removing it. This operation is constant-time as it only involves accessing the last item in the stack, making its complexity O(1).

4. is_empty: The is_empty function checks if the stack is empty by verifying if the internal list is empty. This check is done in constant time, resulting in a complexity of O(1).

5. size: The size function returns the number of items in the stack. It directly returns the length of the internal list, which is a constant-time operation, making its complexity O(1).

#### Observation

1. __str__: The __str__ function returns a string representation of the stack. This operation has a time complexity of O(n), where n is the number of items in the stack, because it involves converting the internal list to a string format

