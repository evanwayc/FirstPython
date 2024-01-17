# resul = reduce(function, list)

from functools import reduce
numbers = [1, 2, 3, 4, 5]

resul = reduce(lambda x, y: x  + y ,numbers)

print(resul)
