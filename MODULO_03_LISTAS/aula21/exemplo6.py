def teste(b):
    global a
    a = 8
    b += 100
    print(f'Na função teste, A vale {a}')
    print(f'Na função teste, B vale {b}')

# Programa principal
a = 5
b = 1
print(f'Na função principal, A vale {a}')
teste(a)
print(f'Na função principal, B vale {b}')