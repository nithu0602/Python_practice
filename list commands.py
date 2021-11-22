# -*- coding: utf-8 -*-
"""
Various builtin commands to use on lists
"""

mylist=['happy', 13,'python','nithu',13]
mylist.append(12)
print(mylist)

list1=mylist.copy()
print(list1)
a=mylist.count(13)
print(a)

pos=[6,12,1,-4,0]
pos.sort()
print(pos)

num=[2,5,8-1,3]
num.extend(pos)
print(num)
print(num.index(2))

myl=[1,4,6,7]
myl.insert(2,5)
print(myl)

myl.pop(3)
print(myl)