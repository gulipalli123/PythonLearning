# Tuples hold records; each item in the tuple holds the data for one field and the position of the item  gives its meaning
# If you think of a tuple  just as an immutable list,  the quantity ad the order of the items may or may not be important
# But when using a tuple as a collection of fields, the number of items is often fixed and their order is vital.

# Tuple used as records
# Note that in every expression sorting the tuple would destroy the information because the meaning of each item 
# is given by its position in the tuple
lax_coordinates = (33.95123, -118.40867)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveller_ids = [('USA', '31189567'), ('BRA', 'CE34512'), ('ESP', 'XSA32083')]

for passport in sorted(traveller_ids):
    print('%s/%s' % passport)

# tuple unpacking - the below for loop knows how to retrieve the items of a tuple separately - this id called tuple unpacking
for country, _ in traveller_ids:
    print(country)

# The most visible form of tuple unpacking is parallel assignment
lax_coordinates_e = (23.67, -34.526)

# another example of tuple unpacking is prefixing an argument with a star when calling a function
print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))
# enabling functions to return multiple values in a way that is convenient to the user  - is anohter use of tuple unpacking
quotient, remainder = divmod(*t)
print(quotient, remainder)

# os.path.split() builds a tuple (path, lastpart) from a filesystem path
import os
_, filename = os.path.split('/home-kiran/.ssh/idrsa.pub')
print(filename)

# _ is one of the way to use when we want only specific variables in the tuple
# there is another better way of focusing on just some of the items when unpacking a tuple is to use *
# Defining function parameters with *args to grab arbitrary excess arguments is a classic python feature

a, b, *rest = range(5)
print(a, b, rest)
a, b, *rest = range(3)
print(a, b, rest)
a, b, *rest = range(2)
print(a, b, rest)

# In the context of parallel assignment, the * prefix can be applied to exactly one variable , but it can appear in any position
a, *body, c, d = range(5)
print(a, body, c, d)

#Nested tuple Unpacking
metro_areas = [('Tokyo', 'JP', 36.933, (35.689722, 139.675423)),
                ('Delhi NCR', 'IN', 21.935, (28.613889, -77.08992))]
print('{:15} | {:^9} | {:^9}'.format('', '.lat', '.long'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))

#Named Tuples: Tuples are handy but there is a missing feature while using them as records. Sometimes it is desirable to name the fields.
#For this reason, namedtuples came. 
#The collections.namedtuple function is a factory that produces subclasses of tuple enhanced with field names and a class name
#Card = collections.namedtuple('Card', ['rank', 'suit'])

# Defining andd using a named tuple
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.675423))
print(tokyo)

#Named tuple attributes and methods
print(City._fields)                                                     #_fields is a tuple with the field names of the class
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208999))
delhi = City._make(delhi_data)                                         #_make allow to instantiate a named tuple from an iterable
print(delhi._asdict())                                                 #_asdict() returns collections.OrderedDict built from the named tuple inst

#Tuples role as an immutable variant of the list type

# When using a tuple as an immutable variation of list, it helps to know how similar they actually are.
# Tuple supports all list methods that do not involve adding or removing items
# methods and atrributes found in list or tuple
#|   method                 | list  | tuple| Description     |
#| s.__add__(s2)            | yes   | yes  | s + s2 --concatenation |
#| s.__iadd__(s2)           |yes    | no   |  s +=s2 -- in-place concatenation   |
#| s.append(e)              |yes    | no   | append one element after last    |
#| s.clear()                |yes    | no   | delete all items     |
#| s.__contains(e)          |yes    | yes  | e in s    |
#| s.copy()                 |yes    | no   | Shallow copy of the list    |
#|s.count(e)                |yes    | yes  | count occurences of an element     |
#|s.__delitem__(p)          |yes    | no   |  remove item at position p    |
#|s.extend(it)              |yes    | no   |  Append items from iterable it   |
#|s.__getitem__(p)          |yes    | yes  |  Get item at position p    |
#|s.__getnewargs__()        | no    | yes  |. Support for optimized serialization with pickle     |
#|s.index(e)                |yes    | yes  |. Find position of first occurrence of e     |
#|s.insert(p, e)            |yes    | no   | Insert element e before the item at position p     |
#|s.__iter__()              |yes    | yes  | Get iterator     |
#|s.__len__()               |yes    | yes  | len(s) - number of items     |
#|s.__mul__(n)              |yes    | yes  | s * n -- repeated concatenation     |
#|s.__imul__(n)             |yes    | no   | s *=n -- in-place repeated concatenation     |
#|s.__rmul__(n)             |yes    | yes  | n * s -- reversed repeated concatenation     |
#|s.pop([p])                |yes    | no   | Remove and return last item or item at optional position p    |
#|s.remove(e)               |yes    | no   | Remove first occurrence of element e by value     |
#|s.reverse()               |yes    | no   | reverse thew order of the items in place     |
#|s.__reversed__()          |yes    | no   | Get iterator to scan items from last to first     |
#|s.__setitem__(p, e)       |yes    | no   | s[p] = e - put e in position p, overwriting existing item     |
#|s.sort([key], [reverse])  |yes    | no   | Sort items in place with optional keyword arguments key and reverse     |
