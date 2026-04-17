def soma(l, n=None):

    if n is None:
        n = len(l)

    if n == 0:
        return 0

    return l[n - 1] + soma(l, n - 1)


# Testes
exemplos = [
    [1, 2, 3, 4, 5],
    [10, -3, 7, -1, 5],
    [42],
    [],
    [2, 2, 2, 2, 2],
]

for lista in exemplos:
    print(f"Lista: {lista}")
    print(f"Soma: {soma(lista)}\n")
