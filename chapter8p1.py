# OOPS-1
# class student:
#     name="siri"
# s1= student()
# print(s1.name) # siri
# class car:
#     colour="Blue"
#     Brand="BMW"
# c=car()
# print(c.colour)
# print(c.Brand)
# class student:
#     def __init__(self,fullname):
#         self.name=fullname
# s1=student("siri")
# print(s1.name)        
# class student:
#      def __init__(self,name,marks):
#          self.name=name
#          self.marks=marks
# s1=student("siri",9.08)
# print(s1.name,s1.marks)        
# class student:
#     def __init__(self,name):
#         self.name=name
#     def hello(self):
#         print("welcome",self.name)
# s1=student("siri")
# s1.hello() # these are methods used to perform fucntions
# class student:
#     def __init__(self,name,marks1,marks2,marks3):
#         self.name=name
#         self.marks1=marks1
#         self.marks2=marks2
#         self.marks3=marks3
#     def average(self):
#         average=(self.marks1+self.marks2+self.marks3)/3
#         print(self.name)
#         print(average)
# s1=student("siri",99,97,95)
# s1.average()
#@static method
# class student:
#     @staticmethod # takes no parameter.. like self
#     def college():
#         print("sandip university")
# s1=student()
# s1.college() 
# Abstraction is hiding unwanted data and printing only wanted data
# credit debit method
# class account:
#     def __init__(self,bal,acc):
#         self.bal=bal
#         self.acc=acc
#     def credit(self,amount):
#         self.bal +=amount
#         print(amount)
#         print("total balance:",self.get_balance())
#     def debit(self,amount):
#         self.bal -=amount
#         print(amount)
#         print("Total balance:",self.get_balance())
#     def get_balance(self):
#         return self.bal
# a1=account(1000,2000000)
# a1.credit(19728)