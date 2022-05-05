# print ('hello world')

# print (3-24)
# print (3*24)
# print (3/24)
# print ((2+4)/3)


# # print(round((2+4)/7,2))

# # x=5
# # x=x*2+3
# # print(x)

# # beta=3
# # x=5
# # y=10
#Class # z=x+y
# # print(z)

# # 1apple_number=3
# # print(1apple_number)

# # a=3.0
# # print(type(a))

# # #escape (forward slash)
# # # a="I love my dog\'s ear"
# # # print(a)

# # # a="I love my dog\'s ear" + " yes!"
# # # print(a)

# # # a="yes!"*3
# # # print(a)

# # a="hellohellohellohellohellohellohellohellohellohello?"
# # print(a[-1])

# # #截取子集：slice(切片)
# # a="hello"
# # print(a[1:3])

# # #step：步长
# # a="hello!mate"
# # print(a[0:8:2])

# # fruits=['apple','orange','other']
# # print(fruits[0:2])

# # #add elements
# # fruits=['apple','orange','other']
# # fruits.append('cherry')
# # #全局方法(global method)
# # print(fruits)
# #dot
# #alt + / 出所有选项

# # fruits=['apple','orange','other']
# # fruits.remove('orange')
# # print(fruits)

# # fruits.pop(-1)
# # print(fruits)

# # fruits=['apple','orange','other']
# # print(len(fruits))

# #tuple 元组 存储不能修改的值
# # hack 强行
# #自增运算符
# #+=
# # fruits=('apple','orange','other')
# # new_fruit=('cherry',)
# # fruits+=new_fruit
# # #自减运算符
# # #-=
# # fruits=fruits+ new_fruit
# # print(len(fruits))

# #Dictionary 字典 对象（object）
# #1: {} 花括号 curly bracket
# #2： 键值对 { 'age':8, 'name':"ollie"}

# person={'age':18,'name':"ollie"}
# #index: Dictionary key
# print(person['age'])

# person={1:18,'name':'ollie'}
# #person['gender']='male'
# new_obj={'gender':'male'}
# person.update(new_obj)
# #index:Dictionary key
# # result=person.pop('name')
# # print(result)
# #the pop () method removes the specified item from the dictionary
# #the value of the removed item 
# del person['name']
# print(len(person))

# #most commonly-used: 
# #array/list []
# #object/dic {}

# class=[{},{},{},{}]

#api 的细节
# list1=['a','b']
# res=list1.pop(0)
# print(res)

#Set 集合

#去除重复作用 （去重）
# numbers={1,2,3,'3',3}
# # print(numbers)

# #无顺序-每次print结果都不一样
# numbers.update({50,20})
# # print(numbers)
# #unindexed：无法被索引
# print(numbers[0])

array=['apple']
array.insert(0,'cherry')
print(array)
