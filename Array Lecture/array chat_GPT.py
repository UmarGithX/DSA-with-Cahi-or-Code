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
    print(arr[i])

# total = 0
# for i in range(0,len(arr)):
#     total = total+(arr[i])

# print("The Sum Function :",total) #using the sum function.
# Q2
# lo = arr[i]
# hi = arr[i]
# for i in range(0,n):
#     if arr[i] > hi:
#         hi=arr[i]
#     if arr[i] < lo:
#         lo=arr[i]

# print("lower",lo)
# print("higher",hi)

# Q3
# even = 0
# odd = 0
# for i in range(0,n):
#     if arr[i] % 2==0:
#         even +=1
#     else:
#         odd +=1
# evenly = []
# oddly = []

# for i in arr:
#     if i % 2==0:
#         evenly.append(i)
#     else:
#         oddly.append(i)

# print("even numbers are:", evenly)
# print("Odd numbers are:" ,oddly)

# print("even ",even)
# print("odd ",odd)

# Q4

# print("revursed Array")
# for i in range(len(arr)-1,-1,-1):
#     print(arr[i])
# Q5
x= int(input("search:"))
for i in range(0,len(arr)):
    if arr[i]==x:
        print("its index is",i)
else:
    print("element not found")