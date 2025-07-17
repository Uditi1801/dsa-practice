class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_max_in_linked_list(head):
    if not head:
        return None  

    max_val = head.val
    current = head.next

    while current:
        if current.val > max_val:
            max_val = current.val
        current = current.next

    return max_val
node1=Node(10)
node2=Node(29)
node3=Node(45)
node1.next=node2
node2.next=node3
 

print("Maximum Value:", find_max_in_linked_list(node1))
