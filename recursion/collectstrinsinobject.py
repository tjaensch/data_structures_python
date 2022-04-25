def collectStrings(obj):
    arr = []
    for key, value in obj.items():
      if type(value) is str:
        arr.append(value)
      if type(key) is dict:
        arr = arr + collectStrings(key)
    return arr

print(collectStrings({'hello':'blah'}))