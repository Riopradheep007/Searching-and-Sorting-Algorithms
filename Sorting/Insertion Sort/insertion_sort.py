#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 15:21:29 2021

@author: kpr
"""

""" 
left side sorted element  comparing the right side element to sort
worst case O(n^2)
best case O(n)
"""
def insertion_sort(ls):
    for i in range(1,len(ls)):
        current_element=ls[i]
        pos=i
        while current_element<ls[pos-1] and pos>0:
            ls[pos]=ls[pos-1]
            pos-=1
        ls[pos]=current_element
    return ls
ls=[4,3,1,2,5]
print(insertion_sort(ls))
