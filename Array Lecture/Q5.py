# Q5: Search an Element in an Array (Linear Search)
# ❓ Problem
# Take an array of n integers from the user
# Take a number x to search
# If x exists:
# print its index
# If it does NOT exist:
# print "Element not found"
from numpy import *

arr =([])
n = int(input("Enter the Limit: "))

for i in range(0,n):
    arr.append(int(input("Enter next Number: ")))
for i in arr:
    print(i)

sea = arr
search = int(input("Enter the Search value : "))
for i in sea:
    if search == sea:
        print(sea.index())
else:
    print("Element not in this array")