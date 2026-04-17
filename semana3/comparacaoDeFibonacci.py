import time


def fib_rec(n):
    if n < 2:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)


def fib_it(n):
    res = n
    a, b = 0, 1
    for l in range(2, n+1):
        res = a + b
        a, b = b, res
    return res


n = 35
start = time.time()
print(fib_rec(n))
print('Recursive: {} seconds'.format(time.time() - start))
start = time.time()
print(fib_it(n))
print('Iterative: {} seconds'.format(time.time() - start))
