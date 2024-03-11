
arr = [63, 35, 21, 11, 29, 10, 89, 90]

def quick_sort (arr):
    if len (arr) <=1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quick_sort((left) + [pivot] + quick_sort (right))
sorted_array = quick_sort(arr)

print( "sorted_array is: ", sorted_array)
