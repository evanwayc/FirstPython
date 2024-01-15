
def my_func(name):
    return f"Hello {name}"

f = my_func
print(f("Mary"))

print("=======================================")

ff = lambda name: f"Hello {name}"
print(ff("Tom"))

print("=======================================")

# 傳入函數，但是並沒有先求得解，直到f()被呼叫時才會求得
alist = []

for i in range(1,4):
    alist.append(lambda:i)

for f in alist:
    print(f())
    