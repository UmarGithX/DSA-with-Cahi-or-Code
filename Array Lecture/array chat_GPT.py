# Q1.
# Create an array of n integers taken from user input and:
# print the array
# print the sum of all elements
# 👉 (No shortcuts like sum() for now)
from array import *

arr = array('i',[])
n = int(input("Enter the size of array"))

for i in range(0,n):
    arr.append(int(input("Enter the Next Number:")))

for i in range(0,len(arr)):
    print(i)

print("The Sum Function :",sum(arr)) #using the sum function.

