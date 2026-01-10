# To initialize tuples, arrays and other type of sequences, you can also start from a listcomp
# but a genexp saves memory because it yields items one by one using the iterator protocol instead of 
# building a whole list just to feed another constructor

#Genexps use the same syntax as listcomps, but are enclosed in parentheses rather than brackets


# Initialize a tuple and array from a generator expression

symbols = '$!«:?'
print(tuple(ord(symbol) for symbol in symbols))
import array
print(array.array('I', (ord(symbol) for symbol in symbols)))

#If the generator expression is the single argument in a function call, there is no need to duplicate the enclsoing parenthesis
#The array constructor takes 2 arguments  so parenthesis around the generator expression are mondatory.

# cartesian product in a generator expression

# The below generator expression yields items one by one; a list with all six T-shirt variations is never produced

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

for tshirt in ('%s %s' %(c, s) for c in colors for s in sizes):
    print(tshirt)
