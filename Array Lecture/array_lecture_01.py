# import array #this is the basic way to import a module in python
# import array as arr #this way we can name the array to arr with the help of "as" word
from array import * #this way we dont need to write any name for using the dubule code.deep

val = array('i',[1,2,3,4,5,6,7,8,9,10])

# print(val)
# using for loop to print the values
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

# to add add the first of array any element
x[6] = 21 # so at 6th index the value will be come 16 and the older value will be deleted
print(x)


#==================================================================================#
# now to copy an existing array

carray = array(x.typecode,(ca for ca in x))
for i in range(0,len(x)):
    print(carray[i],"hi")

# to delete a element in array

arr= array('i',[21,22,23,24,25,26,27,28,29,30])
arr.pop()
print(arr , end=" ")

#======================================================================================#
#slicing A Array
# arr2 = arr[Stating index : Ending of the Index) that you want to make a seperate Array of it.

arr2 = arr[0:5]
for a in range(0,len(arr2)):
   print(arr2[a])

print(arr2)

# we can also revurse the array with the help of slicing
Umar = array('i',[1,2,3,4,5,6,7,8,9,10])

Array3= arr2[::-1]
# for i in Array2:
    # print(i)

for i in range(0,len(Array3)):
    print(Array3[i],end=" ")

#=========================================================================================#
# we can insert the array Size at the runtime from the user

ar = array('i',[]) # we create an emty array 
n = int(input("\nEnter a number : ")) # the we add another variable which is used for user to input the array size;

for i in range(0,n): #then we create the loop which 
    ar.append(int(input("Enter input:")))


print("The Output is :")
for i in ar:
    print(i)


#==========================================================================================#
# we can search in arry #
Hassan = Umar # this i copy an existing array for time saving 

i = Hassan.index(5) # with the help of the .index i can search the index of the element
print("the index of The entered Number is: ",i) 


#the end#