'''
Crie um programa onde o usuário digite uma expressão qualquer
que use parênteses.
Seu aplicativo deverá analisar se a expressão passada 
está com os parênteses abertos e fechados na ordem correta.
'''
exp = str(input('Digite a expressão: '))
lista = []
for simb in exp:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()        
        else:
            lista.append(')')
            break
if len(lista) > 0:
    print('expressão inválida')
else:
    print('expressão OK')