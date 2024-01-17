# iterator = map(function,list)

salaries = [1000, 2000, 3000, 4000, 5000]

def double_salary(x):
    return x * 2

new_salaries = list(map(double_salary, salaries))
print(new_salaries)

print("=====================")

lambda_salaries = list(map(lambda x: x * 2, salaries))
print(lambda_salaries)

print("=====================")

students = [
    ('jack',23),
    ('mary',21),
    ('john',20),
]


ages = list(map(lambda s:s[1],students))
print(ages)