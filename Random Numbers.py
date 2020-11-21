import random

a = random.random()  # generates a random float number between 0 and 1
print(a)

b = random.uniform(1, 10)  # generates a float number between the 2 given inputs
print(b)

c = random.uniform(1, 20)  # generates a float number between the 2 given inputs. Include upper bound
print(c)

d = random.randint(1, 20)  # generates a number between the 2 given inputs. NOT Include upper bound
print(d)

e = random.normalvariate(0, 1)  # mean is first input and std deviation is 2nd input
print(e)

mylist = list("ABCDEFGH")
f = random.choice(mylist)
g = random.sample(mylist, 3)
h = random.choices(mylist, k=3)
random.shuffle(mylist)
print(f)
print(g)
print(h)
print(mylist)

random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))

random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))

import secrets

a = secrets.randbelow(10)
print(a)
b = secrets.randbits(4)  # 4 bits means 4 random binary number. Max for 1111 which amounts to 15
# (1111 is 2^3 + 2^2 + 2^1 + 2^0)
print(b)

mylist2 = list("ABCEDFGH")
c = secrets.choice(mylist)
print(c)

import numpy as np

a = np.random.rand(3, 4)
print(a)

b = np.random.randint(0, 10, (3, 4))
print(b)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
np.random.shuffle(arr)
print(arr)

np.random.seed(1)  # use seed method from numpy rather than just random seed method
print(np.random.rand(3, 3))
np.random.seed(1)
print(np.random.rand(3, 3))
