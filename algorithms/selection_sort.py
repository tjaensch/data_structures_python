# repeatedly find minimum element and move to sorted part of array, in place, performs well on small lists, space efficient
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [3, 6, 2, 1, 9, 7, 8, 5, 4]
print(selection_sort(arr))