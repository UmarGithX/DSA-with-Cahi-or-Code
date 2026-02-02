class node:
    def __init__(self,data):
        self.data = data
        self.next = None
# Here we start adding the values to node   
n1 = node(10)
n2 = node(15)
n3 = node(30)
n4 = node(40)
n5 = node(50)
#  now we will link the nodes with each other
head = n1
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5

# now we will treverse it 
def trever(head):
    temper = head
    while temper is not None:
        print(temper.data , end=" => ")
        temper = temper.next
    print("original List")
trever(head)

new =node(500)
temp = head
while temp is not None:
    if temp.data == 15:
        new.next = temp.next
        temp.next = new
        break
    temp = temp.next
print("After insertion at the middle:")
trever(head)   