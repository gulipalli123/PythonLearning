# A common feature of list, tuple, str and all sequence types in Python is the support of slicing operations
# Slices and Range Exclude the last item because of the zero-based indexing used in Python

l = [10, 20, 30, 40, 50, 60]
print(l[:2])
print(l[2:])
print(l[4:])

#Slice Objects
s = 'bicycle'
print(s[:2])
print(s[3:])
print(s[0:4:2])          #slicing evaluates the expr s[a:b:c] as seq[start:stop:step]

#Line items from a flat-file invoice

invoice = """
0.....6..................................40............52...55........
1909  Pimoroni PiBrella                       $17.50     3     $52.50
1489  6mm Tactile Switch x20                   $4.95     2      $9.90
1510 Panavise Jr.   - PV-201                  $28.00     1     $28.00
PiTFT Mini Kit 320 * 240                      $34.95     1     $34.95
"""

SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[UNIT_PRICE], item[6:40:1])

#Multidimensional Slicing and Ellipsis
# The operator [] can also take multiple indexes or slices separated by commas. This is  used, for instance,
# in the external NumPy package, where items of a two-dimensional numpy.ndarray can be fetched using the syntax
# a[i, j] and a 2-dimensional slice obtained with an expression like a[m:n, k:l]

# The Ellipsis - written with 3 full stops (...) is recognised as a token by python parser
# It is an alias to the Ellpisis object, the single instance of the Ellipsis class
# As such it can be passed as an argument to functions and as part of a slice specification, as in f(a, ..., z) or a[i:...]
#NumPy uses ... as a shortcut when slicing arrays of many dimensions
# e.g. if x is 4-dimensional array, x[i, ...] is a shortcut for x[i, :, :, :]

#Assigning to slices
# Mutable sequences can be grafted, exercised and otherwise modified inplace using slice notation on the left side
# of an assignment statement
l = list(range(10))
print (l)
l[2:5] = [20, 30]
print(l)
del l[5:7]
print(l)

#Using + and * with sequences : both + and * always create a new object, and never change their operands
l = [1, 2, 3]
print(l * 5)
print(l)
