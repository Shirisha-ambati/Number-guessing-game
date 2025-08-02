# OOPS-2
#del keyword
# class student:
#     def __init__(self,name):
#         self.name=name
# s1=student("siri")
# s2=student("venu")
# s3=student("giri")
# s4=student("hari")
# print(s1.name)
# print(s2.name)
# del s1.name
# print(s1.name)# error 
# class person:
#     __name="siri"
# p1=person()
# print(p1.__name) # error bcz __ (double underscore makes it private attribute)
# inheritance
# class car:
#     @staticmethod
#     def start():
#         print("car started")
#     @staticmethod
#     def stop():
#         print("car stopped")
# class Toyotacar(car):
#     def __init__(self,name):
#         self.name=name
# c1=Toyotacar("BMW")
# # (c1.stop())
# class siri: #inheritance types multi-level
#     @staticmethod
#     def grade():
#         print("siri's grade is 14")
#     @staticmethod
#     def age():
#         print("siri has age about 19")
# class venu(siri):
#     def __init__(self,love):
#         self.love=love
# class marks(venu):
#     def __init__(self,marks):
#         self.marks=marks
# s1=marks(99)
# s1.age()
# multiple
# class A:
#     varA="welcome to class A"
# class B:
#     varB="welcome to class B"
# class C(A,B):
#     varC="welcome to class c"
# c1=C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)
# import os
# os.remove("demo.txt")
