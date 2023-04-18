'''Dicionário na estrutura for, semelhante ao enumerate de list()'''
filme = {'Titulo':'Star Wars', 
         'Ano':1977,
         'diretor':'George Lucas',
        }
print(filme.values())
print(filme.keys())
print(filme.items())
print('-='*30)
for k, v in filme.items():
    print(f'O {k} é {v}')