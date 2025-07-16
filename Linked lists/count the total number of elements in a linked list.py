#count the total number of nodes in a linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def count_nodes(head):
    count=0
    current=head
    while current is not None:
        count+=1
        current=current.next
    return count
node1=Node(1)
node2=Node(2)
node3=Node(3)
node1.next=node2
node2.next=node3
