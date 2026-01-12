# Building lists of lists
# sometimes we need to initialize a list with a certain number of nested lists- e.g.
# to distribute students in a list of teams or to represent squares on a game board

board = [['_'] * 3 for  i in range(3)]
print(board)
board[1][2] = 'X'
print(board)

# A list  with references  to the same list is useless
weird_board = [['_'] * 3] *  3 # its wrong

#Augmented assignment with Sequences
# augumented assignment - +=, *= etc

# for a  += b , If a implements __iadd__, that will be called. 
# In the case of mutable sequences - list, bytearray, array.array, a will be changed in place.
# However, if __iadd__  is not implemented by a,  the expression a += b has the same effect as a = a + b
# in this case, the expression a + b is evalueated first, producing a new object and which is then bound to a
# In general, for mutable sequences, it is a good bet that __iadd__ is implemented and that += happens in place.
l = [1, 2, 3]
print(l, id(l))
l *= 2
print(l, id(l))
t = (1, 2, 3)
print(t, id(t))
t *= 2
print(t, id(t))

# Repeated concatenation of immutable sequences  is inefficient, because instead of just appending the new items,
# the interpreter has to  copy the whole target sequence to create a new one with the new items concatenated
#(1, 2, 3) 135294861448000
#(1, 2, 3, 1, 2, 3) 135294862948960

t = (1, 2, [30, 40])
print(t, id(t))
#t[2] += [50, 60]
#print(t, id(t))

#Putting mutable items in tuple is not a good idea
#Augmented operation is not atomic operation - it can throw exception after doing its part of operation

#list.sort and the sorted built-in function
# The list.sort methof sorts a list in place, that is without making a copy. It returns None
# to remind us that , it changes the target object and does not create a new list.
#Functions or methods that change object in place, should retunr None to make it clear to the caller
#that the object itself was modified and no new object was created

# The drawback of returning None to signal in-place changes, you cannot cascade calls to those methods

#Incontrast the built-in function sorted creates a new list and returns it
#Both list.sort and sorted take two optional keyword-only arguments
#reverse : if True, the items are returned on reverse order, default value is false
#key: a one-argument function that will be applied to each item to produce its sorting key

fruits = ['grape', 'rasberry', 'apple', 'banana']
print(sorted(fruits))
print(fruits)
print(sorted(fruits, reverse=True))
print(sorted(fruits, key=len, reverse=True))
fruits.sort()
print(fruits)
#Once the sequences are sorted, they can be very efficiently searched

#Managing Ordered Sequences with bisect
#The bisect module offers two main functions - bisect and insort - that use the binary search algorithm 
#to quickly find and insert item in any sorted sequence

#Searching with bisect
import bisect
import sys

HAYSTACK= [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES=[0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))

if __name__ =='__main__':
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

print('DEMO: ', bisect_fn.__name__)
print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
demo(bisect_fn)

# Inserting with bisect.insort : sorting is expensive, so once you have sorted a sequence,
# its good to keep it that way. thats why bisect.insort was created
# insort(seq, item), iserts item into seq so as to keep seq in ascending order

import bisect
import random

SIZE = 7
random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%d ->' % new_item, my_list)

# When a List is not the Answer
# if you need to store 10 million floating-point values, an array is much more efficient because an array
# does not actually hold full-fledged float objects, but only the packed bytes representing thier amchine values
#If you are constantly adding and removing items from the  ends of a list as FIFO data structure, a deque(double ended queue) works better
# If the code does a lot of containment checks(e.g. item in my_collection), consider using set for my_collection
#