# 集合 (Set) 其實和數組 (Tuple) 與串列 (List) 很類似, 不同的點在於集合不會包含重複的資料


print("============宣告與建立集合 (Set)==================")

# 宣告與建立集合 (Set)
set1 = set()# 建立空的集合

set2 = {1, 2, 3, 4, 5}

# 從串列 (List) 來建立集合
set3 = set([i for i in range(20, 30)])

# 從數組 (Tuple) 來建立集合
set4 = set((10, 20, 30, 40, 50))

# 集合不會包含重複的資料, 你可以從 set5 印出來的結果得知
set5 = set((1, 1, 1, 2, 2, 3))

print(set1)
print(set2)
print(set3)
print(set4)
print(set5)
# 注意： 建立空集合的方法是 set1 = set() 而不是 set1 = {}

print("============集合加入與刪除元素==================")

# 集合加入與刪除元素
# 可以使用 add(value) 來加入新元素, 也可以使用 remove(value) 來移除元素

set2 = {1, 2, 3, 4, 5}
set4 = set((10, 20, 30, 40, 50))

set2.add(6) # 在 set2 中加入 6
set4.remove(20) # 將 set4 中的 20 刪除

print(set2)
print(set4)


print("=============集合可使用的函式=================")

# 集合可使用的函式
# 與串列 (List) 和數組 (Tuple) 一樣可以使用以下函式

# len() 回傳長度

# sum() 回傳總和

# max() 回傳最大值

# min() 回傳最小值

set1 = {2, 4, 6, 8, 10}

print(len(set1))
print(sum(set1))
print(max(set1))
print(min(set1))

print("===========判斷元素是否存在於集合中===================")


# 判斷元素是否存在於集合中
# 與串列 (List) 和數組 (Tuple) 一樣可以使用 in 和 not in 來判斷元素是否存在於集合中

set1 = {2, 4, 6, 8, 10}

print(2 in set1)
print(11 in set1)
print(3 not in set1)
print(4 not in set1)

print("============利用 for 迴圈來印出集合==================")


# 利用 for 迴圈來印出集合
# 因為集合 (Set) 沒辦法使用索引 (Index) 來印出, 所以用 for 迴圈寫時要這樣寫

set1 = {2, 4, 6, 8, 10}

for i in set1:
	print(i, end = ' ')
	print()
# 注意： 集合和串列數組不同, 不可以使用索引來擷取特定元素

print("=========聯集 交集 差集 對稱差集=====================")

# 聯集 交集 差集 對稱差集
# union : 聯集
# intersection : 交集
# difference : 差集
# symmetric_difference : 對稱差集

setA = {1, 6, 8, 10, 20}
setB = {1, 3, 8, 10}

# 以下兩個都是 聯集 的寫法
print(setA.union(setB))
print(setA | setB)

# 以下兩個都是 交集 的寫法
print(setA.intersection(setB))
print(setA & setB)

# 以下兩個都是 差集 的寫法
print(setA.difference(setB))
print(setA - setB)

# 以下兩個都是 對稱差集 的寫法
print(setA.symmetric_difference(setB))
print(setA ^ setB)

# 聯集： A B 集合的所有項目
# 交集： A B 集合的共有項目
# 差集： A 集合扣掉 A B 集合的共有項目
# 對稱差集： A B 集合的獨有項目

print("=========子集合與超集合=====================")
# 子集合與超集合
# 除了上面提到的集合外, 還有其他兩種集合： 子集合 (subset) 與超集合 (superset)
# 子集合 (sebset) ： 若 A 集合的所有項目是 B 集合的部分集合, 則稱 A 為 B 的子集合
# 超集合 (superset) ： 若 A 集合的所有項目是 B 集合的部分集合, 則稱 B 為 A 的超集合

setA = {1, 6, 8}
setB = {1, 6, 8, 10, 20}

# 使用 issubset() 來判斷 A 是否為 B 的子集合
print(setA.issubset(setB))

# 使用 issuperset() 來判斷 B 是否為 A 的子集合
print(setB.issuperset(setA))


print("=========兩個集合是否相等=====================")

# 判斷兩個集合是否相等
# 使用 == 與 != 來判斷兩個集合是否相同

setA = {1, 6, 8}
setB = {1, 6, 8, 10, 20}

print(setA == setB)
print(setA != setB)
