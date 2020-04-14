def fib(ile):
    lista = [1, 1]
    for index in range(2, ile+2, 1):
        lista.append(lista[index-1] + lista[index-2])
        yield lista[index-2]
ile = 20
ob = fib(ile)
for i in range(ile):
    print(next(ob))
