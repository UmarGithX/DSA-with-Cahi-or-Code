from numpy import *
arr = array([1,"TRON",2,3,4,5,6.5]) 
# The Dig main Difference Between the simple array and the numpy array is that the numpy array can hold differrnt datatypes init.and the simple one not do it.
for i in range(0,len(arr)):
    print(arr[i])

#-------------------------------------------------
# the arange fucntion is used to make the array it has three parameters arange(staring,ending,Differnece)
auto = arange(1,121,1)
print(auto)

#-------------------------------------------------
# it just pirnt the Zeros But i dont know for what purpose we will use it,
zero = zeros(21)
print(zero)

#--------------------------------------------------
# the full fuction is used to print the repeated number ecxept 0 and 1 because it can be printed directly with the help of the above function.
any_number = full(15,5) #full(Repetations,Number)
print(any_number)

#----------------------------------------------
 # 2D array

two = array([[1,2,3],[4,5,6]])
print(two)


#   3D Array

three = array([[[1,2,3], [4,5,6],[7,8,9]]])
print(three)

#the end