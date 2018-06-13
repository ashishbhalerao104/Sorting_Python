from random import randint
# Create an array of size 10 randomly
def create_array(length =10, maxint = 50):
    new_arr = [randint(0,maxint) for _ in range(length)]
    return new_arr
# Insertion sorting
def insertion_sort(arr):
    for sort_len in range(len(arr)):
        cur_item = arr[sort_len]
        insert_idx = sort_len
        
        while insert_idx > 0 and cur_item < arr[insert_idx - 1]:
            arr[insert_idx] = arr[insert_idx - 1]
            insert_idx -= 1
        a[insert_idx] = cur_item
    return arr
# Check whether an array is sorted correctly or not using built-in sorted method
def is_sorted(arr):
    sorted_arr = sorted(arr)
    return arr == sorted_arr

a = create_array()
print(a)

b= insertion_sort(a)
print(b)

print(is_sorted(a))
