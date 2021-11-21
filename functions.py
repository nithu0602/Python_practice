# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 23:45:18 2021

@author: Nithyashri

"""
import math

def add(a,b,c):
    sum=a+b+c;
    return sum

def dist(x1,y1,x2,y2):
    i=(x1-x2)**2
    j=(y1-y2)**2
    len=math.sqrt(i+j)
    return len

def welcome():
    print("Hello.")
    
 
print("Select a number 1:add 2:dist 3:welcome")
n=eval(input())

if n==2:
    print("Input the cordinates")
    x1=eval(input())
    y1=eval(input())
    x2=eval(input())
    y2=eval(input())
    print(dist(x1,y1,x2,y2))
    
elif n==1:
    print("Enter 3 numbers ")
    a=eval(input())
    b=eval(input())
    c=eval(input())
    print(add(a,b,c))
    
elif n==3:
    welcome()


    
    

    