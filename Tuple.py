
# Tuple: ordered, immutable, allows duplicate elements # list and tuple only difference is list is mutable

# mytuple = 'Max', 28, 'Boston'
# mytuple = ('Max',) # must add coma to make it a tuple if not str


# mytuple = tuple(['Max', 28 , 'Boston'])
# print(mytuple)
#
# if 'Max' in mytuple:
#     print('yes')
# else:
#     print('no')
#
# my_tuple = ('a','b','c','d','e')
#
# print(len(my_tuple))
# print(my_tuple.count('e'))
# print(my_tuple.index('a'))
#
# mylist = list(my_tuple)
# print(mylist)
#
# my_tuple2 = tuple(mylist)
# print(my_tuple2)
#
# a=(1,2,3,4,5,6,7,8,9)
# b=a[2::-1]
# print(b)

# my_tuple = 'Max', 28, 'Boston'
#
# name, age, city = my_tuple
# print(name)
# print(age)
# print(city)
#
# my_tuple = 1,2,3
#
# i1,i2,i3 = my_tuple
# print(i1)
# print(i2)
# print(i3)

# my_tuple = 1,2,3,4,5,6
#
# i1,*i2,i3,i4 = my_tuple #the star prints everything in between the whole i
# print(i1) #this will be 1
# print(i3) # this will be 5
# print(i2) # this will be 2,3,4

# import sys
# my_list = [0,1,2, 'hello',True]
# my_tuple = (0,1,2, 'hello',True)
# print(sys.getsizeof(my_list),'bytes') #list has higher bytes - 96
# print(sys.getsizeof(my_tuple),'bytes') #tuple has lower bytes - 80

# import timeit
# print(timeit.timeit(stmt = "[0,1,2,3,4,5]",number = 1000000)) #list take more time to compute than tuple
# print(timeit.timeit(stmt = "(0,1,2,3,4,5)",number = 1000000)) #tuple is more efficient than list

