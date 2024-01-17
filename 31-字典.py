empty_dict={}

student = {
    'name':'Tom',
    'age':20,
    'hobbies':['game','travel','code']
}


# 新增
student['gender']='Male'
print(student)
# 修改
student['gender']='Female'
print(student)
# 刪除
del student['gender']
print(student)

print('=============================')

print(student['name'])
print(student.get('age'))
print('=============================')

# 取得不存在的項目
# print(student['address']) #遇到沒有的項目，程式會崩潰
print('+++++')
print(student.get('address')) #遇到沒有的項目，程式會回傳None，不崩潰
print(student.get('address','Taipei')) #遇到沒有的項目，會回傳預設值
print('=============================')

# 遍歷字典

print(student.items()) #回傳一個元組的列表
print(student.keys()) #回傳一個列表 key
print(student.values()) #回傳一個列表 Value

for s in student.values():
    print(s)