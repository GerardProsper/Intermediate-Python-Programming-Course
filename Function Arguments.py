
# difference between arguements and parameters

def print_name(name): # name here is parameter
    print(name)

print_name('Gerard') # Gerard here is arguments

def fool(a,b,c):
    print(a,b,c)

fool(1,2,3)
fool(a=1,c=3,b=2) # this is keyword arguments. order doesnt matter
fool(2, b=3, c=5) # this would work but there are errors in different arragement

def fool(a,b,c,d=6): # default arguments must be at the end of parameters
    print(a,b,c,d)

fool(1,2,3)
fool(2,3,4,9)


# if mark parameters with one *, can mark any number of positional arguements thru function. this is tuple.
# if mark parameters with two **, can mark any number of keyword arguements thru function. this is dict
# can call whatever I like. after * or **. just using args and kwargs
def foo(a,b, *args, **kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key,kwargs[key])

# below is variable length arguemnts
foo(1,2,3,4,5, six=6, seven=7) # 1,2 are positional arguments. 3,4,5 are the args and six=6, seven=7 are kwargs
foo(1,2, six=6, seven=7) # can do
foo(1,2,3,4,5) # can do


def foo(a,b, *,c,d):
    print(a,b,c,d)

foo(1,2,c=3,d=4)



def foo(*args,last):
    for arg in args:
        print(arg)
    print(last)

foo(1,2,last=1000)


def foo(a,b,c):
    print(a,b,c)

my_list = [0,1,2] #this is list. numbers must match function
foo(*my_list)
my_tuple = (0,1,2) #this is tuple. numbers must match function
foo(*my_tuple)
my_dict = {'a':1,'b':2, 'c':3} #positional arguments must match above. abc
foo(*my_dict)
my_dict = {'a':1,'b':2, 'c':3} #positional arguments must match above. abc
foo(**my_dict)



def foo():
    x = number
    print('number inside function: ', x)

number = 3
foo()




def foo():
    global number
    x = number
    number = 3 # this is local variable without global above.
    print('number inside function: ', x)

number = 0
foo()
print(number)



def foo():
    number = 3 # this is local variable without global above. This only lives in this function

number = 0
foo()
print(number) #will print number = 0



def foo():
    global number # if want to modify the global number from 0 to 3
    number = 3  # this is local variable without global above. This only lives in this function

number = 0
foo()
print(number)  # will print number = 3



def foo(x):
    x = 5 # mutable objects can be modified in a function

var = 10
foo(var)
print(var)  # var = 10



def foo(a_list):
    a_list = [200,300,400] # this is local variable. Hence will not change my_list= [1,2,3]
    a_list.append(4) # immutable objects within a mutable objects can be changed
    a_list[0] = -100

my_list = [1,2,3]
foo(my_list)
print(my_list)




def foo(a_list):
    a_list += [200,300,400] # this will change my_list 
    a_list = a_list + [200,300,400] # this is local variable. Hence will not change my_list= [1,2,3]

my_list = [1,2,3]
foo(my_list)
print(my_list)
