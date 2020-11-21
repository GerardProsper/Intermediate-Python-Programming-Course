
#Errors and Exceptions

#syntax error
# a = 5 print(a)

#type error
#a = 5 +'10'

#module not found error. typing the wrong

#name error
#a = 5, b = c

#file not found error. opening some file that doesnt exist

#value error. when the value is not in list and others

#index error. trying to access index that doesnt exist

#key error. when key is not in dictonary

# x = -5
# # if x < 0:
# #     raise Exception ('x should be positive')
#
# assert(x>=0), 'x is not positive' # will get Assertion Error if statement is false

try:
    #a = 5/0 #will get zero division error
    a = 5/1
    #b = a + '10'
    b = a + 10
# except:
#     print('an error happened')
# except Exception as e:
#     print(e)
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('No errors')
finally:
    print('Cleaning up......')

class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x >100:
        raise ValueTooHighError('Value is too high')
    if x < 5:
        raise ValueTooSmallError('Value is too small',x)
try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)


