grade_set = {50, 70, 66}

new_grade_set = {grade * 1.2 for grade in grade_set if grade >= 60}

print(new_grade_set)


a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

mix1 = a | b #聯集
mix2 = a & b #交集
mix3 = a - b #差集 (a 中有而 b 中沒有)
mix4 = a ^ b #對稱差集 (a 中有而 b 中沒有, b 中有而 a 中沒有)

print(mix1)
print(mix2)
print(mix3)
print(mix4)

c = {1, 2, 3}
d = {1, 2, 3, 4, 5}



print(c.issubset(d)) #判斷c是否是d的子集
print(c <= d) #判斷c是否是d的子集
print(d.issuperset(c)) #判斷d是否是c的父集
print(d >= c) #判斷d是否是c的父集


print(c.isdisjoint(d)) #判斷c和d是否有相同的元素