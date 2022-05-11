#Class: 必须首字母大写；pass是占位符，还没想好写啥，先占位；
#tom是object具体学生，Student是class，后加()；
#instance 实例=object，没有本质区别；

from email.message import EmailMessage


# class Student:
#     name = 'Tom' 

#     def greet(self): #self refers to any instance of this Class when the instance created. 
#         print(1)
#         print(2)
#         return "bye"
#    #哪一个instance调用了greet（），那么，这个instance对于greet（）来说就是self
#    # 当nancy调用了greet（），self就是nancy；emma调用了greet（），self就是emma；
#    # == 谁调用函数，self就指向谁；    

# nancy = Student()
# # marry=Student()
# # print(Student.name)
# # print(tom.name)
# # print(marry.name)
# # result=nancy.greet() 
# #要调用greet这个method，一定要greet后面有小括号，
# # 所以结果出Hello!就说明greet method被调用了 Return和调用method无关
# # print(result)
# # print(nancy.greet())

# # nancy.greet() #instance调用这个method （）里无需填啥，若用class student调用，需要（）里填instance
# # print(Student.greet(nancy))

# print(nancy.greet())

# print(Student.greet(self=nancy))

# nancy.greet()
# Student.greet(self=nancy)

# #local Variable: function scope里
# class Student:
#     name = 'Tom' 

#     def add(self,a,b): 
#         print(a+b) 

# nancy=Student()
# emma=Student()

# nancy_addition_result=nancy.add(1,2)
# emma_addition_result=emma.add(3,4)

#initial method: 给创造的instanc一个初始状态
# class Student:
#     name = 'Tom' 

#     def __init__(self,age,height): 
#         self.age=age #class variable做不到随instance而变
#         self.height=height
#         print('ínitial is called')

#     def add(self,a,b):
#         print(a+b)

# nancy=Student(18,180)
# emma=Student(20,178)


# #how 只assign age 不 assign height给 sunny

# #第二个def 不删，就显示syntax error？


# print(nancy.age)
# print(emma.height)

#引入module都要放在最顶端
from math import pi
from math import radians as rad

print(pi)
print(rad(1))

#可以用一个python文件去调用另一个python文件
from code2 import empty_set

#inheritance




























# class Student:
#     name = 'Tom' 

#     def __init__(self,age,height): 
#         self.age=age #class variable做不到随instance而变
#         self.height=height
#         print('ínitial is called')

#     def add(self,a,b):
#         print(a+b)

# nancy=Student(18,180)
# emma=Student(20,178)
