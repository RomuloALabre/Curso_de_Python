frase = ' Curso em Vídeo python'

#conta letra O
print('conta letra O: ',frase.count('o'))
#Escreve em maiuscula
print('Escreve em maiuscula: ',frase.upper())
#Escreve em minuscola
print('Escreve em minuscola: ',frase.lower())
# Muda a primeira letra para maiuscola
print('Muda a primeira letra para maiuscola: ',frase.capitalize())
# Muda a primeira letra para maiuscola
print('Muda a primeira letra para maiuscola: ',frase.title())
#tamanho da frase
print('tamanho da frase: ',len(frase))
#exclui espaço em branco
print('exclui espaço em branco: ',frase.strip())
#troca uma palavra por outra
print('troca uma palavra por outra: ',frase.replace('Python', 'Romulo'))
#mostra o caracter 3
print('mostra o caracter 3: ',frase[3])
#existe 'curso' na frase?
print('Curso' in frase)
#procure 'curso'
print(frase.find('Curso'))
# divide as palavras em lista
print(frase.split())
