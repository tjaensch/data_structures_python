#https://www.udemy.com/course/advanced-exercises-python-programming/learn/quiz/5221968#overview

def json_to_object():
    import json
    from collections import namedtuple
    
    with open('coding_problems/users.json', 'r') as json_data:
        users = []

        json_data = json.load(json_data)
        for user in json_data:
            User = namedtuple('User', user.keys())
            user = User(**user)
            users.append(user)

        return users

print(json_to_object())

