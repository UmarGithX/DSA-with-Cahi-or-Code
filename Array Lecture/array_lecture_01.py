# import array #this is the basic way to import a module in python
# import array as arr #this way we can name the array to arr with the help of "as" word
from array import * #this way we dont need to write any name for using the dubule code.deep

val = array('i',[1,2,3,4,5,6,7,8,9,10])

# print(val)
 
#  using for loop to output the values
print("1st for loop")
for i in range(1,len(val)):
    print(i, end=" ") #the last end=" " used for printing the number in one line like 1,2,3,4,5,6;

# for loop 2nd method
print("\n2nd for loop")
for i in val:
    print(i , end=" ")
# in python we dont need to To specify how many memory we need to give its alutomativally give it.


#----------------------------------------------------------------------------#

# we can find the typecode of the existing array.
print("\n the typecode is:",val.typecode)

#to revurse the array 
# val.reverse()
# print(val)

#reversing using for loop
val.reverse()
# print("Reversed array:")
# for i in val:
#     print(i)

for i in range(0,len(val)):
    print(val[i])

#------------------------------------------------------------------------------#
#inserting in array

#the insert funcition will add the number in array .insert(2,13) the first 2 was the index nummber and the 13 was the element we want to inset in array;
x = array('i',[11,12,14,15,16,17,19])
x.insert(2,13)
print(x)


#to all the elememnt at the last
x.append(20)
print(x)
# for i in x:
#     print(i)

to add a 