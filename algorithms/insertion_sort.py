# divide array into two parts, take first element from unsorted array and find correct position in sorted array
# space efficient, but not stable, useful when continuou inflow of numbers
def insertion_sort(arr):
    # always start from the second element
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

arr = [5, 2, 4, 6, 1, 3]
print(insertion_sort(arr))