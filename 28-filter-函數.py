# iterator = filter(function, list)

salaries = [6300, 5800, 6700, 9000]

filtered_salaries = filter(lambda x: x > 6000, salaries)

print(list(filtered_salaries))

print("===================")


def up6500(salary):
    return salary > 6000

f_s = filter(up6500, salaries)
print(list(f_s))


students = [
    ('Tom',23),
    ('Jack',21),
    ('Mary',20)
]

print(list(filter(lambda s:s[1] >= 21, students)))

