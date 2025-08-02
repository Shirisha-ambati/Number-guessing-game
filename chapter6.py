# Functions and recursion
# def sum(a,b):
#     s=a+b
#     return s
# print(sum(2,3))
# def print_hello():
#     print("hello")
# print_hello()    # without parameters
# def avg_num(a,b,c):
#     av=(a+b+c)/3
#     return av
# print(avg_num(3,6,8))
# def sum(a,b):
#     s=a+b
#     return s
# print(sum()) # gives error
# def sum(a,b=1):
#     s=a+b
#     return s
# print(sum(2)) # accepted
# def sum(a=3,b=4):
#     s=a+b
#     return s
# print(sum()) # accepted
# list=[1,3,4,5,55]
# def print_len():
#     print(len(list))
# print_len()    
# # or
# def prt_len(list):
#     p=len(list)
#     return p
# print(prt_len(list))
# list=[2,89,0,9,3] 
# def prt_items(list):
#     for item in list:
#         print(item,end= " ")
# print(prt_items(list))
# n=int(input("n:"))  
# def fact(): # factorial
#     fac=1 
#     for i in range (1,n+1):
#         fac*=i
#     print(fac)
#  fact()        
# def show(n): # print numbers from n to 1
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
# print(show(5))    
# def fact(n): #c factorial of a number
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))
# def sum(n):
#     if (n==0):
#         return 0
#     else:
#         return sum(n-1)+(n)
#  sum_m=sum(5)
#  print(sum_m)
# def list_(list,idx): # print no.s of list using recursive call
#     if (idx==len(list)):
#         return
#     print(list[idx])
#     list_(list,idx+1)
# nums=[23,76,89]
# list_(nums,0)    
