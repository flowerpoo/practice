# word count 
"""
from collections import Counter
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

# plot

import matplotlib as p

def chart():
    xvalue=range(1,10)
    yvalue=[1,3,2,4,3,5]
    p.plot(xvalue,yvalue)
    p.xlabel('X Values')
    p.ylabel('Y Values')
    p.show()
chart()
