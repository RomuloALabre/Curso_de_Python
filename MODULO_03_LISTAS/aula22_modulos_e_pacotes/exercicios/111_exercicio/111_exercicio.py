"""
Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 107, 108, 109 e 110 para o primeiro pacote e mantenha tudo funcionando.
"""
import moeda
preço = float(input('Digite um valor: R$ '))
#taxaa = float(input('Insira a taxa: '))
moeda.resumo(preço, 30, 10)