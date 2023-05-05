"""
 Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
 e todos os dicionários em uma lista. No final, mostre:
 A) Quantas pessoas foram cadastradas;
 B) A média de idade;
 C) Uma lista com as mulheres;
 D) Uma lista de pessoas com idade acima da média.
"""
user = list()
dados = dict()
soma = media = 0
while True:
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo: ')).lower().strip()[0]
        if dados['sexo'] in 'mf':
            break
        print('ERRO! Tente novamente!')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    user.append(dados.copy())
    dados.clear()
    resp = str(input('Deseja cadastrar mais alguém? ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('ERRO! Deseja cadastrar mais alguém? ')).upper().strip()[0]
    if resp == 'N':
        break
print(user)
print(f'A) Foram cadastradas {len(user)} pessoas.')
media = soma / len(user)
print(f'B) A média de idade das pessoas cadastradas é: {media:5.2f}')
print(f'C) As mulheres cadastradas foram: ', end='')
for u in user:
    if u['sexo'] in 'f':
        print(f'{u["nome"]} ', end='')
print()
print('D) Pessoas com idade acima da média: ')
for u in user:
    if u['idade'] >= media:
        '''print(f'{u["nome"]} ', end='')    Até aqui ja resolve'''
        print('   ', end='')
        for k, v in u.items():
            print(f'{k} = {v}; ', end='')
        print()
print()
print('<< ENCERRADO >>')
