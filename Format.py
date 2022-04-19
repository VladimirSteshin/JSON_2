import json
from pprint import pprint
with open('group_people.json', 'r') as file:
    work = json.load(file)
counting_people = {}
for i in work:
    group = i['id_group']
    persons = []
    for val in i['people']:
        if val['gender'].lower() == 'female' and val['year'] >= 1977:
            persons.append(val)
    counting_people[group] = persons