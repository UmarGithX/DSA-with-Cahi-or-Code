stack = []

stack.append(10)
stack.append(20)
stack.append(30)
# print("stake after Pushes:",stack)    


#To Add element to stake:------------
def adding(stack):
    stack.append(123)
    print('stake after adding new elemnet: ',stack)


# see what is at the top-----------
def see(stack):
    if len(stack) == 0:
        print("stack is empty")
    else:
        saw = stack[-1]
        print(saw)
        
        
# remove from Stake
def delete(stack):
    if len(stack) == 0:
        print("stack is empty") 
        raise Exception ("stake is Empty") #if code fail this will also show in the Terminal
    else:    
        remove = stack.pop()         
        print("After removing the top",stack)
    
# delete(stack) # to delete on top 
# adding(stack) # adding element on top
# see(stack) # see what is at the TOP!!!!

