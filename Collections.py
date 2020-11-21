# Collections: Counter, namedtuple, orderedDict, defaultdict, deque

from collections import Counter

a="aaaaaaaabbbbccccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.values())
print(my_counter.most_common(1)[0][0]) #most common in the string
print(list(my_counter.elements()))


from collections import namedtuple

Point = namedtuple('Point','x,y')
pt = Point(1,-4)
print(pt)
print(pt.x,pt.y)

from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict = {}
ordered_dict['a'] = 1
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['b'] = 2
print(ordered_dict)
# normal dictonaries now can still remember the order as old Python couldn't

from collections import defaultdict

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['b'])

from collections import deque

d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)

d.pop()
print(d)

d.popleft()
print(d)

# d.clear()
# print(d)

d.extend([4,5,6])
print(d)

d.extendleft([6,7,9])
print(d)

d.rotate(-2) #will rotate items to the right if positve and left if negative
print(d)