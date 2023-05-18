def contador(i , f, p):
    """
    (function) def contador(
    i: Any,
    f: Any,
    p: Any
) -> None"""
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

contador(2 , 10, 2)
help(contador)