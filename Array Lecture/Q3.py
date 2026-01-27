# 🟡 Q3: Count Even & Odd Numbers
# Take an array and:
# count how many elements are even
# count how many are odd
# 👉 Rule: no shortcuts like count()
# 👉 Use % operator

from numpy import *
arr = ([])
n = int(input("Enter The Array Length : "))

for i in range(0,n):
    arr.append(int(input("Enter Next :")))

for i in arr:
    print(i)
even = 0
odd = 0
for i in arr:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

evenly = []
oddly = []
for i in arr:
    if i % 2==0:
        evenly.append(i)
    else:
        oddly.append(i)

print("Even Array :" , evenly,"\nTotal Numbers of Even is : ",even )
print("Odd Array :" , oddly ,"\nTotal Numbers of Odd is : ",odd)

# print("This is even numbers :" , even)
# print("This is Odd numbers :" , odd)