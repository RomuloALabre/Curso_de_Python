"""
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. 
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), 
mas com uma validação de dados para aceitar apenas valores que sejam monetários.
"""
import moeda
preço = moeda.leiaDinheiro('Digite um valor: R$ ')
#taxaa = float(input('Insira a taxa: '))
moeda.resumo(preço, 30, 10)