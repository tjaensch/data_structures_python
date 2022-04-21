def binary_search(arr, ele):
    
    # First and last index of the array
    first = 0
    last = len(arr) - 1

    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if arr[mid] == ele:
            found = True
        else:
            if ele < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(binary_search(arr, 4))