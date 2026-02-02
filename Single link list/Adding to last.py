# class node:
#     def __init__(self,data,next=None):
#         self.data = data
#         self.next = None
      
# n1 = node(12)
# n2 = node(13)
# n3 = node(14)
# n4 = node(15)
# n5 = node(16)

# head = n1
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5

# #tervresing part

# def terverse(head):
#     temp = head
#     while temp is not None:
#         print(temp.data ,end=" => ")
#         temp = temp.next
#     print("no more Elements")
        
# terverse(head)
# # addint to last wala seen -=-
# new = node(45)
# temp = head
# while temp.next is not None:
#     temp = temp.next
# temp.next = new

# print("ather Insertion")
# terverse(head)


class node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = None
        
n1 = node(20)
n2 = node(230)
n3 = node(210)
n4 = node(120)
n5 = node(340)

head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

def tre(head):
    temp = head
    while temp is not None:
        print(temp.data , end=" -> ")
        temp = temp.next
    print("original list")
    
tre(head)

new = node(11)
temp = head
while temp.next is not None:
    temp = temp.next
temp.next = new
print("after adding new element:")
tre(head)