
# # strings : ordered, immutable, text representative
#
# mystring = """Hello \
# World"""
# print(mystring)
#
# mystring2 = "Hello World"
# char = mystring2[3]
# print(char)
#
# # mystring2[2] = 'w' #this would not work as str is immutable
#
# print(mystring2[::-1])
#
# mystring3 = 'Tom'
# combo = mystring2 + ' ' + mystring3
# print(combo)
#
# if 't' in mystring3:  # case sensitive
#     print('Yes')
# else:
#     print('No')
#
# mystring4 = "   Hello World   "
# mystring4 = mystring4.strip()  # have to assign it back to work
# print(mystring4)
#
# print(mystring4.startswith('H'))
# print(mystring4.startswith('Hello'))
# print(mystring4.endswith('d'))
# print(mystring4.endswith('World'))
# print(mystring4.find('o'))  # returns first index of str, can use integer
# print(mystring4.count('o'))
# print(mystring4.replace('W', 'p'))  # will return a new string and not change the original one
# # if can't find the string will return nothing for replace()
#
# mystring5 = 'how are you doing'
# mylist = mystring5.split()  # will convert str to list
# print(mylist)
# newstring = ' '.join(mylist)  # will make list into string
# print(newstring)
#
# mystring6 = 'how,are,you,doing'
# mylist2 = mystring6.split(",")  # will convert str to list
# print(mylist2)
#
# mylist3 = ['a'] * 6
# print(mylist3)
#
# from timeit import default_timer as timer
#
# # this is bad code below
# start = timer()
# my_string = ''
# for i in mylist3:
#     my_string += i
# stop = timer()
# print(my_string)
# print(stop - start, 'timer bad')
# # this is good code
# start = timer()
# my_string = ' '.join(mylist3)
# stop = timer()
# print(my_string)  # same result as above but cleaner
# print(stop - start, 'timer good')
#
# # %,.format(),f-strings
# var = "Tom"
# mystrings = "The variable is %s" % var  # %s is called place holder
# print(mystrings)
#
# var2 = 3.1234567
# mystrings2 = "The variable is %.2f" % var2  # %d is decimal and will show first integer, %f will show float
# print(mystrings2)              # %.2f is 2 decimal places
#
# var3 = 3.12345678
# var4 = 8
# mystrings3 = "The variable is {:.2f} and {}".format(var3,var4)
# print(mystrings3)
#
# var3 = 3.12345678
# var4 = 8
# mystrings4 = f"The variable is {var3*2:.2f} and {var4}"
# print(mystrings4)



