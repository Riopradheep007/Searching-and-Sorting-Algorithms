#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: pradheep
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

    for i in range(len(ls)-1,0,-1):
        for j in range(i):
            if ls[j]>ls[j+1]:
                ls[j],ls[j+1]=ls[j+1],ls[j]
    return ls
ls=[10,9,8,7,6,5,4,3,2,1]
print(bubble_sort(ls))
