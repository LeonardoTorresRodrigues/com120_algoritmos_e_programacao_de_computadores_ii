def fat(n):
    if n == 0:
        return 1
    else:
        res = n * fat(n-1)
        return res


print(fat(1))
print(fat(0))
print(fat(4))
print(fat(5))
