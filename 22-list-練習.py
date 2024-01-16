
alist = []
while True:
    num = input("Enter a number (exit): ")
    if num == "exit":
        break
    alist.append(int(num))

print(f"總和為：{sum(alist)}\n平均為:{sum(alist)/len(alist)}")
