def add(n):
    if n==0:
        return 1
    return n*add(n-1)
print(add(5))