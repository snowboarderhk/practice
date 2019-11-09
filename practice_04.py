"""
class Orange:
    def __init__(self,w,c):
        self.weight = w
        self.color = c
        print("created!")

or1 = Orange(10,"dark orange")
or2 = Orange(3,"pink")
or3 = Orange(11.1,"red")

print(or1.weight)

class Rectangle:
    def __init__ (self,w,l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

    def change_size(self,w,l):
        self.width = w
        self.len = l

rectangle = Rectangle(20,20)
print(rectangle.area())

rectangle.change_size(30,30)
print(rectangle.area())
"""

#3==== p156 challenge 1 ===
"""
class Apple:
    def __init__(self,s,w,c,p):
        self.size = s
        self.weight = w
        self.color = c
        self.price = p
        print("created!!")

ap = Apple(12,200,"red",320)
print(ap.price,"yen")
"""
#===== challenge2===
"""
import math

class Circle:
    def __init__(self,d):
        self.diameter = d

    def area(self):
        return 1/4*self.diameter**2*math.pi

test = Circle(20)
print(test.area())
"""

#=== challenge 3 ===
"""
class Triangle:
    def __init__ (self,l,h):
        self.length = l
        self.height = h

    def area(self):
        return self.length * self.height /2

test = Triangle(2,3)
print(test.area())
"""

#==== challenge 4 ===
"""
class Hexagon:
    def __init__ (self,r):
        self.radius = r

    def outline(self):
        return self.radius *6

test = Hexagon(3)
print(test.outline())
"""

"""
class Data:
    def __init__(self):
        self.nums = [1,2,3,4,4]

    def change_data(self,index,n):
        self.nums[index] = n

data_one = Data()
data_one.nums[3] = 100
print(data_one.nums)

data_two = Data()
data_two.change_data(3,100)
print(data_two.nums)

class Shape:
    def __init__(self,w,l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} by {}".format(self.width,self.len))

my_shape = Shape(20,30)
my_shape.print_size()

class Square(Shape):
    def area(self):
        return self.width * self.len

a_square = Square(40,40)
print(a_square.area())


class Dog:
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:
    def __init__(self,name):
        self.name = name

mick = Person("Mick Jagger")
stan = Dog("Stanley","bulldog",mick)
print(stan.owner.name)
"""
#====p169 challenge 1 ====
"""
class Rectangle:
    def __init__(self,l,w):
        self.len = l
        self.width = w

    def calculate_perimeter(self):
        return self.len*2 + self.width*2

class Square:
    def __init__ (self,a):
        self.a = a
    def calculate_perimeter(self):
        return self.a*4
    #===challenge2  start ===
    def change_size(self,c):
        self.a = self.a + c
    #===challenge2 end   ===
rectest = Rectangle(2,3)
print(rectest.calculate_perimeter())

sqtest = Square(4)
print(sqtest.calculate_perimeter())

#====p169 challenge2 =======
sqtest2 =  Square(5)
sqtest2.change_size(4)
print(sqtest2.calculate_perimeter())

#===p169 challenge 3 ====
class Shape:
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self,l,w):
        self.len = l
        self.width = w

class Square(Shape):
    def __init__ (self,a):
        self.a = a
    def calculate_perimeter(self):
        return self.a*4

test1 = Rectangle(20,30)
test2 = Square(3)
test1.what_am_i()
test2.what_am_i()

#=== p169 challenge 4 ===
class Horse:
    def __init__(self,name,type,rider):
        self.name = name
        self.type = type
        self.rider = rider
class Rider:
    def __init__(self,name):
        self.name = name

mick = Rider("Mick")
stan = Horse("stan","horse",mick)
print(stan.rider.name)
"""
"""
class Rectangle:
    recs = []
    def __init__(self,w,l):
        self.width = w
        self.len = l
        self.recs.append((self.width,self.len))

    def print_size(self):
        print("{}by{}".format(self.width,self.len))

r1 = Rectangle(10,24)
r2 = Rectangle(20,3)
r3 = Rectangle(33,22)

print(Rectangle.recs)
"""
"""
class Lion:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return self.name

lion = Lion("pochi")
print(lion)
"""
"""
class AlwaysPositive:
    def __init__(self,number):
        self.n = number

    def __add__(self,other):
        return abs(self.n + other.n)

x = AlwaysPositive(-30)
y = AlwaysPositive(2)

print(x+y)
"""
"""
class Person:
    def __init__(self):
        self.name = "bob"
bob = Person()
same_bob = bob

print(bob is same_bob)

another_bob = Person()
print(bob is another_bob)
"""
"""
x = 10
if x is None:
    print("x is None:(1")
else:
    print("x isnt None2")

x = None
if x is None:
    print("x is None3")
else:
    print("x isnt None4")
"""

#===practice p 177 No.1===
"""
class Square:
    square_list = []
    def __init__(self,l):
        self.len = l
        self.square_list.append(self.len)

    def print_list(self):
        print(self.square_list)

a = Square(2)
b = Square(33)
c = Square(83)

c.print_list()
"""
"""
#===challenge2 p 177
class Shape():
    def what_am_i(self):
        print("I am a shape.")


class Square(Shape):
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self.s1)

    def calculate_perimeter(self):
        return self.s1 * 4

    def what_am_i(self):
        super().what_am_i()
        print("I am a Square.")

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1)

a_square = Square(29)
print(a_square)
"""
"""
#+++challenge3 p177 +++
def compare(a,b):
    return a is b

print(compare(2,2))
"""
