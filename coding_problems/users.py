#https://www.udemy.com/course/advanced-exercises-python-programming/learn/quiz/5221960#overview

import json


def filter_active_users():
    with open("coding_problems/users.json", "r") as f:
        users = json.load(f)

    active = [user for user in users if user['is_active']]

    open("coding_problems/active_users.json", "w").write(json.dumps(active, indent=2))

    return users

print(filter_active_users())