def maior_elemento(l, n=None):

    if n is None:
        n = len(l)

    if n == 1:
        return l[0]

    maior_do_restante = maior_elemento(l, n - 1)

    return l[n - 1] if l[n - 1] > maior_do_restante else maior_do_restante


# Testes
exemplos = [
    [3, 1, 4, 1, 5, 9, 2, 6],
    [-10, -3, -7, -1, -5],
    [42],
    [7, 7, 7, 7],
]

for lista in exemplos:
    print(f"Lista: {lista}")
    print(f"Maior elemento: {maior_elemento(lista)}\n")
