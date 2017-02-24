#!/bin/env python

def sort_and_count(a):
    if len(a) == 1: 
        return a, 0
    m = len(a)/2
    left, x = sort_and_count(a[:m])
    right, y = sort_and_count(a[m:])
    sorted_list, z = merge(left,right)
    return sorted_list, x+y+z

def merge(left,right):
    split_count = 0 
    sorted_list = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            sorted_list.append(left[0])
            left.pop(0)
        else:
            sorted_list.append(right[0])
            right.pop(0)
            split_count += len(left)
    while len(left) > 0:
        sorted_list.append(left[0])
        left.pop(0)
    while len(right) > 0:
        sorted_list.append(right[0])
        right.pop(0)
    return sorted_list, split_count

a = []
with open('IntegerArray.txt') as myfile:
    for line in myfile:
        a.append(int(line.strip('\n')))
print sort_and_count(a)[1]
