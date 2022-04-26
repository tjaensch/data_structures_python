def sumofpairs(arr, num):

  result = []

  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      if (arr[i] + arr[j]) == num:
        t = (arr[i],arr[j])
        result.append(t)
  return result
        

print(sumofpairs([3,5,6,7,2,1,3], 6))