alist = [5,8,6,4,3,7,9]
print(alist)

alist.sort()
print(alist)

blist = sorted(alist)
print(blist)


print("========================")

students = [
    ('Jack',15),
    ('Tom',10),
    ('Mary',12),
]
print(students)


def students_sort_key(student):
    return student[1]

students.sort(key=students_sort_key, reverse=True)
print(students)
