def print_sequence(n:int):
    print(n)
    if n > 1:
        print_sequence(n-1)

print_sequence(8)


def summary(n:int):
    if n == 1:
        return 1
    else:
        return n + summary(n-1)
    
print(summary(100))