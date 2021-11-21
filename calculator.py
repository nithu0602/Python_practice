# -*- coding: utf-8 -*-
"""
SIMPLE CALCULATOR TO FIND SUM, DIFFERENCE, PRODUCT AND QUOTIENT ALONG WITH
EXPONENTS AND FACTORIAL
"""
import math

def add(a,b):
    ans=a+b
    return ans

def sub(a,b):
    
    ans=a-b
    return ans

def prd(a,b):
   
    ans=a*b
    return ans

def div(a,b):
    
    ans= a/b
    return ans

def power(a,b):
   
    ans=a**b
    return ans

def fact(a):
        
    ans=math.factorial(a)
    return ans
    
    

print("Please type in the math operation you would like to complete: ")
print ("+ for addition - for subtraction * for multiplication / for division")
print("e to find power  f for factorial")

ans=0
c=(input())


if c=='+':
    print("Enter 2 nos ")
    a=eval(input())
    b=eval(input())
    print(add(a,b))
    
elif c=='-':
    print("Enter 2 nos ")
    a=eval(input())
    b=eval(input())
    print(sub(a,b))
    
elif c=='*':
    print("Enter 2 nos ")
    a=eval(input())
    b=eval(input())
    print(prd(a,b))
    
elif c=='/':
    print("Enter 2 nos ")
    a=eval(input())
    b=eval(input())
    print(div(a,b))
    
elif c=='e':
    print("Enter 2 nos ")
    a=eval(input())
    b=eval(input())
    print(power(a,b))
    
elif c=='f':
    print("Enter a no")
    a=eval(input())
    print(fact(a))   
    
    
    
    
    
    


