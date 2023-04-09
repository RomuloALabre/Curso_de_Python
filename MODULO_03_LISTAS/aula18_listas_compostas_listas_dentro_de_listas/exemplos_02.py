teste = list()
teste.append('Romulo')
teste.append(35)
galera = list()

galera.append(teste[:])
print(f'1 - {galera}')

teste[0] = 'Maria'
teste[1] = 22

galera.append(teste[:])
print(f'2 - {galera}')