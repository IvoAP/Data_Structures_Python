from linked_list import Linked_List


def main():
    my_linked_list = Linked_List()
    my_linked_list.append(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)
    my_linked_list.append(5)

   
    print("Original Linked List:")
    my_linked_list.display()  # Out Expected: 1 -> 2 -> 3 -> 4 -> 5 -> None

    print("\nRemove node with value 3:")
    my_linked_list.remove(3)

    my_linked_list.display()  #  Out Expected: 1 -> 2 -> 4 -> 5 -> None

    print("\nRemove node with value 1 (head of the list):")
    my_linked_list.remove(1)
    my_linked_list.display()  #  Out Expected: 2 -> 4 -> 5 -> None

    print("Tamanho da lista:", my_linked_list.size_list())  # Out: Size of the list is: 2
    print("Lista está vazia?", my_linked_list.is_empty_list())  # Out: Lista is empty? False




if __name__ == "__main__":
    main()