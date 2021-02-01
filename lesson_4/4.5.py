from functools import reduce

list = [el for el in range(99, 1001) if el % 2 == 0]
print(list)
multi = reduce(lambda x, y: x * y, list)
print(multi)