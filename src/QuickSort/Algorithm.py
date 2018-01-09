'''
Created on Feb 4, 2014

@author: Starfox
'''

def quickSort(array): 
    if len(array) <= 1:
        return array
    else:
        quickSort([x for x in array[1:] if x<array[0]]) + [array[0]] + quickSort([x for x in array[1:] if x>=array[0]])