#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 16:16:55 2021

@author: kpr
"""


"""
best case:O( n log n)
worst case:O(n^2)


 When implemented well, it can be somewhat faster than merge sort and about two or three times faster than heapsort.
 
 
 Quick sort is a divide and conquer algorithm

"""
def quick_sort(ls):
    length=len(ls)
    if length<=1:
        return ls
    else:
        pivot=ls.pop()
        small_items=[]
        large_items=[]
        for i in ls:
            if i<pivot:
                small_items.append(i)
            else:
                large_items.append(i)
    return quick_sort(small_items)+[pivot]+quick_sort(large_items)
ls=[4,1,-2,0,7,5,-1]
print(quick_sort(ls))
                