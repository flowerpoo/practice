"""def add(item,qual):
    print(f"added{item} with this{qual}")

add("app",3)"""

"""def greet_user(name="bleady"):
    print(f"{name} welcome")

#greet_user("poo")
greet_user()"""

"""def calc(*args):
    total=sum(args)
    averg= total/len(args)
    print(averg)
calc(2,4,6)"""

"""def calcul_area(length,width):
    area=length*width
    print(area)
calcul_area(2,2)
print(area)"""

"""def calcul_total(*prices):
    total=sum(prices)
    print(total)
item=[2,2,2]
calcul_total(2,2,2)
#print(area)"""

"""def calcul(length,width):
    area=length*width
    perimeter=2*(length+width)
    return area,perimeter
rec_area,rec_peri= calcul(2,2)
print(calcul(2,2))
#print(rec_peri)"""

"""def get_userdetail(user_id):
    name="poo"
    email="khdjk@bm"
    age=23
    return email,age,name
#user_name,user_dog,user_a=get_userdetail(12)
user_email,user_name,user_a=get_userdetail(12)
print(user_email)"""

products:{
    1:{'name':'poo', 'category':'excellent','price':'10000000'},
    2:{'name':'chendur', 'category':'worst','price':'1'},
    3:{'name':'vish', 'category':'ok','price':'100'},
}

"""def product_search(**kwargs):
    mached_product=[]
    for products_id, attributes in products.items():
        if all(attributes.get(key)== value for key, value in kwargs.items()):
            mached_product.append((products_id, attributes))
    return mached_product
result = product_search(category='worst',price=1)
for products_id, attribute in result:
    print(products_id)
    print(attribute['name'])
    print(attribute['categoty'])
    print(attribute['price'])"""

"""customer_balance={
    123: 1200,
    234:500,
    456:1000
}

def process_transaction(customer_id,transaction_amount):
    if customer_id not in customer_balance:
        print("customer not found")
        return
    balance=customer_balance[customer_id]
    newbalance= balance - transaction_amount
    customer_balance[customer_id]=newbalance

    print("customer id", customer_id)
    print("current balance", newbalance)

process_transaction(12,200)"""

"""def analyz_sensor_data(temperature,humidity,pressure):
    averg_temp= calculate_average(temperature)
    max_humidity= max(humidity)
    min_pressure= min(pressure)
    return averg_temp,max_humidity,min_pressure"""

"""import prac
prac.example()"""

"""import datetime as d

curdat = d.datetime.now()
print(curdat)"""

"""import math 
import os
import random
squar= math.sqrt(25)
print(squar)
c=os.getcwd()
print(c)
rn= random.randint(1,100)
#print(rn)
myli=[1,2,3,4,5]
myra=random.choice(myli)
print(myra)
"""

"""from collections import Counter
def word_count(poo):
    try:
        with open (poo, 'r')as  file:
            text= file.read()
        words=text.lower().split()
        word_counts=Counter(words)
        print("word count")
        for word, count in word_counts.items():
            print(f"{word.capitalize()}:{count}")
    except FileNotFoundError:
        print ("fime not found")
    except Exception as e:
        print(f"Error:{e}")
word_count("poo.txt")
"""
import matplotlib.pyplot as py
def plat_chart():
    xvalue=range(1,7)
    yvalue=[1,3,2,4,6]

    py.plot(xvalue,yvalue)
    py.xlabel('X values')
    py.ylabel(' Y values')
    py.show()

plat_chart()
 



