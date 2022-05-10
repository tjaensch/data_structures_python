#divide and conquer algorithm
#find pivot number and make sure smaller numbers located at the left of pivot
#and larger numbers located at the right of pivot
#unlike merge sorge extra space is not used

def quick_sort_recursion(arr):
    # base case
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort_recursion(less) + [pivot] + quick_sort_recursion(greater)

print(quick_sort_recursion([10, 5, 2, 3]))