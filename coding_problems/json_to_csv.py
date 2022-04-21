# https://www.udemy.com/course/advanced-exercises-python-programming/learn/quiz/5221962#overview

def json_to_csv(json_file, csv_file):
    import json
    import csv
    with open(json_file, 'r') as json_data:
        json_data = json.load(json_data)
        with open(csv_file, 'w') as csv_data:
            writer = csv.writer(csv_data)
            writer.writerow(['id', 'first_name', 'last_name', 'email', 'gender', 'is_active'])
            for user in json_data:
                writer.writerow([user['id'], user['first_name'], user['last_name'], user['email'], user['gender'], user['is_active']])

json_to_csv('coding_problems/users.json', 'coding_problems/users.csv')