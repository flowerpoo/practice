#print("Hello world")
"""a="hi"
b=2
print(a*b)"""
"""p=int(input("Enter the amount"))
i=int(input("Enter the interest"))
y=int(input("Enter the year"))
si= (p*i*y)/100
total=p+si
print(total)"""
"""car=int(input("Enter the numebr of car"))
bike=int(input("Enter number of bike"))
total=(car*6*20)+(bike*6*10)
if(total>=10000):
    print("good day")
else:
    print("bad day")
print("outside")"""
"""n=int(input("enter the number"))
sum=0
for i in range(n):
    if(i%2 !=0 ):
        sum=sum+i
print(sum)"""

"""class goa:
    drink=""
    def party(self):
        print("lets drink")
    def beach(self):
        print("enjoy beach")

ramesh=goa()
suresh=goa()
ramesh.party() """
#names=["poo","paul","sinto","chendur"]
#feedback=[1,2,3,4]
learner=[]
sum=0
num=int(input("enter the number of elements in list "))
for i in range(num):
    le={}
    a=input("ener name:")
    b=int(input("enter feedback:"))
    le["name"]= a
    le["feedback"]=b
    learner.append(le)
    sum=sum+b

avg=sum/num
print(avg)
print(learner)

"""le=[{
    "name":"poo",
    "feed":2},
    {
    "name":"chendur"
}]
print(le[0]["name"])"""
   
