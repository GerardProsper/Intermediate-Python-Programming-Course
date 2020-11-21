
# shallow copy: one level deep, only references of nested child objects
# deep copy:full independent copy

import copy

org = 5
cpy = org
cpy = 6
print(org)
print(cpy)


org = [0,1,2,3,4]
cpy = org
cpy[0] = -10
print(cpy)
print(org)



#shallow copy
org = [0,1,2,3,4]
cpy = copy.copy(org)
# cpy = org.copy() #will make shallow copy. Type 1/3
# cpy = list(org) #will make shallow copy. Type 2/3
# cpy = org[:] #will make shallow copy. . Type 3/3
cpy[0] = -10
print(cpy)
print(org)

org = [[0,1,2,3,4],[5,6,7,8,9]]
cpy = copy.copy(org)
cpy[0][1] = -10
print(cpy) #cpy and org still same
print(org) #cpy and org still same



# deep copy
org = [[0,1,2,3,4],[5,6,7,8,9]]
cpy = copy.deepcopy(org)
cpy[0][1] = -10
print(cpy) #cpy and org NOT same
print(org) #cpy and org NOT same


class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee

p1 = Person ('Mark', 45)
p2 = Person ('Joe', 29)

company = Company(p1,p2)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 46

print(company_clone.boss.age)
print(company.boss.age)

