#The built-in memoryview class is a shared-memory sequence type that lets you handle
#slices of arrays without copying bytes
#A memoryview is essentialy a generalized NumPy array structure in Python itself,
#it allows to share memory between data structures(things like PIL images, SQLite data bases, NumPy arrays)
# without first copying. This is very important for large datasets

# Changing the value of an array item by poking one of its bytes
from array import array 

numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))

print(memv[0])

memv_oct = memv.cast('B')
print(memv_oct.tolist())
memv_oct[5] = 4
print(numbers)
