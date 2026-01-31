class node:
    def __init__(self,data):
        self.data = data
        self.next = None

#creating initial linklist ------------
n1 = node(10)
n2 = node(854)
n3 = node(521)

head = n1
n1.next = n2
n2.next = n3

# treversing Function
def treveral(head):
    temp = head
    while temp is not None:
        print(temp.data , end="  ->  ")
        temp = temp.next
    print("No More link Data")
print("original linked list:")
treveral(head)

#Insertion at start-------------------

new_node = node(52)
new_node.next = head
head = new_node

print("linkist after insertion at beginning : ")
treveral(head)