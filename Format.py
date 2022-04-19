import json
from pprint import pprint

with open('group_people.json', 'r') as file:
    work = json.load(file)
counting_people = {}
for i in work:
    group = i['id_group']
    persons = 0
    for val in i['people']:
        if val['gender'].lower() == 'female' and val['year'] >= 1977:
            persons += 1
    counting_people[group] = persons
winner = max(counting_people.values())
for key, value in counting_people.items():
    if value == winner:
        print(key, value)
