#calculate the sum of the data values stored in the nodes of linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def sum_of_data_vals(head):
    sum=0
    current=head
    while current is not None:
        sum+=current.data
        current=current.next
    return sum
node1=Node(1)
node2=Node(2)
node3=Node(3)
node1.next=node2
node2.next=node3
print("the sum is:",sum_of_data_vals(node1))
