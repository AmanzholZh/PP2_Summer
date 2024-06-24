#1
def f(gramm):   
      print(28.3495231*gramm)
f(int(input()))
#2
def f():
      F=int(input())
      print((5/9)*(F-32))
f()
#3
def solve(numheads,numlegs):
    for a in range (numheads):
        for b in range (numlegs):
            if(a+b==numheads and 2*a+4*b==numlegs):
                print(a,b)
solve(35,94)
#4
def f(a):
      for i in range(len(a)):
            a[i]=int(a[i])
            ans=True
            if(a[i]==1):
                  ans=False
            for k in range(2,a[i]):
                  if(a[i]%k==0):
                        ans=False
                        break
            if (ans==True):
                 print(a[i])

a=input().split()
f(a)
#5
def un(a):
    b = []
    for i in a:
         if i not in b:
            b.append(i)
    b = " ".join(b)
    print(b)
a = input().split()
un(a)
#6
def f(a):
    b = a[::-1]
    c = " ".join(b)
    print(c)

a = input().split()
f(a)
#7
def has_33():
    a=input().split()
    cnt=0
    for i in range(len(a)-1):
        if(a[i]=="3" and a[i+1]=="3"):
            cnt+=1           
    if (cnt=="0"):
        print("False")
    else:
         print("True")

has_33()
#8
def f(a):
    b=[]
    for i in a:
        if(i=="0"):
            b.append(i)
        elif (i=="7"):
            b.append(i)
    if(len(b)>=3):
        if(b[0]=="0" and b[1]=="0" and b[2]=="7"):
            print("True")
    else:
        print("False")
a=input().split()
f(a)
#9
import math
def f(rad):
    val=(4/3*rad**3*math.pi)
    print(val)
rad=int(input())
f(rad)
#10
import itertools
def f(s):
    s1=itertools.permutations(s)
    for i in s1:
     i = "".join(i)
     print(i)
s=input()
f(s)
#11
def f(s):
    s1=s[::-1]
    if(s==s1):
        print("Yes")
    else:
        print("No")
s=input()
f(s)
#12
def histogram(a):
    for i in range (len(a)):
        print("*"*int(a[i]))
a=input().split()
histogram(a)
#13
import random
def rand():
    a = []
    for i in range(20):
        a.append(i)
    print('Hello! What is your name?')
    print('KBTU')
    print()
    print('Well, KBTU, I am thinking of a number between 1 and 20.')
    print('Take a guess.')
    print(random.choice(a))
    print('')
    print('Your guess is too low.')
    print('Take a guess.')
    print(random.choice(a))
    print('')
    print('Your guess is too low.')
    print('Take a guess.')
    print(random.choice(a))
    print('')
    print('Good job, KBTU! You guessed my number in 3 guesses!')
rand()