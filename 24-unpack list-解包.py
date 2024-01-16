nums = [3,5,6]
n1 = nums[0]
n2 = nums[1]
n3 = nums[2]

a1,a2,a3 = nums

print(f'{n1},{n2},{n3}')
print(f'{a1},{a2},{a3}')

# 解包可以用 *來保存後面的
b1, *other = nums
print(b1,other)

data = ['Tom',23,'This is a strong guy.']

name,age,desc = data
print(name,age,desc)