# https://www.udemy.com/course/advanced-exercises-python-programming/learn/quiz/5221602#overview

def clean_hashtags():
    """
    Reads the file and returns a list of hashtags
    """
    with open('coding_problems/hashtags.txt', 'r') as f:
        lines = f.read().split(' ')
    
    cleaned = [x for x in lines if len(x) <= 5]

    result = sorted(set(cleaned))
    
    return result

print(clean_hashtags())