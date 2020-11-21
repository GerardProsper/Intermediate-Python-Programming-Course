import functools


# def start_end_decorator(func):
#
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):# if def wrapper(), it does not take any argument hence
#                                 # add5(10) will not work. Need to change it to *args,**kwargs then will work
#                                 # for add5(10) when postional arguments are given
#         print('Start')
#         #Do.....
#         result = func(*args,**kwargs)    #Need to change () to (*args,**kwargs) if arguments have
#         #Do ........
#         print('End')
#         return result
#     return wrapper
#
# @start_end_decorator
# # def print_name():
# #     print('Alex')
#
# #print_name = start_end_decorator(print_name)
#
# # print_name()
#
# def add5(x):
#     return x + 5

# result = add5(10)
# print(result)

# print(help(add5))
# print(add5.__name__)

# def repeat(num_times):
#
#     def decerator_repeat(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decerator_repeat
#
#
# @repeat(num_times=3)
# def greet(name):
#     print(f'Hello {name}')
#
# greet('Gerard')

#
# def start_end_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):  # if def wrapper(), it does not take any argument hence
#         # add5(10) will not work. Need to change it to *args,**kwargs then will work
#         # for add5(10) when postional arguments are given
#         print('Start')
#         # Do.....
#         result = func(*args, **kwargs)  # Need to change () to (*args,**kwargs) if arguments have
#         # Do ........
#         print('End')
#         return result
#
#     return wrapper
#
# def debug(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         args_repr = [repr(a) for a in args]
#         kwargs_repr = [f"{k}={v!r}" for k,v in kwargs.items()]
#         signature = ", ".join(args_repr + kwargs_repr)
#         print(f"Calling {func.__name__}({signature})")
#         result = func(*args, **kwargs)
#         print(f"{func.__name__!r} returned {result!r}")
#         return result
#     return wrapper
#
#
# @debug #the decorators will be execute the first func
# @start_end_decorator
# def say_hello(name):
#     greeting = f'Hello {name}'
#     print(greeting)
#     return greeting
#
#
# say_hello('Gerard')

class CountCalls:

    def __init__(self,func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)

@CountCalls  #class decorator, maintain and update a state
def say_hello():
    print('Hello')

say_hello()
say_hello()