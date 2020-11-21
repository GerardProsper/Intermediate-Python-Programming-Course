
# Javascript object notation

import json

# person = {"name": "Gerard", "age":30, "city":"Melaka", "hasChildren":False, "titles":["engineer", "pilot"]}
#
# personJSON = json.dumps(person, indent=4, sort_keys=True) #this is in JSON format
# # print(personJSON)
#
# # with open('person.json','w') as file:
# #     json.dump(person,file, indent=4)
#
# person = json.loads(personJSON) #changing into python format. load from a string is 'loads'
# print(person)
#
# with open('person.json','r') as file: #loading from JSON file
#     person = json.load(file)
#     print(person)

class User:

    def __init__(self,name,age):
        self.name = name
        self.age = age

user = User('Gerard', 30)

def encode_user(o):
    if isinstance(o, User):
        return{'name':o.name, 'age':o.age, o.__class__.__name__:True}
    else:
        raise TypeError('Object of type Iser is not JSON serializable')

userJSON = json.dumps(user, default=encode_user)
print(userJSON)

from json import JSONEncoder

class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o,User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)

userJSON = UserEncoder().encode(user) #this is in JSON format
print(userJSON)

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'],age=dct['age'])
    return dct


user = json.loads(userJSON, object_hook=decode_user) #this is in python format
print(user.name)
print(user.age)
print(type(user))


