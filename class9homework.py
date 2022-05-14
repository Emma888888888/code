"""
Python OOP Practice


1. 建立一个Animal类，要求
- 具有以下属性：年龄 age，性别 gender，名字 name
- 具有以下方法：
1 greeting( ) --说明：当由Animal的对象调用greeting时，该方法会print出“Hello, I am” 加上该对象的名字name
2 eat(food) --说明： eat方法接受一个参数food，当由Animal的对象调用eat时，该方法会print出“I want to eat” 加上food参数

2. 建立一个Dog类，要求
- 继承Animal类
- 具有以下属性：价格 price
- 具有以下方法：
1 bark() --说明： 当Dog的对象调用bark时, 该方法会print出“My price is” 加上该对象的价格price

3. 建立一个Animal对象， 分别调用greeting() 和eat(food) 方法
4. 建立一个Dog对象，调用bark()方法

"""


class animal:
    def __init__(self,age,gender, name): 
        self.age=age #class variable做不到随instance而变
        self.gender=gender
        self.name= name
    def greeting(self):
        print("Hello, I am", self.name)
    def eat(self, food):
        print("I want to eat", food)


class dog(animal):
    def __init__(self, age, gender, name, price):
        super().__init__(age, gender, name)
        self.price = price
    def bark(self):
        print("My price is ", self.price)
    

x = animal(10, "female", "notadog")
x.greeting()
x.eat("vegetable")

y = dog(12, "male", "imadog", 100)
y.bark()