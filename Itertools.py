# itertools: product, permutations, combinations, accumulate, groupby, and infiite iterators

# from itertools import product
#
# a = [1, 2]
# b = [3]
#
# prod = product(a, b, repeat=2)
# print(list(prod))

from itertools import permutations

a1 = [1, 2, 3]

perm = permutations(a1, 2)
print(list(perm))

from itertools import combinations

a2 = [1, 2, 3, 4]

comb = combinations(a2,2)
print(list(comb))

from itertools import combinations, combinations_with_replacement

a3 = [1, 2, 3, 4]

comb_wr = combinations_with_replacement(a3,2) #will make 1 of itself together with others
print(list(comb_wr))

from itertools import accumulate

a4 = [1, 2, 3, 4]

acc = accumulate((a4)) #will sum the numbers before it and includes itself
print(list(acc))

from itertools import accumulate
import  operator

a5 = [1, 2, 3, 4]

acc2 = accumulate(a4,func=operator.mul) #will multiply the numbers before it and includes itself
print(list(acc2))

a6 = [1, 2, 3, 5, 4]
acc3 = accumulate(a6,func=max) #will show the max number and any number after that will be the max
print(list(acc3))

from itertools import groupby

def smaller_than_3(x):
    return x < 3


a7 = [1,2,3,4]

group_obj = groupby(a7,key=smaller_than_3)
for key,value in group_obj:
    print(key,list(value))

group_obj = groupby(a7,key=lambda x: x<3) #same as above just using lambda function
for key,value in group_obj:
    print(key,list(value))

persons = [{'name':'Tim', 'age':25}, {'name':'Dan', 'age':25},
{'name':'Lisa', 'age':27}, {'name':'Claire', 'age':28}]

group_obj = groupby(persons,key=lambda x: x['age']) #same as above just using lambda function
for key,value in group_obj:
    print(key,list(value))


from itertools import count, cycle, repeat


for z in count(10): #starts at 10 and keeps going
    print(z)
    if z == 15:
        break

a8= [1,2,3]

for x in cycle(a8):
    print(x)
    if x == 3:
        break

for x in repeat(1,6): #will repeat the same number 6 times
    print(x)