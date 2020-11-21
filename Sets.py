# #Sets:unordered, mutable, no duplicates
#
# myset = {1,2,3,1,2}
# print(myset)
#
# myset2 = set("Hello")
# print(myset2)
#
# myset3 = {} #this is a dictionary and not a set
# print(myset3)
# print(type(myset3))
#
# myset4 = set() #this is a set
# print(myset4)
# print(type(myset4))
# myset4.add(3)
# myset4.add(7)
# myset4.add(5)
# myset4.add(8)
# # print(myset4)
# # myset4.discard(3)
# # myset4.pop()
# # print(myset4)
#
# if 7 in myset4:
#     print('yes')
#
# odds = {1,3,5,7,9}
# evens = {0,2,4,6,8}
# primes = {2,3,5,7}
#
# u = odds.union(evens)
# print(u)
#
# i = odds.intersection(evens)
# print(i)
#
# i2 = odds.intersection(primes)
# print(i2)
#
# setA = {1,2,3,4,5,6,7,8,9}
# setB = {1,2,3,10,11,12}
#
# diff = setA.difference(setB) #will show what is in set A that is not in set B
# print(diff)
#
# diff2 = setB.difference(setA) #will show what is in set B that is not in set A
# print(diff2)
#
# diff3 = setA.symmetric_difference(setB) #will NOT show the same items in both sets & only show the different items
# print(diff3)
#
# diff4 = setB.symmetric_difference(setA) #same as diff3
# print(diff4)
#
# # setA.update(setB)
# # print(setA) #will change set A obviously
#
# # setA.intersection_update(setB)
# # print(setA)
#
# # setA.difference_update(setB)
# # print(setB)
#
# setA.symmetric_difference_update(setB)
# print(setA)

# setA = {1,2,3,4,5,6}
# setB = {1,2,3}
# setC = {7,8}
#
# print(setA.issubset(setB)) #All the elements of the first set is the elements of second set
# print(setB.issubset(setA)) #All the elements of the first set is the elements of second set
#
# print(setA.issuperset(setB)) #All the elements of the first set contains all the elements of second set
# print(setB.issuperset(setA))
#
# print(setA.isdisjoint(setB))# if both sets are null/no same elements
# print(setA.isdisjoint(setC))

# setA = {1,2,3,4,5,6}
#
# setB = setA #this will change original set when new set is changed
# setC = setA.copy() #this will NOT change original set when new set is changed
# setD = set(setA) #this will NOT change original set when new set is changed
#
# setB.add(7)
# print(setB)
# print(setA)

# a =frozenset([1,2,3,4]) #will not allow a change of set
#
# a.add(2) #will not happen
# a.remove(3) #will not happen
#
# #union and intersection method will work though for frozenset
