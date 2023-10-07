"""n=int(input())
sum=0
for i in range(1,n+1):
    sum=sum+i
    #n-=1
print(sum)
"""
"""a="poo"
print(type(a))"""
"""a=int("10")
b=int("10")
print(a+b)"""
"""name=input()
age=input()
print("name is:", name)
print("age is:", age)"""
"""a=int(input())
b=int(input())
c=int(input())
d=a+b+c
e=a*b*c
f=e/d
print(f)"""
#print("w"=="wfs")
"""for i in range(1,5):
    print()
    for j in range(1,i+1):
        print("*", end=" ")"""

"""i=3
fac=1
while(i>0):
    fac=fac*i
    i-=1
print(fac"""
"""
a=[1,2,3,4,5,6]
b=[7,8]
a.extend(b)
print(a)"""

"""class student:
    def __init__(self):
        self.name="poo"
        self.reg="yes"
    def display(self):
        print("display printed")
s1=student()
print(s1.name)
s1.display()"""

"""class fruit:
    def __init__(self,col):
        self.color=col

apple=fruit("red")
print(apple)"""

"""class teacher:
    def __init__(self,name,reg):
        self.name=name
        self.reg=reg
    def display(self):
        print("name", self.name)
        print("reg", self.reg)

t1=teacher("poo","1")
t2=teacher("chen","2")
t1.display()
t2.display()"""

"""
from typing import Any


class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        c=self.a+self.b
        print(c)
    def sub(self):
        c=self.a-self.b
        print(c)
    def mul(self):
        print(a*b)
ob=calculator(2,3)
ob.mul()"""
    
"""class dad():
   
    def phone(self):
        print("dads phone")
class mom(dad):
    def sweets(self):
        print("mom's sweet")
class son(mom):
    def laptop(self):
        print("son's laptop")

poo=son()
poo.sweets()
poo.phone()
vi=mom()
vi.phone()"""
"""class a():
     def __init__(self):
        print("a")
     def display(self):
         print("display")
class b(a):
    def __init__(self):
        super().__init__()
        print("b")
    def display(self):
        print("b display")
class c(a):
    def __init__(self):
        super().__init__()
        print("c")
    def display(self):
        print("c display")
ob=b()"""
"""class vehicle:
    def start(self):
        print("vehicle started")
class car(vehicle):
    def start(self):
        print("car start")
v1=car()
v1.start()"""

"""class Employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary"""

"""class company():
    def __init__(self):
        self.__name="wipro"
    def name(self):
        print(self.__name)
c=company()
c.name()
print(c.__name)"""

"""
""""""
number = int(request.args.get('num1'))
    temp = number
    rev = 0
    while (number > 0):
        dig = number % 10
        rev = rev * 10 + dig
        number = number // 10
    if (temp == rev):
        return "The number is a palindrome!"
    else:
        return "The number isn't a palindrome!"
"""




    
