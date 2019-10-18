class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # singly

    def __str__(self):
        return hex(id(self))


class LinkedList:  # our list
    def __init__(self):
        self.head = None

    def print_objects(self):
        while self.head is not None:
            print(self.head)  # address
            print("---------------------")
            print(self.head.data)
            self.head = self.head.next


if __name__ == "__main__":
    linked_list = LinkedList()  # (first)list []->[]->[]->None

    linked_list.head = Node("hello")  # head of list
    second_node = Node("from")
    third_node = Node("dark_side")

    linked_list.head.next = second_node  # ["hello"] -> ["from"]
    second_node.next = third_node  # ["from"]  -> ["dark_side"]

    print(linked_list.print_objects())
    # print(linked_list.head.data)
    # print(linked_list.head.next)
    # print(second_node.data)
    # print(second_node.next)
    # print(third_node.data)
    # print(third_node.next)
