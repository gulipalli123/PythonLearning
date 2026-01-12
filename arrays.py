#If the list will only contain numbers, an array.array is more efficient that a list
#An array supports all mutable sequence operations(including .pop, .insert, and .extend)
#and additional methods for fast loading and saving such as .frombytes and .tofile

from array import array
from random import random
floats = array('d', (random() for i in range(10*7)))
print(floats[-1])
fp = open('/workspaces/PythonLearning/floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('/workspaces/PythonLearning/floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])

#pickle module is another fast and more flexible way of saving numeric dat for object serialization
#saving an array of floats with pickle.dump is almost as fast as with array.tofile
#pickle handles almost all built-in types, including complex numbers, nested collections and even
# userdefined classes automatically(if they are not too tricky in thier implementation)

#For the specific cases of numeric arrays representing binary data, such as raster images, 
# Python has the bytes, bytearray types