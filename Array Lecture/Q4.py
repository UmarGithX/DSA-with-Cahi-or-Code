# 🟠 Q4: Reverse the Array (NO shortcuts)
# ❓ Problem
# Write a program to reverse an array without using:
# reverse()
# slicing ([::-1])
# 👉 Use loops only.

from numpy import *

print("Original Array")
arr = array([1,2,3,4,5,6,7,8])
for i in arr:
    print(i,end=" ")

print("\nRevursed Array")
for i in range((len(arr))-1,-1,-1):
    print(arr[i],end=" ")


# Table_number = int(input("Enter number"))

# for i in range(1,11):
#     print(f"{Table_number} X {i} {Table_number*i}")