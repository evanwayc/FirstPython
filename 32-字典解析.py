grades = {"Jack": 70, "Tom": 30, "Bob": 60}

new_grades = {name: int(grades * 1.1) for name, grades in grades.items() if grades >= 60}
print(new_grades)


# 字典合併

dic1={
    'math':90,
    'english':80
}

dic2={
    'math':80,
    'chinese':90
}

dic_mix = {**dic1, **dic2}  # **表示字典合併，將兩個字典合併成一個字典，後面vaule的會取代前面的 (math)
print(dic_mix)