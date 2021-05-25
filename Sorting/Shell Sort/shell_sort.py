"""
It is a optimization of insertion sort


worst case O(n^2)
average case O(n logn)

"""


def shell_sort(ls):
    gap=len(ls)//2
    while gap>0:
        for i in range(gap,len(ls)):
            current_ele=ls[i]
            pos=i
            while pos>=gap and current_ele<ls[pos-gap]:
                ls[pos]=ls[pos-gap]
                pos=pos-gap
            ls[pos]=current_ele
        gap=gap//2
    return ls
ls=[5,3,7,1,9,2,0,4]
print(shell_sort(ls))
