# 🟡 Q2: Find Largest & Smallest Element (NO max / min)
# ❓ Problem Statement
# Write a Python program to:
# Take an array of n integers from the user
# Find:
# the largest element
# the smallest element
# Do NOT use:
# max()
# min()

from array import *

arr = array('i',[])
n = int(input("Enter Size of array : "))
for i in range(0,n):
    arr.append(int(input("Enter next Number:")))
for i in arr:
    print(i)

larger = arr[i]
smaller= arr[i]
for i in range(1,n):
    if arr[i]<larger:
        larger = arr[i]
    if arr[i]> smaller:
        smaller = arr[i]


print("Larger Element is :" , larger )
print("samller Element is :" , smaller )

# arr = [4, 7, 2, 9, 1]
# print("Max Is :",max(arr))
# print("Min Is :",min(arr))