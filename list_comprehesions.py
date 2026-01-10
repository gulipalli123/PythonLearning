# A quick way to build a sequence is using a list comprehesions(if the target is a list)
# or a generator expression (for all other kind of sequences)

# Build a list of code points from a string
symbols = '$§%&#'
#codes = []
#for symbol in symbols:
 #   codes.append(ord(symbol))
codes = [ord(symbol) for symbol in symbols]  # List comprehesions 

print (codes)

# Listcomps Versus map and filter
# List comps do everything the map and filter functions do, without the contortions of the functionally challenged Python lambda

symbols = '$§%&#'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)

# cartesian product using a list comprehesnion
# Listcomps are used to build lists, to fill up other sequence types, a genexp is the way to go.
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)
tshirts = [(color, size)  for size in sizes for color in colors]
print(tshirts)

