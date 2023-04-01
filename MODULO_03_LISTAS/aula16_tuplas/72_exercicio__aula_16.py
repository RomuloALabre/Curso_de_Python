'''
Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso de zero até vinte
Seu programa deverá ler um número pelo teclado
(entre 0 e 20) e mostrá-lo por extenso'''
extensos = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", 
            "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
while True:
    num = int(input('Digite "00" para sair ou digite um número para converter: '))
    if num == 00 or num > 20:
        break
    print(extensos[num])