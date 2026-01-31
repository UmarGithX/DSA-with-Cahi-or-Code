# def table(a):
#     for i in range(1,11):
#         print(f"{a} X {i}=",a*i)
        

# num = int(input("Enter the number :"))
# table(num)

# # Q2=============================================
# def square(a):
#   return a*a

# x=int(input("Enter number :"))
# print(square(x))

# # Q3============================================
# def even_odd(a):
#     if a % 2==0:
#         return("its a even number")
#     else:
#         return("This is an odd number")


# d = int(input("Enter a number:"))
# print(even_odd(d))


# # Q4=========================================

def sum_n(a):
    total = 0
    for i in range(1,a+1):
        total = total+i
    return total
    

print(sum_n(4))
