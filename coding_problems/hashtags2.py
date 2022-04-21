#https://www.udemy.com/course/advanced-exercises-python-programming/learn/quiz/5221608#overview

def clean_hashtags(input_file, output_file, length):
    with open(input_file, 'r') as f:
        lines = f.read().split(' ')

    cleaned = [x for x in lines if len(x) <= length + 1]
    result = sorted(set(cleaned))

    with open(output_file, 'w') as file:
        for hashtag in result:
            file.write(hashtag + '\n')

clean_hashtags('coding_problems/hashtags.txt', 'coding_problems/clean.txt', 5)