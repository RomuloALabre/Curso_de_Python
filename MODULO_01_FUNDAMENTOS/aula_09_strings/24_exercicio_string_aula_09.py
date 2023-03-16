# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra 'SANTO'
cid = str(input('Digite o nome da cidade: ')).strip()
print(cid.lower().find('santo'))

#resposta do professor
print(cid[:5].lower() == 'santo')


