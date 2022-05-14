#创建一个python function，要求如下
#1. 要可以接收参数，即parameter
#2. 要有返回值，即需要return
#3. 函数内要有if/else结构
#4. 函数内要用到for loop或者while loop的任意一种


def find_first_intersection(a, b):
    for x in a:
        for y in b:
            if x == y:
                return x


emma=find_first_intersection("python", "excellent")

print(emma)
    