def reverse(strng):
  if strng == "":
    return strng
  else:
    return reverse(strng[1:]) + strng[0]

print(reverse('cow'))