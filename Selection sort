from random import randint
# Create an array of size 10 randomly
def create_array(length=10, maxint=50):
    new_arr = [randint(0, maxint) for _ in range(length)]
    return new_arr
# Selection sorting
def selection_sort(arr):
    sort_len = 0 
    while sort_len < len(arr):
        min_idx = None
        for i,ele in enumerate(arr[sort_len:]):
            if min_idx == None or ele < arr[min_idx]:
                min_idx = i+ sort_len
        arr[sort_len], arr[min_idx] = arr[min_idx], arr[sort_len]
        sort_len += 1
    return arr

a = create_array()
print(a)

b= selection_sort(a)
print(b)
