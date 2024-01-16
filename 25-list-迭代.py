ages = [23, 18, 21, 38]


# enumerate
for index, age in enumerate(ages):
    print(index, age)


# iterator  迭代器  iter()

it = iter(ages)

print(next(it))
print(next(it))
print(next(it))
print(next(it))

