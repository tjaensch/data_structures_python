def balanced_parentheses(string):
    """
    Given a string of parentheses, check if it's balanced.
    """
    stack = []
    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

print(balanced_parentheses('((()))'))