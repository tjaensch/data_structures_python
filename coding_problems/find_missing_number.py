def find_missing_number(nums):
    """
    Given a list of numbers, find the missing number.
    """
    # Find the sum of all the numbers in the list
    total = sum(nums)
    # Find the sum of all the numbers from 1 to the length of the list
    total_range = (len(nums) + 1) * (len(nums) + 2) // 2
    # Find the difference between the two sums
    return total_range - total

print(find_missing_number([1, 2, 3, 4, 5, 6, 7, 9, 10]))