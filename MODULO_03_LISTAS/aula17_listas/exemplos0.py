# num = (2, 3, 9, 1)
# num[2] = 4   '''esta operação não funciona em tuplas, para alterá-la devemos transformá-la em lista
# print(num)
print('Realizando alteração de dados: ')
num = [2, 3, 9, 1]
num[2] = 4
print(num)

print('Inserindo um valor no final: ')
num.append(7)
print(num)

print('Organizando em ordem crescente:')
num.sort()
print(num)

print('Organizando em ordem DESCRESCENTE:')
num.sort(reverse = True)
print(num)

print('Mostrar o tamanho da lista:')
print(len(num))

print('Para inserir valores:')
num.insert(1 , 3)
print(num)

print('Para EXCLUIR um valor:')
num.pop(2)
print(num)

print('Para remover um elemento: O "remove" busca a primeira ocorrência do valor.')
num.remove(3)
print(num)

print('Encontrar o menor e o maior valor da lista:')
print(f'O menor valor da lista é: {min(num)} e está na posição {num.index(min(num))+1}')   
print(f'O maior valor da lista é: {max(num)} e está na posição {num.index(max(num))+1}') 