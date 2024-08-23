# Linked List

# Node => data, next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def show_all_nodes(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def add_first_node(self, new_data):
        node = Node(new_data)
        node.next = self.head
        self.head = node

    def add_last_node(self, new_data):
        node = Node(new_data)
        if self.head is None:
            self.head = node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = node

    def insert_node(self, prev_data, new_data):
        if self.head is None:
            raise Exception('The previous node is empty')
        node = Node(new_data)
        node.next = prev_data.next
        prev_data.next = node


node1 = Node('January')
node2 = Node('February')
node3 = Node('March')

llist = LinkedList()
llist.head = node1
node1.next = node2
node2.next = node3
llist.add_first_node('December')
llist.add_last_node('April')
llist.add_last_node('June')
llist.insert_node(node3.next, 'May')
# llist.insert_node(node1.next.next.next, 'May', )
llist.show_all_nodes()
# llist.head.next = node2
# llist.head.next.next = node3
