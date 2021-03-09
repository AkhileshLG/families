# code here
from typing import Any

import json

# some dictionaries
p1 = { "name":"Dad", "job":"scientist", "residence":"United States", "color":"blue"}
p2 = { "name":"Mom", "job":"pharmacist", "residence":"United States", "color":"red"}
p3 = { "name":"Akhil", "job":"high schooler", "residence":"United States", "color":"grey"}
p4 = { "name":"Grandfather", "job":"retired", "residence":"India", "color":"yellow"}
p5 = { "name":"Grandmother", "job":"retired", "residence":"India", "color":"brown"}

# a list of dictionaries
family = [p1, p2, p3, p4, p5]
# write some code to Print List of people one by one
print("List of people")
print(type(family))
print(family)
for person in family:
    print(person['name'] + "," + person['job'] + "," + person['residence'] + "," + person['color'])
print()

# turn list to dictionary of people
dict_people = {'people': family}
print("Dictionary of people")
print(type(dict_people))
print(dict_people)

# write some code to Print People from Dictionary
##list_of_people2 = dict_people ['people']
for person in dict_people['people']:
    print(person['name'] + " = " + person['job'] + " = " + person['residence'] + " = " + person['color'])
print()



# turn dictionary to JSON (aka string)
json_people = json.dumps(family)
print("turning dictionary to JSON...")
print(type(json_people))
print(json_people)
# write some code to print a space between each character of JSON
# hint use print(char, end ="-")
# INSERT CODE HERE






# turn dictionary to JSON, this can be sent via a browser
json_people = json.dumps(family)
# the result is a JSON file:
print("JSON People #2")
print(type(json_people))
print(json_people)
# write some code to unwind JSON using json.loads and print the people
# INSERT CODE HERE
print()

list_of_people = json.loads(json_people)
print(type(json_people))
print(type(family))

print(family)
for person in family:
    print(person['name'] + "," + person['job'] + "," + person['residence'] + "," + person['color'])
