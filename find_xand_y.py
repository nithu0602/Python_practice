# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 16:38:00 2021

@author: Nithyashri
"""
#list=[10,1,8,3,6,5,4,7]#x,y]
l1=[]
n=eval(input())
l=n//2
for i in range (0,n):
    if i%2==1:
        no=i
        l1.append(no)
        
    elif i%2==0:
        no=2*l
        l=l-1
        l1.append(no)
print (l1);
        
        
