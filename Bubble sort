from random import randint
# Create an array of size 10 randomly
def create_array(length=10, maxint=50):
    new_arr = [randint(0, maxint) for _ in range(length)]
    return new_arr
# Bubble sorting
def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                swapped = True
    return arr
# Check whether an array is sorted correctly or not using built-in sorted method
def is_sorted(arr):
    sorted_arr = sorted(arr)
    return arr == sorted_arr 

a = create_array()
print(a)

b = bubble_sort(a)
print(b)

print(is_sorted(a))
