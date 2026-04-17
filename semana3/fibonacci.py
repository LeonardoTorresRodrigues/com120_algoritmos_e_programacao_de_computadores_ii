def fib(n):
    if n >= 2:
        res = fib(n-1)+fib(n-2)
        return res
    elif n == 1:
        res = 1
        return res
    else:
        res = 0
        return res


print(fib(5))
print(fib(4))
print(fib(3))
print(fib(2))
print(fib(1))
print(fib(0))
