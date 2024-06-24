#1
class str():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input()

    def print_String(self):
        print(self.str1.upper())

str1 = str()
str1.get_String()
str1.print_String()
#2
class filterprime:
    def init(self, a):
        self.a = a

    def filter_prime(y):
        y=[]
        for i in range(len(a)):
           if a[i] == 1:
                continue
           t = True
           for j in range(2, a[i]):
                if a[i] % j == 0:
                   t = False
                   break
           if t == True:
                y.append(a[i])
        print(y)

a = [int(x) for x in input().split()]
print(a)
p = filterprime(a)
p.filter_prime()
#3
class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self):
        Shape.__init__(self)
        self.lenght=int(input())

    def area(self):
        return self.lenght*self.lenght

sqr=Square()
print(sqr.area())
#4
class Account:
    owner = " "
    balance = 0
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    
    def __str__(self):
        return f'Account owner: {self.owner} \nAccount balance: {self.balance}'
    
    def deposit(self, amount):
        self.balance += amount
        return "Deposit Accepted"
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return "Withdrawl Accepted:"
        return "Funds Unavailable!"
#5
import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def show(self):
        return self.x, self.y


    def move(self, x, y):
        self.x += x
        self.y += y


    def dist(self, pt):
        dx = pt.x - self.x
        dy = pt.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)

p1 = Point(2, 3)
p2 = Point(3, 3)

p1.show()
p2.show()

p1.move(5, -4)
p1.show()

p1.dist(p2)
#6
class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, l, w):
        self.lenght=l
        self.width=w

    def area(self):
        return self.lenght*self.width

rct=Rectangle(5,9)
print(rct.area())