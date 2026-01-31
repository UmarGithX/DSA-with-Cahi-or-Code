# class linklist:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
        
# node1= linklist(11)
# node2= linklist(20)
# node3= linklist(30)
# node4= linklist(40)

# head = node1
# node1.next = node2
# node2.next = node3
# node3.next = node4
# # node4.next = None

# def treversing(head):
#     temp = head
#     while temp is not None:
#         print(temp.data ,end=" -> ")
#         temp = temp.next
#     print("none")
# print(f"{treversing(head)}")

# new_node = linklist(8)
# new_node.next = head
# head = new_node

# print("new Link list is ")
# treversing(head)


class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
n1 = node(20)
n2 = node(30)
n3 = node(40)
n4 = node(50)

# lets link then-=-=-=-=-=-=-=-=
head = n1
n1.next = n2
n2.next = n3
n3.next = n4

# now to treverse each elenemt of single_linklist
def tre(head):
    temp = head
    while temp is not None:
        print(temp.data , end=" => ")
        temp = temp.next
    print("List Finished>")
print("original list")
tre(head)
# now to add a number at the starting

new_Node = node(48)
new_Node.next = head
head = new_Node
print("after adding new element :")
tre(head)
