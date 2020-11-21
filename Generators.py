
# def mygenerator():
#     yield 3
#     yield 2
#     yield 1
#
# g = mygenerator()
#
# # for i in g:
# #     print(i)
#
# # value = next(g)
# # print(value)
# #
# # value = next(g)
# # print(value)
#
# #print(sum(g))
#
# print(sorted(g))


# def countdown(num):
#     print("starting")
#     while num > 0:
#         yield num
#         num -= 1
#
# cd = countdown(4)
#
# value = next(cd)
# print(value)
#
# print(next(cd))
# print(next(cd))
# print(next(cd))

import sys

# def firstn(n):
#     nums = []
#     num = 0
#     while num < n:
#         nums.append(num)
#         num += 1
#     return nums
#
# def firstn_generator(n):
#     num = 0   #no need to save all the numbers in the nums
#     while num < n:
#         yield num
#         num += 1

# print(sys.getsizeof(firstn(100000))) #more memory being used at 824456 for 100000
# print(sys.getsizeof(firstn_generator(100000))) #less memory being used at 112 for 100000



# def fibonacci(limit):
#     # 0 1 2 3 5 8 13 ............
#     a,b = 0, 1
#     while a < limit:
#         yield a
#         a, b = b, a + b
#
# fib = fibonacci(30)
#
# for i in fib:
#     print(i)



mygenerator = (i for i in range(10) if i % 2 == 0)
#print(list(mygenerator))
print(sys.getsizeof(mygenerator)) #takes up smaller memory
print(type(mygenerator))

# for i in mygenerator:
#     print(i)

mylist = [i for i in range(10) if i % 2 == 0]
# print(mylist)
print(sys.getsizeof(mylist)) #takes up larger memory
print(type(mylist))

