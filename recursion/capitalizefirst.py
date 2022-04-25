'''def capitalize_first(s):
    """
    Given a string, capitalize the first letter of each word.
    """
    if len(s) == 0:
        return s
    else:
        return s[0].upper() + capitalize_first(s[1:])'''

def cap_first(arr):
    if len(arr) == 0:
        return arr
    else:
        return [arr[0].title()] + cap_first(arr[1:])

print(cap_first(['hello', 'world']))