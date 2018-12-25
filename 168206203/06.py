# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 19:04:07 2018

@author: Yan
"""

 
# 归并函数，将相邻的两个区间合并为一个

def MergeSort(lists):
    if len(lists) <= 1:
        return lists
    num = int( len(lists) / 2 )
    left = MergeSort(lists[:num])
    right = MergeSort(lists[num:])
    return Merge(left, right)
def Merge(left,right):
    r, l=0, 0
    result=[]
    while l<len(left) and r<len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result
lists=[1, 2, 3, 4, 5, 6, 7, 90, 21, 23, 45]
print(MergeSort(lists))
