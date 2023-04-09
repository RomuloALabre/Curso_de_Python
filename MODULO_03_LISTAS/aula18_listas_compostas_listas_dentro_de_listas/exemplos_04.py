nomes = list()
dados = list()
menor = maior = 0
for r in range(0 , 3):
    dados.append(str(input('Digite o nome: ')))
    dados.append(int(input('Idade: ')))
    nomes.append(dados[:])
    dados.clear()
print(nomes)

for p in nomes:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        maior += 1
    else:
        print(f'{p[0]} é de menor')
        menor += 1
print(f'Temos {menor} menor de idade e {maior} maior de idade')