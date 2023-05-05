pessoas = {'nome':'Romulo', 'sexo':'Masculino', 'idade':35}
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k in pessoas.items():
    print(k)

for k, v in pessoas.items():
    print(f'{k}: {v}')

del pessoas['sexo']
pessoas['nome'] = 'Rodrigo'
pessoas['peso'] = 90
print(pessoas)
