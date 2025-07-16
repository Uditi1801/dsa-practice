class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

print_linked_list(node1)
