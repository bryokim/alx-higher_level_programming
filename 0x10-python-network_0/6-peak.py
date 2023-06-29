#!/usr/bin/python3
"""Find the peak in a list"""

def find_peak(list_of_integers):
    """Find the peak in a list"""
    if not list_of_integers:
        return None
    
    return heapify(list_of_integers)

def heapify(arr):
    """Heapify an array"""
    size = len(arr)
    i = (size - 1) // 2 

    while i >=0 :
        left = 2 * i + 1
        swap = i
        if left < size and arr[swap] < arr[left]:
            swap = left

        if (left + 1 < size) and arr[swap] < arr[left + 1]:
            swap = left + 1

        if swap != i:
            temp = arr[i]
            arr[i] = arr[swap]
            arr[swap] = temp
        i -= 1

    return arr[0]
