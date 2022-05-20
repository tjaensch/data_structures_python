def find_max_product(arr):

  last = sorted(arr)[-1]
  secondlast = sorted(arr)[-2]

  maxp = last * secondlast

  return maxp

print(find_max_product([10,2,3,4,5,3,2]))


def findMaxProduct(array):
    maxProduct = 0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]*array[j] > maxProduct:
                maxProduct = array[i]*array[j]
                pairs = str(array[i])+ "," + str(array[j])
    print(pairs)
    print(maxProduct)

findMaxProduct([10,2,3,4,5,3,2])