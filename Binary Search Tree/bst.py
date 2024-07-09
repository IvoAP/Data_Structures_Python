class Node :
    def __init__(self,key : int) -> None:
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self,key :int):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root,key)

    def _insert(self, current_node : Node , key : int):
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert(current_node.left, key)

        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert(current_node.right, key)

    def search (self, key : int) -> Node :
        return self._search(self.root, key)
    
    def _search(self, current_node : Node, key: int) -> Node:
        if current_node is None or current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self.search(current_node.left, key)
        else:
            return self._search(current_node.right, key)
        