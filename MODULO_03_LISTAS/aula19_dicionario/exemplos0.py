dados = dict() #OU dados = {}
dados = {'nome':'Romulo', 'idade':'35'}
print(dados['nome'])  #imprime Romulo
print(dados['idade']) #imprime 35

print('-='*30)
# Para adicionar elementos ao dicionário:
dados['sexo'] = 'M'
print(dados['sexo']) #imprime 'M'

print('-='*30)
# para deletar um elemento
del dados['idade']