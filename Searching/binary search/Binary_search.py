#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 17:33:33 2021

@author: kpr
"""

def binary_Search(ls,low,high,target):
    """
    This algoirithm complixty is O(log n)
    """
    if high>low:
        mid=(high+low)//2
        if ls[mid]==target:
            return mid
        elif ls[mid]>target:
            return binary_Search(ls,low,mid-1,target)
        else:
            return binary_Search(ls,mid+1,high,target)
            
    else:
        return -1
ls=[*range(1,30)]
print(ls)
target=30       
print(binary_Search(ls,0,len(ls)-1,target))

