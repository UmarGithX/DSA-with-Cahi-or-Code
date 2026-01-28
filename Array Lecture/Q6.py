# 🔴 Q6: Find the Second Largest Element in an Array
# ❓ Problem
# Given an array of integers, find the second largest element
# ⚠️ Rules
# ❌ Do NOT use sort()
# ❌ Do NOT use max()
# ✅ Use logic + loops only
# Assume the array has at least 2 different values

from numpy import *

arr=([1,2,3,4,5,6,7,8])

n=len(arr)

higher = arr[0]
Sec_higher = arr[0]

i=0
while n>i:
    if arr[i] > higher:
        higher = arr[i]
    elif arr[i] < higher and arr[i] > Sec_higher:
        Sec_higher = arr[i]
    i +=1


print(arr)
print("higher" , higher)
print("2nd Higher" , Sec_higher)