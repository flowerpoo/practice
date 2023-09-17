#print("welcome")
#print("hi d ppp")

"""n1=10
n2=5

print(n1+n2) """

"""def add(a,b):
    return a+b
n1=input("n1")
n2=input("n2")

sum = int(n1)+int(n2)
print(sum)"""

"""def maximun(a,b):
    if a>=b:
        return a
    else:
        return b
    
a=2
b=8
x=[a,b]
x.sort()
print (x[0])"""

"""def factorial(n):
    return 1 if (n==1 or n==0) else n*factorial(n-1)
num=5
print(factorial(num))"""
"""def factorial(n):
    if (n<0):
        return 0
    elif (n==0 or n==1):
        return 1
    else:
        fac=1
        while(n>1):
            fac*=n
            n-=1
        return fac
num=5
print(factorial(num))"""

"""def sim(p,t,r):
    s=p*(pow((1+r/100),t))
    ci= s-p
    print(ci)
   # return s
sim(10000,10.25,5)
"""
"""n=15
s=n
l=len(str(n))
sum=0
while n!=0:
    temp=n%10
    sum= sum+(temp**l)
    n=n//10
if(sum == s):
    print("153: yes")
else:
    print("no")"""

def example():
    print("example from prac")