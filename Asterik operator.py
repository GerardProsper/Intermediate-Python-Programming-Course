
result = 7*8
print(result)

result = 2**4  # power operation
print(result)

zeros = [0,1] * 10
print(zeros) #this is a list

zeros = (0,1) * 10
print(zeros) #this is a tuple

zeros = "AB" * 10
print(zeros)



def foo(a,b,*args,**kwargs):
    print(a)
    for arg in args: #args is a tuple
        print(arg)
    for key in kwargs: #kwargs is a dict
        print(key, kwargs[key])

foo(1,2,3,4,5, six=6, seven=7)



numbers = [1,2,3,4,5,6]

*beginning, last = numbers
print(beginning) # will unpack into list no matter if tuple of list initially. will unpack all items execept last item
print(last) # will unpack only last number




numbers = (1,2,3,4,5,6)

beginning, *middle, secondlast, last = numbers
print(beginning) # will unpack first number only
print(middle) # will unpack all middle numbers
print(secondlast)
print(last) # will unpack only last number



my_tuple = (1,2,3)
my_list = [4,5,6]

new_list = [*my_tuple, *my_list]
print(new_list)

my_tuple = (1,2,3)
my_set = {4,5,6} #this is a set

new_list = [*my_tuple, *my_set]
print(new_list)



dict_a = {'a':1, 'b':2}
dict_b = {'c':3, 'd':4}
my_dict = {**dict_a, **dict_b}
print(my_dict)