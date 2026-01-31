#single link list#
#Only one way treversing is Possible


# 🧠 What is a Singly Linked List?
# A singly linked list is a collection of nodes where:
# Each node stores:
# Data
# Address of next node

# [data | next] → [data | next] → [data | Null]

class node:
    def __init__(self,info,next=None):
        self.data = info
        self.next = next

class singly_link_list:
    def __init__(self,head=None):
        self.head = head


    def in_at_End(self,value):
        temp = node(30)
        if(self.head != None):
            t1 = self.head 
            while(t1.next != None):
                t1 = t1.next
            t1.next = temp