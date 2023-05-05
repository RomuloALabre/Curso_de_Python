def contador(*num):
    print(num)
    print()
    for valor in num:
        print(f'{valor} ', end='')


contador(3,6,9)
contador(1,2,3,4,5,6,7,8,9)