'''
Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção
(sem usar o sort()).
No final, mostre a lista ordenada na tela.
'''
valores = []
for v in range(0 , 5):
    num = int(input('Um numero: '))
    if v == 0:
        valores.append(num)
        print('Adicionado primeiro valor da lista')
    elif num > valores[-1]:
        valores.append(num)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos , num)
                print(f'Adicionado na posição {pos+1} da lista')
                break
            else:
                pos+=1
print(f'Os valores em ordem crescente foram: {valores}')