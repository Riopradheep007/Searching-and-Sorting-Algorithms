#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 19:28:21 2021

@author: kpr
"""

'''
worst case  O(n^2)
best case   O(n)
'''
   """
    last element is the highest number fix that number compare the other number
    worst case O(n^2)
    """
def bubble_sort(ls):
    """
    last element is the highest number fix that number compare the other number
    wordt case O(n^2)
    """
    for i in range(len(ls)-1,0,-1):
        for j in range(i):
            if ls[j]>ls[j+1]:
                ls[j],ls[j+1]=ls[j+1],ls[j]
    return ls
ls=[10,9,8,7,6,5,4,3,2,1]
print(bubble_sort(ls))
