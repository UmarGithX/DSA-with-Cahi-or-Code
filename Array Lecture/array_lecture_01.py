import array

val = array.array('i',[1,2,3,4,5,6])

# print(val)
 
#  using for loop to output the values
print("1st for loop")
for i in range(1,7):
    print(i, end=" ") #the last end=" " used for printing the number in one line like 1,2,3,4,5,6;

# for loop 2nd method
print("2nd for loop")
for i in val:
    print(i , end=" ")
