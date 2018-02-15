import random
import turtle as t 
#generate 2 numbers between 1 and 6 inclusive
'''
d1 = random.randint(1,6)
d2 = random.randint(1,6)

print(d1,d2)'''

'''
for i in range(2):
    random_num1= random.randint(1,7)
    random_num2= random.randint(1,7)
    print(random_num1)
    print(random_num2)
    
'''

def square(size):
    for i in range(4):
        t.forward(size)
        t.right(90)
        t.speed(100)

square(random.randint(10,100))

for i in range(25):
    square(random.randint(10,100))
    
        
