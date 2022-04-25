def flatten(array):
    """
    Flatten a nested array.
    """
    result = []
    for element in array:
        if isinstance(element, list):
            result.extend(flatten(element))
        else:
            result.append(element)
    return result