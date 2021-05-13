#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 17:17:30 2021

@author: pradheep
"""


"""
      This algorithm complexity is O(n)
      Linear operation check the each and every individual elements one by one
"""
def Linear_search(ls,target):

    for i in ls:
        if i==target:
            return "Element {} is found".format(i)
    return "Not found"
    
ls=[*range(1,100)]
target=99
print(Linear_search(ls,target))
