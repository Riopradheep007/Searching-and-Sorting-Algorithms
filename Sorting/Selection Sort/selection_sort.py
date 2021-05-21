#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 14:50:08 2021

@author: pradheep
"""

"""
find the minimum value placed in the left side
very worst algorithm

Best case O(n^2)
worst case O(n*2)
"""
def selection_sort(ls):

	for i in range(len(ls)):
	    min_var=i
	    for j in range(i,len(ls)):
    		if ls[j]<ls[min_var]:
    		    min_var=j
	    ls[i],ls[min_var]=ls[min_var],ls[i]
	print(ls)


ls=[0,7,3,5,2,8,6,1,2]
selection_sort(ls)
