# Create an array of size 10 randomly
from random import randint
def create_array(length= 2, maxint= 50):
    new_arr = [randint(0,maxint) for _ in range(length)]
    return new_arr

def merge(a,b):
    c = []
    a_idx, b_idx = 0, 0
    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            c.append(a[a_idx])
            a_idx += 1
        else:
            c.append(b[b_idx])
            b_idx += 1
    if a_idx == len(a): 
        c.extend(b[b_idx:])
    else: 
        c.extend(a[a_idx:])
    return c
# Merge Sorting
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    left, right = merge_sort(arr[0:len(arr)/2]), merge_sort(arr[len(arr)/2:])
    return merge(left, right)
    
a = create_array()
print(a)

b = merge_sort(a)
print(b)
