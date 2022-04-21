#https://www.udemy.com/course/advanced-exercises-python-programming/learn/quiz/5221610#overview

def binary_to_int():
    """
    Converts a binary number to an integer
    """
    with open('coding_problems/binary.txt', 'r') as f:
        lines = f.read().split('\n')

    return [ int(x, base=2) for x in lines ]

print(binary_to_int())