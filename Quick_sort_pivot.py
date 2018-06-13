from random import randint
# Create an array of size 10 randomly
def create_array(length= 11, maxint =50):
    new_arr = [randint(0, maxint) for _ in range(length)]
    return new_arr
# Quick sort using Pivot
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    smaller, equal, larger= [], [], []
    pivot = arr[randint(0, len(arr)-1)]
    for i in arr:
        if i < pivot:
            smaller.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            larger.append(i)
    return quicksort(smaller)+equal+quicksort(larger)

a= create_array()
print(a)

b= quicksort(a)
print(b)
