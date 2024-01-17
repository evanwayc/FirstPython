
# 對一個"列表"操作，生成 "新的列表"

# [輸出表達式 for 元素 in 列表]
# [輸出表達式 for 元素 in 列表 if ...]

a_list = [1, 2, 3, 4, 5]

b_list = [ x**2 for x in a_list]
print(b_list)

# 帶條件列表解析
c_list = [ x**2 for x in a_list if x >3]
print(c_list)